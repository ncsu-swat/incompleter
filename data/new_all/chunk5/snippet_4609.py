# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/54243287/using-cythonized-code-causing-typeerror-hasattr-attribute-name-must-be-stri
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from distutils.core import setup
    _l_(705339)

except ImportError:
    pass
try:
    from distutils.extension import Extension
    _l_(705341)

except ImportError:
    pass
try:
    import os
    _l_(705343)

except ImportError:
    pass
try:
    import sys
    _l_(705345)

except ImportError:
    pass
try:
    from Cython.Build import cythonize
    _l_(705347)

except ImportError:
    pass
try:
    from Cython.Distutils import build_ext
    _l_(705349)

except ImportError:
    pass
try:
    from Cython.Compiler import Options
    _l_(705351)

except ImportError:
    pass

_n_(705352, "Options", lambda: Options).emit_code_commments = False
_l_(705353)
_n_(705354, "Options", lambda: Options).generate_cleanup_code = True
_l_(705355)


TOP_DIR = "root"
_l_(705356)
NAME = "root"
_l_(705357)
PACKAGES = [
"root",
]
_l_(705358)
INCLUDE = []
_l_(705359)

file_ending = ".py"
_l_(705360)
COMPILE_ARGS = ["-O3", "-Wall"]
_l_(705361)
LINK_ARGS = ["-g"]
_l_(705362)


def get_extensions(directory):
    _l_(705437)

    extensions = _c_(705364, _n_(705363, "list", lambda: list))
    _l_(705365)

    for f in _c_(705369, _a_(705367, _n_(705366, "os", lambda: os), "listdir"), _n_(705368, "directory", lambda: directory)):
        _l_(705434)

        path = _c_(705375, _a_(705372, _a_(705371, _n_(705370, "os", lambda: os), "path"), "join"), _n_(705373, "directory", lambda: directory), _n_(705374, "f", lambda: f))
        _l_(705376)
        if _c_(705381, _a_(705379, _a_(705378, _n_(705377, "os", lambda: os), "path"), "isfile"), _n_(705380, "path", lambda: path)) and _c_(705385, _a_(705383, _n_(705382, "path", lambda: path), "endswith"), _n_(705384, "file_ending", lambda: file_ending)):
            _l_(705433)

            path_split = _c_(705390, _a_(705388, _a_(705387, _n_(705386, "os", lambda: os), "path"), "split"), _n_(705389, "path", lambda: path))
            _l_(705391)

            ext_name = _c_(705397, _a_(705393, _n_(705392, "path_split", lambda: path_split)[0], "replace"), _a_(705396, _a_(705395, _n_(705394, "os", lambda: os), "path"), "sep"), ".")
            _l_(705398)

            module_name = _n_(705399, "path_split", lambda: path_split)[1][:-_c_(705402, _n_(705400, "len", lambda: len), _n_(705401, "file_ending", lambda: file_ending))]
            _l_(705403)
            if _n_(705404, "module_name", lambda: module_name) != "__init__":
                _l_(705409)

                ext_name += "." + _c_(705407, _n_(705405, "str", lambda: str), _n_(705406, "module_name", lambda: module_name))
                _l_(705408)


            _c_(705418, _a_(705411, _n_(705410, "extensions", lambda: extensions), "append"), _c_(705417, _n_(705412, "Extension", lambda: Extension), _n_(705413, "ext_name", lambda: ext_name),
                    [
                        _n_(705414, "path", lambda: path),
                    ],
                    include_dirs=[
                        ".",
                    ],
                    extra_compile_args=_n_(705415, "COMPILE_ARGS", lambda: COMPILE_ARGS),
                    extra_link_args=_n_(705416, "LINK_ARGS", lambda: LINK_ARGS),
                )
            )
            _l_(705419)
        elif _c_(705424, _a_(705422, _a_(705421, _n_(705420, "os", lambda: os), "path"), "isdir"), _n_(705423, "path", lambda: path)):
            _l_(705432)

            _c_(705430, _a_(705426, _n_(705425, "extensions", lambda: extensions), "extend"), _c_(705429, _n_(705427, "get_extensions", lambda: get_extensions), _n_(705428, "path", lambda: path)))
            _l_(705431)
    aux = _n_(705435, "extensions", lambda: extensions)
    _l_(705436)

    return aux


# Build Extension objects
extensions = _c_(705440, _n_(705438, "get_extensions", lambda: get_extensions), _n_(705439, "TOP_DIR", lambda: TOP_DIR))
_l_(705441)

# Do setup
_c_(705450, _n_(705442, "setup", lambda: setup), name=_n_(705443, "NAME", lambda: NAME),
    packages=_n_(705444, "PACKAGES", lambda: PACKAGES),
    ext_modules=_c_(705447, _n_(705445, "cythonize", lambda: cythonize), _n_(705446, "extensions", lambda: extensions),
        compiler_directives={
            "language_level": "3",
        },
    ),
    include_dirs=_n_(705448, "INCLUDE", lambda: INCLUDE),
    cmdclass={
        "build_ext": _n_(705449, "build_ext", lambda: build_ext),
    },
)
_l_(705451)