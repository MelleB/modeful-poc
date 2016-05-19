

from modeful.model import Model

class ClassElement(Model):

    x = 0
    y = 0
    size = (100, 30)
    name = 'Class'

    #TODO properties for abstract + interface
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.prop_to_model('attributes', ClassAttribute)

        
class ClassAttribute(Model):
    pass


class Association(Model):
    pass

class DirectedAssociation(Association):
    pass
