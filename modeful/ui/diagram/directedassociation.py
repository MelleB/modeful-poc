import math

from kivy.graphics import Color, Line

from modeful.ui.diagram.association import Association
from modeful import sign

class DirectedAssociation(Association):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        with self.canvas.before:
            Color(0, 0, 0, .5)
            self._arrowhead_line = Line(points=[], width=1)

    def redraw(self, x1, y1, x2, y2):
        super().redraw(x1, y1, x2, y2)
        # http://math.stackexchange.com/a/68051
        
        dx, dy = x2 - x1, y2 - y1
        a = math.atan2(dy, dx) - math.pi / 2
        a1 = math.pi / 3
        s = 20

        p1x = x2 - math.cos(a + a1) * s
        p1y = y2 - math.sin(a + a1) * s
        p2x = x2 + math.cos(a - a1) * s
        p2y = y2 + math.sin(a - a1) * s
        
        self._arrowhead_line.points = [p1x, p1y, x2, y2, p2x, p2y]
