# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/74524141/matplotlib-attributeerror-nonetype-object-has-no-attribute-get-view
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(473909)

except ImportError:
    pass
try:
    from numpy import sqrt
    _l_(473911)

except ImportError:
    pass
try:
    from random import randint
    _l_(473913)

except ImportError:
    pass
try:
    import math
    _l_(473915)

except ImportError:
    pass
try:
    from matplotlib import pyplot as plt
    _l_(473917)

except ImportError:
    pass
try:
    from matplotlib import collections
    _l_(473919)

except ImportError:
    pass
_a_(473921, _n_(473920, "plt", lambda: plt), "rcParams")["figure.figsize"] = 4, 4
_l_(473922)
try:
    from matplotlib.animation import FuncAnimation
    _l_(473924)

except ImportError:
    pass

np_rnd = _c_(473928, _a_(473927, _a_(473926, _n_(473925, "np", lambda: np), "random"), "default_rng"))
_l_(473929)


class Ball:
    _l_(473972)

    x0 = 0
    _l_(473930)
    y0 = 0
    _l_(473931)
    x = 0
    _l_(473932)
    y = 0
    _l_(473933)
    r = 0
    _l_(473934)
    t = 0
    _l_(473935)
    m = 0
    _l_(473936)
    v_speed = _c_(473939, _a_(473938, _n_(473937, "np", lambda: np), "array"), [0, 0])
    _l_(473940)
    v_accel = _c_(473943, _a_(473942, _n_(473941, "np", lambda: np), "array"), [0, 0])
    _l_(473944)

    def __init__(self, x_, y_, r_, m_, v_speed_, v_accel_):
        _l_(473971)

        _n_(473945, "self", lambda: self).m = _n_(473946, "m_", lambda: m_)
        _l_(473947)
        _n_(473948, "self", lambda: self).x = _n_(473949, "x_", lambda: x_)
        _l_(473950)
        _n_(473951, "self", lambda: self).y = _n_(473952, "y_", lambda: y_)
        _l_(473953)
        _n_(473954, "self", lambda: self).x0 = _n_(473955, "x_", lambda: x_)
        _l_(473956)
        _n_(473957, "self", lambda: self).y0 = _n_(473958, "y_", lambda: y_)
        _l_(473959)
        _n_(473960, "self", lambda: self).r = _n_(473961, "r_", lambda: r_)
        _l_(473962)
        _n_(473963, "self", lambda: self).v_speed = _n_(473964, "v_speed_", lambda: v_speed_)
        _l_(473965)
        _n_(473966, "self", lambda: self).v_accel = _n_(473967, "v_accel_", lambda: v_accel_)
        _l_(473968)
        _n_(473969, "self", lambda: self).t = 0
        _l_(473970)


def get_cmap(n, name='hsv'):
    _l_(473980)

    aux = _c_(473978, _a_(473975, _a_(473974, _n_(473973, "plt", lambda: plt), "cm"), "get_cmap"), _n_(473976, "name", lambda: name), _n_(473977, "n", lambda: n))
    _l_(473979)
    return aux


FPS = 77
_l_(473981)

X_MIN = -1
_l_(473982)
X_MAX = 100
_l_(473983)

Y_MIN = -1
_l_(473984)
Y_MAX = 100
_l_(473985)


RADIUS_MIN = 1
_l_(473986)
RADIUS_MAX = 3
_l_(473987)

K_RADIUS = 50
_l_(473988)
MASS_MAX = 6
_l_(473989)

SPEED_MAX = 0.5
_l_(473990)
ACCEL_MAX = 0
_l_(473991)

N = 5
_l_(473992)
T = 1
_l_(473993)


ball_list = []
_l_(473994)
xy_balls = _a_(473996, _n_(473995, "np", lambda: np), "c_")[_c_(474004, _a_(473998, _n_(473997, "np_rnd", lambda: np_rnd), "integers"), _n_(473999, "X_MIN", lambda: X_MIN)+_n_(474000, "RADIUS_MAX", lambda: RADIUS_MAX), _n_(474001, "X_MAX", lambda: X_MAX)-_n_(474002, "RADIUS_MAX", lambda: RADIUS_MAX),_n_(474003, "N", lambda: (N))),
                 _c_(474012, _a_(474006, _n_(474005, "np_rnd", lambda: np_rnd), "integers"), _n_(474007, "Y_MIN", lambda: Y_MIN)+_n_(474008, "RADIUS_MAX", lambda: RADIUS_MAX), _n_(474009, "Y_MAX", lambda: Y_MAX)-_n_(474010, "RADIUS_MAX", lambda: RADIUS_MAX),_n_(474011, "N", lambda: (N)))]
_l_(474013)

r_balls = _c_(474019, _a_(474015, _n_(474014, "np_rnd", lambda: np_rnd), "integers"), _n_(474016, "RADIUS_MIN", lambda: RADIUS_MIN), _n_(474017, "RADIUS_MAX", lambda: RADIUS_MAX), _n_(474018, "N", lambda: N))
_l_(474020)
color_balls = _c_(474024, _a_(474022, _n_(474021, "np", lambda: np), "arange"), 0, _n_(474023, "N", lambda: N))
_l_(474025)




fig, ax = _c_(474028, _a_(474027, _n_(474026, "plt", lambda: plt), "subplots"))
_l_(474029)
_c_(474034, _a_(474031, _n_(474030, "ax", lambda: ax), "plot"), [_n_(474032, "X_MIN", lambda: X_MIN), _n_(474033, "X_MAX", lambda: X_MAX)], [0, 0], color='black', linewidth=0.5)
_l_(474035)
_c_(474039, _a_(474037, _n_(474036, "plt", lambda: plt), "annotate"), "x", xy=(_n_(474038, "X_MAX", lambda: X_MAX) - 2, 0))
_l_(474040)
_c_(474045, _a_(474042, _n_(474041, "ax", lambda: ax), "plot"), [0, 0], [_n_(474043, "Y_MIN", lambda: Y_MIN), _n_(474044, "Y_MAX", lambda: Y_MAX)], color='black', linewidth=0.5)
_l_(474046)
_c_(474050, _a_(474048, _n_(474047, "plt", lambda: plt), "annotate"), "y", xy=(0, _n_(474049, "Y_MAX", lambda: Y_MAX) - 2))
_l_(474051)
_c_(474054, _a_(474053, _n_(474052, "plt", lambda: plt), "annotate"), "0", xy=(2, 2))
_l_(474055)
cmap = _c_(474058, _n_(474056, "get_cmap", lambda: get_cmap), _n_(474057, "N", lambda: N))
_l_(474059)
for i in _c_(474062, _n_(474060, "range", lambda: range), _n_(474061, "N", lambda: N)):
    _l_(474086)

    _c_(474084, _a_(474064, _n_(474063, "ball_list", lambda: ball_list), "append"), _c_(474083, _n_(474065, "Ball", lambda: Ball), _n_(474066, "xy_balls", lambda: xy_balls)[_n_(474067, "i", lambda: i)][0],
                          _n_(474068, "xy_balls", lambda: xy_balls)[_n_(474069, "i", lambda: i)][1],
                          _n_(474070, "r_balls", lambda: r_balls)[_n_(474071, "i", lambda: i)],
                          _c_(474074, _n_(474072, "randint", lambda: randint), 1, _n_(474073, "MASS_MAX", lambda: MASS_MAX)),
                          _c_(474078, _a_(474076, _n_(474075, "np_rnd", lambda: np_rnd), "uniform"), 0, _n_(474077, "SPEED_MAX", lambda: SPEED_MAX), size=2),
                          _c_(474082, _a_(474080, _n_(474079, "np_rnd", lambda: np_rnd), "uniform"), 0, _n_(474081, "ACCEL_MAX", lambda: ACCEL_MAX), size=2)
                          )
                     )
    _l_(474085)

balls_plt = [_c_(474094, _a_(474088, _n_(474087, "plt", lambda: plt), "Circle"), _n_(474089, "center", lambda: center), radius=_n_(474090, "radius", lambda: radius), color=_c_(474093, _n_(474091, "cmap", lambda: cmap), _n_(474092, "color", lambda: color))) for center, radius, color in _c_(474099, _n_(474095, "zip", lambda: zip), _n_(474096, "xy_balls", lambda: xy_balls), _n_(474097, "r_balls", lambda: r_balls), _n_(474098, "color_balls", lambda: color_balls))]
_l_(474100)

balls_plt_updater = _n_(474101, "balls_plt", lambda: balls_plt)
_l_(474102)



def checkBorder(ball):
    _l_(474197)

    if (_a_(474104, _n_(474103, "ball", lambda: ball), "x") > _n_(474105, "X_MAX", lambda: X_MAX)) or (_a_(474107, _n_(474106, "ball", lambda: ball), "x") < _n_(474108, "X_MIN", lambda: X_MIN)):
        _l_(474149)

        _n_(474109, "ball", lambda: ball).x = (_n_(474110, "X_MAX", lambda: X_MAX) - 1) if _a_(474112, _n_(474111, "ball", lambda: ball), "x") > _n_(474113, "X_MAX", lambda: X_MAX) else _n_(474114, "X_MIN", lambda: X_MIN) + 1
        _l_(474115)
        _n_(474116, "ball", lambda: ball).x0 = _a_(474118, _n_(474117, "ball", lambda: ball), "x")
        _l_(474119)
        _n_(474120, "ball", lambda: ball).y0 = _a_(474122, _n_(474121, "ball", lambda: ball), "y")
        _l_(474123)
        _a_(474125, _n_(474124, "ball", lambda: ball), "v_speed")[0] = -(_a_(474127, _n_(474126, "ball", lambda: ball), "v_speed")[0] + _a_(474129, _n_(474128, "ball", lambda: ball), "t") * _a_(474131, _n_(474130, "ball", lambda: ball), "v_accel")[0])
        _l_(474132)
        _a_(474134, _n_(474133, "ball", lambda: ball), "v_speed")[1] = _a_(474136, _n_(474135, "ball", lambda: ball), "v_speed")[1] + _a_(474138, _n_(474137, "ball", lambda: ball), "t") * _a_(474140, _n_(474139, "ball", lambda: ball), "v_accel")[1]
        _l_(474141)
        _a_(474143, _n_(474142, "ball", lambda: ball), "v_accel")[0] = -_a_(474145, _n_(474144, "ball", lambda: ball), "v_accel")[0]
        _l_(474146)
        _n_(474147, "ball", lambda: ball).t = 0
        _l_(474148)

    if (_a_(474151, _n_(474150, "ball", lambda: ball), "y") > _n_(474152, "Y_MAX", lambda: Y_MAX)) or (_a_(474154, _n_(474153, "ball", lambda: ball), "y") < _n_(474155, "Y_MIN", lambda: Y_MIN)):
        _l_(474196)

        _n_(474156, "ball", lambda: ball).y = (_n_(474157, "Y_MAX", lambda: Y_MAX) - 1) if _a_(474159, _n_(474158, "ball", lambda: ball), "y") > _n_(474160, "Y_MAX", lambda: Y_MAX) else _n_(474161, "Y_MIN", lambda: Y_MIN) + 1
        _l_(474162)
        _n_(474163, "ball", lambda: ball).x0 = _a_(474165, _n_(474164, "ball", lambda: ball), "x")
        _l_(474166)
        _n_(474167, "ball", lambda: ball).y0 = _a_(474169, _n_(474168, "ball", lambda: ball), "y")
        _l_(474170)
        _a_(474172, _n_(474171, "ball", lambda: ball), "v_speed")[0] = _a_(474174, _n_(474173, "ball", lambda: ball), "v_speed")[0] + _a_(474176, _n_(474175, "ball", lambda: ball), "t") * _a_(474178, _n_(474177, "ball", lambda: ball), "v_accel")[0]
        _l_(474179)
        _a_(474181, _n_(474180, "ball", lambda: ball), "v_speed")[1] = -(_a_(474183, _n_(474182, "ball", lambda: ball), "v_speed")[1] + _a_(474185, _n_(474184, "ball", lambda: ball), "t") * _a_(474187, _n_(474186, "ball", lambda: ball), "v_accel")[1])
        _l_(474188)
        _a_(474190, _n_(474189, "ball", lambda: ball), "v_accel")[1] = -_a_(474192, _n_(474191, "ball", lambda: ball), "v_accel")[1]
        _l_(474193)
        _n_(474194, "ball", lambda: ball).t = 0
        _l_(474195)


def checkBite(ball1, ball2):
    _l_(474322)

    D = _c_(474208, _a_(474199, _n_(474198, "math", lambda: math), "sqrt"), ((_a_(474201, _n_(474200, "ball1", lambda: ball1), "x") - _a_(474203, _n_(474202, "ball2", lambda: ball2), "x")) ** 2) + ((_a_(474205, _n_(474204, "ball1", lambda: ball1), "y") - _a_(474207, _n_(474206, "ball2", lambda: ball2), "y")) ** 2))
    _l_(474209)

    if _n_(474210, "D", lambda: D) < (_a_(474212, _n_(474211, "ball1", lambda: ball1), "r") + _a_(474214, _n_(474213, "ball2", lambda: ball2), "r")):
        _l_(474321)

        _a_(474216, _n_(474215, "ball1", lambda: ball1), "v_speed")[0] = ((_a_(474218, _n_(474217, "ball1", lambda: ball1), "m") - _a_(474220, _n_(474219, "ball2", lambda: ball2), "m")) * _a_(474222, _n_(474221, "ball1", lambda: ball1), "v_speed")[0] + 2 * _a_(474224, _n_(474223, "ball2", lambda: ball2), "m") * _a_(474226, _n_(474225, "ball2", lambda: ball2), "v_speed")[0]) / (
                    _a_(474228, _n_(474227, "ball1", lambda: ball1), "m") + _a_(474230, _n_(474229, "ball2", lambda: ball2), "m"))
        _l_(474231)
        _a_(474233, _n_(474232, "ball1", lambda: ball1), "v_speed")[1] = ((_a_(474235, _n_(474234, "ball1", lambda: ball1), "m") - _a_(474237, _n_(474236, "ball2", lambda: ball2), "m")) * _a_(474239, _n_(474238, "ball1", lambda: ball1), "v_speed")[1] + 2 * _a_(474241, _n_(474240, "ball2", lambda: ball2), "m") * _a_(474243, _n_(474242, "ball2", lambda: ball2), "v_speed")[1]) / (
                    _a_(474245, _n_(474244, "ball1", lambda: ball1), "m") + _a_(474247, _n_(474246, "ball2", lambda: ball2), "m"))
        _l_(474248)
        _a_(474250, _n_(474249, "ball2", lambda: ball2), "v_speed")[0] = ((_a_(474252, _n_(474251, "ball2", lambda: ball2), "m") - _a_(474254, _n_(474253, "ball1", lambda: ball1), "m")) * _a_(474256, _n_(474255, "ball2", lambda: ball2), "v_speed")[0] + 2 * _a_(474258, _n_(474257, "ball1", lambda: ball1), "m") * _a_(474260, _n_(474259, "ball1", lambda: ball1), "v_speed")[0]) / (
                    _a_(474262, _n_(474261, "ball1", lambda: ball1), "m") + _a_(474264, _n_(474263, "ball2", lambda: ball2), "m"))
        _l_(474265)
        _a_(474267, _n_(474266, "ball2", lambda: ball2), "v_speed")[1] = ((_a_(474269, _n_(474268, "ball2", lambda: ball2), "m") - _a_(474271, _n_(474270, "ball1", lambda: ball1), "m")) * _a_(474273, _n_(474272, "ball2", lambda: ball2), "v_speed")[1] + 2 * _a_(474275, _n_(474274, "ball1", lambda: ball1), "m") * _a_(474277, _n_(474276, "ball1", lambda: ball1), "v_speed")[1]) / (
                    _a_(474279, _n_(474278, "ball1", lambda: ball1), "m") + _a_(474281, _n_(474280, "ball2", lambda: ball2), "m"))
        _l_(474282)

        _n_(474283, "ball1", lambda: ball1).x0 = _a_(474285, _n_(474284, "ball1", lambda: ball1), "x") + (_a_(474287, _n_(474286, "ball1", lambda: ball1), "v_speed")[0] * _a_(474289, _n_(474288, "ball1", lambda: ball1), "r"))
        _l_(474290)
        _n_(474291, "ball1", lambda: ball1).y0 = _a_(474293, _n_(474292, "ball1", lambda: ball1), "y") + (_a_(474295, _n_(474294, "ball1", lambda: ball1), "v_speed")[1] * _a_(474297, _n_(474296, "ball1", lambda: ball1), "r"))
        _l_(474298)
        _n_(474299, "ball2", lambda: ball2).x0 = _a_(474301, _n_(474300, "ball2", lambda: ball2), "x") + (_a_(474303, _n_(474302, "ball2", lambda: ball2), "v_speed")[0] * _a_(474305, _n_(474304, "ball2", lambda: ball2), "r"))
        _l_(474306)
        _n_(474307, "ball2", lambda: ball2).y0 = _a_(474309, _n_(474308, "ball2", lambda: ball2), "y") + (_a_(474311, _n_(474310, "ball2", lambda: ball2), "v_speed")[1] * _a_(474313, _n_(474312, "ball2", lambda: ball2), "r"))
        _l_(474314)
        _n_(474315, "ball1", lambda: ball1).t = _n_(474316, "T", lambda: T)
        _l_(474317)
        _n_(474318, "ball2", lambda: ball2).t = _n_(474319, "T", lambda: T)
        _l_(474320)



def setCoord(ball):
    _l_(474350)

    _n_(474323, "ball", lambda: ball).x = _a_(474325, _n_(474324, "ball", lambda: ball), "x0") + _a_(474327, _n_(474326, "ball", lambda: ball), "v_speed")[0] * _a_(474329, _n_(474328, "ball", lambda: ball), "t") + (_a_(474331, _n_(474330, "ball", lambda: ball), "v_accel")[0] * (_a_(474333, _n_(474332, "ball", lambda: ball), "t") ** 2)) / 2
    _l_(474334)
    _n_(474335, "ball", lambda: ball).y = _a_(474337, _n_(474336, "ball", lambda: ball), "y0") + _a_(474339, _n_(474338, "ball", lambda: ball), "v_speed")[1] * _a_(474341, _n_(474340, "ball", lambda: ball), "t") + (_a_(474343, _n_(474342, "ball", lambda: ball), "v_accel")[1] * (_a_(474345, _n_(474344, "ball", lambda: ball), "t") ** 2)) / 2
    _l_(474346)
    _n_(474347, "ball", lambda: ball).t += _n_(474348, "T", lambda: T)
    _l_(474349)



def animate(i, balls):
    _l_(474378)

    for j in _c_(474355, _n_(474351, "range", lambda: range), _c_(474354, _n_(474352, "len", lambda: len), _n_(474353, "balls", lambda: balls))):
        _l_(474375)

        #for k in range(j+1, len(balls)):
        #    checkBite(balls[j], balls[k])
        _c_(474359, _n_(474356, "checkBorder", lambda: checkBorder), _n_(474357, "balls", lambda: balls)[_n_(474358, "j", lambda: j)])
        _l_(474360)
        _c_(474364, _n_(474361, "setCoord", lambda: setCoord), _n_(474362, "balls", lambda: balls)[_n_(474363, "j", lambda: j)])
        _l_(474365)
        _n_(474366, "balls_plt", lambda: balls_plt)[_n_(474367, "j", lambda: j)].center = _a_(474370, _n_(474368, "balls", lambda: balls)[_n_(474369, "j", lambda: j)], "x"), _a_(474373, _n_(474371, "balls", lambda: balls)[_n_(474372, "j", lambda: j)], "y")
        _l_(474374)
    aux = _n_(474376, "balls_plt_updater", lambda: balls_plt_updater)
    _l_(474377)


    return aux


anim = _c_(474390, _n_(474379, "FuncAnimation", lambda: FuncAnimation), fig=_n_(474380, "fig", lambda: fig), func=_n_(474381, "animate", lambda: animate), fargs=(_n_(474382, "ball_list", lambda: ball_list),),
                     frames=_c_(474388, _a_(474384, _n_(474383, "np", lambda: np), "linspace"), 0, _n_(474385, "FPS", lambda: FPS) * 2, num=1000, dtype=_a_(474387, _n_(474386, "np", lambda: np), "intc"), endpoint=False),
                     interval=1000 / _n_(474389, "FPS", lambda: (FPS)), blit=True, repeat=True)
_l_(474391)

_c_(474394, _a_(474393, _n_(474392, "plt", lambda: plt), "show"))
_l_(474395)