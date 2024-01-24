# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59756898/within-contextlib-redirect-stdout-the-print-function-causes-an-attributeerro
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
dummy_file = "dummy_textfile.txt"  # file to which the stdout shall be redirected
_l_(433900)  # file to which the stdout shall be redirected

with _c_(433904, _a_(433902, _n_(433901, "contextlib", lambda: contextlib), "redirect_stdout"), _n_(433903, "dummy_file", lambda: dummy_file)):
    _l_(433912)

    # Direct print()-function call
    _c_(433906, _n_(433905, "print", lambda: print), "Informative string which shall go to the textfile instead of the console.")
    _l_(433907)

    # Indirect print()-function calls (internally)
    _c_(433910, _n_(433908, "custom_function_with_internal_print_calls", lambda: custom_function_with_internal_print_calls), **_n_(433909, "kwargs", lambda: kwargs))
    _l_(433911)