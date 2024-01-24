# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/70685618/copying-files-with-concurrent-futures-raising-attributeerror-silently
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def download_files(directories: _n_(553258, "set", lambda: set), path_tuples: _n_(553259, "set", lambda: set)) -> _a_(553261, _n_(553260, "os", lambda: os), "path"):
    _l_(553335)

    """Copies the files"""
    def copy_file(_path_tuple: _n_(553262, "tuple", lambda: tuple)):
        _l_(553288)

        from_path, to_path = _n_(553263, "_path_tuple", lambda: _path_tuple)
        _l_(553264)
        try:
            _l_(553287)

            _c_(553269, _a_(553266, _n_(553265, "shutil", lambda: shutil), "copy"), _n_(553267, "from_path", lambda: from_path), _n_(553268, "to_path", lambda: to_path))
            _l_(553270)
            aux = _n_(553271, "to_path", lambda: to_path)
            _l_(553272)
            return aux

        except _n_(553273, "PermissionError", lambda: PermissionError):
            _l_(553279)

            _c_(553277, _n_(553274, "print", lambda: print), f"Tried to copy file from {_n_(553275, 'from_path', lambda: from_path)} to {_n_(553276, 'to_path', lambda: to_path)}, but was denied access")
            _l_(553278)
        
        except _n_(553280, "FileNotFoundError", lambda: FileNotFoundError):
            _l_(553286)

            _c_(553284, _n_(553281, "print", lambda: print), f"Tried to copy file from {_n_(553282, 'from_path', lambda: from_path)} to {_n_(553283, 'to_path', lambda: to_path)}, but invalid path!")
            _l_(553285)

    _c_(553296, _n_(553289, "print", lambda: print), f"Found {_c_(553292, _n_(553290, 'len', lambda: len), _n_(553291, 'path_tuples', lambda: path_tuples))} files to copy, in {_c_(553295, _n_(553293, 'len', lambda: len), _n_(553294, 'directories', lambda: directories))}")
    _l_(553297)

    for directory in _n_(553298, "directories", lambda: directories):
        _l_(553326)

        if not _c_(553303, _a_(553301, _a_(553300, _n_(553299, "os", lambda: os), "path"), "exists"), _n_(553302, "directory", lambda: directory)):
            _l_(553325)

            _c_(553305, _n_(553304, "print", lambda: print), f"Local directory didn't exist, create it")
            _l_(553306)
            try:
                _l_(553324)

                _c_(553310, _a_(553308, _n_(553307, "os", lambda: os), "mkdir"), _n_(553309, "directory", lambda: directory))
                _l_(553311)
            except _n_(553312, "PermissionError", lambda: PermissionError):
                _l_(553317)

                _c_(553315, _n_(553313, "print", lambda: print), f"Tried to make folder at {_n_(553314, 'directory', lambda: directory)}, but was denied access")
                _l_(553316)
            except _n_(553318, "FileNotFoundError", lambda: FileNotFoundError):
                _l_(553323)

                _c_(553321, _n_(553319, "print", lambda: print), f"Tried to make folder at {_n_(553320, 'directory', lambda: directory)}, but invalid path!")
                _l_(553322)
    if _n_(553327, "path_tuples", lambda: path_tuples):
        _l_(553334)

        
        # with concurrent.futures.ProcessPoolExecutor() as executor:
        #     results = {executor.submit(copy_file, path_tuple) for path_tuple in path_tuples}
        #
        #     for target_path in concurrent.futures.as_completed(results):
        #         print(f"Done copying file {target_path}")
        
        for path_tuple in _n_(553328, "path_tuples", lambda: path_tuples):
            _l_(553333)

            _c_(553331, _n_(553329, "copy_file", lambda: copy_file), _n_(553330, "path_tuple", lambda: path_tuple))
            _l_(553332)