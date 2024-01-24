# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/44598427/open-a-html-file-inside-a-zip-file-python-3-6-typeerror-zipfile-object-is-n
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import zipfile
    _l_(559156)

except ImportError:
    pass


file = _c_(559159, _a_(559158, _n_(559157, "zipfile", lambda: zipfile), "ZipFile"), "John.zip", "r")
_l_(559160)


with _c_(559162, _n_(559161, "file", lambda: file), 'John.zip') as myzip:
    _l_(559173)

    with _c_(559165, _a_(559164, _n_(559163, "myzip", lambda: myzip), "open"), "news.html") as myfile:
        _l_(559172)

        _c_(559170, _n_(559166, "print", lambda: print), _c_(559169, _a_(559168, _n_(559167, "myfile", lambda: myfile), "read")))
        _l_(559171)