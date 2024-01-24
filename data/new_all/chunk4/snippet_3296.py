# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/76001766/typeerror-cannot-convert-0-0-to-eagertensor-of-dtype-int64
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
EPOCHS = 500
_l_(624207)
VAL_SUBSPLITS = 1
_l_(624208)
#VALIDATION_STEPS = info.splits['test'].num_examples//BATCH_SIZE//VAL_SUBSPLITS
VALIDATION_STEPS = _n_(624209, "train_n_sample", lambda: train_n_sample)//_n_(624210, "BATCH_SIZE", lambda: BATCH_SIZE)//_n_(624211, "VAL_SUBSPLITS", lambda: VAL_SUBSPLITS)
_l_(624212)
VALIDATION_STEPS = 10
_l_(624213)
#VALIDATAION_SPILIT=tf.cast(VALIDATAION_SPILIT, tf.int64)
model_history = _c_(624222, _a_(624215, _n_(624214, "model", lambda: model), "fit"), x=_n_(624216, "train_imgarray", lambda: train_imgarray), y=_n_(624217, "trainmask_imgarray", lambda: trainmask_imgarray), batch_size=_n_(624218, "BATCH_SIZE", lambda: BATCH_SIZE), epochs=_n_(624219, "EPOCHS", lambda: EPOCHS),
                          steps_per_epoch=_n_(624220, "STEPS_PER_EPOCH", lambda: STEPS_PER_EPOCH),
                          validation_split=_n_(624221, "VALIDATAION_SPILIT", lambda: VALIDATAION_SPILIT))
_l_(624223)