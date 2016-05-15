
from kivy.graphics import Color, Line, Rectangle
from kivy.uix.widget import Widget
from kivy.uix.scatter import ScatterPlane

from modeful.event import Event
from modeful.ui.behaviors.keyboardnavigationbehavior import KeyboardNavigationBehavior
from modeful.ui.palette import White, LighterGray
from modeful.ui.element.klass import Class
from modeful.ui.diagram.association import Association

from modeful.model.diagram.klass.diagram import ClassDiagram

_GRID_SIZE = 30

class Diagram(ScatterPlane, KeyboardNavigationBehavior):

    do_rotation = False
    do_colllide_after_children = True

    model = None
    elements = {}
    associations = {}
    
    _rect = None
    _grid_lines_x = []
    _grid_lines_y = []

    _selected_tool = 'class'

    _type_mapping = {
        'class': Class 
    }
    
    
    def __init__(self, model=None, **kwargs):
        super().__init__(**kwargs)
        self.model = model
        model.on_change(self.redraw)
        self.bind(size=self.redraw, pos=self.redraw)

        Event.on(Event.TOOL_SELECTED, self.on_tool_selected)
        Event.on(Event.MODEL_ELEMENT_ADDED_ + str(self.model.id), self.add_element)

        for e in self.model.elements:
            self.add_element(e)

        for a in self.model.associations:
            c = Association.from_model(a)
            self.associations[a.id] = c
            self.add_widget(c)

    def add_element(self, model):
        cls = self._type_mapping[model.type]
        c = cls.from_model(model)
        self.elements[model.id] = c
        self.add_widget(c)

    def on_tool_selected(self, tool_name):
        self._selected_tool = tool_name

    def redraw(self, instance, value, *args):
        self._draw_grid()

    def get_element_by_id(self, id):
        return self.elements.get(id, None)
        
    def _draw_grid(self):
        with self.canvas.before:
            # Draw white rectangle as bg
            Color(*White)
            if self._rect is None:
                self._rect = Rectangle(pos=self.pos, size=self.size)
            else:
                self._rect.pos = (-self.pos[0], -self.pos[1])
                self._rect.size = self.size

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
        super().add_navigation_element(w)
        super().add_widget(w)
        super().set_active(w)

    class_count = 0
    
    def on_touch_down(self, touch):
        in_visible_area = self.parent.collide_point(*touch.pos) if isinstance(self.parent, Widget) else True
        if in_visible_area and self.collide_point(*touch.pos) and touch.is_double_tap:
            if any(w.collide_point(*self.to_local(*touch.pos)) for w in self.children):
                return super().on_touch_down(touch)
            self.class_count += 1
            Event.emit(Event.MODEL_ELEMENT_ADD_ + str(self.model.id), \
                       self._selected_tool, \
                       x=touch.pos[0], y=touch.pos[1], name='Class %d' % self.class_count)
            return True
        elif not in_visible_area:
            return False
        else:
            return super().on_touch_down(touch)
