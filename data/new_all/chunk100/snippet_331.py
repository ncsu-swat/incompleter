# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/3451111/unzipping-files-in-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import zipfile
    _l_(61453)

except ImportError:
    pass
with _c_(61456, _a_(61455, _n_(61454, "zipfile", lambda: zipfile), "ZipFile"), "file.zip","r") as zip_ref:
    _l_(61461)

    _c_(61459, _a_(61458, _n_(61457, "zip_ref", lambda: zip_ref), "extractall"), "targetdir")
    _l_(61460)

