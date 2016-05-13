import operator

from kivy.properties import BooleanProperty

from modeful.event import Event

class KeyboardNavigationBehavior:

    _NAVIGATION_AXIS_THRESHOLD = 0.1

    element_list = []
    active_element = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        Event.on(Event.COMMAND_KEYBOARD_UP, self._move, 'y', '+')
        Event.on(Event.COMMAND_KEYBOARD_DOWN, self._move, 'y', '-')
        Event.on(Event.COMMAND_KEYBOARD_LEFT, self._move, 'x', '-')
        Event.on(Event.COMMAND_KEYBOARD_RIGHT, self._move, 'x', '+')
        

    def add_navigation_element(self, element):
        self.element_list.append(element)

    def set_active(self, element):
        if self.active_element == element:
            return
        
        if self.active_element is not None:
            self.active_element.active = False

        self.active_element = element
        self.active_element.active = True

    def move_in(self):
        pass

    def move_out(self):
        pass

    def _move(self, axis, direction):

        best = (self.active_element, float("inf"))
        ort_axis = 'y' if axis == 'x' else 'x'
        compare = operator.lt if direction == '+' else operator.gt

        axis_attr_ael = getattr(self.active_element, 'center_' + axis)
        ort_axis_attr_ael = getattr(self.active_element, 'center_' + ort_axis)

        for el in self.element_list:
            axis_attr_el = getattr(el, 'center_' + axis)
            if el == self.active_element or compare(axis_attr_el, axis_attr_ael):
                continue

            ort_axis_attr_el = getattr(el, 'center_' + ort_axis)
            d_axis = axis_attr_el - axis_attr_ael
            d_ort_axis = ort_axis_attr_el - ort_axis_attr_ael

            if d_ort_axis != 0.0 and abs(d_axis / d_ort_axis) < self._NAVIGATION_AXIS_THRESHOLD:
                continue

            # Use a custom distance function, axis diff is more important than ort_axis diff
            dist = d_axis**2 + d_ort_axis**2/2
            if dist < best[1]:
                best = (el, dist)

        if best[0] is not None:
            self.set_active(best[0])

        return best[0]


class KeyboardNavigationNode:
    
    active = BooleanProperty(False)

    def on_active(self, instance, value):
        pass



