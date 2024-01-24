# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/31497208/python-3-why-am-i-getting-an-attributeerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import sys
    _l_(460444)

except ImportError:
    pass
try:
    from Parser import AssemblyParser
    _l_(460446)

except ImportError:
    pass
try:
    from Code import Code
    _l_(460448)

except ImportError:
    pass

parser = _c_(460452, _n_(460449, "AssemblyParser", lambda: AssemblyParser), _a_(460451, _n_(460450, "sys", lambda: sys), "argv")[1])
_l_(460453)
translator = _c_(460455, _n_(460454, "Code", lambda: Code))
_l_(460456)

out_file = _c_(460462, _a_(460461, _c_(460460, _n_(460457, "str", lambda: str), _a_(460459, _n_(460458, "sys", lambda: sys), "argv")[1]), "split"), ".")
_l_(460463)
out_file = _c_(460466, _n_(460464, "str", lambda: str), _n_(460465, "out_file", lambda: out_file)[:1]) + ".hack"
_l_(460467)

with _c_(460470, _n_(460468, "open", lambda: open), _n_(460469, "out_file", lambda: out_file), 'w', encoding='utf-8') as f:
    _l_(460531)

    while _c_(460473, _a_(460472, _n_(460471, "parser", lambda: parser), "hasMoreCommands")):
        _l_(460530)

        _c_(460476, _a_(460475, _n_(460474, "parser", lambda: parser), "advance"))
        _l_(460477)
        if _c_(460480, _a_(460479, _n_(460478, "parser", lambda: parser), "commandType")) == "A_COMMAND":
            _l_(460520)

            dec_num = _c_(460483, _a_(460482, _n_(460481, "parser", lambda: parser), "symbol"))
            _l_(460484)
            binary = _c_(460487, _a_(460485, "{0:b}", "format"), _n_(460486, "dec_num", lambda: dec_num))
            _l_(460488)
        elif _c_(460491, _a_(460490, _n_(460489, "parser", lambda: parser), "commandType")) == "C_COMMAND":
            _l_(460519)

            default_bits = "111"
            _l_(460492)
            comp_bits += _c_(460498, _a_(460494, _n_(460493, "translator", lambda: translator), "comp"), _c_(460497, _a_(460496, _n_(460495, "parser", lambda: parser), "comp")))
            _l_(460499)
            dest_bits += _c_(460505, _a_(460501, _n_(460500, "translator", lambda: translator), "dest"), _c_(460504, _a_(460503, _n_(460502, "parser", lambda: parser), "dest")))
            _l_(460506)
            jump_bits += _c_(460512, _a_(460508, _n_(460507, "translator", lambda: translator), "jump"), _c_(460511, _a_(460510, _n_(460509, "parser", lambda: parser), "jump")))
            _l_(460513)
            binary = _n_(460514, "default_bits", lambda: default_bits) + _n_(460515, "comp_bits", lambda: comp_bits) + _n_(460516, "dest_bits", lambda: dest_bits) + _n_(460517, "jump_bits", lambda: jump_bits)
            _l_(460518)
        assert _c_(460523, _n_(460521, "len", lambda: len), _n_(460522, "binary", lambda: binary)) == 16
        _l_(460524)
        _c_(460528, _a_(460526, _n_(460525, "f", lambda: f), "write"), _n_(460527, "binary", lambda: binary))
        _l_(460529)