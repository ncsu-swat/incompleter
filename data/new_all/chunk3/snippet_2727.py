# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65366376/pytorch-typeerror-caught-typeerror-in-dataloader-worker-process-0
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
BATCH_SIZE = 16
_l_(558672)
train_data_loader = _c_(558678, _n_(558673, "create_data_loader", lambda: create_data_loader), _n_(558674, "df_train", lambda: df_train), _n_(558675, "tokenizer", lambda: tokenizer), _n_(558676, "MAX_LEN", lambda: MAX_LEN), _n_(558677, "BATCH_SIZE", lambda: BATCH_SIZE))
_l_(558679)
val_data_loader = _c_(558685, _n_(558680, "create_data_loader", lambda: create_data_loader), _n_(558681, "df_val", lambda: df_val), _n_(558682, "tokenizer", lambda: tokenizer), _n_(558683, "MAX_LEN", lambda: MAX_LEN), _n_(558684, "BATCH_SIZE", lambda: BATCH_SIZE))
_l_(558686)
test_data_loader = _c_(558692, _n_(558687, "create_data_loader", lambda: create_data_loader), _n_(558688, "df_test", lambda: df_test), _n_(558689, "tokenizer", lambda: tokenizer), _n_(558690, "MAX_LEN", lambda: MAX_LEN), _n_(558691, "BATCH_SIZE", lambda: BATCH_SIZE))
_l_(558693)