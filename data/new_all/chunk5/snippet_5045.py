# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/69686855/python-throws-nonetype-error-when-trying-to-write-to-yaml-file
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(663249)

except ImportError:
    pass
try:
    import YAML
    _l_(663251)

except ImportError:
    pass

drives = ["A:\\", "B:\\", "C:\\", "D:\\", "E:\\", 
          "F:\\", "G:\\", "H:\\", "I:\\", "J:\\", "L:\\"]
_l_(663252)

for drive in _n_(663253, "drives", lambda: drives):
    _l_(663323)

    _c_(663256, _n_(663254, "print", lambda: print), "Searching in drive: " + f"'{_n_(663255, 'drive', lambda: drive)}'")
    _l_(663257)
    dir_path = _n_(663258, "drive", lambda: drive)
    _l_(663259)
    for root, dirs, files in _c_(663263, _a_(663261, _n_(663260, "os", lambda: os), "walk"), _n_(663262, "dir_path", lambda: dir_path)):
        _l_(663322)

        for file in _n_(663264, "files", lambda: files):
            _l_(663321)


            # change the extension from '.mp3' to
            # the one of your choice.
            if _c_(663267, _a_(663266, _n_(663265, "file", lambda: file), "endswith"), '.exe'):
                _l_(663320)

                back = '\\'
                _l_(663268)
                _c_(663275, _n_(663269, "print", lambda: print), "File path: " + f"'{_n_(663270, 'root', lambda: root) + _n_(663271, 'back', lambda: back) + _c_(663274, _n_(663272, 'str', lambda: str), _n_(663273, 'file', lambda: file))}'")
                _l_(663276)
                program = _n_(663277, "file", lambda: file)
                _l_(663278)
                path = _n_(663279, "root", lambda: root) + _n_(663280, "back", lambda: back) + _c_(663283, _n_(663281, "str", lambda: str), _n_(663282, "file", lambda: file))
                _l_(663284)

                with _c_(663286, _n_(663285, "open", lambda: open), 'programs.yaml', 'r') as yaml_file:
                    _l_(663308)

                    cur_yaml = _c_(663290, _a_(663288, _n_(663287, "yaml", lambda: yaml), "safe_load"), _n_(663289, "yaml_file", lambda: yaml_file))
                    _l_(663291)
                    info = _n_(663292, "program", lambda: program) + ": " + _n_(663293, "path", lambda: path)
                    _l_(663294)
                    _c_(663297, _n_(663295, "print", lambda: print), "YAML data: " + f"'{_n_(663296, 'info', lambda: info)}'")
                    _l_(663298)
                    _c_(663302, _a_(663300, _n_(663299, "cur_yaml", lambda: cur_yaml), "append"), _n_(663301, "info", lambda: info))
                    _l_(663303)
                    _c_(663306, _n_(663304, "print", lambda: print), "curyaml:" + _n_(663305, "cur_yaml", lambda: cur_yaml))
                    _l_(663307)
                if _n_(663309, "cur_yaml", lambda: cur_yaml):
                    _l_(663319)

                    with _c_(663311, _n_(663310, "open", lambda: open), 'programs.yaml', 'w') as yaml_file:
                        _l_(663318)

                        _c_(663316, _a_(663313, _n_(663312, "yaml", lambda: yaml), "safe_dump"), _n_(663314, "cur_yaml", lambda: cur_yaml), _n_(663315, "yaml_file", lambda: yaml_file))
                        _l_(663317)