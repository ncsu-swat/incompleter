# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/42178236/typeerror-unsupported-operand-types-for-nonetype-and-int-python-3
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
decimaal = 0
_l_(642522)


# Laat de gebruiker een waarde in typen
def user_input():
    _l_(642538)

    getal = _c_(642526, _n_(642523, "int", lambda: int), _c_(642525, _n_(642524, "input", lambda: input), 'Geef het getal: '))
    _l_(642527)
    if _n_(642528, "getal", lambda: getal) < 10000:
        _l_(642537)

        aux = _n_(642529, "getal", lambda: getal)
        _l_(642530)
        return aux
    else:
        _c_(642532, _n_(642531, "print", lambda: print), 'Het getal moet kleiner zijn dan 10.000!')
        _l_(642533)
        _c_(642535, _n_(642534, "user_input", lambda: user_input))
        _l_(642536)


# functie om getal in het decimaal- naar octaal-stelsel om te zetten
def decimaal_octaal_converter(decimaal):
    _l_(642574)

    resultaat = []
    _l_(642539)
    quotient = _n_(642540, "decimaal", lambda: decimaal)
    _l_(642541)
    rest = 0
    _l_(642542)

    # Maakt een lijst met het octale resultaat
    while _n_(642543, "quotient", lambda: quotient) != 0:
        _l_(642552)

        """
        Soms geeft lijn 28 de volgende error:
        TypeError: unsupported operand type(s) for %: 'NoneType' and 'int'
        Maar waarom?
        """
        rest = _n_(642544, "quotient", lambda: quotient) % 8
        _l_(642545)
        quotient //= 8
        _l_(642546)
        _c_(642550, _a_(642548, _n_(642547, "resultaat", lambda: resultaat), "append"), _n_(642549, "rest", lambda: rest))
        _l_(642551)

    # Lijst moet omgedraaid worden
    _c_(642555, _a_(642554, _n_(642553, "resultaat", lambda: resultaat), "reverse"))
    _l_(642556)
    octaal = ''
    _l_(642557)

    # De lijst naar een string omzetten zodat de gebruiker het kan lezen
    for i in _c_(642562, _n_(642558, "range", lambda: range), _c_(642561, _n_(642559, "len", lambda: len), _n_(642560, "resultaat", lambda: resultaat))):
        _l_(642568)

        octaal += _c_(642566, _n_(642563, "str", lambda: str), _n_(642564, "resultaat", lambda: resultaat)[_n_(642565, "i", lambda: i)])
        _l_(642567)
    aux = _c_(642572, _n_(642569, "print", lambda: print), 'Het getal %s in octaal is %s' % (_n_(642570, "decimaal", lambda: decimaal), _n_(642571, "octaal", lambda: octaal)))
    _l_(642573)

    return aux


# De hoofd functie voor het omzetten van decimaal naar octaal
def converter():
    _l_(642580)

    _c_(642578, _n_(642575, "decimaal_octaal_converter", lambda: decimaal_octaal_converter), _c_(642577, _n_(642576, "user_input", lambda: user_input)))
    _l_(642579)

_c_(642582, _n_(642581, "converter", lambda: converter))
_l_(642583)