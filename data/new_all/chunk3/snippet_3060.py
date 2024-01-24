# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/50773148/typeerror-datetime-on-x-axis-through-matplotlib-animation
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import random
    _l_(540437)

except ImportError:
    pass
try:
    import time
    _l_(540439)

except ImportError:
    pass
try:
    from matplotlib import pyplot as plt
    _l_(540441)

except ImportError:
    pass
try:
    from matplotlib import animation
    _l_(540443)

except ImportError:
    pass
try:
    import datetime
    _l_(540445)

except ImportError:
    pass

# Plot parameters
fig, ax = _c_(540448, _a_(540447, _n_(540446, "plt", lambda: plt), "subplots"))
_l_(540449)
line, = _c_(540452, _a_(540451, _n_(540450, "ax", lambda: ax), "plot"), [], [], 'k-', label = 'ABNA: Price', color = 'blue')
_l_(540453)
legend = _c_(540456, _a_(540455, _n_(540454, "ax", lambda: ax), "legend"), loc='upper right',frameon=False)
_l_(540457)
_c_(540463, _a_(540459, _n_(540458, "plt", lambda: plt), "setp"), _c_(540462, _a_(540461, _n_(540460, "legend", lambda: legend), "get_texts")), color='grey')
_l_(540464)
_c_(540467, _a_(540466, _n_(540465, "ax", lambda: ax), "margins"), 0.05)
_l_(540468)
_c_(540471, _a_(540470, _n_(540469, "ax", lambda: ax), "grid"), True, which='both', color = 'grey')
_l_(540472)

# Creating data variables
x = []
_l_(540473)
y = []
_l_(540474)
_c_(540477, _a_(540476, _n_(540475, "x", lambda: x), "append"), 1)
_l_(540478)
_c_(540481, _a_(540480, _n_(540479, "y", lambda: y), "append"), 1)
_l_(540482)

def init():
    _l_(540491)

    _c_(540487, _a_(540484, _n_(540483, "line", lambda: line), "set_data"), _n_(540485, "x", lambda: x)[:1],_n_(540486, "y", lambda: y)[:1])
    _l_(540488)
    aux = _n_(540489, "line", lambda: line),
    _l_(540490)
    return aux

def animate(args):
    _l_(540583)

    # Args are the incoming value that are animated    
    _n_(540492, "animate", lambda: animate).counter += 1
    _l_(540493)
    i = _a_(540495, _n_(540494, "animate", lambda: animate), "counter")
    _l_(540496)
    win = 60
    _l_(540497)
    imin = _c_(540507, _n_(540498, "min", lambda: min), _c_(540502, _n_(540499, "max", lambda: max), 0, _n_(540500, "i", lambda: i) - _n_(540501, "win", lambda: win)), _c_(540505, _n_(540503, "len", lambda: len), _n_(540504, "x", lambda: x)) - _n_(540506, "win", lambda: win))
    _l_(540508)

    _c_(540512, _a_(540510, _n_(540509, "x", lambda: x), "append"), _n_(540511, "args", lambda: args)[0])
    _l_(540513)
    _c_(540517, _a_(540515, _n_(540514, "y", lambda: y), "append"), _n_(540516, "args", lambda: args)[1])
    _l_(540518)

    xdata = _n_(540519, "x", lambda: x)[_n_(540520, "imin", lambda: imin):_n_(540521, "i", lambda: i)]
    _l_(540522)
    ydata = _n_(540523, "y", lambda: y)[_n_(540524, "imin", lambda: imin):_n_(540525, "i", lambda: i)]
    _l_(540526)

    _c_(540531, _a_(540528, _n_(540527, "line", lambda: line), "set_data"), _n_(540529, "xdata", lambda: xdata), _n_(540530, "ydata", lambda: ydata))
    _l_(540532)
    _c_(540535, _a_(540534, _n_(540533, "line", lambda: line), "set_color"), "red")
    _l_(540536)

    _c_(540539, _a_(540538, _n_(540537, "plt", lambda: plt), "title"), 'ABNA CALCULATIONS', color = 'grey')
    _l_(540540)
    _c_(540543, _a_(540542, _n_(540541, "plt", lambda: plt), "ylabel"), "Price", color ='grey')
    _l_(540544)
    _c_(540547, _a_(540546, _n_(540545, "plt", lambda: plt), "xlabel"), "Time", color = 'grey')
    _l_(540548)

    _c_(540551, _a_(540550, _n_(540549, "ax", lambda: ax), "set_facecolor"), 'black')
    _l_(540552)
    _c_(540557, _a_(540556, _a_(540555, _a_(540554, _n_(540553, "ax", lambda: ax), "xaxis"), "label"), "set_color"), 'grey')
    _l_(540558)
    _c_(540561, _a_(540560, _n_(540559, "ax", lambda: ax), "tick_params"), axis='x', colors='grey')
    _l_(540562)
    _c_(540567, _a_(540566, _a_(540565, _a_(540564, _n_(540563, "ax", lambda: ax), "yaxis"), "label"), "set_color"), 'grey')
    _l_(540568)
    _c_(540571, _a_(540570, _n_(540569, "ax", lambda: ax), "tick_params"), axis='y', colors='grey')
    _l_(540572)

    _c_(540575, _a_(540574, _n_(540573, "ax", lambda: ax), "relim"))
    _l_(540576)
    _c_(540579, _a_(540578, _n_(540577, "ax", lambda: ax), "autoscale"))
    _l_(540580)
    aux = _n_(540581, "line", lambda: line), #line2
    _l_(540582) #line2

    return aux #line2
_n_(540584, "animate", lambda: animate).counter = 0
_l_(540585)

def frames1():
    _l_(540636)

    # Generating time variable
    x = 10
    _l_(540586)
    target_time = _c_(540592, _a_(540591, _c_(540590, _a_(540589, _a_(540588, _n_(540587, "datetime", lambda: datetime), "datetime"), "now")), "strftime"), "%d %B %Y %H:%M:%000")
    _l_(540593)
    # Extracting time
    FMT = "%d %B %Y %H:%M:%S"
    _l_(540594)
    target_time = _c_(540600, _a_(540597, _a_(540596, _n_(540595, "datetime", lambda: datetime), "datetime"), "strptime"), _n_(540598, "target_time", lambda: target_time), _n_(540599, "FMT", lambda: FMT))
    _l_(540601)
    target_time = _c_(540606, _a_(540605, _c_(540604, _a_(540603, _n_(540602, "target_time", lambda: target_time), "time")), "isoformat"))    
    _l_(540607)    
    # Converting to time object
    target_time = _c_(540612, _a_(540610, _a_(540609, _n_(540608, "datetime", lambda: datetime), "datetime"), "strptime"), _n_(540611, "target_time", lambda: target_time),'%H:%M:%S') 
    _l_(540613) 
    while True:
        _l_(540635)

        # Add new time + 60 seconds
        target_time = _n_(540614, "target_time", lambda: target_time) + _c_(540617, _a_(540616, _n_(540615, "datetime", lambda: datetime), "timedelta"), seconds=60)
        _l_(540618)
        x = _n_(540619, "target_time", lambda: target_time)
        _l_(540620)
        y = _c_(540623, _a_(540622, _n_(540621, "random", lambda: random), "randint"), 250,450)/10
        _l_(540624)
        yield (_n_(540625, "x", lambda: x),_n_(540626, "y", lambda: y))  
        _l_(540627)  
        _c_(540633, _a_(540629, _n_(540628, "time", lambda: time), "sleep"), _c_(540632, _a_(540631, _n_(540630, "random", lambda: random), "randint"), 2,5))
        _l_(540634)

anim = _c_(540643, _a_(540638, _n_(540637, "animation", lambda: animation), "FuncAnimation"), _n_(540639, "fig", lambda: fig), _n_(540640, "animate", lambda: animate),init_func=_n_(540641, "init", lambda: init),frames=_n_(540642, "frames1", lambda: frames1))
_l_(540644)

_c_(540647, _a_(540646, _n_(540645, "plt", lambda: plt), "show"))
_l_(540648)