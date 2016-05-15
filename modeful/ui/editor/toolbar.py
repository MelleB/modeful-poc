from kivy.uix.boxlayout import BoxLayout
from kivy.uix.togglebutton import ToggleButton
from kivy.properties import StringProperty

from modeful.event import Event

#FIXME: This should be moved inside the diagram, since every diagram type has it's own set of tools
class Toolbar(BoxLayout):
    pass

class ToolbarItem(ToggleButton):

    tool = StringProperty(None)

    def on_state(self, _, state):
        if state == 'down':
            Event.emit(Event.TOOL_SELECTED, self.tool)

    
    
