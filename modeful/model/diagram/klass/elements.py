
from modeful.model import Model

class ClassElement(Model):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.prop_to_model('attributes', ClassAttribute)

        
class ClassAttribute(Model):
    pass


class Association(Model):
    pass
