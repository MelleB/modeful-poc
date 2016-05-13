
import unittest

from modeful.model import Model
from modeful.model.diagram.klass.diagram import ClassDiagram
from modeful.model.diagram.klass.elements import ClassElement, ClassAttribute, Association
from tests import DiagramTestCaseWithClassModel

class ModelTestCase(DiagramTestCaseWithClassModel):

    def test_determine_model(self):
        typestrs = [
            ('class-diagram', ClassDiagram) 
        ]
        for s, expected in typestrs:
            self.assertEqual(expected, Model.determine_model(s))

    def test_from_file(self):
        m = self.model
        self.assertIsInstance(m, ClassDiagram)
        self.assertEqual(m['type'], 'class-diagram')

        self.assertEqual(len(m.elements), 4)
        self.assertIsInstance(m.elements[0], ClassElement)
        self.assertIsInstance(m.elements[3], ClassElement)
        
        self.assertEqual(len(m.elements[0].attributes), 2)
        self.assertIsInstance(m.elements[0].attributes[0], ClassAttribute)
        self.assertIsInstance(m.elements[0].attributes[1], ClassAttribute)

        self.assertEqual(len(m.associations), 1)
        self.assertIsInstance(m.associations[0], Association)

    _cb_called = False
    def _register_callback_called(self):
        self._cb_called = True
        
    def test_on_change(self):
        m = self.model
        e = m.elements[0]

        ae = self.assertEqual
        cb = self._register_callback_called
        def my_func(self, prop, value):
            cb()
            ae(prop, 'name')
            ae(value, 'Test')

        e.on_change(my_func)
        e.name = 'Test'

        self.assertTrue(self._cb_called)

    

        
        
