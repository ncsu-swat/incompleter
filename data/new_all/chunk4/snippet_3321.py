# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75704300/attributeerror-stablediffusionkdiffusionpipeline-object-has-no-attribute-sam
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
if not _c_(621839, _a_(621837, _a_(621836, _n_(621835, "os", lambda: os), "path"), "exists"), _n_(621838, "IMAGE_SAVE_PATH", lambda: IMAGE_SAVE_PATH)):
    _l_(621845)

    _c_(621843, _a_(621841, _n_(621840, "os", lambda: os), "mkdir"), _n_(621842, "IMAGE_SAVE_PATH", lambda: IMAGE_SAVE_PATH))
    _l_(621844)

def generate_image_name(prompt, ext='.png'):
    _l_(621858)

    try:
        from uuid import uuid4
        _l_(621847)

    except ImportError:
        pass
    aux = f"{_n_(621848, 'IMAGE_SAVE_PATH', lambda: IMAGE_SAVE_PATH)}/{_c_(621852, _n_(621849, 'str', lambda: str), _c_(621851, _n_(621850, 'uuid4', lambda: uuid4)))}{_c_(621855, _a_(621854, _n_(621853, 'prompt', lambda: prompt)[:25], 'replace'), ' ', '-')}.{_n_(621856, 'ext', lambda: ext)}"
    _l_(621857)
    return aux

pipe = _c_(621864, _a_(621860, _n_(621859, "StableDiffusionKDiffusionPipeline", lambda: StableDiffusionKDiffusionPipeline), "from_pretrained"), _n_(621861, "V5_MODEL_PATH", lambda: V5_MODEL_PATH), torch_dtype=_a_(621863, _n_(621862, "torch", lambda: torch), "float16"), revision='fp16')
_l_(621865)
_c_(621868, _a_(621867, _n_(621866, "pipe", lambda: pipe), "to"), "cuda")
_l_(621869)
with _c_(621871, _n_(621870, "autocast", lambda: autocast), 'cuda'):
    _l_(621877)

    image = _a_(621875, _c_(621874, _n_(621872, "pipe", lambda: pipe), _n_(621873, "prompt", lambda: prompt)), "images")[0]
    _l_(621876)
_c_(621883, _a_(621879, _n_(621878, "image", lambda: image), "save"), _c_(621882, _n_(621880, "generate_image_name", lambda: generate_image_name), _n_(621881, "prompt", lambda: prompt)))
_l_(621884)