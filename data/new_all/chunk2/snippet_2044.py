# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67182310/typeerror-pack-configure-missing-1-required-positional-argument-self
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
my_window = _c_(425545, _n_(425544, "Tk", lambda: Tk))
_l_(425546)
my_canvas_1 = _c_(425549, _n_(425547, "Canvas", lambda: Canvas), _n_(425548, "my_window", lambda: my_window), height=500, width=500, bg='white')
_l_(425550)
my_canvas_2 = _c_(425553, _n_(425551, "Canvas", lambda: Canvas), _n_(425552, "my_window", lambda: my_window), height=500, width=250, bg='white')
_l_(425554)
_c_(425557, _a_(425556, _n_(425555, "my_canvas_1", lambda: my_canvas_1), "grid"), row=0, column=0)
_l_(425558)
_c_(425561, _a_(425560, _n_(425559, "my_canvas_2", lambda: my_canvas_2), "grid"), row=0, column=1)
_l_(425562)
_c_(425565, _a_(425564, _n_(425563, "Canvas", lambda: Canvas), "pack"))
_l_(425566)
_c_(425569, _a_(425568, _n_(425567, "my_window", lambda: my_window), "mainloop")) 
_l_(425570) 