# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67647299/attributeerror-module-torch-has-no-attribute-rfft-with-pytorch
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from skimage import io
    _l_(413485)

except ImportError:
    pass
try:
    import torch
    _l_(413487)

except ImportError:
    pass
try:
    import piq
    _l_(413489)

except ImportError:
    pass

@_c_(413492, _a_(413491, _n_(413490, "torch", lambda: torch), "no_grad"))
def main():
    _l_(413523)

    x = _c_(413500, _a_(413499, _c_(413498, _a_(413494, _n_(413493, "torch", lambda: torch), "tensor"), _c_(413497, _a_(413496, _n_(413495, "io", lambda: io), "imread"), 'scikit_image\cover\cover_1.tiff')), "permute"), 2, 0, 1)[None, ...] / 255.
    _l_(413501)
    y = _c_(413509, _a_(413508, _c_(413507, _a_(413503, _n_(413502, "torch", lambda: torch), "tensor"), _c_(413506, _a_(413505, _n_(413504, "io", lambda: io), "imread"), 'scikit_image\stego\stego_1.tiff')), "permute"), 2, 0, 1)[None, ...] / 255.
    _l_(413510)

    fsim_index: _a_(413512, _n_(413511, "torch", lambda: torch), "Tensor") = _c_(413517, _a_(413514, _n_(413513, "piq", lambda: piq), "fsim"), _n_(413515, "x", lambda: x), _n_(413516, "y", lambda: y), data_range=1., reduction='none')
    _l_(413518)

    _c_(413521, _n_(413519, "print", lambda: print), _n_(413520, "fsim_index", lambda: fsim_index))
    _l_(413522)

if _n_(413524, "__name__", lambda: __name__) == "__main__":
    _l_(413528)

    _c_(413526, _n_(413525, "main", lambda: main))
    _l_(413527)