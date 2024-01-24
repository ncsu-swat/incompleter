# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/69620035/typeerror-dimension-value-must-be-integer-or-none-in-keras-vq-vae-example
# Create a mini sampler model.
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
inputs = _c_(539229, _a_(539226, _n_(539225, "layers", lambda: layers), "Input"), shape=_a_(539228, _n_(539227, "pixel_cnn", lambda: pixel_cnn), "input_shape")[1:])
_l_(539230)
x = _c_(539233, _n_(539231, "pixel_cnn", lambda: pixel_cnn), _n_(539232, "inputs", lambda: inputs), training=False)
_l_(539234)
dist = _c_(539239, _a_(539237, _a_(539236, _n_(539235, "tfp", lambda: tfp), "distributions"), "Categorical"), logits=_n_(539238, "x", lambda: x))
_l_(539240)
sampled = _c_(539243, _a_(539242, _n_(539241, "dist", lambda: dist), "sample"))
_l_(539244)
sampler = _c_(539249, _a_(539246, _n_(539245, "keras", lambda: keras), "Model"), _n_(539247, "inputs", lambda: inputs), _n_(539248, "sampled", lambda: sampled))
_l_(539250)

# Create an empty array of priors.
batch = 10
_l_(539251)
priors = _c_(539257, _a_(539253, _n_(539252, "np", lambda: np), "zeros"), shape=(_n_(539254, "batch", lambda: batch),) + _a_(539256, _n_(539255, "pixel_cnn", lambda: pixel_cnn), "input_shape")[1:])
_l_(539258)
batch, rows, cols = _a_(539260, _n_(539259, "priors", lambda: priors), "shape")
_l_(539261)

# Iterate over the priors because generation has to be done sequentially pixel by pixel.
for row in _c_(539264, _n_(539262, "range", lambda: range), _n_(539263, "rows", lambda: rows)):
    _l_(539281)

    for col in _c_(539267, _n_(539265, "range", lambda: range), _n_(539266, "cols", lambda: cols)):
        _l_(539280)

        # Feed the whole array and retrieving the pixel value probabilities for the next
        # pixel.
        probs = _c_(539271, _a_(539269, _n_(539268, "sampler", lambda: sampler), "predict"), _n_(539270, "priors", lambda: priors))
        _l_(539272)
        # Use the probabilities to pick pixel values and append the values to the priors.
        _n_(539273, "priors", lambda: priors)[:, _n_(539274, "row", lambda: row), _n_(539275, "col", lambda: col)] = _n_(539276, "probs", lambda: probs)[:, _n_(539277, "row", lambda: row), _n_(539278, "col", lambda: col)]
        _l_(539279)

_c_(539285, _n_(539282, "print", lambda: print), f"Prior shape: {_a_(539284, _n_(539283, 'priors', lambda: priors), 'shape')}")
_l_(539286)