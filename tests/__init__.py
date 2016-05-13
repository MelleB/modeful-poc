import unittest

from modeful.model import Model

class DiagramTestCaseWithClassModel(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.model = Model.from_file('./tests/testdata/class-diagram.mdfl')
