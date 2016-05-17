from kivy.graphics import Color, Line, Ellipse
from kivy.uix.widget import Widget
from kivy.uix.behaviors import FocusBehavior

class Association(Widget, FocusBehavior):

    def __init__(self, model, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #self.model = model
        
        with self.canvas.before:
            Color(0, 0, 0, .5)
            self._line = Line(points=[], width=1)
            Color(0, 0, 255, 1)                
            self._src = Ellipse(size=(6, 6))
            Color(0, 255, 0, 1)
            self._dst = Ellipse(size=(6, 6))

    def redraw(self, x1, y1, x2, y2):
        if x1 < x2:
            x1, y1, x2, y2 = x2, y2, x1, y1

        self._line.points = [x1, y1, x2, y2]
        self._src.pos = (x1 - 3, y1 - 3)
        self._dst.pos = (x2 - 3, y2 - 3)        

            
