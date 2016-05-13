
from modeful.model import Model

class Diagram(Model):

    element_dict = {}
    prop_mapping = {}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for k, v in self.prop_mapping.items():
            self.prop_to_model(k, v)

        for e in self.elements:
            e.diagram = self
            self.element_dict[e.id] = e

        for a in self.associations:
            a.diagram = self

    def get_element_by_id(self, id):
        return self.element_dict.get(id, None)
