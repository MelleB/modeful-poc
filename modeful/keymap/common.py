from enum import IntEnum

class ModifierKeys(IntEnum):
    SHIFT = 1
    CONTROL = 2
    ALT = 4
    META = 8

class Common:
    def _get_modifier_code(self, modifiers):
        c = 0
        for m in modifiers:
            if   m == 'S' or m == 'shift': c |= ModifierKeys.SHIFT
            elif m == 'C' or m == 'ctrl' : c |= ModifierKeys.CONTROL
            elif m == 'A' or m == 'alt' :  c |= ModifierKeys.ALT
            elif m == 'M' or m == 'super': c |= ModifierKeys.META
        return c
