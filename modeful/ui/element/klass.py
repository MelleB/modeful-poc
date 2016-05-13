
from kivy.clock import Clock
from kivy.uix.behaviors import DragBehavior, FocusBehavior
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle

from modeful.ui.editablelabel import EditableLabel
from modeful.ui.element.base import ElementBase
from modeful.ui.palette import LightBlue, Orange

class Class(ElementBase, FocusBehavior, DragBehavior, EditableLabel):

    _bgcolor = LightBlue
    _bgcolor_focus = Orange
    _bgrect = None

    def __init__(self, model, **kwargs):
        self.size = model.size if 'size' in model else (100, 30)
        self.text = model.name if 'name' in model else 'Class'

        super().__init__(model, **kwargs)
        
        self.halign = 'center'
        self.valign = 'middle'

    def redraw(self, _, value, *args):
        self.drag_rectangle = self.x, self.y, self.width, self.height

        with self.canvas.before:
            if self._bgrect is None or type(value) == type(True):
                self.canvas.before.clear()
                Color(*self._bgcolor if not self.active else self._bgcolor_focus)
                self._bgrect = None # To delete previos rect
                self._bgrect = Rectangle(pos=self.pos, size=self.size)
            else:
                self._bgrect.pos = self.pos
                self._bgrect.size = self.size


