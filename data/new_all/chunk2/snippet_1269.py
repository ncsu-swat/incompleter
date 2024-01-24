# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58963669/vapory-error-filenotfounderror-winerror-2-the-system-cannot-find-the-file-sp
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from vapory import *
    _l_(428211)

except ImportError:
    pass

camera = _c_(428213, _n_(428212, "Camera", lambda: Camera), 'location', [0,2,-3], 'look_at', [0,1,2] )
_l_(428214)
light = _c_(428216, _n_(428215, "LightSource", lambda: LightSource), [2,4,-3], 'color', [1,1,1] )
_l_(428217)
sphere = _c_(428223, _n_(428218, "Sphere", lambda: Sphere), [0,1,2], 2, _c_(428222, _n_(428219, "Texture", lambda: Texture), _c_(428221, _n_(428220, "Pigment", lambda: Pigment), 'color', [1,0,1] )))
_l_(428224)

scene = _c_(428229, _n_(428225, "Scene", lambda: Scene), _n_(428226, "camera", lambda: camera), objects= [_n_(428227, "light", lambda: light), _n_(428228, "sphere", lambda: sphere)])
_l_(428230)
_c_(428233, _a_(428232, _n_(428231, "scene", lambda: scene), "render"), "purple_sphere.png", width=400, height=300)
_l_(428234)