# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/73760419/typeerror-init-got-an-unexpected-keyword-argument-has-model-config-whil
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
trainer = _c_(581044, _n_(581039, "Trainer", lambda: Trainer), model=_n_(581040, "model", lambda: model),
    args=_n_(581041, "args", lambda: args),
    train_dataset=_n_(581042, "train_data", lambda: train_data),
    # eval_dataset=train_data,
    # data_collator=data_collator,
    # compute_metrics=compute_metrics,
    tokenizer=_n_(581043, "tokenizer", lambda: tokenizer))
_l_(581045)
_c_(581048, _a_(581047, _n_(581046, "trainer", lambda: trainer), "train"))
_l_(581049)