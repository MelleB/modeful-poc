import unittest

from modeful.model import Model
from modeful.model.diagram import Diagram
from modeful.model.diagram.klass.diagram import ClassDiagram
from modeful.model.diagram.klass.elements import ClassElement, ClassAttribute
from tests import DiagramTestCaseWithClassModel

class DiagramTestCase(DiagramTestCaseWithClassModel):

    def test_get_element_by_id(self):

        self.assertIsInstance(self.model, Diagram)
        
        e0 = self.model.elements[0]

        def equal(attr):
            self.assertEqual(
                getattr(e0, attr),
                getattr(self.model.get_element_by_id(e0.id), attr))

        [equal(a) for a in ['id', 'type', 'pos', 'size', 'attributes']] 

