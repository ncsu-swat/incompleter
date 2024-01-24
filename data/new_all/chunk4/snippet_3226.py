# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/77108546/typeerror-berttokenizer-object-is-not-callable-bert-base-multilingual-cased
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from transformers import AutoTokenizer, AutoModel
    _l_(606775)

except ImportError:
    pass
try:
    import torch
    _l_(606777)

except ImportError:
    pass

tokenizer = _c_(606780, _a_(606779, _n_(606778, "AutoTokenizer", lambda: AutoTokenizer), "from_pretrained"), "bert-base-multilingual-cased")
_l_(606781)
model = _c_(606784, _a_(606783, _n_(606782, "AutoModel", lambda: AutoModel), "from_pretrained"), "bert-base-multilingual-cased")
_l_(606785)

text = 'welcome to Miami'
_l_(606786)
inputs = _c_(606789, _n_(606787, "tokenizer", lambda: tokenizer), _n_(606788, "text", lambda: text), return_tensors='pt', padding=True)
_l_(606790)
with _c_(606793, _a_(606792, _n_(606791, "torch", lambda: torch), "no_grad")):
    _l_(606801)

    outputs = _c_(606796, _n_(606794, "model", lambda: model), **_n_(606795, "inputs", lambda: inputs))
    _l_(606797)
    embeddings = _a_(606799, _n_(606798, "outputs", lambda: outputs), "last_hidden_state")[:, 0, :]
    _l_(606800)
_c_(606808, _a_(606807, _c_(606806, _a_(606805, _c_(606804, _a_(606803, _n_(606802, "embeddings", lambda: embeddings), "detach")), "cpu")), "numpy"))
_l_(606809)