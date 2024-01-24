# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75581482/how-to-resolve-batchlabel-name-torch-tensorbatchlabel-name-dtype-torch-i
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
args = _c_(604178, _n_(604177, "TrainingArguments", lambda: TrainingArguments), "spanbert_",
    save_strategy="epoch",
    learning_rate=2e-5,
    num_train_epochs=2,
    weight_decay=0.01,
    per_device_train_batch_size=2,

)
_l_(604179)