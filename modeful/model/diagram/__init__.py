
from modeful.model import Model
from modeful.event import Event

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

        Event.on(Event.MODEL_ELEMENT_ADD_ + str(self.id), self.add_element)

    def add_element(self, type, **kwargs):
        cls = self.prop_mapping['elements'][type]
        e = cls(type=type, **kwargs)
        self.elements.append(e)

        Event.emit(Event.MODEL_ELEMENT_ADDED_ + str(self.id), e)

    def get_element_by_id(self, id):
        return self.element_dict.get(id, None)
