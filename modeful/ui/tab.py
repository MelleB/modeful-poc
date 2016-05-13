import os.path

from kivy.core.window import Window
from kivy.uix.tabbedpanel import TabbedPanelHeader
from kivy.uix.stencilview import StencilView

from modeful.filemanager import File
from modeful.ui.diagram import Diagram

class Tab(TabbedPanelHeader):

    def __init__(self, file=None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.view = StencilView()
        self.view.background_color = (255, 0, 0, .5)
        self.view.size = Window.size

        self.file = file
        self.text = os.path.basename(file.name)[:-len('.mdfl')] 

        if file:
            self.diagram = Diagram(file.model)
            self.diagram.size = Window.size
            self.view.add_widget(self.diagram)
            self.content = self.view
        

