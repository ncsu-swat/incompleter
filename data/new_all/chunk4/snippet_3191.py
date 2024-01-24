# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/77544820/attributeerror-tensorflow-python-util-pywrap-checkpoint-reader-c-object-has
# Directory where the checkpoints will be saved
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
checkpoint_dir = "./training_checkpoints"
_l_(624498)
# Name of the checkpoint files
checkpoint_prefix = _c_(624503, _a_(624501, _a_(624500, _n_(624499, "os", lambda: os), "path"), "join"), _n_(624502, "checkpoint_dir", lambda: checkpoint_dir), "ckpt_{epoch}")
_l_(624504)

checkpoint_callback=_c_(624510, _a_(624508, _a_(624507, _a_(624506, _n_(624505, "tf", lambda: tf), "keras"), "callbacks"), "ModelCheckpoint"), filepath=_n_(624509, "checkpoint_prefix", lambda: checkpoint_prefix),
    save_weights_only=True
)
_l_(624511)

checkpoint_num = 10
_l_(624512)
_c_(624522, _a_(624514, _n_(624513, "model", lambda: model), "load_weights"), _c_(624521, _a_(624517, _a_(624516, _n_(624515, "tf", lambda: tf), "train"), "load_checkpoint"), './training_checkpoints/ckpt_' + _c_(624520, _n_(624518, "str", lambda: str), _n_(624519, "checkpoint_num", lambda: checkpoint_num))))
_l_(624523)
_c_(624529, _a_(624525, _n_(624524, "model", lambda: model), "build"), _c_(624528, _a_(624527, _n_(624526, "tf", lambda: tf), "TensorShape"), [1, None]))
_l_(624530)