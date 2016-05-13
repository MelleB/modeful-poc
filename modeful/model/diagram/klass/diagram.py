
import importlib

from modeful.model import Model
from modeful.model.diagram import Diagram
from modeful.model.diagram.klass.elements import ClassElement, Association

class ClassDiagram(Diagram):

    prop_mapping = {
        'elements': {'class': ClassElement},
        'associations': Association
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)




    
