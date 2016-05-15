from kivy.app import App
from kivy.base import EventLoop
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

from modeful import Mode
from modeful.event import Event
from modeful.keymap.handler import Handler
from modeful.keymap.parser import Parser
from modeful.filemanager import FileManager
from modeful.ui.diagram import Diagram
from modeful.ui.tab import Tab

keymap_dict = {
    Mode.COMMAND: [
        ('command.keyboard.up', 'k'),
        ('command.keyboard.down', 'j'),
        ('command.keyboard.left', 'h'),
        ('command.keyboard.right', 'l'),
        ('command.file.open', 'f o')
    ],
    Mode.LINK: [
        ('command.func_x', 'C-l x'),
        ('command.func_y', 'C-l y'),
        ('command.func_z', 'C-l z')
    ],
}

class Editor(BoxLayout):

    current_mode = Mode.COMMAND
    _handler = None
    filemanager = FileManager()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        Clock.schedule_once(self._setup)

        Event.on(Event.MODE_CHANGED, self.on_mode_changed)
        Event.on(Event.FILE_LOADED, self.on_file_loaded)

    def _setup(self, *largs):
        self._keymap = Parser().parse_keymap(keymap_dict)
        self._handler = Handler(self._keymap[self.current_mode])

        window = EventLoop.window
        window.bind(on_keyboard=self._handler.get())

    def on_mode_changed(self, new_mode):
        if self.current_mode == new_mode:
            return

        new_keymap = self._keymap[new_mode]
        self._handler.switch_keymap(new_keymap)
        
        self.current_mode = new_mode

    def on_file_loaded(self, f):
        t = Tab(f)
        self.tabarea.add_widget(t)
        
        #FIXME: There should be a better way to handle this
        Clock.schedule_once(lambda _: self.tabarea.switch_to(t), .01)


        
        
