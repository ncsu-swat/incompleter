# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67690534/filenotfounderror-when-using-shutil-copy
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import shutil
    _l_(583324)

except ImportError:
    pass
destination_folder = "path_to_the_destination_folder"
_l_(583325)
source_file = "path_to_source_file\file1.pdf"
_l_(583326)
destination_file = "f{destination_folder}\any_random_folder_from_n_nested_folders\file1.pdf"
_l_(583327)
new_file= _c_(583332, _a_(583329, _n_(583328, "shutil", lambda: shutil), "copy"), _n_(583330, "source_file", lambda: source_file), _n_(583331, "destination_file", lambda: destination_file) )
_l_(583333)
_c_(583336, _n_(583334, "print", lambda: print), _n_(583335, "new_file", lambda: new_file))
_l_(583337)