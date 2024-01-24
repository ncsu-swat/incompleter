# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/76052537/attributeerror-clipvisionmodelwithprojection-object-has-no-attribute-get-ima
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from pathlib import Path
    _l_(621893)

except ImportError:
    pass
try:
    from lambda_diffusers import StableDiffusionImageEmbedPipeline
    _l_(621895)

except ImportError:
    pass
try:
    from PIL import Image
    _l_(621897)

except ImportError:
    pass
try:
    import torch
    _l_(621899)

except ImportError:
    pass

#device = "cuda" if torch.cuda.is_available() else "cpu"
device = "cpu"
_l_(621900)
pipe = _c_(621903, _a_(621902, _n_(621901, "StableDiffusionImageEmbedPipeline", lambda: StableDiffusionImageEmbedPipeline), "from_pretrained"), "lambdalabs/sd-image-variations-diffusers")
_l_(621904)
pipe = _c_(621908, _a_(621906, _n_(621905, "pipe", lambda: pipe), "to"), _n_(621907, "device", lambda: device))
_l_(621909)

im = _c_(621912, _a_(621911, _n_(621910, "Image", lambda: Image), "open"), "/home/cvpr/Desktop/bird.jpg")
_l_(621913)
num_samples = 4
_l_(621914)
image = _c_(621918, _n_(621915, "pipe", lambda: pipe), _n_(621916, "num_samples", lambda: num_samples)*[_n_(621917, "im", lambda: im)], guidance_scale=3.0)
_l_(621919)
image = _n_(621920, "image", lambda: image)["sample"]
_l_(621921)

base_path = _c_(621923, _n_(621922, "Path", lambda: Path), "outputs/im2im")
_l_(621924)
_c_(621927, _a_(621926, _n_(621925, "base_path", lambda: base_path), "mkdir"), exist_ok=True, parents=True)
_l_(621928)
for idx, im in _c_(621931, _n_(621929, "enumerate", lambda: enumerate), _n_(621930, "image", lambda: image)):
    _l_(621938)

    _c_(621936, _a_(621933, _n_(621932, "im", lambda: im), "save"), _n_(621934, "base_path", lambda: base_path)/f"{_n_(621935, 'idx', lambda: idx):06}.jpg")
    _l_(621937)