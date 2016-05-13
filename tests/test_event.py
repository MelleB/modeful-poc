
import unittest

from modeful.event import Event

count = 0
cb = None

class EventTestCase(unittest.TestCase):

    def test_callbacks(self):

        class Test:

            state = 0

            def __init__(self):
                global cb
                Event.on('add', self.addXY)
                cb = Event.on('add', Test.addX)
            
            def addXY(self, x):
                self.state += 1

            @staticmethod
            def addX(x):
                global count
                count += x

        t = Test()

        Event.emit('add', 2)
        self.assertEqual(count, 2)
        self.assertEqual(t.state, 1)

        self.assertTrue(Event.off('add', cb))
        Event.emit('add', 2)
        self.assertEqual(count, 2)

    def test_name_in_class(self):
        self.assertEqual(Event.MODE_CHANGED, 'MODE_CHANGED')
