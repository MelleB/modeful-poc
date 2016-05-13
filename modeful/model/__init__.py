
import collections
import toml
import importlib

from modeful.event import Event 

class Model(dict):
      _has_listners = False

      def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.__dict__ = self
            self.__getattr__ = dict.__getitem__

      def on_change(self, fn, *args, children=False):
            self._has_listners = True
            Event.on('MODEL_CHANGE_' + str(self.id), fn, *args)

            if children:
                  [self[p].on_change(fn, args, True) for p in self if isinstance(p, Model)]

      def __setattr__(self, name, value):
          super().__setattr__(name, value)
          if self._has_listners and name[0] != '_':
                Event.emit('MODEL_CHANGE_' + str(self.id), self, name, value)

      def prop_to_model(self, prop_name, map_obj):
            if not prop_name in self:
                  return

            def helper(prop):
                  if isinstance(map_obj, dict):
                        if prop['type'] not in map_obj:
                              print("Error: Unknown type %s found in property %s" \
                                    % (prop['type'], prop.__name__))
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
                  model = Model.determine_model(d['type'])
                  instance = model(d)
                  return instance

      @staticmethod
      def determine_model(typestr):
            clsname = typestr.title().replace('-','')
            pkgname = typestr.lower().replace('-', '.').replace("class", "klass")
            m = importlib.import_module('modeful.model.diagram.'+pkgname)
            cls = getattr(m, clsname)
            return cls

      @staticmethod
      def get_class(fq_name):
            module_name, cls_name = fq_name.rsplit('.', 1)
            m = importlib.import_module(module_name)
            cls = getattr(m, cls_name)
            return cls
