from modeful.event import Event
from modeful.keymap.common import Common


class Handler(Common):
    def __init__(self, keymap):
        super()
        self.switch_keymap(keymap)

    def get(self):
        return self._on_key_down

    def switch_keymap(self, keymap):
        self.keymap = keymap
        self.current_keymap = self.keymap
        
    def _on_key_down(self, window, keycode, codepoint, text, modifiers):
        #self.root.log_output.text = "%s (modifiers: %s) (text: %s)\n" % (keycode[1], modifiers, text)
        #self.root.log_output.text += "\n\n%r" % self.current_keymap
        m = self._get_modifier_code(modifiers)
        k = (keycode, m)

        if k in self.current_keymap:
            if isinstance(self.current_keymap[k], str):
                event = self.current_keymap[k]
                self.current_keymap = self.keymap
                Event.emit(event)
            else:
                self.current_keymap = self.current_keymap[k]
        
        return True

        
