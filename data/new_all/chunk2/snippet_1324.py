# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/43023315/python3-typeerror-a-bytes-like-object-is-required-not-str
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import sys
    _l_(451506)

except ImportError:
    pass
try:
    import glob
    _l_(451508)

except ImportError:
    pass
try:
    import struct
    _l_(451510)

except ImportError:
    pass
try:
    import argparse
    _l_(451512)

except ImportError:
    pass
try:
    import traceback
    _l_(451514)

except ImportError:
    pass


def exception_response(e):
    _l_(451532)

    exc_type, exc_value, exc_traceback = _c_(451517, _a_(451516, _n_(451515, "sys", lambda: sys), "exc_info"))
    _l_(451518)
    lines = _c_(451524, _a_(451520, _n_(451519, "traceback", lambda: traceback), "format_exception"), _n_(451521, "exc_type", lambda: exc_type), _n_(451522, "exc_value", lambda: exc_value), _n_(451523, "exc_traceback", lambda: exc_traceback))
    _l_(451525)
    for line in _n_(451526, "lines", lambda: lines):
        _l_(451531)

        _c_(451529, _n_(451527, "print", lambda: print), _n_(451528, "line", lambda: line))
        _l_(451530)

def get_args():
    _l_(451554)

    parser = _c_(451535, _a_(451534, _n_(451533, "argparse", lambda: argparse), "ArgumentParser"))
    _l_(451536)
    _c_(451539, _a_(451538, _n_(451537, "parser", lambda: parser), "add_argument"), '-v', dest='vec_directory')
    _l_(451540)
    _c_(451543, _a_(451542, _n_(451541, "parser", lambda: parser), "add_argument"), '-o', dest='output_filename')
    _l_(451544)
    args = _c_(451547, _a_(451546, _n_(451545, "parser", lambda: parser), "parse_args"))
    _l_(451548)
    aux = (_a_(451550, _n_(451549, "args", lambda: args), "vec_directory"), _a_(451552, _n_(451551, "args", lambda: args), "output_filename"))
    _l_(451553)
    return aux

def merge_vec_files(vec_directory, output_vec_file):
    _l_(451729)



    # Check that the .vec directory does not end in '/' and if it does, remove it.
    if _c_(451557, _a_(451556, _n_(451555, "vec_directory", lambda: vec_directory), "endswith"), '/'):
        _l_(451560)

        vec_directory = _n_(451558, "vec_directory", lambda: vec_directory)[:-1]
        _l_(451559)
    # Get .vec files
    files = _c_(451566, _a_(451562, _n_(451561, "glob", lambda: glob), "glob"), _c_(451565, _a_(451563, '{0}/*.vec', "format"), _n_(451564, "vec_directory", lambda: vec_directory)))
    _l_(451567)

    # Check to make sure there are .vec files in the directory
    if _c_(451570, _n_(451568, "len", lambda: len), _n_(451569, "files", lambda: files)) <= 0:
        _l_(451581)

        _c_(451575, _n_(451571, "print", lambda: print), _c_(451574, _a_(451572, 'Vec files to be mereged could not be found from directory: {0}', "format"), _n_(451573, "vec_directory", lambda: vec_directory)))
        _l_(451576)
        _c_(451579, _a_(451578, _n_(451577, "sys", lambda: sys), "exit"), 1)
        _l_(451580)
    # Check to make sure there are more than one .vec files
    if _c_(451584, _n_(451582, "len", lambda: len), _n_(451583, "files", lambda: files)) == 1:
        _l_(451595)

        _c_(451589, _n_(451585, "print", lambda: print), _c_(451588, _a_(451586, 'Only 1 vec file was found in directory: {0}. Cannot merge a single file.', "format"), _n_(451587, "vec_directory", lambda: vec_directory)))
        _l_(451590)
        _c_(451593, _a_(451592, _n_(451591, "sys", lambda: sys), "exit"), 1)
        _l_(451594)


    # Get the value for the first image size
    prev_image_size = 0
    _l_(451596)
    try:
        _l_(451630)

        with _c_(451599, _n_(451597, "open", lambda: open), _n_(451598, "files", lambda: files)[0], 'r', encoding='utf-8', errors='ignore') as vecfile:
            _l_(451616)

            content = _c_(451607, _a_(451600, '', "join"), (_c_(451603, _n_(451601, "str", lambda: str), _n_(451602, "line", lambda: line)) for line in _c_(451606, _a_(451605, _n_(451604, "vecfile", lambda: vecfile), "readlines"))))
            _l_(451608)
            val = _c_(451612, _a_(451610, _n_(451609, "struct", lambda: struct), "unpack"), '<iihh', _n_(451611, "content", lambda: content)[:12])
            _l_(451613)
            prev_image_size = _n_(451614, "val", lambda: val)[1]
            _l_(451615)
    except _n_(451617, "IOError", lambda: IOError) as e:
        _l_(451629)

        f = None
        _l_(451618)
        _c_(451623, _n_(451619, "print", lambda: print), _c_(451622, _a_(451620, 'An IO error occured while processing the file: {0}', "format"), _n_(451621, "f", lambda: f)))
        _l_(451624)
        _c_(451627, _n_(451625, "exception_response", lambda: exception_response), _n_(451626, "e", lambda: e))
        _l_(451628)


    # Get the total number of images
    total_num_images = 0
    _l_(451631)
    for f in _n_(451632, "files", lambda: files):
        _l_(451684)

        try:
            _l_(451683)

            with _c_(451635, _n_(451633, "open", lambda: open), _n_(451634, "f", lambda: f), 'r', encoding='utf-8', errors='ignore') as vecfile:
                _l_(451670)

                content = _c_(451643, _a_(451636, '', "join"), (_c_(451639, _n_(451637, "str", lambda: str), _n_(451638, "line", lambda: line)) for line in _c_(451642, _a_(451641, _n_(451640, "vecfile", lambda: vecfile), "readlines"))))
                _l_(451644)
                val = _c_(451648, _a_(451646, _n_(451645, "struct", lambda: struct), "unpack"), '<iihh', _n_(451647, "content", lambda: content)[:12])
                _l_(451649)
                num_images = _n_(451650, "val", lambda: val)[0]
                _l_(451651)
                image_size = _n_(451652, "val", lambda: val)[1]
                _l_(451653)
                if _n_(451654, "image_size", lambda: image_size) != _n_(451655, "prev_image_size", lambda: prev_image_size):
                    _l_(451667)

                    err_msg = _c_(451660, _a_(451656, """The image sizes in the .vec files differ. These values must be the same. \n The image size of file {0}: {1}\n 
                        The image size of previous files: {0}""", "format"), _n_(451657, "f", lambda: f), _n_(451658, "image_size", lambda: image_size), _n_(451659, "prev_image_size", lambda: prev_image_size))
                    _l_(451661)
                    _c_(451665, _a_(451663, _n_(451662, "sys", lambda: sys), "exit"), _n_(451664, "err_msg", lambda: err_msg))
                    _l_(451666)

                total_num_images += _n_(451668, "num_images", lambda: num_images)
                _l_(451669)
        except _n_(451671, "IOError", lambda: IOError) as e:
            _l_(451682)

            _c_(451676, _n_(451672, "print", lambda: print), _c_(451675, _a_(451673, 'An IO error occured while processing the file: {0}', "format"), _n_(451674, "f", lambda: f)))
            _l_(451677)
            _c_(451680, _n_(451678, "exception_response", lambda: exception_response), _n_(451679, "e", lambda: e))
            _l_(451681)


    # Iterate through the .vec files, writing their data (not the header) to the output file
    # '<iihh' means 'little endian, int, int, short, short'
    header = _c_(451689, _a_(451686, _n_(451685, "struct", lambda: struct), "pack"), '<iihh', _n_(451687, "total_num_images", lambda: total_num_images), _n_(451688, "image_size", lambda: image_size), 0, 0)
    _l_(451690)
    try:
        _l_(451728)

        with _c_(451693, _n_(451691, "open", lambda: open), _n_(451692, "output_vec_file", lambda: output_vec_file), 'wb') as outputfile:
            _l_(451721)

            _c_(451697, _a_(451695, _n_(451694, "outputfile", lambda: outputfile), "write"), _n_(451696, "header", lambda: header))
            _l_(451698)

            for f in _n_(451699, "files", lambda: files):
                _l_(451720)

                with _c_(451702, _n_(451700, "open", lambda: open), _n_(451701, "f", lambda: f), 'w', encoding='utf-8', errors='ignore') as vecfile:
                    _l_(451719)

                    content = _c_(451710, _a_(451703, '', "join"), (_c_(451706, _n_(451704, "str", lambda: str), _n_(451705, "line", lambda: line)) for line in _c_(451709, _a_(451708, _n_(451707, "vecfile", lambda: vecfile), "readlines"))))
                    _l_(451711)
                    data = _n_(451712, "content", lambda: content)[12:]
                    _l_(451713)
                    _c_(451717, _a_(451715, _n_(451714, "outputfile", lambda: outputfile), "write"), _n_(451716, "data", lambda: data))
                    _l_(451718)
    except _n_(451722, "Exception", lambda: Exception) as e:
        _l_(451727)

        _c_(451725, _n_(451723, "exception_response", lambda: exception_response), _n_(451724, "e", lambda: e))
        _l_(451726)


if _n_(451730, "__name__", lambda: __name__) == '__main__':
    _l_(451751)

    vec_directory, output_filename = _c_(451732, _n_(451731, "get_args", lambda: get_args))
    _l_(451733)
    if not _n_(451734, "vec_directory", lambda: vec_directory):
        _l_(451739)

        _c_(451737, _a_(451736, _n_(451735, "sys", lambda: sys), "exit"), 'mergvec requires a directory of vec files. Call mergevec.py with -v /your_vec_directory')
        _l_(451738)
    if not _n_(451740, "output_filename", lambda: output_filename):
        _l_(451745)

        _c_(451743, _a_(451742, _n_(451741, "sys", lambda: sys), "exit"), 'mergevec requires an output filename. Call mergevec.py with -o your_output_filename')
        _l_(451744)

    _c_(451749, _n_(451746, "merge_vec_files", lambda: merge_vec_files), _n_(451747, "vec_directory", lambda: vec_directory), _n_(451748, "output_filename", lambda: output_filename))
    _l_(451750)