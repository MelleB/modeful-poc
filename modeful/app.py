import kivy
kivy.require('1.9.1')
from kivy.app import App
from kivy.config import Config
from kivy.core.window import Window

from modeful import __version__
from modeful.ui.root import ModedRoot

from kivy.uix.screenmanager import ScreenManager, Screen


class ModefulApp(App):

    title = "Moded " + __version__

    def __init__(self, files=[]):
        super().__init__()
        self.root = ModedRoot(files=files)

        # By default right click simulates mutli-touch in Kivy
        Config.set("input", "mouse", "mouse, disable_multitouch")

    def build(self):
        Window.size = (1024, 768)
        return self.root

    def on_build(self, *args):
        print('build', args)
