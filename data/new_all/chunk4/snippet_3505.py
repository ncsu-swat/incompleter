# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/73171934/attribute-error-when-closing-from-file-learn-python-the-hard-way-ex17
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from os.path import exists
    _l_(644270)

except ImportError:
    pass

script, from_file, to_file = _n_(644271, "argv", lambda: argv)
_l_(644272)

_c_(644276, _n_(644273, "print", lambda: print), f"Copying from {_n_(644274, 'from_file', lambda: from_file)} to {_n_(644275, 'to_file', lambda: to_file)}")
_l_(644277)

#I am attempting to shorten the code here
indata = _c_(644282, _a_(644281, _c_(644280, _n_(644278, "open", lambda: open), _n_(644279, "from_file", lambda: from_file)), "read"))
_l_(644283)

_c_(644288, _n_(644284, "print", lambda: print), f"The input file is {_c_(644287, _n_(644285, 'len', lambda: len), _n_(644286, 'indata', lambda: indata))} bytes long")
_l_(644289)

_c_(644294, _n_(644290, "print", lambda: print), f"Does the output file exist? {_c_(644293, _n_(644291, 'exists', lambda: exists), _n_(644292, 'to_file', lambda: to_file))}")
_l_(644295)
_c_(644297, _n_(644296, "print", lambda: print), "Ready, hit RETURN to continue, CTRL-C to abort.")
_l_(644298)
_c_(644300, _n_(644299, "input", lambda: input))
_l_(644301)

out_file = _c_(644304, _n_(644302, "open", lambda: open), _n_(644303, "to_file", lambda: to_file), 'w')
_l_(644305)
_c_(644309, _a_(644307, _n_(644306, "out_file", lambda: out_file), "write"), _n_(644308, "indata", lambda: indata))
_l_(644310)

_c_(644312, _n_(644311, "print", lambda: print), "Alright, all done.")
_l_(644313)

_c_(644316, _a_(644315, _n_(644314, "out_file", lambda: out_file), "close"))
_l_(644317)
# This line is drawing the attribute error
_c_(644320, _a_(644319, _n_(644318, "from_file", lambda: from_file), "close"))
_l_(644321)