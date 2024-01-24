# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/54361250/how-to-fix-this-nameerror-problem-in-python-3-6
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
filenames = [
    "The Wallypug in London.txt", 
    "Chats on Old Silver.txt", 
    "Jack Jingle, and Sucky Shingle.txt", 
    "Superstition and Force.txt"
]
_l_(339677)


def count_word(filename, word):
    _l_(339695)

    with _c_(339680, _n_(339678, "open", lambda: open), _n_(339679, "filename", lambda: filename)) as open_file:
        _l_(339685)

        file_content = _c_(339683, _a_(339682, _n_(339681, "open_file", lambda: open_file), "read"))
        _l_(339684)

    count_num = _c_(339691, _a_(339689, _c_(339688, _a_(339687, _n_(339686, "file_content", lambda: file_content), "lower")), "count"), _n_(339690, "word", lambda: word))
    _l_(339692)
    aux = _n_(339693, "count_num", lambda: count_num)
    _l_(339694)
    return aux


for filename in _n_(339696, "filenames", lambda: filenames):
    _l_(339708)

    _c_(339699, _n_(339697, "count_word", lambda: count_word), _n_(339698, "filename", lambda: filename), "great")
    _l_(339700)
    _c_(339706, _n_(339701, "print", lambda: print), 'There are ' + _c_(339704, _n_(339702, "str", lambda: str), _n_(339703, "count_num", lambda: count_num)) + " 'great' in " + _n_(339705, "filename", lambda: filename) + ".")
    _l_(339707)