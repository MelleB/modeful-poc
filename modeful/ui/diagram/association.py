from kivy.graphics import Color, Line, Ellipse
from kivy.uix.widget import Widget
from kivy.uix.behaviors import FocusBehavior

class Association(Widget, FocusBehavior):

    _line = None
    _src_bp = None
    _dst_bp = None

    def __init__(self, model, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.model = model
        self.bind(parent=self.redraw, size=self.redraw)

        src = self.model.diagram.get_element_by_id(self.model.src_id)
        dst = self.model.diagram.get_element_by_id(self.model.dst_id)
        src.on_change(self.redraw)
        dst.on_change(self.redraw)

    @classmethod
    def from_model(cls, model):
        c = cls(model)
        model.on_change(c.redraw)
        return c

    def redraw(self, *_):
        src = self.parent.get_element_by_id(self.model.src_id)
        dst = self.parent.get_element_by_id(self.model.dst_id)

        src_x, src_y = src.x + src.width/2, src.y + src.height/2 
        dst_x, dst_y = dst.x + dst.width/2, dst.y + dst.height/2

        src_bp_x, src_bp_y = src.get_boundary_point(dst_x, dst_y)
        dst_bp_x, dst_bp_y = dst.get_boundary_point(src_x, src_y)
        
        points = [src_bp_x, src_bp_y, dst_bp_x, dst_bp_y] \
                 if src.x < dst.x \
                    else [dst_bp_x, dst_bp_y, src_bp_x, src_bp_y]
        
        with self.canvas.before:
            Color(0, 0, 0, .5)
            if self._line is None:
                self._line = Line(points=points, width=1)
            else:
                self._line.points = points

            if self._src_bp is None:
                Color(0, 0, 255, 1)                
                self._src_bp = Ellipse(pos=(src_bp_x - 3, src_bp_y - 3), size=(6, 6))
            else:
                self._src_bp.pos = (src_bp_x - 3, src_bp_y - 3)

            if self._dst_bp is None:
                Color(0, 255, 0, 1)
                self._dst_bp = Ellipse(pos=(dst_bp_x - 3, dst_bp_y - 3), size=(6, 6))
            else:
                self._dst_bp.pos = (dst_bp_x - 3, dst_bp_y - 3)
            
