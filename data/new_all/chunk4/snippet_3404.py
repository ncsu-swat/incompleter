# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/74859282/got-typeerror-when-adding-return-indices-true-to-nn-maxpool2d-in-pytorch
# B = Batch size
# decoder (B, 8) => (B, 3, 224, 224)
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Decoder(_a_(645065, _n_(645064, "nn", lambda: nn), "Module")):
    _l_(645149)

    def __init__(self):
        _l_(645130)

        _c_(645068, _a_(645067, _n_(645066, "super", lambda: super)(), "__init__"))
        _l_(645069)
        _n_(645070, "self", lambda: self).decoder_fc = _c_(645085, _a_(645072, _n_(645071, "nn", lambda: nn), "Sequential"), _c_(645075, _a_(645074, _n_(645073, "nn", lambda: nn), "Linear"), 8, 1024),
            _c_(645078, _a_(645077, _n_(645076, "nn", lambda: nn), "ReLU"), True),
            _c_(645081, _a_(645080, _n_(645079, "nn", lambda: nn), "Linear"), 1024, 64*7*7),
            _c_(645084, _a_(645083, _n_(645082, "nn", lambda: nn), "ReLU"), True)
        )
        _l_(645086)
        _n_(645087, "self", lambda: self).unflat = _c_(645090, _a_(645089, _n_(645088, "nn", lambda: nn), "Unflatten"), dim=1, unflattened_size=(64, 7, 7))
        _l_(645091)
        _n_(645092, "self", lambda: self).decoder_cnn = _c_(645128, _a_(645094, _n_(645093, "nn", lambda: nn), "Sequential"), _c_(645097, _a_(645096, _n_(645095, "nn", lambda: nn), "MaxUnpool2d"), 2),
            _c_(645100, _a_(645099, _n_(645098, "nn", lambda: nn), "BatchNorm2d"), 64),
            _c_(645103, _a_(645102, _n_(645101, "nn", lambda: nn), "ConvTranspose2d"), 64, 32, kernel_size=3, stride=2, padding=1),
            _c_(645106, _a_(645105, _n_(645104, "nn", lambda: nn), "ReLU"), True),
            _c_(645109, _a_(645108, _n_(645107, "nn", lambda: nn), "ConvTranspose2d"), 32, 16, kernel_size=3, stride=2, padding=1),
            _c_(645112, _a_(645111, _n_(645110, "nn", lambda: nn), "MaxUnpool2d"), 2),
            _c_(645115, _a_(645114, _n_(645113, "nn", lambda: nn), "BatchNorm2d"), 16),
            _c_(645118, _a_(645117, _n_(645116, "nn", lambda: nn), "ReLU"), True),
            _c_(645121, _a_(645120, _n_(645119, "nn", lambda: nn), "ConvTranspose2d"), 16, 8, kernel_size=3, stride=2, padding=0),
            _c_(645124, _a_(645123, _n_(645122, "nn", lambda: nn), "ReLU"), True),
            _c_(645127, _a_(645126, _n_(645125, "nn", lambda: nn), "ConvTranspose2d"), 8, 3, kernel_size=3, stride=1, padding=0)
        )
        _l_(645129)
    def forward(self, x):
        _l_(645148)

        x = _c_(645134, _a_(645132, _n_(645131, "self", lambda: self), "decoder_fc"), _n_(645133, "x", lambda: x))
        _l_(645135)
        x = _c_(645139, _a_(645137, _n_(645136, "self", lambda: self), "unflat"), _n_(645138, "x", lambda: x))
        _l_(645140)
        x = _c_(645144, _a_(645142, _n_(645141, "self", lambda: self), "decoder_cnn"), _n_(645143, "x", lambda: x))
        _l_(645145)
        aux = _n_(645146, "x", lambda: x)
        _l_(645147)
        return aux