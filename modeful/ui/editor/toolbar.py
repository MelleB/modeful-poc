from kivy.uix.boxlayout import BoxLayout
from kivy.uix.togglebutton import ToggleButton
from kivy.properties import StringProperty

from modeful.event import Event

#FIXME: This should be moved inside the diagram, since every diagram type has it's own set of tools
class Toolbar(BoxLayout):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        Event.on(Event.TOOL_SELECTED, self.on_tool_selected)

    def on_tool_selected(self, tool):
        for c in self.children:
            if hasattr(c, 'tool'):
                if c.state == 'down' and c.tool != tool:
                    c.state = 'normal'
                elif c.state != 'down' and c.tool == tool:
                    c.state = 'down'

                

class ToolbarItem(ToggleButton):

    tool = StringProperty(None)

    def on_state(self, _, state):
        if state == 'down':
            Event.emit(Event.TOOL_SELECTED, self.tool)

    
    
