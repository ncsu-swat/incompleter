# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/49762189/keep-getting-name-error-name-getname-not-defined
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Pet :
    _l_(460433)


    def main() :
        _l_(460404)

        _c_(460392, _n_(460389, "print", lambda: print), _c_(460391, _n_(460390, "getName", lambda: getName)))
        _l_(460393)
        _c_(460397, _n_(460394, "print", lambda: print), _c_(460396, _n_(460395, "getSpecies", lambda: getSpecies)))
        _l_(460398)
        _c_(460402, _n_(460399, "print", lambda: print), _c_(460401, _n_(460400, "getAge", lambda: getAge)))
        _l_(460403)

    def getName(self) :
        _l_(460412)

        name = _c_(460408, _n_(460405, "str", lambda: str), _c_(460407, _n_(460406, "input", lambda: input), "What is your pets name: "))
        _l_(460409)
        aux = _n_(460410, "name", lambda: name)
        _l_(460411)
        return aux

    def getSpecies(self) :
        _l_(460420)

        species = _c_(460416, _n_(460413, "str", lambda: str), _c_(460415, _n_(460414, "input", lambda: input), "What is your pets species: "))
        _l_(460417)
        aux = _n_(460418, "species", lambda: species)
        _l_(460419)
        return aux

    def getAge(self) :
        _l_(460430)

        age = _c_(460424, _n_(460421, "int", lambda: int), _c_(460423, _n_(460422, "input", lambda: input), "Please type in your age: "))
        _l_(460425)
        aux = _c_(460428, _n_(460426, "print", lambda: print), _n_(460427, "age", lambda: age))
        _l_(460429)
        return aux

    _c_(460431, main)
    _l_(460432)