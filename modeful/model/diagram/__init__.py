
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

        Event.on(Event.MODEL_ELEMENT_ADD_ + self.id, self.add_element)
        Event.on(Event.MODEL_RELATIONSHIP_ADD_ + self.id, self.add_association)

    def add_element(self, type, **kwargs):
        cls = self.prop_mapping['elements'][type]
        e = cls(type=type, **kwargs)
        e.diagram = self
        self.elements.append(e)

        Event.emit(Event.MODEL_ELEMENT_ADDED_ + self.id, e)

    def add_association(self, type, **kwargs):
        cls = self.prop_mapping['associations'][type]
        a = cls(type=type, **kwargs)
        a.diagram = self
        self.associations.append(a)

        Event.emit(Event.MODEL_RELATIONSHIP_ADDED_ + self.id, a)

    def get_element_by_id(self, id):
        return self.element_dict.get(id, None)
