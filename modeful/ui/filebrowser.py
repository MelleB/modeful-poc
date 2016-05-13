
import libs.garden.filebrowser as garden

from modeful.event import Event 

class FileBrowser(garden.FileBrowser):

    filters = ['*.mdfl']
    path = '.'
    select_string = 'Select'

    def __init__(self, cancel_cb):
        super().__init__()
        Event.on(Event.FILEBROWSER_CANCEL, cancel_cb)

    def on_success(self, *args):
        if self.selection:
            Event.emit(Event.FILE_LOAD, self.selection[0])

    def on_canceled(self, *args):
        Event.emit(Event.FILEBROWSER_CANCEL)
    
