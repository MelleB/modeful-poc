
import importlib

from modeful.model import Model
from modeful.model.diagram import Diagram
from modeful.model.diagram.klass.elements import ClassElement, \
                                                 Association, \
                                                 DirectedAssociation, \
                                                 Generalization, \
                                                 Aggregation, \
                                                 Composition

class ClassDiagram(Diagram):

    prop_mapping = {
        'elements': {'class': ClassElement},
        'associations': { 'association': Association,
                          'directed-association': DirectedAssociation,
                          'generalization': Generalization,
                          'aggregation': Aggregation,
                          'composition': Composition
        },
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)




    
