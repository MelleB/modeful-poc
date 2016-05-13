
from kivy.uix.behaviors import DragBehavior
from kivy.uix.widget import Widget

from modeful import sign
from modeful.ui.behaviors.keyboardnavigationbehavior \
    import KeyboardNavigationNode, KeyboardNavigationBehavior


class ElementBase(KeyboardNavigationNode, Widget):

    def __init__(self, model, **kwargs):
        super().__init__()
        self.model = model

        self.bind(size=self.redraw, pos=self.redraw, active=self.redraw)
        self.center_x, self.center_y = model.x, model.y


    @classmethod
    def from_model(cls, model):
        c = cls(model)
        model.on_change(c.redraw)
        return c
    
    def redraw(self, *args):
        pass

    
    def __setattr__(self, attr, value):
        dragged = isinstance(self, DragBehavior) \
                  and hasattr(self, '_drag_touch') \
                  and self._drag_touch != None
        in_model = hasattr(self, 'model') \
                   and attr in self.model
        if attr != 'model' and in_model:
            if getattr(self.model, attr) != value:
                setattr(self.model, attr, value)
        super().__setattr__(attr, value)

        
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos) \
           and isinstance(self.parent, KeyboardNavigationBehavior):
            self.parent.set_active(self)
        return super().on_touch_down(touch)

    def get_boundary_point(self, x, y):
        """ Return the point of boundary entry as seen from `pos` """
        dx = float(self.center_x - x)
        dy = float(self.center_y - y)

        sr = self.width / float(self.height)
        r = dx / dy if dy != 0.0 else 1.0

        if abs(r) < sr: # entry at top/bottom
            p = self.width / 2.0 * (r/sr) * sign(dy)
            q = self.height / 2.0 * sign(dy)
            return self.center_x - p, \
                   self.center_y - q
        else: # entry at left/right
            p = self.width / 2.0 * sign(dx)
            q = self.height / r * sign(dx)
            return self.center_x - p, \
                   self.center_y - q
