# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75581482/how-to-resolve-batchlabel-name-torch-tensorbatchlabel-name-dtype-torch-i
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class BERT_CRF(_a_(615942, _n_(615941, "nn", lambda: nn), "Module")):
    _l_(616058)

    

    def __init__(self, bert_model, num_labels):
        _l_(615973)

       
        _c_(615947, _a_(615946, _n_(615943, "super", lambda: super)(_n_(615944, "BERT_CRF", lambda: BERT_CRF), _n_(615945, "self", lambda: self)), "__init__"))
        _l_(615948)
        _n_(615949, "self", lambda: self).bert = _n_(615950, "bert_model", lambda: bert_model)
        _l_(615951)
        _n_(615952, "self", lambda: self).config = _a_(615955, _a_(615954, _n_(615953, "self", lambda: self), "bert"), "config")
        _l_(615956)
        _n_(615957, "self", lambda: self).dropout = _c_(615960, _a_(615959, _n_(615958, "nn", lambda: nn), "Dropout"), 0.25)     
        _l_(615961)     
        _n_(615962, "self", lambda: self).classifier = _c_(615966, _a_(615964, _n_(615963, "nn", lambda: nn), "Linear"), 768, _n_(615965, "num_labels", lambda: num_labels))
        _l_(615967)
        _n_(615968, "self", lambda: self).crf = _c_(615971, _n_(615969, "CRF", lambda: CRF), _n_(615970, "num_labels", lambda: num_labels), batch_first=True)
        _l_(615972)

    def forward(self, input_ids, attention_mask, labels=None, token_type_ids=None):
        _l_(616057)

        outputs = _c_(615978, _a_(615975, _n_(615974, "self", lambda: self), "bert"), _n_(615976, "input_ids", lambda: input_ids), attention_mask=_n_(615977, "attention_mask", lambda: attention_mask))
        _l_(615979)
       

        sequence_output = _c_(615988, _a_(615987, _c_(615986, _a_(615981, _n_(615980, "torch", lambda: torch), "stack"), (_n_(615982, "outputs", lambda: outputs)[1][-1], _n_(615983, "outputs", lambda: outputs)[1][-2], _n_(615984, "outputs", lambda: outputs)[1][-3], _n_(615985, "outputs", lambda: outputs)[1][-4])), "mean"), dim=0)
        _l_(615989)
        
        sequence_output = _c_(615993, _a_(615991, _n_(615990, "self", lambda: self), "dropout"), _n_(615992, "sequence_output", lambda: sequence_output))
        _l_(615994)
      
        emission = _c_(615998, _a_(615996, _n_(615995, "self", lambda: self), "classifier"), _n_(615997, "sequence_output", lambda: sequence_output))  # [32,256,17]
        _l_(615999)  # [32,256,17]

        labels = _c_(616008, _a_(616001, _n_(616000, "labels", lambda: labels), "reshape"), _c_(616004, _a_(616003, _n_(616002, "attention_mask", lambda: attention_mask), "size"))[0], _c_(616007, _a_(616006, _n_(616005, "attention_mask", lambda: attention_mask), "size"))[1])
        _l_(616009)
      

        if _n_(616010, "labels", lambda: labels) is not None:
            _l_(616056)

        
            loss = -_c_(616022, _a_(616012, _n_(616011, "self", lambda: self), "crf"), _c_(616015, _n_(616013, "log_soft", lambda: log_soft), _n_(616014, "emission", lambda: emission), 2), _n_(616016, "labels", lambda: labels), mask=_c_(616021, _a_(616018, _n_(616017, "attention_mask", lambda: attention_mask), "type"), _a_(616020, _n_(616019, "torch", lambda: torch), "uint8")), reduction='mean')
            _l_(616023)
       
            prediction = _c_(616033, _a_(616026, _a_(616025, _n_(616024, "self", lambda: self), "crf"), "decode"), _n_(616027, "emission", lambda: emission), mask=_c_(616032, _a_(616029, _n_(616028, "attention_mask", lambda: attention_mask), "type"), _a_(616031, _n_(616030, "torch", lambda: torch), "uint8")))
            _l_(616034)
          
            _c_(616038, _n_(616035, "print", lambda: print), [_n_(616036, "loss", lambda: loss), _n_(616037, "prediction", lambda: prediction)])
            _l_(616039)
            aux = [_n_(616040, "loss", lambda: loss), _n_(616041, "prediction", lambda: prediction)]
            _l_(616042)
            return aux

        else:
      
            prediction = _c_(616052, _a_(616045, _a_(616044, _n_(616043, "self", lambda: self), "crf"), "decode"), _n_(616046, "emission", lambda: emission), mask=_c_(616051, _a_(616048, _n_(616047, "attention_mask", lambda: attention_mask), "type"), _a_(616050, _n_(616049, "torch", lambda: torch), "uint8")))
            _l_(616053)
            aux = _n_(616054, "prediction", lambda: prediction)
            _l_(616055)
            return aux