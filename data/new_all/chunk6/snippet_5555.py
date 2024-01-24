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
_l_(371081)


def count_word(filename, word):
    _l_(371099)

    with _c_(371084, _n_(371082, "open", lambda: open), _n_(371083, "filename", lambda: filename)) as open_file:
        _l_(371089)

        file_content = _c_(371087, _a_(371086, _n_(371085, "open_file", lambda: open_file), "read"))
        _l_(371088)

    count_num = _c_(371095, _a_(371093, _c_(371092, _a_(371091, _n_(371090, "file_content", lambda: file_content), "lower")), "count"), _n_(371094, "word", lambda: word))
    _l_(371096)
    aux = _n_(371097, "count_num", lambda: count_num)
    _l_(371098)
    return aux


for filename in _n_(371100, "filenames", lambda: filenames):
    _l_(371112)

    _c_(371103, _n_(371101, "count_word", lambda: count_word), _n_(371102, "filename", lambda: filename), "great")
    _l_(371104)
    _c_(371110, _n_(371105, "print", lambda: print), 'There are ' + _c_(371108, _n_(371106, "str", lambda: str), _n_(371107, "count_num", lambda: count_num)) + " 'great' in " + _n_(371109, "filename", lambda: filename) + ".")
    _l_(371111)