# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/47740542/typeerror-generator-object-is-not-callable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def lines(file):
    _l_(393158)

    for line in _n_(393153, "file", lambda: file):
        _l_(393156)

        yield _n_(393154, "line", lambda: line)
        _l_(393155)
    yield '\n'
    _l_(393157)

def blocks(file):
    _l_(393182)

    block = []
    _l_(393159)
    for line in _c_(393162, _n_(393160, "lines", lambda: lines), _n_(393161, "file", lambda: file)):
        _l_(393181)

        if _c_(393165, _a_(393164, _n_(393163, "line", lambda: line), "strip")):
            _l_(393180)

            _c_(393169, _a_(393167, _n_(393166, "block", lambda: block), "append"), _n_(393168, "line", lambda: line))
            _l_(393170)
        elif _n_(393171, "block", lambda: block):
            _l_(393179)

            yield _c_(393176, _a_(393175, _c_(393174, _a_(393172, '', "join"), _n_(393173, "block", lambda: block)), "strip"))
            _l_(393177)
            block = []
            _l_(393178)


with _c_(393184, _n_(393183, "open", lambda: open), r'test_input.txt', 'r') as f:
    _l_(393199)

    lines = _c_(393187, _n_(393185, "lines", lambda: lines), _n_(393186, "f", lambda: f))
    _l_(393188)
    file = _c_(393191, _n_(393189, "blocks", lambda: blocks), _n_(393190, "lines", lambda: lines))
    _l_(393192)
    for line in _n_(393193, "file", lambda: file):
        _l_(393198)

        _c_(393196, _n_(393194, "print", lambda: print), _n_(393195, "line", lambda: line))
        _l_(393197)