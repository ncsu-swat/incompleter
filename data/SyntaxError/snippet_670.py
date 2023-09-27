# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/135041/should-you-always-favor-xrange-over-range
from __future__ import division
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_l_(1545591)

def read_xrange(xrange_object):
    _l_(1545609)

    # returns the xrange object's start, stop, and step
    start = _n_(1545592, "xrange_object", lambda: xrange_object)[0]
    _l_(1545593)
    if _c_(1545596, _n_(1545594, "len", lambda: len), _n_(1545595, "xrange_object", lambda: xrange_object)) > 1:
        _l_(1545601)

        step = _n_(1545597, "xrange_object", lambda: xrange_object)[1] - _n_(1545598, "xrange_object", lambda: xrange_object)[0]
        _l_(1545599)
    else:
        step = 1
        _l_(1545600)
    stop = _n_(1545602, "xrange_object", lambda: xrange_object)[-1] + _n_(1545603, "step", lambda: step)
    _l_(1545604)
    aux = _n_(1545605, "start", lambda: start), _n_(1545606, "stop", lambda: stop), _n_(1545607, "step", lambda: step)
    _l_(1545608)
    return aux

class Xrange(_n_(1545610, "object", lambda: object)):
    _l_(1545803)

    ''' creates an xrange-like object that supports slicing and indexing.
    ex: a = Xrange(20)
    a.index(10)
    will work

    Also a[:5]
    will return another Xrange object with the specified attributes

    Also allows for the conversion from an existing xrange object
    '''
    _l_(1545611)
    def __init__(self, *inputs):
        _l_(1545675)

        # allow inputs of xrange objects
        if _c_(1545614, _n_(1545612, "len", lambda: len), _n_(1545613, "inputs", lambda: inputs)) == 1:
            _l_(1545633)

            test, = _n_(1545615, "inputs", lambda: inputs)
            _l_(1545616)
            if _c_(1545619, _n_(1545617, "type", lambda: type), _n_(1545618, "test", lambda: test)) == _n_(1545620, "xrange", lambda: xrange):
                _l_(1545632)

                _n_(1545621, "self", lambda: self).xrange = _n_(1545622, "test", lambda: test)
                _l_(1545623)
                _n_(1545624, "self", lambda: self).start, _n_(1545625, "self", lambda: self).stop, _n_(1545626, "self", lambda: self).step = _c_(1545629, _n_(1545627, "read_xrange", lambda: read_xrange), _n_(1545628, "test", lambda: test))
                _l_(1545630)
                aux = ""
                _l_(1545631)
                return aux

        # or create one from start, stop, step
        _n_(1545634, "self", lambda: self).start, _n_(1545635, "self", lambda: self).step = 0, None
        _l_(1545636)
        if _c_(1545639, _n_(1545637, "len", lambda: len), _n_(1545638, "inputs", lambda: inputs)) == 1:
            _l_(1545664)

            _n_(1545640, "self", lambda: self).stop, = _n_(1545641, "inputs", lambda: inputs)
            _l_(1545642)
        elif _c_(1545645, _n_(1545643, "len", lambda: len), _n_(1545644, "inputs", lambda: inputs)) == 2:
            _l_(1545663)

            _n_(1545646, "self", lambda: self).start, _n_(1545647, "self", lambda: self).stop = _n_(1545648, "inputs", lambda: inputs)
            _l_(1545649)
        elif _c_(1545652, _n_(1545650, "len", lambda: len), _n_(1545651, "inputs", lambda: inputs)) == 3:
            _l_(1545662)

            _n_(1545653, "self", lambda: self).start, _n_(1545654, "self", lambda: self).stop, _n_(1545655, "self", lambda: self).step = _n_(1545656, "inputs", lambda: inputs)
            _l_(1545657)
        else:
            raise _c_(1545660, _n_(1545658, "ValueError", lambda: ValueError), _n_(1545659, "inputs", lambda: inputs))
            _l_(1545661)

        _n_(1545665, "self", lambda: self).xrange = _c_(1545673, _n_(1545666, "xrange", lambda: xrange), _a_(1545668, _n_(1545667, "self", lambda: self), "start"), _a_(1545670, _n_(1545669, "self", lambda: self), "stop"), _a_(1545672, _n_(1545671, "self", lambda: self), "step"))
        _l_(1545674)

    def __iter__(self):
        _l_(1545681)

        aux = _c_(1545679, _n_(1545676, "iter", lambda: iter), _a_(1545678, _n_(1545677, "self", lambda: self), "xrange"))
        _l_(1545680)
        return aux

    def __getitem__(self, item):
        _l_(1545763)

        if _c_(1545684, _n_(1545682, "type", lambda: type), _n_(1545683, "item", lambda: item)) is _n_(1545685, "int", lambda: int):
            _l_(1545696)

            if _n_(1545686, "item", lambda: item) < 0:
                _l_(1545691)

                item += _c_(1545689, _n_(1545687, "len", lambda: len), _n_(1545688, "self", lambda: self))
                _l_(1545690)
            aux = _a_(1545693, _n_(1545692, "self", lambda: self), "xrange")[_n_(1545694, "item", lambda: item)]
            _l_(1545695)

            return aux

        if _c_(1545699, _n_(1545697, "type", lambda: type), _n_(1545698, "item", lambda: item)) is _n_(1545700, "slice", lambda: slice):
            _l_(1545762)

            # get the indexes, and then convert to the number
            start, stop, step = _a_(1545702, _n_(1545701, "item", lambda: item), "start"), _a_(1545704, _n_(1545703, "item", lambda: item), "stop"), _a_(1545706, _n_(1545705, "item", lambda: item), "step")
            _l_(1545707)
            start = _n_(1545708, "start", lambda: start) if _n_(1545709, "start", lambda: start) != None else 0 # convert start = None to start = 0
            _l_(1545710) # convert start = None to start = 0
            if _n_(1545711, "start", lambda: start) < 0:
                _l_(1545714)

                start += _n_(1545712, "start", lambda: start)
                _l_(1545713)
            start = _n_(1545715, "self", lambda: self)[_n_(1545716, "start", lambda: start)]
            _l_(1545717)
            if _n_(1545718, "start", lambda: start) < 0:
                _l_(1545722)

raise _c_(1545721, _n_(1545719, "IndexError", lambda: IndexError), _n_(1545720, "item", lambda: item))            step = (_a_(1545724, _n_(1545723, "self", lambda: self), "step") if _a_(1545726, _n_(1545725, "self", lambda: self), "step") != None else 1) * (_n_(1545727, "step", lambda: step) if _n_(1545728, "step", lambda: step) != None else 1)
            _l_(1545729)
            stop = _n_(1545730, "stop", lambda: stop) if _n_(1545731, "stop", lambda: stop) is not None else _a_(1545733, _n_(1545732, "self", lambda: self), "xrange")[-1]
            _l_(1545734)
            if _n_(1545735, "stop", lambda: stop) < 0:
                _l_(1545738)

                stop += _n_(1545736, "stop", lambda: stop)
                _l_(1545737)

            stop = _n_(1545739, "self", lambda: self)[_n_(1545740, "stop", lambda: stop)]
            _l_(1545741)
            stop = _n_(1545742, "stop", lambda: stop)
            _l_(1545743)

            if _n_(1545744, "stop", lambda: stop) > _a_(1545746, _n_(1545745, "self", lambda: self), "stop"):
                _l_(1545749)

                raise _n_(1545747, "IndexError", lambda: IndexError)
                _l_(1545748)
            if _n_(1545750, "start", lambda: start) < _a_(1545752, _n_(1545751, "self", lambda: self), "start"):
                _l_(1545755)

                raise _n_(1545753, "IndexError", lambda: IndexError)
                _l_(1545754)
            aux = _c_(1545760, _n_(1545756, "Xrange", lambda: Xrange), _n_(1545757, "start", lambda: start), _n_(1545758, "stop", lambda: stop), _n_(1545759, "step", lambda: step))
            _l_(1545761)
            return aux

    def index(self, value):
        _l_(1545796)

        error = _c_(1545768, _n_(1545764, "ValueError", lambda: ValueError), _c_(1545767, _a_(1545765, 'object.index({0}): {0} not in object', "format"), _n_(1545766, "value", lambda: value)))
        _l_(1545769)
        index = (_n_(1545770, "value", lambda: value) - _a_(1545772, _n_(1545771, "self", lambda: self), "start"))/_a_(1545774, _n_(1545773, "self", lambda: self), "step")
        _l_(1545775)
        if _n_(1545776, "index", lambda: index) % 1 != 0:
            _l_(1545779)

            raise _n_(1545777, "error", lambda: error)
            _l_(1545778)
        index = _c_(1545782, _n_(1545780, "int", lambda: int), _n_(1545781, "index", lambda: index))
        _l_(1545783)


        try:
            _l_(1545793)

            _a_(1545785, _n_(1545784, "self", lambda: self), "xrange")[_n_(1545786, "index", lambda: index)]
            _l_(1545787)
        except (_n_(1545788, "IndexError", lambda: IndexError), _n_(1545789, "TypeError", lambda: TypeError)):
            _l_(1545792)

            raise _n_(1545790, "error", lambda: error)
            _l_(1545791)
        aux = _n_(1545794, "index", lambda: index)
        _l_(1545795)
        return aux

    def __len__(self):
        _l_(1545802)

        aux = _c_(1545800, _n_(1545797, "len", lambda: len), _a_(1545799, _n_(1545798, "self", lambda: self), "xrange"))
        _l_(1545801)
        return aux

