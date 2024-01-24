# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63680459/typeerror-only-integers-slices-ellipsis-tf-newaxis-none-and
#load data from disk
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
X_patches=_c_(411067, _a_(411064, _c_(411063, _a_(411062, _n_(411061, "np", lambda: np), "load"), "./x_training.npy"), "astype"), _a_(411066, _n_(411065, "np", lambda: np), "float32"))
_l_(411068)
Y_labels_valid=_c_(411075, _a_(411072, _c_(411071, _a_(411070, _n_(411069, "np", lambda: np), "load"), "./y_training.npy"), "astype"), _a_(411074, _n_(411073, "np", lambda: np), "float32"))
_l_(411076)
X33_train=_n_(411077, "X_patches", lambda: X_patches)
_l_(411078)
Y_train=_n_(411079, "Y_labels", lambda: Y_labels)
_l_(411080)
train_generator=_c_(411084, _n_(411081, "img_msk_gen", lambda: img_msk_gen), X33_train=_n_(411082, "X_patches", lambda: X_patches),Y_train=_n_(411083, "Y_labels", lambda: Y_labels),seed= 9999)
_l_(411085)
_c_(411093, _a_(411087, _n_(411086, "model", lambda: model), "fit_generator"), _n_(411088, "train_generator", lambda: train_generator),steps_per_epoch=_c_(411091, _n_(411089, "len", lambda: len), _n_(411090, "X33_train", lambda: X33_train))//_n_(411092, "batch_size", lambda: batch_size),
                    verbose=1)
_l_(411094)