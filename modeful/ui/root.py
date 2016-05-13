from kivy.clock import Clock
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen

from modeful.event import Event
from modeful.ui.editor import Editor
from modeful.ui.filebrowser import FileBrowser

class EditorScreen(Screen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, name='editor')
        self.add_widget(Editor())

class FileBrowserScreen(Screen):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, name='filebrowser')
        Clock.schedule_once(self._setup)

    def _setup(self, _):
        #TODO: Show loading indicator since this might block the UI...
        self._filebrowser = FileBrowser(self.close) 
        self.add_widget(self._filebrowser)

        Event.on(Event.FILE_LOAD, self.close)

    def close(self, *args):
        self.manager.current = self.manager.previous()


class ModedRoot(ScreenManager):

    filebrowser = ObjectProperty(None)
    editor = ObjectProperty(None)

    def __init__(self, files=[], *args, **kwargs):
        super().__init__()

        self.transition.direction = 'up'
        Clock.schedule_once(lambda _: self._setup(files))
        
        Event.on(Event.COMMAND_FILE_OPEN, self.show_filebrowser)

    def _setup(self, files):
        self.editor = EditorScreen()
        self.add_widget(self.editor)

        for f in files:
            Event.emit(Event.FILE_LOAD, f)


    def show_filebrowser(self):
        if self.filebrowser is None:
            self.filebrowser = FileBrowserScreen()
            self.add_widget(self.filebrowser)
            
        self.current = self.filebrowser.name

        

