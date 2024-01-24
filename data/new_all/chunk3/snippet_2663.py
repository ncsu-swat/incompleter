# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67504836/pythonpytorch-typeerror-string-indices-must-be-integers
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
TRANSFORMERS = {
    "bert-multi-cased": (_n_(565867, "BertModel", lambda: BertModel), _n_(565868, "BertTokenizer", lambda: BertTokenizer), "bert-base-uncased"),
}
_l_(565869)

class Transformer(_a_(565871, _n_(565870, "nn", lambda: nn), "Module")):
    _l_(565904)

    def __init__(self, model, num_classes=1):
        _l_(565872)

        """
        Constructor
    
    Arguments:
        model {string} -- Transformer to build the model on. Expects "camembert-base".
        num_classes {int} -- Number of classes (default: {1})
    """
    _c_(565875, _a_(565874, _n_(565873, "super", lambda: super)(), "__init__"))
    _l_(565876)
    self.name = model
    _l_(565877)

    model_class, tokenizer_class, pretrained_weights = _n_(565878, "TRANSFORMERS", lambda: TRANSFORMERS)[model]
    _l_(565879)

    bert_config = _c_(565881, _a_(565880, BertConfig, "from_json_file"), MODEL_PATHS[model] + 'bert_config.json')
    _l_(565882)
    bert_config.output_hidden_states = True
    _l_(565883)
    
    self.transformer = _c_(565884, BertModel, bert_config)
    _l_(565885)

    self.nb_features = _a_(565889, _a_(565888, _a_(565887, _a_(565886, self, "transformer"), "pooler"), "dense"), "out_features")
    _l_(565890)

    self.pooler = _c_(565898, _a_(565891, nn, "Sequential"), _c_(565895, _a_(565892, nn, "Linear"), _a_(565893, self, "nb_features"), _a_(565894, self, "nb_features")), 
        _c_(565897, _a_(565896, nn, "Tanh")),
    )
    _l_(565899)

    self.logit = _c_(565902, _a_(565900, nn, "Linear"), _a_(565901, self, "nb_features"), num_classes)
    _l_(565903)

def forward(self, tokens):
    _l_(565925)

    """
    Usual torch forward function
    
    Arguments:
        tokens {torch tensor} -- Sentence tokens
    
    Returns:
        torch tensor -- Class logits
    """
    _, _, hidden_states = _c_(565911, _a_(565906, _n_(565905, "self", lambda: self), "transformer"), _n_(565907, "tokens", lambda: tokens), attention_mask=_c_(565910, _a_(565909, (_n_(565908, "tokens", lambda: tokens) > 0), "long"))
    )
    _l_(565912)

    hidden_states = _n_(565913, "hidden_states", lambda: hidden_states)[-1][:, 0] # Use the representation of the first token of the last layer
    _l_(565914) # Use the representation of the first token of the last layer

    ft = _c_(565918, _a_(565916, _n_(565915, "self", lambda: self), "pooler"), _n_(565917, "hidden_states", lambda: hidden_states))
    _l_(565919)
    aux = _c_(565923, _a_(565921, _n_(565920, "self", lambda: self), "logit"), _n_(565922, "ft", lambda: ft))
    _l_(565924)

    return aux