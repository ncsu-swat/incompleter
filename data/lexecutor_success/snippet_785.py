# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/2501457/what-do-i-use-for-a-max-heap-implementation-in-python
from __future__ import annotations  # To allow "MinHeap.push -> MinHeap:"
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_l_(1542484)  # To allow "MinHeap.push -> MinHeap:"
try:
    from typing import Generic, List, Optional, TypeVar
    _l_(1542486)

except ImportError:
    pass
try:
    from heapq import heapify, heappop, heappush, heapreplace
    _l_(1542488)

except ImportError:
    pass


T = _c_(1542490, _n_(1542489, "TypeVar", lambda: TypeVar), 'T')
_l_(1542491)


class MinHeap(_n_(1542492, "Generic", lambda: Generic)[_n_(1542493, "T", lambda: T)]):
    _l_(1542568)

    '''
    MinHeap provides a nicer API around heapq's functionality.
    As it is a minimum heap, the first element of the heap is always the
    smallest.
    >>> h = MinHeap([3, 1, 4, 2])
    >>> h[0]
    1
    >>> h.peek()
    1
    >>> h.push(5)  # N.B.: the array isn't always fully sorted.
    [1, 2, 4, 3, 5]
    >>> h.pop()
    1
    >>> h.pop()
    2
    >>> h.pop()
    3
    >>> h.push(3).push(2)
    [2, 3, 4, 5]
    >>> h.replace(1)
    2
    >>> h
    [1, 3, 4, 5]
    '''
    _l_(1542494)
    def __init__(self, array: _n_(1542495, "Optional", lambda: Optional)[_n_(1542496, "List", lambda: List)[_n_(1542497, "T", lambda: T)]] = None):
        _l_(1542508)

        if _n_(1542498, "array", lambda: array) is None:
            _l_(1542500)

            array = []
            _l_(1542499)
        _c_(1542503, _n_(1542501, "heapify", lambda: heapify), _n_(1542502, "array", lambda: array))
        _l_(1542504)
        _n_(1542505, "self", lambda: self).h = _n_(1542506, "array", lambda: array)
        _l_(1542507)
    def push(self, x: _n_(1542509, "T", lambda: T)) -> _n_(1542510, "MinHeap", lambda: MinHeap):
        _l_(1542519)

        _c_(1542515, _n_(1542511, "heappush", lambda: heappush), _a_(1542513, _n_(1542512, "self", lambda: self), "h"), _n_(1542514, "x", lambda: x))
        _l_(1542516)
        aux = _n_(1542517, "self", lambda: self)  # To allow chaining operations.
        _l_(1542518)  # To allow chaining operations.
        return aux  # To allow chaining operations.
    def peek(self) -> _n_(1542520, "T", lambda: T):
        _l_(1542524)

        aux = _a_(1542522, _n_(1542521, "self", lambda: self), "h")[0]
        _l_(1542523)
        return aux
    def pop(self) -> _n_(1542525, "T", lambda: T):
        _l_(1542531)

        aux = _c_(1542529, _n_(1542526, "heappop", lambda: heappop), _a_(1542528, _n_(1542527, "self", lambda: self), "h"))
        _l_(1542530)
        return aux
    def replace(self, x: _n_(1542532, "T", lambda: T)) -> _n_(1542533, "T", lambda: T):
        _l_(1542540)

        aux = _c_(1542538, _n_(1542534, "heapreplace", lambda: heapreplace), _a_(1542536, _n_(1542535, "self", lambda: self), "h"), _n_(1542537, "x", lambda: x))
        _l_(1542539)
        return aux
    def __getitem__(self, i) -> _n_(1542541, "T", lambda: T):
        _l_(1542546)

        aux = _a_(1542543, _n_(1542542, "self", lambda: self), "h")[_n_(1542544, "i", lambda: i)]
        _l_(1542545)
        return aux
    def __len__(self) -> _n_(1542547, "int", lambda: int):
        _l_(1542553)

        aux = _c_(1542551, _n_(1542548, "len", lambda: len), _a_(1542550, _n_(1542549, "self", lambda: self), "h"))
        _l_(1542552)
        return aux
    def __str__(self) -> _n_(1542554, "str", lambda: str):
        _l_(1542560)

        aux = _c_(1542558, _n_(1542555, "str", lambda: str), _a_(1542557, _n_(1542556, "self", lambda: self), "h"))
        _l_(1542559)
        return aux
    def __repr__(self) -> _n_(1542561, "str", lambda: str):
        _l_(1542567)

        aux = _c_(1542565, _n_(1542562, "str", lambda: str), _a_(1542564, _n_(1542563, "self", lambda: self), "h"))
        _l_(1542566)
        return aux


class Reverse(_n_(1542569, "Generic", lambda: Generic)[_n_(1542570, "T", lambda: T)]):
    _l_(1542646)

    '''
    Wrap around the provided object, reversing the comparison operators.
    >>> 1 < 2
    True
    >>> Reverse(1) < Reverse(2)
    False
    >>> Reverse(2) < Reverse(1)
    True
    >>> Reverse(1) <= Reverse(2)
    False
    >>> Reverse(2) <= Reverse(1)
    True
    >>> Reverse(2) <= Reverse(2)
    True
    >>> Reverse(1) == Reverse(1)
    True
    >>> Reverse(2) > Reverse(1)
    False
    >>> Reverse(1) > Reverse(2)
    True
    >>> Reverse(2) >= Reverse(1)
    False
    >>> Reverse(1) >= Reverse(2)
    True
    >>> Reverse(1)
    1
    '''
    _l_(1542571)
    def __init__(self, x: _n_(1542572, "T", lambda: T)) -> None:
        _l_(1542576)

        _n_(1542573, "self", lambda: self).x = _n_(1542574, "x", lambda: x)
        _l_(1542575)
    def __lt__(self, other: _n_(1542577, "Reverse", lambda: Reverse)) -> _n_(1542578, "bool", lambda: bool):
        _l_(1542586)

        aux = _c_(1542584, _a_(1542581, _a_(1542580, _n_(1542579, "other", lambda: other), "x"), "__lt__"), _a_(1542583, _n_(1542582, "self", lambda: self), "x"))
        _l_(1542585)
        return aux
    def __le__(self, other: _n_(1542587, "Reverse", lambda: Reverse)) -> _n_(1542588, "bool", lambda: bool):
        _l_(1542596)

        aux = _c_(1542594, _a_(1542591, _a_(1542590, _n_(1542589, "other", lambda: other), "x"), "__le__"), _a_(1542593, _n_(1542592, "self", lambda: self), "x"))
        _l_(1542595)
        return aux
    def __eq__(self, other) -> _n_(1542597, "bool", lambda: bool):
        _l_(1542603)

        aux = _a_(1542599, _n_(1542598, "self", lambda: self), "x") == _a_(1542601, _n_(1542600, "other", lambda: other), "x")
        _l_(1542602)
        return aux
    def __ne__(self, other: _n_(1542604, "Reverse", lambda: Reverse)) -> _n_(1542605, "bool", lambda: bool):
        _l_(1542613)

        aux = _c_(1542611, _a_(1542608, _a_(1542607, _n_(1542606, "other", lambda: other), "x"), "__ne__"), _a_(1542610, _n_(1542609, "self", lambda: self), "x"))
        _l_(1542612)
        return aux
    def __ge__(self, other: _n_(1542614, "Reverse", lambda: Reverse)) -> _n_(1542615, "bool", lambda: bool):
        _l_(1542623)

        aux = _c_(1542621, _a_(1542618, _a_(1542617, _n_(1542616, "other", lambda: other), "x"), "__ge__"), _a_(1542620, _n_(1542619, "self", lambda: self), "x"))
        _l_(1542622)
        return aux
    def __gt__(self, other: _n_(1542624, "Reverse", lambda: Reverse)) -> _n_(1542625, "bool", lambda: bool):
        _l_(1542633)

        aux = _c_(1542631, _a_(1542628, _a_(1542627, _n_(1542626, "other", lambda: other), "x"), "__gt__"), _a_(1542630, _n_(1542629, "self", lambda: self), "x"))
        _l_(1542632)
        return aux
    def __str__(self):
        _l_(1542639)

        aux = _c_(1542637, _n_(1542634, "str", lambda: str), _a_(1542636, _n_(1542635, "self", lambda: self), "x"))
        _l_(1542638)
        return aux
    def __repr__(self):
        _l_(1542645)

        aux = _c_(1542643, _n_(1542640, "str", lambda: str), _a_(1542642, _n_(1542641, "self", lambda: self), "x"))
        _l_(1542644)
        return aux


class MaxHeap(_n_(1542647, "MinHeap", lambda: MinHeap)):
    _l_(1542702)

    '''
    MaxHeap provides an implement of a maximum-heap, as heapq does not provide
    it. As it is a maximum heap, the first element of the heap is always the
    largest. It achieves this by wrapping around elements with Reverse,
    which reverses the comparison operations used by heapq.
    >>> h = MaxHeap([3, 1, 4, 2])
    >>> h[0]
    4
    >>> h.peek()
    4
    >>> h.push(5)  # N.B.: the array isn't always fully sorted.
    [5, 4, 3, 1, 2]
    >>> h.pop()
    5
    >>> h.pop()
    4
    >>> h.pop()
    3
    >>> h.pop()
    2
    >>> h.push(3).push(2).push(4)
    [4, 3, 2, 1]
    >>> h.replace(1)
    4
    >>> h
    [3, 1, 2, 1]
    '''
    _l_(1542648)
    def __init__(self, array: _n_(1542649, "Optional", lambda: Optional)[_n_(1542650, "List", lambda: List)[_n_(1542651, "T", lambda: T)]] = None):
        _l_(1542664)

        if _n_(1542652, "array", lambda: array) is not None:
            _l_(1542658)

            array = [_c_(1542655, _n_(1542653, "Reverse", lambda: Reverse), _n_(1542654, "x", lambda: x)) for x in _n_(1542656, "array", lambda: array)]  # Wrap with Reverse.
            _l_(1542657)  # Wrap with Reverse.
        _c_(1542662, _a_(1542660, _n_(1542659, "super", lambda: super)(), "__init__"), _n_(1542661, "array", lambda: array))
        _l_(1542663)
    def push(self, x: _n_(1542665, "T", lambda: T)) -> _n_(1542666, "MaxHeap", lambda: MaxHeap):
        _l_(1542676)

        _c_(1542672, _a_(1542668, _n_(1542667, "super", lambda: super)(), "push"), _c_(1542671, _n_(1542669, "Reverse", lambda: Reverse), _n_(1542670, "x", lambda: x)))
        _l_(1542673)
        aux = _n_(1542674, "self", lambda: self)
        _l_(1542675)
        return aux
    def peek(self) -> _n_(1542677, "T", lambda: T):
        _l_(1542683)

        aux = _a_(1542681, _c_(1542680, _a_(1542679, _n_(1542678, "super", lambda: super)(), "peek")), "x")
        _l_(1542682)
        return aux
    def pop(self) -> _n_(1542684, "T", lambda: T):
        _l_(1542690)

        aux = _a_(1542688, _c_(1542687, _a_(1542686, _n_(1542685, "super", lambda: super)(), "pop")), "x")
        _l_(1542689)
        return aux
    def replace(self, x: _n_(1542691, "T", lambda: T)) -> _n_(1542692, "T", lambda: T):
        _l_(1542701)

        aux = _a_(1542699, _c_(1542698, _a_(1542694, _n_(1542693, "super", lambda: super)(), "replace"), _c_(1542697, _n_(1542695, "Reverse", lambda: Reverse), _n_(1542696, "x", lambda: x))), "x")
        _l_(1542700)
        return aux


if _n_(1542703, "__name__", lambda: __name__) == '__main__':
    _l_(1542710)

    try:
        import doctest
        _l_(1542705)

    except ImportError:
        pass
    _c_(1542708, _a_(1542707, _n_(1542706, "doctest", lambda: doctest), "testmod"))
    _l_(1542709)

