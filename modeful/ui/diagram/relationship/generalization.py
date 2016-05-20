from kivy.graphics import Color, Line, Triangle

from modeful.ui.diagram.relationship import Trigonometry
from modeful.ui.diagram.relationship.association import Association

class Generalization(Association):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        with self.canvas.before:
            Color(1, 1, 1)
            self._arrowhead_bg = Triangle(points=[0]*6)
            Color(0, 0, 0, .5)
            self._arrowhead_line = Line(points=[], width=1, close=True)
            

    def redraw(self, x1, y1, x2, y2):
        super().redraw(x1, y1, x2, y2)

        points = Trigonometry.get_arrowhead_points(x1, y1, x2, y2, size=20)

        self._arrowhead_bg.points = points
        self._arrowhead_line.points = points
