# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/71196458/python-3-10-filenotfounderror-existing-path-with-unicode-characters
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
for root, _, filenames in _c_(453234, _a_(453232, _n_(453231, "os", lambda: os), "walk"), _n_(453233, "maybe_dir", lambda: maybe_dir)):
    _l_(453283)

    for file in _n_(453235, "filenames", lambda: filenames):
        _l_(453282)

        # Prepare relative paths:
        relative_dir = _c_(453241, _a_(453238, _a_(453237, _n_(453236, "os", lambda: os), "path"), "relpath"), _n_(453239, "root", lambda: root), _n_(453240, "maybe_dir", lambda: maybe_dir))
        _l_(453242)
        relative_file = _c_(453248, _a_(453245, _a_(453244, _n_(453243, "os", lambda: os), "path"), "join"), _n_(453246, "relative_dir", lambda: relative_dir), _n_(453247, "file", lambda: file))
        _l_(453249)

        # Get unique filename:
        unique_filename = _a_(453253, _c_(453252, _a_(453251, _n_(453250, "uuid", lambda: uuid), "uuid4")), "hex")
        _l_(453254)
        unique_filename_with_ext = _n_(453255, "unique_filename", lambda: unique_filename) + _n_(453256, "file_extension", lambda: file_extension)
        _l_(453257)
        new_path_and_filename = _c_(453263, _a_(453260, _a_(453259, _n_(453258, "os", lambda: os), "path"), "join"), _n_(453261, "full_output_path", lambda: full_output_path), _n_(453262, "unique_filename_with_ext", lambda: unique_filename_with_ext)
        )
        _l_(453264)

        current_file = _c_(453274, _a_(453267, _a_(453266, _n_(453265, "os", lambda: os), "path"), "abspath"), _c_(453273, _a_(453270, _a_(453269, _n_(453268, "os", lambda: os), "path"), "join"), _n_(453271, "root", lambda: root), _n_(453272, "file", lambda: file)))
        _l_(453275)

        # Copying files:
        _c_(453280, _a_(453277, _n_(453276, "shutil", lambda: shutil), "copy"), _n_(453278, "current_file", lambda: current_file), _n_(453279, "new_path_and_filename", lambda: new_path_and_filename))
        _l_(453281)