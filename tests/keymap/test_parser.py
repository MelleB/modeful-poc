
import unittest

from modeful import Mode
from modeful.keymap.parser import Parser

class ParserTestCase(unittest.TestCase):

    def test_parse_simple(self):
        keymap_dict = {
            Mode.LINK: [
                ('command.func_x', 'x'),
                ('command.func_y', 'y'),
                ('command.func_z', 'z')
            ]
        }

        keymap = Parser().parse_keymap(keymap_dict)

        self.assertIn(Mode.LINK, keymap_dict)

        values = list(keymap[Mode.LINK].items())
        self.assertIn(((ord('x'), 0), 'COMMAND_FUNC_X'), values)
        self.assertIn(((ord('y'), 0), 'COMMAND_FUNC_Y'), values)
        self.assertIn(((ord('z'), 0), 'COMMAND_FUNC_Z'), values)

    def test_key_sequence(self):
        keymap_dict = {Mode.LINK: [ ('AB', 'a b' ), ('CD', 'c d') ]}
        keymap = Parser().parse_keymap(keymap_dict)[Mode.LINK]

        a = (ord('a'), 0)
        b = (ord('b'), 0)
        c = (ord('c'), 0)
        d = (ord('d'), 0)

        self.assertIn(a, keymap)
        self.assertIn(b, keymap[a])
        self.assertEqual('AB', keymap[a][b])
        
        self.assertIn(c, keymap)
        self.assertIn(d, keymap[c])
        self.assertEqual('CD', keymap[c][d])

    def test_overlapping_key_sequence(self):
        keymap_dict = {Mode.LINK: [ ('AB', 'a b' ), ('AC', 'a c') ]}
        keymap = Parser().parse_keymap(keymap_dict)[Mode.LINK]

        a = (ord('a'), 0)
        b = (ord('b'), 0)
        c = (ord('c'), 0)

        self.assertIn(a, keymap)
        self.assertIn(b, keymap[a])
        self.assertEqual('AB', keymap[a][b])

        self.assertIn(c, keymap[a])
        self.assertEqual('AC', keymap[a][c])
        


    
        

