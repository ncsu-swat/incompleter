# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/69438841/f-writebuf-typeerror-a-bytes-like-object-is-required-not-str
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(359111)

except ImportError:
    pass
try:
    import zlib
    _l_(359113)

except ImportError:
    pass

_np = _a_(359116, _a_(359115, _n_(359114, "os", lambda: os), "path"), "normpath")
_l_(359117)
_j = _a_(359120, _a_(359119, _n_(359118, "os", lambda: os), "path"), "join")
_l_(359121)
def make_path(a, b):
    _l_(359131)

    aux = _c_(359129, _a_(359128, _c_(359127, _n_(359122, "_np", lambda: _np), _c_(359126, _n_(359123, "_j", lambda: _j), _n_(359124, "a", lambda: a), _n_(359125, "b", lambda: b))), "replace"), "\\", "/")
    _l_(359130)
    return aux

def get_crc32(filename):
    _l_(359146)

    crc = 0
    _l_(359132)
    with _c_(359135, _n_(359133, "open", lambda: open), _n_(359134, "filename", lambda: filename), "rb") as f:
        _l_(359143)

        crc = _c_(359141, _a_(359137, _n_(359136, "zlib", lambda: zlib), "crc32"), _c_(359140, _a_(359139, _n_(359138, "f", lambda: f), "read")))
        _l_(359142)
    aux = "%x" % (_n_(359144, "crc", lambda: crc) & 0xffFFffFF)
    _l_(359145)
    return aux

def get_mtime(filename):
    _l_(359159)

    # http://support.microsoft.com/kb/167296
    # How To Convert a UNIX time_t to a Win32 FILETIME or SYSTEMTIME
    EPOCH_AS_FILETIME = 116444736000000000 # January 1, 1970 as MS file time
    _l_(359147) # January 1, 1970 as MS file time
    HUNDREDS_OF_NANOSECONDS = 10000000
    _l_(359148)
    aux = _n_(359149, "EPOCH_AS_FILETIME", lambda: EPOCH_AS_FILETIME) + _c_(359156, _n_(359150, "int", lambda: int), _c_(359155, _a_(359153, _a_(359152, _n_(359151, "os", lambda: os), "path"), "getmtime"), _n_(359154, "filename", lambda: filename))) * _n_(359157, "HUNDREDS_OF_NANOSECONDS", lambda: HUNDREDS_OF_NANOSECONDS)
    _l_(359158)
    return aux

input_folder = _c_(359161, _n_(359160, "_np", lambda: _np), "client")
_l_(359162)
output_folder = _c_(359164, _n_(359163, "_np", lambda: _np), "web")
_l_(359165)
output_version = _c_(359167, _n_(359166, "_np", lambda: _np), "0.0.0.2")
_l_(359168)
output_fv = _c_(359172, _n_(359169, "make_path", lambda: make_path), _n_(359170, "output_folder", lambda: output_folder), _n_(359171, "output_version", lambda: output_version))
_l_(359173)
output_crclist = _c_(359176, _n_(359174, "make_path", lambda: make_path), _n_(359175, "output_fv", lambda: output_fv), "crclist")
_l_(359177)

file_list = []
_l_(359178)
for root, dir, files in _c_(359182, _a_(359180, _n_(359179, "os", lambda: os), "walk"), _n_(359181, "input_folder", lambda: input_folder)):
    _l_(359227)

    for filename in _n_(359183, "files", lambda: files):
        _l_(359226)

        file_elem = {}
        _l_(359184)
        _n_(359185, "file_elem", lambda: file_elem)["path"] = _c_(359189, _n_(359186, "make_path", lambda: make_path), _n_(359187, "root", lambda: root), _n_(359188, "filename", lambda: filename))
        _l_(359190)
        _n_(359191, "file_elem", lambda: file_elem)["real_path"] = _c_(359197, _a_(359196, _n_(359192, "file_elem", lambda: file_elem)["path"][_c_(359195, _n_(359193, "len", lambda: len), _n_(359194, "input_folder", lambda: input_folder))+1:], "replace"), "/", "\\")
        _l_(359198)
        # crc32 calculation
        _n_(359199, "file_elem", lambda: file_elem)["crc32"] = _c_(359202, _n_(359200, "get_crc32", lambda: get_crc32), _n_(359201, "file_elem", lambda: file_elem)["path"])
        _l_(359203)
        # size calculation
        _n_(359204, "file_elem", lambda: file_elem)["size"] = _c_(359209, _a_(359207, _a_(359206, _n_(359205, "os", lambda: os), "path"), "getsize"), _n_(359208, "file_elem", lambda: file_elem)["path"])
        _l_(359210)
        # mtime calculation
        mtime = _c_(359213, _n_(359211, "get_mtime", lambda: get_mtime), _n_(359212, "file_elem", lambda: file_elem)["path"])
        _l_(359214)
        _n_(359215, "file_elem", lambda: file_elem)["mtime1"] = _n_(359216, "mtime", lambda: mtime) >> 32
        _l_(359217)
        _n_(359218, "file_elem", lambda: file_elem)["mtime2"] = _n_(359219, "mtime", lambda: mtime) & 0xFFffFFff
        _l_(359220)
        # add in list
        _c_(359224, _a_(359222, _n_(359221, "file_list", lambda: file_list), "append"), _n_(359223, "file_elem", lambda: file_elem))
        _l_(359225)

# make path if missing
if not _c_(359232, _a_(359230, _a_(359229, _n_(359228, "os", lambda: os), "path"), "exists"), _n_(359231, "output_fv", lambda: output_fv)):
    _l_(359238)

    _c_(359236, _a_(359234, _n_(359233, "os", lambda: os), "makedirs"), _n_(359235, "output_fv", lambda: output_fv))
    _l_(359237)

# generate crclist
_c_(359240, _n_(359239, "print", lambda: print), "Generating crclist:")
_l_(359241)
with _c_(359244, _n_(359242, "open", lambda: open), _n_(359243, "output_crclist", lambda: output_crclist), "wb") as f:
    _l_(359264)

    for elem in _n_(359245, "file_list", lambda: file_list):
        _l_(359263)

        buf = "%s %d %d %d %s\n" % (_n_(359246, "elem", lambda: elem)["crc32"], _n_(359247, "elem", lambda: elem)["size"], _n_(359248, "elem", lambda: elem)["mtime1"], _n_(359249, "elem", lambda: elem)["mtime2"], _n_(359250, "elem", lambda: elem)["real_path"])
        _l_(359251)
        _c_(359255, _a_(359253, _n_(359252, "f", lambda: f), "write"), _n_(359254, "buf", lambda: buf))
        _l_(359256)
        _c_(359261, _n_(359257, "print", lambda: print), _c_(359260, _a_(359259, _n_(359258, "buf", lambda: buf), "replace"), "\n", ""))
        _l_(359262)

# generate lz files
ENABLE_LZ_GENERATION = True
_l_(359265)
if _n_(359266, "ENABLE_LZ_GENERATION", lambda: ENABLE_LZ_GENERATION):
    _l_(359313)

    try:
        import subprocess
        _l_(359268)

    except ImportError:
        pass
    _c_(359270, _n_(359269, "print", lambda: print), "Generating .lz:")
    _l_(359271)
    for elem in _n_(359272, "file_list", lambda: file_list):
        _l_(359312)

        filepath_in = _c_(359276, _n_(359273, "make_path", lambda: make_path), _n_(359274, "input_folder", lambda: input_folder), _n_(359275, "elem", lambda: elem)["real_path"])
        _l_(359277)
        filepath_out = _c_(359281, _n_(359278, "make_path", lambda: make_path), _n_(359279, "output_fv", lambda: output_fv), _n_(359280, "elem", lambda: elem)["real_path"]) + ".lz"
        _l_(359282)
        # create out dir
        dirpath_out = _c_(359287, _a_(359285, _a_(359284, _n_(359283, "os", lambda: os), "path"), "dirname"), _n_(359286, "filepath_out", lambda: filepath_out))
        _l_(359288)
        if not _c_(359293, _a_(359291, _a_(359290, _n_(359289, "os", lambda: os), "path"), "exists"), _n_(359292, "dirpath_out", lambda: dirpath_out)):
            _l_(359299)

            _c_(359297, _a_(359295, _n_(359294, "os", lambda: os), "makedirs"), _n_(359296, "dirpath_out", lambda: dirpath_out))
            _l_(359298)
        # create lz
        cmd = 'mt2lz pack "%s" "%s"' % (_n_(359300, "filepath_in", lambda: filepath_in), _n_(359301, "filepath_out", lambda: filepath_out))
        _l_(359302)
        _c_(359306, _a_(359304, _n_(359303, "subprocess", lambda: subprocess), "call"), _n_(359305, "cmd", lambda: cmd), shell=True)
        _l_(359307)
        _c_(359310, _n_(359308, "print", lambda: print), _n_(359309, "cmd", lambda: cmd))
        _l_(359311)
#