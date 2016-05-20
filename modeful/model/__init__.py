
import collections
import importlib
import uuid
import toml

from modeful.event import Event

class EventEmitter():
    
    _listners = collections.defaultdict(list)

    def bind(self, children=False, **kwargs):
        for event_name, listner in kwargs.items():
            self._listners[event_name].append(listner)

            if children:
                [self[p].bind(change=(fn, args, {'children':True})) for p in self if isinstance(p, Model)]


    def emit(self, event_name, *args):
        for item in self._listners[event_name]:
            # Listners can be stored as a function
            # or a tuple/list of function with arguments
            item(*args) if callable(item) else item[0](item[1:], *args)
                        
class Model(dict, EventEmitter):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__dict__ = self
        self.__getattr__ = dict.__getitem__

        if not hasattr(self, 'id'):
            self.id = str(uuid.uuid4())

    def __setattr__(self, name, value):
        super().__setattr__(name, value)
        if name[0] != '_':
            self.emit('change', self, name, value)

    def prop_to_model(self, prop_name, map_obj):
        if not prop_name in self:
            return

        def helper(prop):
            if isinstance(map_obj, dict):
                if prop['type'] not in map_obj:
                    raise ValueError("Error: Unknown type %s found in property %s" \
                                    % (prop['type'], map_obj))
                else:
                    return map_obj[prop['type']](prop)
            else:
                return map_obj(prop)
            
        if isinstance(self[prop_name], collections.Iterable):
            for i, d in enumerate(self[prop_name]):
                self[prop_name][i] = helper(self[prop_name][i])
        else:
            self[prop_name] = helper(self[prop_name])

    @staticmethod
    def from_file(filename):
        with open(filename, 'r') as f:
            d = toml.load(f)
            model = Model._determine_model(d['type'])
            instance = model(d)
            return instance

    @staticmethod
    def _determine_model(typestr):
        clsname = typestr.title().replace('-','')
        pkgname = typestr.lower().replace('-', '.').replace("class", "klass")
        m = importlib.import_module('modeful.model.diagram.'+pkgname)
        cls = getattr(m, clsname)
        return cls
