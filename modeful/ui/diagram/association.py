from kivy.graphics import Color, Line
from kivy.uix.widget import Widget
from kivy.uix.behaviors import FocusBehavior

class Association(Widget, FocusBehavior):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        with self.canvas.before:
            Color(0, 0, 0, .5)
            self._line = Line(points=[], width=1)

    def redraw(self, x1, y1, x2, y2):
        if x1 < x2:
            x1, y1, x2, y2 = x2, y2, x1, y1

        self._line.points = [x1, y1, x2, y2]

            
