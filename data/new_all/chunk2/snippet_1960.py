# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75351113/pyinstaller-with-customtkinter-exception-when-running-exe-attributeerror-m
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import customtkinter
    _l_(475096)

except ImportError:
    pass

# create the root window
root_file = _c_(475099, _a_(475098, _n_(475097, "customtkinter", lambda: customtkinter), "CTk"))
_l_(475100)
_c_(475103, _a_(475102, _n_(475101, "root_file", lambda: root_file), "title"), 'Data Analysis Tool - File Selection')
_l_(475104)
_c_(475107, _a_(475106, _n_(475105, "root_file", lambda: root_file), "resizable"), False, False)
_l_(475108)
_c_(475111, _a_(475110, _n_(475109, "root_file", lambda: root_file), "geometry"), '350x150')
_l_(475112)

_c_(475115, _a_(475114, _n_(475113, "root_file", lambda: root_file), "mainloop"))
_l_(475116)