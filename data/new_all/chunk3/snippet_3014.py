# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/54327442/filenotfounderror-even-though-file-exist
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def main():
        _l_(545056)

        lines =0
        _l_(545008)
        path = '//10.8.4.49/Projects/QASA_BR_TCL_Env_7.2.250/Utils/BR_Env/Call Generator/results/Console_Logs/*'
        _l_(545009)
        files = _c_(545013, _a_(545011, _n_(545010, "glob", lambda: glob), "glob"), _n_(545012, "path", lambda: path))
        _l_(545014)
        _c_(545016, _n_(545015, "print", lambda: print), "files")
        _l_(545017)
        _c_(545019, _n_(545018, "print", lambda: print), '\n')
        _l_(545020)
        _c_(545023, _n_(545021, "print", lambda: print), _n_(545022, "files", lambda: files))
        _l_(545024)
        for name in _c_(545028, _a_(545026, _n_(545025, "glob", lambda: glob), "glob"), _n_(545027, "path", lambda: path)):
                _l_(545055)

                _c_(545031, _n_(545029, "print", lambda: print), _n_(545030, "path", lambda: path))
                _l_(545032)
                readFile = _c_(545037, _a_(545036, _c_(545035, _a_(545034, _n_(545033, "name", lambda: name), "split"), "/")[9], "split"), "\\")[1]
                _l_(545038)
                _c_(545041, _n_(545039, "print", lambda: print), _n_(545040, "readFile", lambda: readFile))
                _l_(545042)
                with _c_(545045, _n_(545043, "open", lambda: open), _n_(545044, "readFile", lambda: readFile),"r") as file:
                        _l_(545054)

                        lines = _c_(545048, _a_(545047, _n_(545046, "file", lambda: file), "readlines"))
                        _l_(545049)
                        _c_(545052, _n_(545050, "print", lambda: print), _n_(545051, "lines", lambda: lines))
                        _l_(545053)
_c_(545058, _n_(545057, "main", lambda: main))
_l_(545059)

_n_(545060, "files", lambda: files)
_l_(545061)