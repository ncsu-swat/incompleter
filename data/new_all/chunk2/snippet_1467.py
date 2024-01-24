# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55557384/returning-list-append-throws-typeerror-unsupported-operand-types-in-recur
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def helper(cur_seq, seq, cur_i, result):
    _l_(428326)

    if _c_(428273, _n_(428271, "len", lambda: len), _n_(428272, "seq", lambda: seq)) == _n_(428274, "cur_i", lambda: cur_i):
        _l_(428325)

        aux = _c_(428278, _a_(428276, _n_(428275, "result", lambda: result), "append"), _n_(428277, "cur_seq", lambda: cur_seq))
        _l_(428279)
        return aux
    else:
        next_i = _n_(428280, "cur_i", lambda: cur_i) + 1
        _l_(428281)
        if _c_(428284, _n_(428282, "len", lambda: len), _n_(428283, "cur_seq", lambda: cur_seq)) == 0 or _n_(428285, "seq", lambda: seq)[_n_(428286, "cur_i", lambda: cur_i)] > _n_(428287, "cur_seq", lambda: cur_seq)[-1]:
            _l_(428324)

            temp = _c_(428290, _a_(428289, _n_(428288, "cur_seq", lambda: cur_seq), "copy"))
            _l_(428291)
            temp1 = _c_(428294, _a_(428293, _n_(428292, "cur_seq", lambda: cur_seq), "copy"))
            _l_(428295)
            _c_(428300, _a_(428297, _n_(428296, "temp", lambda: temp), "append"), _n_(428298, "seq", lambda: seq)[_n_(428299, "cur_i", lambda: cur_i)])
            _l_(428301)
            aux = _c_(428307, _n_(428302, "helper", lambda: helper), _n_(428303, "temp", lambda: temp), _n_(428304, "seq", lambda: seq), _n_(428305, "next_i", lambda: next_i), _n_(428306, "result", lambda: result)) + _c_(428313, _n_(428308, "helper", lambda: helper), _n_(428309, "temp1", lambda: temp1), _n_(428310, "seq", lambda: seq), _n_(428311, "next_i", lambda: next_i), _n_(428312, "result", lambda: result))
            _l_(428314)
            return aux
        else:
            aux = _c_(428322, _n_(428315, "helper", lambda: helper), _c_(428318, _a_(428317, _n_(428316, "cur_seq", lambda: cur_seq), "copy")), _n_(428319, "seq", lambda: seq), _n_(428320, "next_i", lambda: next_i), _n_(428321, "result", lambda: result))
            _l_(428323)
            return aux


def longest_sub_sequence(seq):
    _l_(428347)

    cur_seq = []
    _l_(428327)

    result = _c_(428331, _n_(428328, "helper", lambda: helper), _n_(428329, "cur_seq", lambda: cur_seq), _n_(428330, "seq", lambda: seq), 0, [])
    _l_(428332)

    max_length = 0
    _l_(428333)
    for i in _n_(428334, "result", lambda: result):
        _l_(428344)

        if _c_(428337, _n_(428335, "len", lambda: len), _n_(428336, "i", lambda: i)) > _n_(428338, "max_length", lambda: max_length):
            _l_(428343)

            max_length = _c_(428341, _n_(428339, "len", lambda: len), _n_(428340, "i", lambda: i))
            _l_(428342)
    aux = _n_(428345, "max_length", lambda: max_length)
    _l_(428346)


    return aux


if _n_(428348, "__name__", lambda: __name__) == "__main__":
    _l_(428358)


    seq = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
    _l_(428349)
    y = _c_(428352, _n_(428350, "longest_sub_sequence", lambda: longest_sub_sequence), _n_(428351, "seq", lambda: seq))
    _l_(428353)
    _c_(428356, _n_(428354, "print", lambda: print), _n_(428355, "y", lambda: y))
    _l_(428357)