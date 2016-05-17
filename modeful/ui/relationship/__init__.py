from kivy.uix.widget import Widget

class Relationship(Widget):

    @staticmethod
    def from_model(cls, model):
        c = Relationship(model, cls(model))
        model.on_change(c.redraw)
        return c

    def __init__(self, model, element, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.model = model
        self.element = element

        self.add_widget(element)
        
        self.bind(parent=self.redraw, size=self.redraw)

        src = self.model.diagram.get_element_by_id(self.model.src_id)
        dst = self.model.diagram.get_element_by_id(self.model.dst_id)
        src.on_change(self.redraw)
        dst.on_change(self.redraw)

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

    
