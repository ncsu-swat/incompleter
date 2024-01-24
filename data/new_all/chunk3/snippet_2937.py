# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57733732/what-is-the-reason-i-am-getting-a-nameerror-name-int-to-roman-is-not-defined
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Roman_Number():
    _l_(547074)

    roman_numeral_table = [
    ("M", 1000), ("CM", 900), ("D", 500),
    ("CD", 400), ("C", 100),  ("XC", 90),
    ("L", 50),   ("XL", 40),  ("X", 10),
    ("IX", 9),   ("V", 5),    ("IV", 4),
    ("I", 1)
    ]
    _l_(547029)


    r = _c_(547031, _n_(547030, "input", lambda: input), 'If you want to go from Roman to Number, enter "1." If you want to go from Number to Roman, enter "2"')
    _l_(547032)

    if r == 1:
        _l_(547037)

        _c_(547033, roman_to_int)
        _l_(547034)
    else:
        _c_(547035, int_to_roman)
        _l_(547036)

    def int_to_roman():
        _l_(547073)

        number = _c_(547041, _n_(547038, "int", lambda: int), _c_(547040, _n_(547039, "input", lambda: input), 'Provide Number: '))
        _l_(547042)
        if _n_(547043, "number", lambda: number) < 1 or _n_(547044, "number", lambda: number) > 3999:
            _l_(547051)

            _c_(547046, _n_(547045, "print", lambda: print), 'Number must be inbetween 1 and 3999')
            _l_(547047)
        else:
            _c_(547049, _n_(547048, "print", lambda: print), 'Valid Number')
            _l_(547050)

        roman_numerals = []
        _l_(547052)
        for numeral, value in _n_(547053, "roman_numeral_table", lambda: roman_numeral_table):
            _l_(547064)

            while _n_(547054, "value", lambda: value) <= _n_(547055, "number", lambda: number):
                _l_(547063)

                number -= _n_(547056, "value", lambda: value)
                _l_(547057)
                _c_(547061, _a_(547059, _n_(547058, "roman_numerals", lambda: roman_numerals), "append"), _n_(547060, "numeral", lambda: numeral))
                _l_(547062)

        _c_(547069, _n_(547065, "print", lambda: print), _c_(547068, _a_(547066, '', "join"), _n_(547067, "roman_numerals", lambda: roman_numerals)))
        _l_(547070)

        def roman_to_int():
            _l_(547072)

            pass
            _l_(547071)