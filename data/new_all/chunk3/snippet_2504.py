# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/74469400/typeerror-init-got-multiple-values-for-argument-dim
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from torch.utils.data import Dataset, DataLoader
    _l_(555406)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(555408)

except ImportError:
    pass
try:
    from torchvision import transforms
    _l_(555410)

except ImportError:
    pass
try:
    from PIL import Image
    _l_(555412)

except ImportError:
    pass
try:
    import torch
    _l_(555414)

except ImportError:
    pass
try:
    import torch.nn as nn
    _l_(555416)

except ImportError:
    pass
try:
    from glob import glob
    _l_(555418)

except ImportError:
    pass
try:
    from pathlib import PurePath
    _l_(555420)

except ImportError:
    pass
try:
    import numpy as np
    _l_(555422)

except ImportError:
    pass
try:
    import timm
    _l_(555424)

except ImportError:
    pass
try:
    import torchvision
    _l_(555426)

except ImportError:
    pass
try:
    import time
    _l_(555428)

except ImportError:
    pass

img_list = _c_(555430, _n_(555429, "glob", lambda: glob), '/media/cvpr/CM_22/OOD-CV-phase2/phase2-cls/images/*.jpg')
_l_(555431)

name_list = [
    'aeroplane',
    'bicycle',
    'boat',
    'bus',
    'car',
    'chair',
    'diningtable',
    'motorbike',
    'sofa',
    'train'
]
_l_(555432)

# conda install pytorch==1.9.0 torchvision==0.10.0 torchaudio==0.9.0 cudatoolkit=10.2 -c pytorch

class PoseData(_n_(555433, "Dataset", lambda: Dataset)):
    _l_(555487)

    def __init__(self, transforms) -> None:
        _l_(555457)

        """
        the data folder should look like
        - datafolder
            - Images
            - labels.csv        
        """
        _c_(555436, _a_(555435, _n_(555434, "super", lambda: super)(), "__init__"))
        _l_(555437)
        _n_(555438, "self", lambda: self).img_list = _c_(555440, _n_(555439, "glob", lambda: glob), '/media/cvpr/CM_22/OOD-CV-phase2/phase2-cls/images/*.jpg')
        _l_(555441)
        _n_(555442, "self", lambda: self).img_list = _c_(555452, _n_(555443, "sorted", lambda: sorted), _a_(555445, _n_(555444, "self", lambda: self), "img_list"), key=lambda x: _c_(555451, _n_(555446, "eval", lambda: eval), _a_(555450, _c_(555449, _n_(555447, "PurePath", lambda: PurePath), _n_(555448, "x", lambda: x)), "parts")[-1][:-4]))
        _l_(555453)
        _n_(555454, "self", lambda: self).trs = _n_(555455, "transforms", lambda: transforms)
        _l_(555456)

    def __len__(self):
        _l_(555463)

        aux = _c_(555461, _n_(555458, "len", lambda: len), _a_(555460, _n_(555459, "self", lambda: self), "img_list"))
        _l_(555462)
        return aux

    def __getitem__(self, index):
        _l_(555486)

        image_dir = _a_(555465, _n_(555464, "self", lambda: self), "img_list")[_n_(555466, "index", lambda: index)]
        _l_(555467)
        image_name = _a_(555471, _c_(555470, _n_(555468, "PurePath", lambda: PurePath), _n_(555469, "image_dir", lambda: image_dir)), "parts")[-1]
        _l_(555472)
        image = _c_(555476, _a_(555474, _n_(555473, "Image", lambda: Image), "open"), _n_(555475, "image_dir", lambda: image_dir))
        _l_(555477)
        image = _c_(555481, _a_(555479, _n_(555478, "self", lambda: self), "trs"), _n_(555480, "image", lambda: image))
        _l_(555482)
        aux = _n_(555483, "image", lambda: image), _n_(555484, "image_name", lambda: image_name)
        _l_(555485)

        return aux


if _n_(555488, "__name__", lambda: __name__) == "__main__":
    _l_(555715)

    normalize = _c_(555491, _a_(555490, _n_(555489, "transforms", lambda: transforms), "Normalize"), mean=[0.485, 0.456, 0.406],
                                     std=[0.229, 0.224, 0.225])
    _l_(555492)
    tfs = _c_(555502, _a_(555494, _n_(555493, "transforms", lambda: transforms), "Compose"), [
        _c_(555497, _a_(555496, _n_(555495, "transforms", lambda: transforms), "Resize"), (224, 224)),
        _c_(555500, _a_(555499, _n_(555498, "transforms", lambda: transforms), "ToTensor")),
        _n_(555501, "normalize", lambda: normalize),
    ])
    _l_(555503)

    model1 = _c_(555507, _a_(555506, _a_(555505, _n_(555504, "timm", lambda: timm), "models"), "swin_base_patch4_window7_224"), pretrained=False, num_classes=15)
    _l_(555508)
    model1 = _c_(555513, _a_(555511, _a_(555510, _n_(555509, "torch", lambda: torch), "nn"), "DataParallel"), _n_(555512, "model1", lambda: model1))
    _l_(555514)
    _c_(555520, _a_(555516, _n_(555515, "model1", lambda: model1), "load_state_dict"), _c_(555519, _a_(555518, _n_(555517, "torch", lambda: torch), "load"), '/media/cvpr/CM_22/OOD_CV/swin15_best.pth.tar')['state_dict'],strict=False)
    _l_(555521)
    model1 = _c_(555524, _a_(555523, _n_(555522, "model1", lambda: model1), "cuda"))
    _l_(555525)
    _c_(555528, _a_(555527, _n_(555526, "model1", lambda: model1), "eval"))
    _l_(555529)

    model2 = _c_(555533, _a_(555532, _a_(555531, _n_(555530, "timm", lambda: timm), "models"), "convnext_base"), pretrained=False, num_classes=15)
    _l_(555534)
    model2 = _c_(555539, _a_(555537, _a_(555536, _n_(555535, "torch", lambda: torch), "nn"), "DataParallel"), _n_(555538, "model2", lambda: model2))
    _l_(555540)
    _c_(555546, _a_(555542, _n_(555541, "model2", lambda: model2), "load_state_dict"), _c_(555545, _a_(555544, _n_(555543, "torch", lambda: torch), "load"), 'convnext15_best.pth.tar')['state_dict'],strict=False)
    _l_(555547)
    model2 = _c_(555550, _a_(555549, _n_(555548, "model2", lambda: model2), "cuda"))
    _l_(555551)
    _c_(555554, _a_(555553, _n_(555552, "model2", lambda: model2), "eval"))
    _l_(555555)

    dataset = _c_(555558, _n_(555556, "PoseData", lambda: PoseData), _n_(555557, "tfs", lambda: tfs))
    _l_(555559)
    loader = _c_(555562, _n_(555560, "DataLoader", lambda: DataLoader), _n_(555561, "dataset", lambda: dataset), batch_size=128, shuffle=False, drop_last=False, num_workers=4)
    _l_(555563)

    image_dir = []
    _l_(555564)
    preds = []
    _l_(555565)
    for image, pth in _n_(555566, "loader", lambda: loader):
        _l_(555680)

        _c_(555572, _a_(555568, _n_(555567, "image_dir", lambda: image_dir), "append"), _c_(555571, _n_(555569, "list", lambda: list), _n_(555570, "pth", lambda: pth)))
        _l_(555573)
        image = _c_(555576, _a_(555575, _n_(555574, "image", lambda: image), "cuda"))
        _l_(555577)

        with _c_(555580, _a_(555579, _n_(555578, "torch", lambda: torch), "no_grad")):
            _l_(555660)


            _c_(555583, _a_(555582, _n_(555581, "model1", lambda: model1), "eval"))
            _l_(555584)
            pred1 = _c_(555587, _n_(555585, "model1", lambda: model1), _n_(555586, "image", lambda: image))
            _l_(555588)
            _c_(555591, _a_(555590, _n_(555589, "model2", lambda: model2), "eval"))
            _l_(555592)
            pred2 = _c_(555595, _n_(555593, "model2", lambda: model2), _n_(555594, "image", lambda: image))
            _l_(555596)

            entropy1 = -_c_(555607, _a_(555598, _n_(555597, "torch", lambda: torch), "sum"), _c_(555602, _a_(555600, _n_(555599, "torch", lambda: torch), "softmax"), _n_(555601, "pred1", lambda: pred1)[:, :10], dim=1) * _c_(555606, _a_(555604, _n_(555603, "nn", lambda: nn), "LogSoftmax"), _n_(555605, "pred1", lambda: pred1)[:, :10], dim=1), dim=-1,
                                  keep_dim=True)
            _l_(555608)
            entropy2 = -_c_(555619, _a_(555610, _n_(555609, "torch", lambda: torch), "sum"), _c_(555614, _a_(555612, _n_(555611, "torch", lambda: torch), "softmax"), _n_(555613, "pred2", lambda: pred2)[:, :10], dim=1) * _c_(555618, _a_(555616, _n_(555615, "nn", lambda: nn), "LogSoftmax"), _n_(555617, "pred2", lambda: pred2)[:, :10], dim=1), dim=-1,
                                  keep_dim=True)
            _l_(555620)
            entropy = _n_(555621, "entropy1", lambda: entropy1) + _n_(555622, "entropy2", lambda: entropy2)
            _l_(555623)

            pred = _c_(555627, _a_(555625, _n_(555624, "torch", lambda: torch), "softmax"), _n_(555626, "pred1", lambda: pred1)[:, :10], dim=1) * (_n_(555628, "entropy", lambda: entropy) - _n_(555629, "entropy1", lambda: entropy1)) / _n_(555630, "entropy", lambda: entropy) + _c_(555634, _a_(555632, _n_(555631, "torch", lambda: torch), "softmax"), _n_(555633, "pred2", lambda: pred2)[:, :10],
                                                                                                        dim=1) * (
                               _n_(555635, "entropy", lambda: entropy) - _n_(555636, "entropy2", lambda: entropy2)) / _n_(555637, "entropy", lambda: entropy)
            _l_(555638)
            pred = _c_(555642, _a_(555640, _n_(555639, "torch", lambda: torch), "argmax"), _n_(555641, "pred", lambda: pred)[:, :10], dim=1)
            _l_(555643)
            p = []
            _l_(555644)
            for i in _c_(555649, _n_(555645, "range", lambda: range), _c_(555648, _a_(555647, _n_(555646, "pred", lambda: pred), "size"), 0)):
                _l_(555659)

                _c_(555657, _a_(555651, _n_(555650, "p", lambda: p), "append"), _n_(555652, "name_list", lambda: name_list)[_c_(555656, _a_(555655, _n_(555653, "pred", lambda: pred)[_n_(555654, "i", lambda: i)], "item"))])
                _l_(555658)
        p = _c_(555664, _a_(555662, _n_(555661, "np", lambda: np), "array"), _n_(555663, "p", lambda: p))
        _l_(555665)
        _c_(555669, _a_(555667, _n_(555666, "preds", lambda: preds), "append"), _n_(555668, "p", lambda: p))
        _l_(555670)
        _c_(555678, _n_(555671, "print", lambda: print), _c_(555677, _n_(555672, "len", lambda: len), _c_(555676, _a_(555674, _n_(555673, "np", lambda: np), "concatenate"), _n_(555675, "preds", lambda: preds))))
        _l_(555679)

    image_dir = _c_(555686, _a_(555682, _n_(555681, "np", lambda: np), "array"), _c_(555685, _n_(555683, "sum", lambda: sum), _n_(555684, "image_dir", lambda: image_dir), []))
    _l_(555687)
    preds = _c_(555691, _a_(555689, _n_(555688, "np", lambda: np), "concatenate"), _n_(555690, "preds", lambda: preds))
    _l_(555692)

    csv = {'imgs': _c_(555696, _a_(555694, _n_(555693, "np", lambda: np), "array"), _n_(555695, "image_dir", lambda: image_dir)), 'pred': _c_(555700, _a_(555698, _n_(555697, "np", lambda: np), "array"), _n_(555699, "preds", lambda: preds)),
           }
    _l_(555701)
    csv = _c_(555705, _a_(555703, _n_(555702, "pd", lambda: pd), "DataFrame"), _n_(555704, "csv", lambda: csv))
    _l_(555706)
    _c_(555709, _n_(555707, "print", lambda: print), _n_(555708, "csv", lambda: csv))
    _l_(555710)

    _c_(555713, _a_(555712, _n_(555711, "csv", lambda: csv), "to_csv"), 'results.csv', index=False)
    _l_(555714)