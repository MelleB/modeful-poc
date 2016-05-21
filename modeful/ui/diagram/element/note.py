
from kivy.uix.behaviors import DragBehavior, FocusBehavior
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle, Line

from modeful.ui.diagram.element import ElementBase
from modeful.ui.editablelabel import EditableLabel
from modeful.ui.palette import LightYellow, Yellow

class Note(ElementBase, FocusBehavior, DragBehavior, EditableLabel):

    _bgcolor = LightYellow
    _bgcolor_focus = Yellow
    
    _bg = None
    _line1 = None
    _line2 = None

    def __init__(self, model, **kwargs):
        super().__init__(model, **kwargs)
        self.width = model.width if 'width' in model else 140
        self.height = model.height if 'height' in model else 50
        self.text = model.content if 'content' in model else ''

        self.valign = 'top'
        self.halign = 'left'
        self.color = (.5, .5, .5)
        self.padding=(5, 5)
        self.multiline = True

    def redraw(self, _, value, *args):
        self.drag_rectangle = self.x, self.y, self.width, self.height

        #
        # p1-----------p2
        # |          s |  \
        # |            p6--p3
        # |                |
        # p5---------------p4
        #

        s = 10
        p5 = self.pos
        p1 = (p5[0], p5[1] + self.height)
        p2 = (p1[0] + self.width - s, p1[1])
        p3 = (p1[0] + self.width, p1[1] - s)
        p4 = (p3[0], p5[1])
        p6 = (p2[0], p2[1] - s)
        outline = [c for p in [p1, p2, p3, p4, p5] for c in p]
        corner = [c for p in  [p2, p6, p3] for c in p]

        with self.canvas.before:
            if self._bg is None or type(value) == type(True):
                self.canvas.before.clear()
                Color(*self._bgcolor if not self.active else self._bgcolor_focus)
                self._bg = None # To delete previos rect
                self._bg = Rectangle(pos=self.pos, size=self.size)
                Color(.5, .5, .5)
                self._line1 = Line(points=outline, close=True)
                self._line2 = Line(points=corner)
            else:
                self._bg.pos = self.pos
                self._bg.size = self.size
                self._line1.points=outline
                self._line2.points=corner
                
                


