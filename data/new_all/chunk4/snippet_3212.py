# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/77344941/typeerror-expected-str-bytes-or-os-pathlike-object-not-nonetype-yolo
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from ultralytics import YOLO
    _l_(606001)

except ImportError:
    pass

model = _c_(606003, _n_(606002, "YOLO", lambda: YOLO), 'yolov8n-cls.pt')
_l_(606004)

_c_(606007, _a_(606006, _n_(606005, "model", lambda: model), "train"), data='./training_dataset', epochs=1, imgsz=64)
_l_(606008)