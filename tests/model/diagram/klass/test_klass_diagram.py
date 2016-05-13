import unittest

from modeful.model import Model
from modeful.model.diagram import Diagram
from modeful.model.diagram.klass.diagram import ClassDiagram
from modeful.model.diagram.klass.elements import ClassElement, ClassAttribute

class KlassDiagramTestCase(unittest.TestCase):

    def test_get_element_by_id(self):

        m = Model.from_file('./tests/testdata/class-diagram.mdfl')
        self.assertIsInstance(m, Diagram)
        
        e0 = m.elements[0]
        self.assertEqual(e0, m.get_element_by_id(e0.id))
        
