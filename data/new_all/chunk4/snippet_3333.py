# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75581482/how-to-resolve-batchlabel-name-torch-tensorbatchlabel-name-dtype-torch-i
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(608885)

except ImportError:
    pass
try:
    import warnings
    _l_(608887)

except ImportError:
    pass
try:
    from collections import Counter
    _l_(608889)

except ImportError:
    pass
try:
    import tqdm
    _l_(608891)

except ImportError:
    pass
try:
    import random
    _l_(608893)

except ImportError:
    pass
_c_(608896, _a_(608895, _n_(608894, "warnings", lambda: warnings), "filterwarnings"), 'ignore')
_l_(608897)
_a_(608899, _n_(608898, "os", lambda: os), "environ")["WANDB_DISABLED"] = "true"
_l_(608900)
_a_(608902, _n_(608901, "os", lambda: os), "environ")["TOKENIZERS_PARALLELISM"]= "true"
_l_(608903)
try:
    from torchcrf import CRF
    _l_(608905)

except ImportError:
    pass
try:
    from transformers import BertTokenizerFast as BertTokenizer
    _l_(608907)

except ImportError:
    pass
try:
    from transformers import BertForTokenClassification
    _l_(608909)

except ImportError:
    pass
try:
    import torch.nn as nn
    _l_(608911)

except ImportError:
    pass
try:
    import torch.nn.functional as F
    _l_(608913)

except ImportError:
    pass
log_soft = _a_(608915, _n_(608914, "F", lambda: F), "log_softmax")
_l_(608916)
try:
    from transformers import (Trainer,TrainingArguments)
    _l_(608918)

except ImportError:
    pass
try:
    from torch.utils.data import TensorDataset
    _l_(608920)

except ImportError:
    pass
try:
    import torch
    _l_(608922)

except ImportError:
    pass
device = _c_(608929, _a_(608924, _n_(608923, "torch", lambda: torch), "device"), "cuda" if _c_(608928, _a_(608927, _a_(608926, _n_(608925, "torch", lambda: torch), "cuda"), "is_available")) else "cpu")
_l_(608930)
n_gpu = _c_(608934, _a_(608933, _a_(608932, _n_(608931, "torch", lambda: torch), "cuda"), "device_count"))
_l_(608935)
_c_(608939, _a_(608938, _a_(608937, _n_(608936, "torch", lambda: torch), "cuda"), "empty_cache"))
_l_(608940)