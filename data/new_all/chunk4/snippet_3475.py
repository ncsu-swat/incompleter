# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/73760419/typeerror-init-got-an-unexpected-keyword-argument-has-model-config-whil
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
args = _c_(639359, _n_(639358, "TrainingArguments", lambda: TrainingArguments), "xlmroberta-finetuned-ner",
#     evaluation_strategy="epoch",
    save_strategy="epoch",
    learning_rate=2e-5,
    num_train_epochs=2,
    weight_decay=0.01,
    per_device_train_batch_size=4,
    # per_device_eval_batch_size=32
    fp16=True
    # bf16=True #Ampere GPU
)
_l_(639360)