# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67690534/filenotfounderror-when-using-shutil-copy
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import shutil
    _l_(580222)

except ImportError:
    pass
destination_folder = "path_to_the_destination_folder"
_l_(580223)
source_file = "path_to_source_file\file1.pdf"
_l_(580224)
destination_file = "f{destination_folder}\any_random_folder_from_n_nested_folders\file1.pdf"
_l_(580225)
new_file= _c_(580230, _a_(580227, _n_(580226, "shutil", lambda: shutil), "copy"), _n_(580228, "source_file", lambda: source_file), _n_(580229, "destination_file", lambda: destination_file) )
_l_(580231)
_c_(580234, _n_(580232, "print", lambda: print), _n_(580233, "new_file", lambda: new_file))
_l_(580235)