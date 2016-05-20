import math

from kivy.uix.widget import Widget

class Relationship(Widget):

    @staticmethod
    def from_model(cls, model):
        c = Relationship(model, cls())
        return c

    def __init__(self, model, element, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.model = model
        self.model.bind(change=self.redraw)
        self.element = element

        self.add_widget(element)
        
        self.bind(parent=self.redraw, size=self.redraw)

        src = self.model.diagram.get_element_by_id(self.model.src_id)
        dst = self.model.diagram.get_element_by_id(self.model.dst_id)
        src.bind(change=self.redraw)
        dst.bind(change=self.redraw)

    def redraw(self, *_):
        src = self.parent.get_element_by_id(self.model.src_id)
        dst = self.parent.get_element_by_id(self.model.dst_id)

        src_x, src_y = src.x + src.width/2, src.y + src.height/2 
        dst_x, dst_y = dst.x + dst.width/2, dst.y + dst.height/2

        src_bp_x, src_bp_y = src.get_boundary_point(dst_x, dst_y)
        dst_bp_x, dst_bp_y = dst.get_boundary_point(src_x, src_y)
        
        self.element.redraw(src_bp_x, src_bp_y, dst_bp_x, dst_bp_y)
    
    
class PartialRelationship(Widget):

    def __init__(self, src, element, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.src = src
        self.element = element
        self.add_widget(element)

        
    def on_touch_move(self, touch):
        x2, y2 = touch.pos
        x1, y1 = self.src.get_boundary_point(x2, y2)
        
        self.element.redraw(x1, y1, x2, y2)

    
class Trigonometry():

    @staticmethod
    def get_arrowhead_points(x1, y1, x2, y2, size):
        """ Returns 3 coordinates of an arrow head pointing to (x2, y2). """

        dx, dy = x2 - x1, y2 - y1
        a = math.atan2(dy, dx) - math.pi / 2
        a1 = math.pi / 3

        p1x = x2 - math.cos(a + a1) * size
        p1y = y2 - math.sin(a + a1) * size
        p2x = x2 + math.cos(a - a1) * size
        p2y = y2 + math.sin(a - a1) * size

        return [p1x, p1y, x2, y2, p2x, p2y]

    @staticmethod
    def get_diamond_points(x1, y1, x2, y2, size):
        """ Returns 4 coordinates of a 'diamond' head pointing to (x2, y2). """

        dx, dy = x2 - x1, y2 - y1
        a = math.atan2(dy, dx) - math.pi / 2
        a1 = math.pi / 2.8

        p1x = x2 - math.cos(a + a1) * size
        p1y = y2 - math.sin(a + a1) * size
        p2x = x2 + math.cos(a - a1) * size
        p2y = y2 + math.sin(a - a1) * size
        p3x = x2 + math.cos(a - math.pi / 2) * size * 1.9
        p3y = y2 + math.sin(a - math.pi / 2) * size * 1.9

        
        return [p1x, p1y, x2, y2, p2x, p2y, p3x, p3y]
    
