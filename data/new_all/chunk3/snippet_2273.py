# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53865361/getting-type-errornonetype-is-not-iterable-in-spacy-to-build-custom-ner-model
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import json
    _l_(530349)

except ImportError:
    pass
try:
    import logging
    _l_(530351)

except ImportError:
    pass
try:
    import spacy
    _l_(530353)

except ImportError:
    pass
try:
    import random
    _l_(530355)

except ImportError:
    pass
try:
    from spacy.util import minibatch, compounding
    _l_(530357)

except ImportError:
    pass
trainingfilename="C:/Users/codemen/Desktop/Timeseries Analytics/Canadianinfo.json"
_l_(530358)

_c_(530363, _a_(530360, _n_(530359, "logging", lambda: logging), "basicConfig"), level=_a_(530362, _n_(530361, "logging", lambda: logging), "INFO"))
_l_(530364)




def ConvertDataturkToSpacy(trainingfilename):
    _l_(530439)


    try:
        _l_(530438)

        trainingData=[]
        _l_(530365)
        lines=[]
        _l_(530366)
        # reading file  and  formating  part
        with _c_(530369, _n_(530367, "open", lambda: open), _n_(530368, "trainingfilename", lambda: trainingfilename),'r') as f:
            _l_(530374)

            lines=_c_(530372, _a_(530371, _n_(530370, "f", lambda: f), "readlines"))
            _l_(530373)
        for line in _n_(530375, "lines", lambda: lines):
            _l_(530424)

            data=_c_(530379, _a_(530377, _n_(530376, "json", lambda: json), "loads"), _n_(530378, "line", lambda: line))
            _l_(530380)
            text=_n_(530381, "data", lambda: data)['content']
            _l_(530382)
            entities=[]
            _l_(530383)
            _c_(530386, _n_(530384, "print", lambda: print), 'entties',_n_(530385, "entities", lambda: entities))
            _l_(530387)
            for annotation in _n_(530388, "data", lambda: data)['annotation']:
                _l_(530417)

                #print("Here is the thing")
                point=_n_(530389, "annotation", lambda: annotation)['points'][0] #single point annotation part
                _l_(530390) #single point annotation part
                #print(point)
                labels=_n_(530391, "annotation", lambda: annotation)['label']
                _l_(530392)
                _c_(530395, _n_(530393, "print", lambda: print), "isintance",_n_(530394, "labels", lambda: labels))
                _l_(530396)
                if not _c_(530400, _n_(530397, "isinstance", lambda: isinstance), _n_(530398, "labels", lambda: labels),_n_(530399, "list", lambda: list)):
                    _l_(530407)

                    labels=[_n_(530401, "labels", lambda: labels)]
                    _l_(530402)
                    _c_(530405, _n_(530403, "print", lambda: print), _n_(530404, "labels", lambda: labels))
                    _l_(530406)

                for label in _n_(530408, "labels", lambda: labels):
                    _l_(530416)

                    #dataturks indices are inclusive but spacy indices are not so dealing with it by adding  with +1
                    #print("Test here")
                    _c_(530414, _a_(530410, _n_(530409, "entities", lambda: entities), "append"), (_n_(530411, "point", lambda: point)['start'],_n_(530412, "point", lambda: point)['end']+1,_n_(530413, "label", lambda: label)))
                    _l_(530415)

            _c_(530422, _a_(530419, _n_(530418, "trainingData", lambda: trainingData), "append"), (_n_(530420, "text", lambda: text),{"entities":_n_(530421, "entities", lambda: entities)}))
            _l_(530423)
        aux = _n_(530425, "trainingData", lambda: trainingData)
        _l_(530426)
        return aux
    except _n_(530427, "Exception", lambda: Exception) as e:
        _l_(530437)

        _c_(530434, _a_(530429, _n_(530428, "logging", lambda: logging), "exception"), "Unable to process item" + _n_(530430, "trainingfilename", lambda: trainingfilename) +"\n"+ "errror ="+_c_(530433, _n_(530431, "str", lambda: str), _n_(530432, "e", lambda: e)))
        _l_(530435)
        aux = None
        _l_(530436)
        return aux

TrainingData=_c_(530442, _n_(530440, "ConvertDataturkToSpacy", lambda: ConvertDataturkToSpacy), _n_(530441, "trainingfilename", lambda: trainingfilename))
_l_(530443)