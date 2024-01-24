# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/76268924/timm-attributeerror-dataparallel-object-has-no-attribute-items
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
ptcfg = _c_(606597, _a_(606596, _a_(606595, _a_(606594, _n_(606593, "timm", lambda: timm), "models"), "registry"), "get_pretrained_cfg"), 'swin_base_patch4_window7_224')
_l_(606598)
_n_(606599, "ptcfg", lambda: ptcfg)['file'] = 'model_swin.pth'
_l_(606600)
model = _c_(606609, _a_(606603, _a_(606602, _n_(606601, "torch", lambda: torch), "nn"), "DataParallel"), _c_(606608, _a_(606606, _a_(606605, _n_(606604, "timm", lambda: timm), "models"), "swin_base_patch4_window7_224"), pretrained=True, pretrained_cfg=_n_(606607, "ptcfg", lambda: ptcfg), drop_path_rate=0.2), device_ids=[0,1])
_l_(606610)
_c_(606613, _a_(606612, _n_(606611, "model", lambda: model), "eval"))
_l_(606614)