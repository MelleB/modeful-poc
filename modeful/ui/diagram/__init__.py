
from kivy.clock import Clock
from kivy.graphics import Color, Line, Rectangle
from kivy.uix.widget import Widget
from kivy.uix.scatter import ScatterPlane

from modeful.event import Event
from modeful.ui.behaviors.keyboardnavigationbehavior import KeyboardNavigationBehavior, KeyboardNavigationNode
from modeful.ui.palette import White, LighterGray
from modeful.ui.diagram.element import ElementBase
from modeful.ui.diagram.element.klass import Class
from modeful.ui.diagram.element.note import Note
from modeful.ui.diagram.relationship.association import Association
from modeful.ui.diagram.relationship.directedassociation import DirectedAssociation
from modeful.ui.diagram.relationship.generalization import Generalization
from modeful.ui.diagram.relationship.aggregation import Aggregation
from modeful.ui.diagram.relationship.composition import Composition
from modeful.ui.diagram.relationship import Relationship, PartialRelationship

from modeful.model.diagram.klass.diagram import ClassDiagram

_GRID_SIZE = 30

class Diagram(ScatterPlane, KeyboardNavigationBehavior):

    do_rotation = False
    do_colllide_after_children = True

    model = None
    elements = {}
    relationships = {}
    
    _rect = None
    _grid_lines_x = []
    _grid_lines_y = []

    _class_counter = 0
    _partial_relationship = None    
    _selected_tool = 'class'
    _type_mapping = { #TODO: Move to mapping class?
        'class': Class,
        'note': Note,
        'association': Association,
        'directed-association': DirectedAssociation,
        'generalization': Generalization,
        'aggregation': Aggregation,
        'composition': Composition
    }
    
    def __init__(self, model=None, **kwargs):
        super().__init__(**kwargs)
        self.model = model

        for e in self.model.elements:
            self.add_element(e)

        for a in self.model.associations:
            self.add_relationship(a)

        with self.canvas.before:
            Color(*White)
            self._rect = Rectangle(pos=self.pos, size=self.size)

        self.bind(size=self.redraw, pos=self.redraw)
        Event.on(Event.TOOL_SELECTED, self.on_tool_selected)
        Event.on(Event.COMMAND_ADD_ELEMENT_CLASS, self.add_element_by_keyboard, 'class')
        Event.on(Event.COMMAND_ADD_ELEMENT_NOTE, self.add_element_by_keyboard, 'note')
        self.model.bind(element_added=self.add_element,
                        relationship_added=self.add_relationship,
                        change=self.redraw)

            
    def add_relationship(self, model):
        cls = self._type_mapping[model.type]
        r = Relationship.from_model(cls, model)
        self.relationships[model.id] = r
        self.add_widget(r)
        Clock.schedule_once(self.redraw)

        
    def add_element(self, model):
        cls = self._type_mapping[model.type]
        c = cls.from_model(model)
        self.elements[model.id] = c
        self.add_widget(c)
        Clock.schedule_once(self.redraw)

    def add_element_by_keyboard(self, type):
        Event.emit(Event.TOOL_SELECTED, type)
        self.model.add_element(
                       type=type,
                       x = 100,
                       y = 100)
        
    def on_tool_selected(self, tool_name):
        self._selected_tool = tool_name

        
    def redraw(self, *args):
        self._rect.pos = (-self.pos[0], -self.pos[1])
        self._rect.size = self.size

        self._draw_grid()


    def get_element_by_id(self, id):
        return self.elements.get(id, None)

    
    def _draw_grid(self):
        with self.canvas.before:
            # Draw vertical grid lines
            Color(*LighterGray)
            offset_x = int(self.pos[0]//_GRID_SIZE)
            old_num_lines = len(self._grid_lines_x)
            new_num_lines = int(self.width + 2*abs(self.pos[0]))//_GRID_SIZE - offset_x
            for i in range(0, new_num_lines):
                pts = [(i-offset_x)*_GRID_SIZE,
                       -self.pos[1],
                       (i-offset_x)*_GRID_SIZE,
                       self.height - self.pos[1]]
                if i < old_num_lines:
                    self._grid_lines_x[i].points = pts 
                else:
                    self._grid_lines_x.append(Line(points=pts))
                
            # Draw horizontal grid lines
            offset_y = int(self.pos[1]//_GRID_SIZE)            
            old_num_lines = len(self._grid_lines_y)
            new_num_lines = int(self.height+2*abs(self.pos[1]))//_GRID_SIZE - offset_y
            for i in range(0, new_num_lines):
                pts = [-self.pos[0],
                       (i-offset_y)*_GRID_SIZE,
                       self.width - self.pos[0],
                       (i-offset_y)*_GRID_SIZE]
                if i < old_num_lines:
                    self._grid_lines_y[i].points = pts 
                else:
                    self._grid_lines_y.append(Line(points=pts))

                    
    def add_widget(self, w):
        super().add_widget(w)
        if isinstance(w, KeyboardNavigationNode):
            super().add_navigation_element(w)
            super().set_active(w)

        
    def on_touch_down(self, touch):
        in_visible_area = self.parent.collide_point(*touch.pos) if isinstance(self.parent, Widget) else True
        child = next((c for c in self.children if c.collide_point(*self.to_local(*touch.pos))), None)

        element_tool_selected = issubclass(self._type_mapping[self._selected_tool], ElementBase)
        association_tool_selected = issubclass(self._type_mapping[self._selected_tool], Association)
        
        if in_visible_area and self.collide_point(*touch.pos):
            if touch.is_double_tap and not child and element_tool_selected:
                self._class_counter += 1
                self.model.add_element(
                    type=self._selected_tool,
                    x=touch.pos[0], y=touch.pos[1], name='Class %d' % self._class_counter)
            elif child and association_tool_selected:
                self._partial_relationship = PartialRelationship( \
                    child, self._type_mapping[self._selected_tool]())
                super().add_widget(self._partial_relationship)
            elif child:
                return super().on_touch_down(touch)
            return True
        elif not in_visible_area:
            return False
        else:
            return super().on_touch_down(touch)

        
    def on_touch_up(self, touch):
        if self._partial_relationship is None:
            super().on_touch_up(touch)
            return False
        
        child = next((c for c in self.children if c.collide_point(*self.to_local(*touch.pos))), None)

        #FIXME: Currently do not allow objects to add relationships to themselves.
        #Should be fixed when routing is added
        if child and child != self._partial_relationship.src:
            self.model.add_association(
                       type=self._selected_tool,
                       src_id = self._partial_relationship.src.model.id,
                       dst_id = child.model.id)

        self.remove_widget(self._partial_relationship)
        self._partial_relationship = None
            
        return True
