# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/76399931/attributeerror-cant-pickle-local-object-flask-init-locals-lambda
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from multiprocessing import Process
    _l_(618158)

except ImportError:
    pass
try:
    import random
    _l_(618160)

except ImportError:
    pass
try:
    import string
    _l_(618162)

except ImportError:
    pass
try:
    import dill
    _l_(618164)

except ImportError:
    pass
try:
    import ServiceLogger as sl
    _l_(618166)

except ImportError:
    pass


class DillProcess(_n_(618167, "Process", lambda: Process)):
    _l_(618201)


    def __init__(self, *args, **kwargs):
        _l_(618181)

        _c_(618172, _a_(618169, _n_(618168, "super", lambda: super)(), "__init__"), *_n_(618170, "args", lambda: args), **_n_(618171, "kwargs", lambda: kwargs))
        _l_(618173)
        _n_(618174, "self", lambda: self)._target = _c_(618179, _a_(618176, _n_(618175, "dill", lambda: dill), "dumps"), _a_(618178, _n_(618177, "self", lambda: self), "_target"))  # Save the target function as bytes, using dill
        _l_(618180)  # Save the target function as bytes, using dill

    def run(self):
        _l_(618200)

        if _a_(618183, _n_(618182, "self", lambda: self), "_target"):
            _l_(618199)

            _n_(618184, "self", lambda: self)._target = _c_(618189, _a_(618186, _n_(618185, "dill", lambda: dill), "loads"), _a_(618188, _n_(618187, "self", lambda: self), "_target"))  # Unpickle the target function before executing
            _l_(618190)  # Unpickle the target function before executing
            _c_(618197, _a_(618192, _n_(618191, "self", lambda: self), "_target"), *_a_(618194, _n_(618193, "self", lambda: self), "_args"), **_a_(618196, _n_(618195, "self", lambda: self), "_kwargs"))  # Execute the target function
            _l_(618198)  # Execute the target function


class ProcessBuilder:
    _l_(618280)


    def __init__(self):
        _l_(618209)

        _n_(618202, "self", lambda: self).processes = []
        _l_(618203)
        _n_(618204, "self", lambda: self).logger = _c_(618207, _a_(618206, _n_(618205, "sl", lambda: sl), "ServiceLogger"))
        _l_(618208)

    def create_process(self, method, args=[]):
        _l_(618228)

        process = _c_(618218, _n_(618210, "DillProcess", lambda: DillProcess), name=_c_(618213, _a_(618212, _n_(618211, "self", lambda: self), "__generate_instance_name")), target=_n_(618214, "method", lambda: method), args=_c_(618217, _n_(618215, "tuple", lambda: tuple), _n_(618216, "args", lambda: args)))
        _l_(618219)
        _c_(618224, _a_(618222, _a_(618221, _n_(618220, "self", lambda: self), "processes"), "append"), _n_(618223, "process", lambda: process))
        _l_(618225)
        aux = _n_(618226, "process", lambda: process)
        _l_(618227)
        return aux

    def get_process_instance(self, process_name):
        _l_(618241)

        for process in _a_(618230, _n_(618229, "self", lambda: self), "processes"):
            _l_(618239)

            if _c_(618234, _n_(618231, "str", lambda: str), _a_(618233, _n_(618232, "process", lambda: process), "name")) == _n_(618235, "process_name", lambda: process_name):
                _l_(618238)

                aux = _n_(618236, "process", lambda: process)
                _l_(618237)
                return aux
        aux = None
        _l_(618240)
        return aux

    def run_process(self, process):
        _l_(618246)

        _c_(618244, _a_(618243, _n_(618242, "process", lambda: process), "start"))
        _l_(618245)

    def kill_process(self, process):
        _l_(618251)

        _c_(618249, _a_(618248, _n_(618247, "process", lambda: process), "kill"))
        _l_(618250)

    def __generate_instance_name(self):
        _l_(618279)

        # printing lowercase
        letters = _a_(618253, _n_(618252, "string", lambda: string), "ascii_lowercase")
        _l_(618254)
        randomString = _c_(618262, _a_(618255, '', "join"), (_c_(618259, _a_(618257, _n_(618256, "random", lambda: random), "choice"), _n_(618258, "letters", lambda: letters)) for i in _c_(618261, _n_(618260, "range", lambda: range), 3)))
        _l_(618263)

        # printing letters
        letters = _a_(618265, _n_(618264, "string", lambda: string), "digits")
        _l_(618266)
        randomDigits = _c_(618274, _a_(618267, '', "join"), (_c_(618271, _a_(618269, _n_(618268, "random", lambda: random), "choice"), _n_(618270, "letters", lambda: letters)) for i in _c_(618273, _n_(618272, "range", lambda: range), 5)))
        _l_(618275)
        aux = _n_(618276, "randomString", lambda: randomString) + "" + _n_(618277, "randomDigits", lambda: randomDigits)
        _l_(618278)

        return aux