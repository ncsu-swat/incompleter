# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57443462/filenotfounderror-winerror-2-the-system-cannot-find-the-file-specified-exift
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import exiftool
    _l_(421573)

except ImportError:
    pass

files = ['file.MP4', 'file.MP4']
_l_(421574)

with _c_(421577, _a_(421576, _n_(421575, "exiftool", lambda: exiftool), "ExifTool")) as et:
    _l_(421583)

    metadata = _c_(421581, _a_(421579, _n_(421578, "et", lambda: et), "get_metadata_batch"), _n_(421580, "files", lambda: files))
    _l_(421582)
for d in _n_(421584, "metadata", lambda: metadata):
    _l_(421592)

    _c_(421590, _n_(421585, "print", lambda: print), _c_(421589, _a_(421586, "{:20.20} {:20.20}", "format"), _n_(421587, "d", lambda: d)["SourceFile"],
                                     _n_(421588, "d", lambda: d)["EXIF:DateTimeOriginal"]))
    _l_(421591)