# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/42427389/typeerror-str-object-is-not-callable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Parser(_n_(334853, "object", lambda: object)):
    _l_(334936)


    def __init__(self, inputFile):
        _l_(334876)

        #open input file and gets ready to parse it
        f = _c_(334856, _n_(334854, "open", lambda: open), _n_(334855, "inputFile", lambda: inputFile), "r")
        _l_(334857)
        _n_(334858, "self", lambda: self).commands = _c_(334861, _n_(334859, "list", lambda: list), _n_(334860, "f", lambda: f))
        _l_(334862)
        _c_(334865, _a_(334864, _n_(334863, "f", lambda: f), "close"))
        _l_(334866)
        _c_(334870, _n_(334867, "print", lambda: print), _a_(334869, _n_(334868, "self", lambda: self), "commands"))
        _l_(334871)
        _n_(334872, "self", lambda: self).currentCommand = 0
        _l_(334873)
        _n_(334874, "self", lambda: self).index = 0
        _l_(334875)

    def hasMoreCommands(self):
        _l_(334892)

        #are there any more commands in the input
        #returns boolean
        if (_a_(334878, _n_(334877, "self", lambda: self), "commands")[_a_(334880, _n_(334879, "self", lambda: self), "currentCommand")][_a_(334882, _n_(334881, "self", lambda: self), "index")] == "\\")  and (_a_(334884, _n_(334883, "self", lambda: self), "commands")[_a_(334886, _n_(334885, "self", lambda: self), "currentCommand")][_a_(334888, _n_(334887, "self", lambda: self), "index")+1] == "n"):
            _l_(334891)

            aux = True
            _l_(334889)
            return aux
        else:
            aux = False
            _l_(334890)
            return aux

    def advance(self):
        _l_(334899)

        #reads next command and makes it current command
        #called only if hasMoreCommands is true
        if _c_(334895, _a_(334894, _n_(334893, "self", lambda: self), "hasMoreCommands")):
            _l_(334898)

            _n_(334896, "self", lambda: self).currentCommand += 1
            _l_(334897)

    def commandType(self):
        _l_(334915)

        #returns type of current command A_COMMAND, C_COMMAND, L_COMMAND
        #C A or L(psuedo command for (XxX))
        #dest=comp; jmp, @, ()
        _n_(334900, "self", lambda: self).type = _a_(334902, _n_(334901, "self", lambda: self), "commands")[_a_(334904, _n_(334903, "self", lambda: self), "currentCommand")][0]
        _l_(334905)
        if _a_(334907, _n_(334906, "self", lambda: self), "type") == "@":
            _l_(334914)

            aux = "A_COMMAND"
            _l_(334908)
            return aux
        elif _a_(334910, _n_(334909, "self", lambda: self), "type") == "(":
            _l_(334913)

            aux = "L_COMMAND"
            _l_(334911)
            return aux
        else:
            aux = "C_COMMAND"
            _l_(334912)
            return aux

    def dest(self):
        _l_(334935)

        #returns dest mnemoic of current C instruction - 8 Poss
        #called when command type is C
        #return string
        if (_c_(334918, _a_(334917, _n_(334916, "self", lambda: self), "commandType")) == "C_COMMAND") and ("=" in _a_(334920, _n_(334919, "self", lambda: self), "commands")[_a_(334922, _n_(334921, "self", lambda: self), "currentCommand")]):
            _l_(334934)

            aux = _a_(334924, _n_(334923, "self", lambda: self), "commands")[_a_(334926, _n_(334925, "self", lambda: self), "currentCommand")][0:_c_(334932, _a_(334931, _a_(334928, _n_(334927, "self", lambda: self), "commands")[_a_(334930, _n_(334929, "self", lambda: self), "currentCommand")], "index"), "=")]
            _l_(334933)
            return aux

def main(inputFile):
    _l_(334953)

    d = _c_(334939, _n_(334937, "Parser", lambda: Parser), _n_(334938, "inputFile", lambda: inputFile))
    _l_(334940)
    _n_(334941, "d", lambda: d).commandType = "C_COMMAND"
    _l_(334942)
    _n_(334943, "d", lambda: d).commands = ["D=A+2\\n", "AMD=A+5\\n"]
    _l_(334944)
    _n_(334945, "d", lambda: d).currentCommand = 0
    _l_(334946)
    _c_(334951, _n_(334947, "print", lambda: print), _c_(334950, _a_(334949, _n_(334948, "d", lambda: d), "dest")))
    _l_(334952)

_c_(334955, _n_(334954, "main", lambda: main), "/Users/user1/Desktop/filelocation/projects/06/add/add.asm")
_l_(334956)