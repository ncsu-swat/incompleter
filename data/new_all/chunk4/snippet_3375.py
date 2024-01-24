# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75038713/how-to-solve-yellowbricktypeerror-the-supplied-model-is-not-a-clustering-estima
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import matplotlib.pyplot as plt
    _l_(614755)

except ImportError:
    pass
try:
    from fcmeans import FCM
    _l_(614757)

except ImportError:
    pass
try:
    from yellowbrick.cluster import SilhouetteVisualizer
    _l_(614759)

except ImportError:
    pass

model = _c_(614761, _n_(614760, "FCM", lambda: FCM), n_clusters=5, random_state=0)
_l_(614762)
visualizer = _c_(614765, _n_(614763, "SilhouetteVisualizer", lambda: SilhouetteVisualizer), _n_(614764, "model", lambda: model), colors='yellowbrick')
_l_(614766)

_c_(614770, _a_(614768, _n_(614767, "visualizer", lambda: visualizer), "fit"), _n_(614769, "X", lambda: X))        
_l_(614771)        
_c_(614774, _a_(614773, _n_(614772, "visualizer", lambda: visualizer), "show"))
_l_(614775)