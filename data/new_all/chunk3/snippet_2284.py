# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53414750/typeerror-line3dcollection-object-is-not-iterable
#Import libraries
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from mpl_toolkits.mplot3d import Axes3D
    _l_(533089)

except ImportError:
    pass
try:
    import matplotlib.pyplot as plt
    _l_(533091)

except ImportError:
    pass
try:
    from matplotlib import animation
    _l_(533093)

except ImportError:
    pass
try:
    import numpy as np
    _l_(533095)

except ImportError:
    pass

#Accept input (theta, phi) from a user
_c_(533097, _n_(533096, "print", lambda: print), "Put angle theta and phi, 0≤ theta ≤180, 0≤ phi ≤360")
_l_(533098)
theta = _c_(533100, _n_(533099, "input", lambda: input), "theta:")
_l_(533101)
phi = _c_(533103, _n_(533102, "input", lambda: input), "phi:")
_l_(533104)
theta = _c_(533110, _a_(533106, _n_(533105, "np", lambda: np), "radians"), _c_(533109, _n_(533107, "float", lambda: float), _n_(533108, "theta", lambda: theta)))
_l_(533111)
phi = _c_(533117, _a_(533113, _n_(533112, "np", lambda: np), "radians"), _c_(533116, _n_(533114, "float", lambda: float), _n_(533115, "phi", lambda: phi)))
_l_(533118)

#Calculate x,y,z coordinates
X = _c_(533122, _a_(533120, _n_(533119, "np", lambda: np), "sin"), _n_(533121, "theta", lambda: theta)) * _c_(533126, _a_(533124, _n_(533123, "np", lambda: np), "cos"), _n_(533125, "phi", lambda: phi))
_l_(533127)
Y = _c_(533131, _a_(533129, _n_(533128, "np", lambda: np), "sin"), _n_(533130, "theta", lambda: theta)) * _c_(533135, _a_(533133, _n_(533132, "np", lambda: np), "sin"), _n_(533134, "phi", lambda: phi))
_l_(533136)
Z = _c_(533140, _a_(533138, _n_(533137, "np", lambda: np), "cos"), _n_(533139, "theta", lambda: theta))
_l_(533141)

#Adjusting the length of an arrow
length = _c_(533147, _a_(533143, _n_(533142, "np", lambda: np), "sqrt"), _n_(533144, "X", lambda: X)**2 + _n_(533145, "Y", lambda: Y)**2 + _n_(533146, "Z", lambda: Z)**2)
_l_(533148)
if _n_(533149, "length", lambda: length) > 1:
    _l_(533159)

    X = _n_(533150, "X", lambda: X)/_n_(533151, "length", lambda: length)
    _l_(533152)
    Y = _n_(533153, "Y", lambda: Y)/_n_(533154, "length", lambda: length)
    _l_(533155)
    Z = _n_(533156, "Z", lambda: Z)/_n_(533157, "length", lambda: length)
    _l_(533158)

# Figure of the animation
fig = _c_(533162, _a_(533161, _n_(533160, "plt", lambda: plt), "figure"))
_l_(533163)
ax = _c_(533166, _a_(533165, _n_(533164, "fig", lambda: fig), "gca"), projection='3d')
_l_(533167)
_c_(533170, _a_(533169, _n_(533168, "ax", lambda: ax), "set_aspect"), "equal")
_l_(533171)
u, v = _a_(533173, _n_(533172, "np", lambda: np), "mgrid")[0:2*_a_(533175, _n_(533174, "np", lambda: np), "pi"):20j, 0:_a_(533177, _n_(533176, "np", lambda: np), "pi"):10j]
_l_(533178)
x = _c_(533182, _a_(533180, _n_(533179, "np", lambda: np), "cos"), _n_(533181, "u", lambda: u))*_c_(533186, _a_(533184, _n_(533183, "np", lambda: np), "sin"), _n_(533185, "v", lambda: v))
_l_(533187)
y = _c_(533191, _a_(533189, _n_(533188, "np", lambda: np), "sin"), _n_(533190, "u", lambda: u))*_c_(533195, _a_(533193, _n_(533192, "np", lambda: np), "sin"), _n_(533194, "v", lambda: v))
_l_(533196)
z = _c_(533200, _a_(533198, _n_(533197, "np", lambda: np), "cos"), _n_(533199, "v", lambda: v))
_l_(533201)
_c_(533204, _a_(533203, _n_(533202, "ax", lambda: ax), "set_xlabel"), 'x')
_l_(533205)
_c_(533208, _a_(533207, _n_(533206, "ax", lambda: ax), "set_ylabel"), 'y')
_l_(533209)
_c_(533212, _a_(533211, _n_(533210, "ax", lambda: ax), "set_zlabel"), 'z')
_l_(533213)
_c_(533219, _a_(533215, _n_(533214, "ax", lambda: ax), "plot_wireframe"), _n_(533216, "x", lambda: x),_n_(533217, "y", lambda: y),_n_(533218, "z", lambda: z), color="black")
_l_(533220)

# Calculate x,y,z coordinates in the process of the change
length = 9
_l_(533221)
xgate_theta = _c_(533229, _a_(533223, _n_(533222, "np", lambda: np), "linspace"), _n_(533224, "theta", lambda: theta),_n_(533225, "theta", lambda: theta)+_a_(533227, _n_(533226, "np", lambda: np), "pi"),_n_(533228, "length", lambda: length))
_l_(533230)
xgate_phi = _c_(533236, _a_(533232, _n_(533231, "np", lambda: np), "linspace"), _n_(533233, "phi", lambda: phi),_n_(533234, "phi", lambda: phi),_n_(533235, "length", lambda: length))
_l_(533237)

#Array of x,y,z coordinates
xgate= []
_l_(533238)

# Only x coordinates
xgate_x = []
_l_(533239)

# Only y coordinates
xgate_y = []
_l_(533240)

# Only z coordinates
xgate_z = []
_l_(533241)

for i in _c_(533244, _n_(533242, "range", lambda: range), _n_(533243, "length", lambda: length)):
    _l_(533273)

    _c_(533248, _a_(533246, _n_(533245, "xgate_x", lambda: xgate_x), "append"), _n_(533247, "X", lambda: X))
    _l_(533249)
    _c_(533257, _a_(533251, _n_(533250, "xgate_z", lambda: xgate_z), "append"), _c_(533256, _a_(533253, _n_(533252, "np", lambda: np), "cos"), _n_(533254, "xgate_theta", lambda: xgate_theta)[_n_(533255, "i", lambda: i)]))
    _l_(533258)
    _c_(533271, _a_(533260, _n_(533259, "xgate_y", lambda: xgate_y), "append"), _c_(533270, _a_(533262, _n_(533261, "np", lambda: np), "sqrt"), 1-_c_(533269, _a_(533264, _n_(533263, "np", lambda: np), "sqrt"), _n_(533265, "xgate_x", lambda: xgate_x)[_n_(533266, "i", lambda: i)]**2+_n_(533267, "xgate_z", lambda: xgate_z)[_n_(533268, "i", lambda: i)]**2))*(-1))
    _l_(533272)
for j in _c_(533276, _n_(533274, "range", lambda: range), _n_(533275, "length", lambda: length)):
    _l_(533290)

    _c_(533288, _a_(533278, _n_(533277, "xgate", lambda: xgate), "append"), _c_(533287, _a_(533280, _n_(533279, "plt", lambda: plt), "quiver"), 0,0,0,_n_(533281, "xgate_x", lambda: xgate_x)[_n_(533282, "j", lambda: j)],_n_(533283, "xgate_y", lambda: xgate_y)[_n_(533284, "j", lambda: j)],_n_(533285, "xgate_z", lambda: xgate_z)[_n_(533286, "j", lambda: j)],color="red"))
    _l_(533289)


ani = _c_(533295, _a_(533292, _n_(533291, "animation", lambda: animation), "ArtistAnimation"), _n_(533293, "fig", lambda: fig),_n_(533294, "xgate", lambda: xgate),interval=1000)
_l_(533296)
_c_(533299, _a_(533298, _n_(533297, "plt", lambda: plt), "show"))
_l_(533300)