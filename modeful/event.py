_callbacks = {}

class Event():

    @staticmethod
    def on(event_name, f = None, *args, **kwargs):
        if f is not None:
            _callbacks[event_name] = _callbacks.get(event_name, []) + [(f, args)]
            return (f, args)
        else:
            return Event.on(event_name, f, *args) 


    @staticmethod
    def emit(event_name, *data, **kwargs):
        [f(*(args + data), **kwargs) for f, args in _callbacks.get(event_name, [])]

    @staticmethod
    def off(event_name, f):
        if f in _callbacks.get(event_name, []):
            _callbacks.get(event_name, []).remove(f)
            return True
        return False

# Add events as properties of Event class
_events = [
    'MODE_CHANGED',
    'COMMAND_KEYBOARD_UP',
    'COMMAND_KEYBOARD_DOWN',
    'COMMAND_KEYBOARD_LEFT',
    'COMMAND_KEYBOARD_RIGHT',
    'COMMAND_FILE_OPEN',
    'FILEBROWSER_CANCEL',
    'FILE_LOAD',
    'FILE_LOADED',
    'FILE_SAVE',
    'TOOL_SELECTED'
]
for e in _events:
    setattr(Event, e, e)
