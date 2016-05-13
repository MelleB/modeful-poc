

from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout

from modeful import Mode
from modeful.event import Event

class ModeBar(BoxLayout):

    mode_mapping = {
        'command': Mode.COMMAND,
        'link': Mode.LINK
    }
        
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_state(self, event):
        btn, state = event
        if state != 'down':
            return

        Event.emit(Event.MODE_CHANGED,
                   self.mode_mapping.get(btn.mode, Mode.COMMAND))
