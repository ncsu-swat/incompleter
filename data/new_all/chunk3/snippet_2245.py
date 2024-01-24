# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56068629/how-to-fix-filenotfounderror-in-file-moving-script-when-it-reads-the-filenames
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import shutil
    _l_(576739)

except ImportError:
    pass
try:
    import os
    _l_(576741)

except ImportError:
    pass
try:
    from pathlib import Path
    _l_(576743)

except ImportError:
    pass

assets_path = _c_(576745, _n_(576744, "Path", lambda: Path), "/Users/Jackson Clark/Desktop/uploads")
_l_(576746)
export_path = _c_(576748, _n_(576747, "Path", lambda: Path), "/Users/Jackson Clark/Desktop/uploads")
_l_(576749)

source = _c_(576753, _a_(576751, _n_(576750, "os", lambda: os), "listdir"), _n_(576752, "assets_path", lambda: assets_path))
_l_(576754)

'''
NOTE: Filters.js is the important file
The logic:
    - Go through each file in the assets_path directory
    - Rename the files to start with RoCode (this could be a seperate script)
    - Create a new directory with the first four characters of the files name
    - Create two sub directories with the names 'image' and 'thumb'
    - Copy the file to both the 'image' and 'thumb' directories
    That should be all, but who knows tbh
Good links:
    - https://www.pythonforbeginners.com/os/python-the-shutil-module
    - https://stackabuse.com/creating-and-deleting-directories-with-python/
'''
_l_(576755)
for f in _n_(576756, "source", lambda: source):
    _l_(576864)

    f_string = _c_(576759, _n_(576757, "str", lambda: str), _n_(576758, "f", lambda: f))
    _l_(576760)
    folder_one_name = _n_(576761, "f_string", lambda: f_string)[0:2]
    _l_(576762)
    folder_two_name = _n_(576763, "f_string", lambda: f_string)[2:4]
    _l_(576764)

    path_to_export_one = _c_(576770, _a_(576767, _a_(576766, _n_(576765, "os", lambda: os), "path"), "join"), _n_(576768, "export_path", lambda: export_path), _n_(576769, "folder_one_name", lambda: folder_one_name))
    _l_(576771)
    path_to_export_two = _c_(576778, _a_(576774, _a_(576773, _n_(576772, "os", lambda: os), "path"), "join"), _n_(576775, "export_path", lambda: export_path), _n_(576776, "folder_one_name", lambda: folder_one_name),
                                      _n_(576777, "folder_two_name", lambda: folder_two_name))
    _l_(576779)

    try:
        _l_(576863)

        _c_(576783, _a_(576781, _n_(576780, "os", lambda: os), "mkdir"), _n_(576782, "path_to_export_one", lambda: path_to_export_one))
        _l_(576784)
        _c_(576788, _a_(576786, _n_(576785, "os", lambda: os), "mkdir"), _n_(576787, "path_to_export_two", lambda: path_to_export_two))
        _l_(576789)
        _c_(576797, _a_(576791, _n_(576790, "os", lambda: os), "mkdir"), _c_(576796, _a_(576794, _a_(576793, _n_(576792, "os", lambda: os), "path"), "join"), _n_(576795, "path_to_export_two", lambda: path_to_export_two), "image"))
        _l_(576798)
        _c_(576806, _a_(576800, _n_(576799, "os", lambda: os), "mkdir"), _c_(576805, _a_(576803, _a_(576802, _n_(576801, "os", lambda: os), "path"), "join"), _n_(576804, "path_to_export_two", lambda: path_to_export_two), "thumb"))
        _l_(576807)
        _c_(576816, _a_(576809, _n_(576808, "shutil", lambda: shutil), "copy"), _n_(576810, "f", lambda: f), _c_(576815, _a_(576813, _a_(576812, _n_(576811, "os", lambda: os), "path"), "join"), _n_(576814, "path_to_export_two", lambda: path_to_export_two), "image"))
        _l_(576817)
        _c_(576826, _a_(576819, _n_(576818, "shutil", lambda: shutil), "copy"), _n_(576820, "f", lambda: f), _c_(576825, _a_(576823, _a_(576822, _n_(576821, "os", lambda: os), "path"), "join"), _n_(576824, "path_to_export_two", lambda: path_to_export_two), "thumb"))
        _l_(576827)
    except _n_(576828, "FileExistsError", lambda: FileExistsError) as err:
        _l_(576856)

        try:
            _l_(576855)

            _c_(576837, _a_(576830, _n_(576829, "shutil", lambda: shutil), "copy"), _n_(576831, "f", lambda: f), _c_(576836, _a_(576834, _a_(576833, _n_(576832, "os", lambda: os), "path"), "join"), _n_(576835, "path_to_export_two", lambda: path_to_export_two), "image"))
            _l_(576838)
            _c_(576847, _a_(576840, _n_(576839, "shutil", lambda: shutil), "copy"), _n_(576841, "f", lambda: f), _c_(576846, _a_(576844, _a_(576843, _n_(576842, "os", lambda: os), "path"), "join"), _n_(576845, "path_to_export_two", lambda: path_to_export_two), "thumb"))
            _l_(576848)
        except _n_(576849, "FileNotFoundError", lambda: FileNotFoundError) as err:
            _l_(576854)

            _c_(576852, _n_(576850, "print", lambda: print), "FileNotFoundError2 on " + _n_(576851, "f", lambda: f) + " file")
            _l_(576853)
    except _n_(576857, "FileNotFoundError", lambda: FileNotFoundError) as err:
        _l_(576862)

        _c_(576860, _n_(576858, "print", lambda: print), "FileNotFoundError1 on " + _n_(576859, "f", lambda: f) + " file")
        _l_(576861)