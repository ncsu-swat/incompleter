# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/69438841/f-writebuf-typeerror-a-bytes-like-object-is-required-not-str
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(357790)

except ImportError:
    pass
try:
    import zlib
    _l_(357792)

except ImportError:
    pass

_np = _a_(357795, _a_(357794, _n_(357793, "os", lambda: os), "path"), "normpath")
_l_(357796)
_j = _a_(357799, _a_(357798, _n_(357797, "os", lambda: os), "path"), "join")
_l_(357800)
def make_path(a, b):
    _l_(357810)

    aux = _c_(357808, _a_(357807, _c_(357806, _n_(357801, "_np", lambda: _np), _c_(357805, _n_(357802, "_j", lambda: _j), _n_(357803, "a", lambda: a), _n_(357804, "b", lambda: b))), "replace"), "\\", "/")
    _l_(357809)
    return aux

def get_crc32(filename):
    _l_(357825)

    crc = 0
    _l_(357811)
    with _c_(357814, _n_(357812, "open", lambda: open), _n_(357813, "filename", lambda: filename), "rb") as f:
        _l_(357822)

        crc = _c_(357820, _a_(357816, _n_(357815, "zlib", lambda: zlib), "crc32"), _c_(357819, _a_(357818, _n_(357817, "f", lambda: f), "read")))
        _l_(357821)
    aux = "%x" % (_n_(357823, "crc", lambda: crc) & 0xffFFffFF)
    _l_(357824)
    return aux

def get_mtime(filename):
    _l_(357838)

    # http://support.microsoft.com/kb/167296
    # How To Convert a UNIX time_t to a Win32 FILETIME or SYSTEMTIME
    EPOCH_AS_FILETIME = 116444736000000000 # January 1, 1970 as MS file time
    _l_(357826) # January 1, 1970 as MS file time
    HUNDREDS_OF_NANOSECONDS = 10000000
    _l_(357827)
    aux = _n_(357828, "EPOCH_AS_FILETIME", lambda: EPOCH_AS_FILETIME) + _c_(357835, _n_(357829, "int", lambda: int), _c_(357834, _a_(357832, _a_(357831, _n_(357830, "os", lambda: os), "path"), "getmtime"), _n_(357833, "filename", lambda: filename))) * _n_(357836, "HUNDREDS_OF_NANOSECONDS", lambda: HUNDREDS_OF_NANOSECONDS)
    _l_(357837)
    return aux

input_folder = _c_(357840, _n_(357839, "_np", lambda: _np), "client")
_l_(357841)
output_folder = _c_(357843, _n_(357842, "_np", lambda: _np), "web")
_l_(357844)
output_version = _c_(357846, _n_(357845, "_np", lambda: _np), "0.0.0.2")
_l_(357847)
output_fv = _c_(357851, _n_(357848, "make_path", lambda: make_path), _n_(357849, "output_folder", lambda: output_folder), _n_(357850, "output_version", lambda: output_version))
_l_(357852)
output_crclist = _c_(357855, _n_(357853, "make_path", lambda: make_path), _n_(357854, "output_fv", lambda: output_fv), "crclist")
_l_(357856)

file_list = []
_l_(357857)
for root, dir, files in _c_(357861, _a_(357859, _n_(357858, "os", lambda: os), "walk"), _n_(357860, "input_folder", lambda: input_folder)):
    _l_(357906)

    for filename in _n_(357862, "files", lambda: files):
        _l_(357905)

        file_elem = {}
        _l_(357863)
        _n_(357864, "file_elem", lambda: file_elem)["path"] = _c_(357868, _n_(357865, "make_path", lambda: make_path), _n_(357866, "root", lambda: root), _n_(357867, "filename", lambda: filename))
        _l_(357869)
        _n_(357870, "file_elem", lambda: file_elem)["real_path"] = _c_(357876, _a_(357875, _n_(357871, "file_elem", lambda: file_elem)["path"][_c_(357874, _n_(357872, "len", lambda: len), _n_(357873, "input_folder", lambda: input_folder))+1:], "replace"), "/", "\\")
        _l_(357877)
        # crc32 calculation
        _n_(357878, "file_elem", lambda: file_elem)["crc32"] = _c_(357881, _n_(357879, "get_crc32", lambda: get_crc32), _n_(357880, "file_elem", lambda: file_elem)["path"])
        _l_(357882)
        # size calculation
        _n_(357883, "file_elem", lambda: file_elem)["size"] = _c_(357888, _a_(357886, _a_(357885, _n_(357884, "os", lambda: os), "path"), "getsize"), _n_(357887, "file_elem", lambda: file_elem)["path"])
        _l_(357889)
        # mtime calculation
        mtime = _c_(357892, _n_(357890, "get_mtime", lambda: get_mtime), _n_(357891, "file_elem", lambda: file_elem)["path"])
        _l_(357893)
        _n_(357894, "file_elem", lambda: file_elem)["mtime1"] = _n_(357895, "mtime", lambda: mtime) >> 32
        _l_(357896)
        _n_(357897, "file_elem", lambda: file_elem)["mtime2"] = _n_(357898, "mtime", lambda: mtime) & 0xFFffFFff
        _l_(357899)
        # add in list
        _c_(357903, _a_(357901, _n_(357900, "file_list", lambda: file_list), "append"), _n_(357902, "file_elem", lambda: file_elem))
        _l_(357904)

# make path if missing
if not _c_(357911, _a_(357909, _a_(357908, _n_(357907, "os", lambda: os), "path"), "exists"), _n_(357910, "output_fv", lambda: output_fv)):
    _l_(357917)

    _c_(357915, _a_(357913, _n_(357912, "os", lambda: os), "makedirs"), _n_(357914, "output_fv", lambda: output_fv))
    _l_(357916)

# generate crclist
_c_(357919, _n_(357918, "print", lambda: print), "Generating crclist:")
_l_(357920)
with _c_(357923, _n_(357921, "open", lambda: open), _n_(357922, "output_crclist", lambda: output_crclist), "wb") as f:
    _l_(357943)

    for elem in _n_(357924, "file_list", lambda: file_list):
        _l_(357942)

        buf = "%s %d %d %d %s\n" % (_n_(357925, "elem", lambda: elem)["crc32"], _n_(357926, "elem", lambda: elem)["size"], _n_(357927, "elem", lambda: elem)["mtime1"], _n_(357928, "elem", lambda: elem)["mtime2"], _n_(357929, "elem", lambda: elem)["real_path"])
        _l_(357930)
        _c_(357934, _a_(357932, _n_(357931, "f", lambda: f), "write"), _n_(357933, "buf", lambda: buf))
        _l_(357935)
        _c_(357940, _n_(357936, "print", lambda: print), _c_(357939, _a_(357938, _n_(357937, "buf", lambda: buf), "replace"), "\n", ""))
        _l_(357941)

# generate lz files
ENABLE_LZ_GENERATION = True
_l_(357944)
if _n_(357945, "ENABLE_LZ_GENERATION", lambda: ENABLE_LZ_GENERATION):
    _l_(357992)

    try:
        import subprocess
        _l_(357947)

    except ImportError:
        pass
    _c_(357949, _n_(357948, "print", lambda: print), "Generating .lz:")
    _l_(357950)
    for elem in _n_(357951, "file_list", lambda: file_list):
        _l_(357991)

        filepath_in = _c_(357955, _n_(357952, "make_path", lambda: make_path), _n_(357953, "input_folder", lambda: input_folder), _n_(357954, "elem", lambda: elem)["real_path"])
        _l_(357956)
        filepath_out = _c_(357960, _n_(357957, "make_path", lambda: make_path), _n_(357958, "output_fv", lambda: output_fv), _n_(357959, "elem", lambda: elem)["real_path"]) + ".lz"
        _l_(357961)
        # create out dir
        dirpath_out = _c_(357966, _a_(357964, _a_(357963, _n_(357962, "os", lambda: os), "path"), "dirname"), _n_(357965, "filepath_out", lambda: filepath_out))
        _l_(357967)
        if not _c_(357972, _a_(357970, _a_(357969, _n_(357968, "os", lambda: os), "path"), "exists"), _n_(357971, "dirpath_out", lambda: dirpath_out)):
            _l_(357978)

            _c_(357976, _a_(357974, _n_(357973, "os", lambda: os), "makedirs"), _n_(357975, "dirpath_out", lambda: dirpath_out))
            _l_(357977)
        # create lz
        cmd = 'mt2lz pack "%s" "%s"' % (_n_(357979, "filepath_in", lambda: filepath_in), _n_(357980, "filepath_out", lambda: filepath_out))
        _l_(357981)
        _c_(357985, _a_(357983, _n_(357982, "subprocess", lambda: subprocess), "call"), _n_(357984, "cmd", lambda: cmd), shell=True)
        _l_(357986)
        _c_(357989, _n_(357987, "print", lambda: print), _n_(357988, "cmd", lambda: cmd))
        _l_(357990)
#