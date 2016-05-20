from kivy.graphics import Color, Line, Quad

from modeful.ui.diagram.relationship import Trigonometry
from modeful.ui.diagram.relationship.association import Association

class Aggregation(Association):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        with self.canvas.before:
            Color(1, 1, 1)
            self._diamond_bg = Quad(points=[0]*8)
            Color(0, 0, 0, .5)
            self._diamond_line = Line(points=[], width=1, close=True)
            

    def redraw(self, x1, y1, x2, y2):
        super().redraw(x1, y1, x2, y2)

        points = Trigonometry.get_diamond_points(x1, y1, x2, y2, size=15)

        self._diamond_bg.points = points
        self._diamond_line.points = points
