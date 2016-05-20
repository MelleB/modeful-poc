
from modeful.event import Event
from modeful.model import Model

class FileManager():

    files = {}

    def __init__(self):
        Event.on(Event.FILE_LOAD, self.on_file_load)
        Event.on(Event.FILE_SAVE, self.on_file_save)

    def on_file_load(self, filename):
        if filename in self.files:
            return

        self.files[filename] = File(filename)

    def on_file_save(self, filename):
        if filename in self.files:
            self.files[filename].save()

class File():

    has_changes = False

    def __init__(self, filename):
        self.name = filename
        self.model = Model.from_file(filename)
        self.model.bind(change=self.on_model_change, children=True)

        Event.emit(Event.FILE_LOADED, self)

    def on_model_change(self, model, prop_name, value):
        self.has_changes = True

    def save(self):
        self.model.to_file(self.name)

