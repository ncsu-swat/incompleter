# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75581482/how-to-resolve-batchlabel-name-torch-tensorbatchlabel-name-dtype-torch-i
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
train_data2=_c_(593181, _n_(593179, "MyDataset", lambda: MyDataset), _n_(593180, "train_data", lambda: train_data))
_l_(593182)
try:
    from transformers import DataCollatorForTokenClassification
    _l_(593184)

except ImportError:
    pass
data_collator = _c_(593187, _n_(593185, "DataCollatorForTokenClassification", lambda: DataCollatorForTokenClassification), tokenizer=_n_(593186, "tokenizer", lambda: tokenizer),return_tensors="pt")
_l_(593188)