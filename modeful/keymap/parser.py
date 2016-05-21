import importlib

from collections import defaultdict

from modeful.keymap.common import Common

class Parser(Common):
    
    def parse_keymap(self, keymap_dict):
        keymap = {}
        for mode, keymap_lines in keymap_dict.items():
            keymap[mode] = defaultdict(dict)
            for func, shortcut in keymap_lines:
                event_name = func.upper().replace('.', '_')
                keymap_tmp = keymap[mode]

                keys = self._parse_shortcut(shortcut)
                for k in keys[:-1]:
                    keymap_tmp = keymap_tmp[k]
                
                keymap_tmp[keys[-1]] = event_name

        return keymap

    def _parse_shortcut(self, shortcuts):
        s = []
        for shortcut in shortcuts.split():
            keys = shortcut.split('-')
            m = self._get_modifier_code(keys[:-1])
            s.append((ord(keys[-1]), m)) 
        return s

