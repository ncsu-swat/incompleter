# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65586172/sqlalchemy-object-throwing-attribute-error-for-sa-instance-state-in-pytest
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class ListAPI(_n_(528386, "Resource", lambda: Resource)):
    _l_(528449)

    def __init__(self):
        _l_(528410)

        _n_(528387, "self", lambda: self).reqparse = _c_(528390, _a_(528389, _n_(528388, "reqparse", lambda: reqparse), "RequestParser"))                                                                                                            
        _l_(528391)                                                                                                            
        _n_(528392, "self", lambda: self).fields = ['description', 'vendorquery', 'campaign', 's3key',                                                                                   
                       'ftimestamp', 'fname', 'source', 'user']                                                                                             
        _l_(528393)                                                                                             
        for f in _a_(528395, _n_(528394, "self", lambda: self), "fields"):
            _l_(528403)

            _c_(528401, _a_(528398, _a_(528397, _n_(528396, "self", lambda: self), "reqparse"), "add_argument"), _n_(528399, "f", lambda: f),                                                                                                                   
                                       type=_n_(528400, "str", lambda: str),                                                                                                            
                                       location='json')                                                                                                     
            _l_(528402)                                                                                                     
        _c_(528408, _a_(528407, _n_(528404, "super", lambda: super)(_n_(528405, "ListAPI", lambda: ListAPI), _n_(528406, "self", lambda: self)), "__init__"))                                                                                                                     
        _l_(528409)                                                                                                                     
    def get(self):
        _l_(528448)

        """Returns all lists."""                                                                                                                            
        try:
            _l_(528447)

            alllists = _c_(528414, _a_(528413, _a_(528412, _n_(528411, "Voterlist", lambda: Voterlist), "query"), "all"))                                                                                                                
            _l_(528415)                                                                                                                
            lists = []                                                                                                                                      
            _l_(528416)                                                                                                                                      
            for l in _n_(528417, "alllists", lambda: alllists):
                _l_(528430)

                l = _a_(528419, _n_(528418, "l", lambda: l), "__dict__")                                                                                                                              
                _l_(528420)                                                                                                                              
                _c_(528423, _a_(528422, _n_(528421, "l", lambda: l), "pop"), '_sa_instance_state', None)                                                                                                           
                _l_(528424)                                                                                                           
                _c_(528428, _a_(528426, _n_(528425, "lists", lambda: lists), "append"), _n_(528427, "l", lambda: l))                                                                                                                             
                _l_(528429)                                                                                                                             
            aux = _c_(528433, _n_(528431, "jsonify", lambda: jsonify), {'lists': _n_(528432, "lists", lambda: lists)})                                                                                                                
            _l_(528434)                                                                                                                
            return aux                                                                                                                
        except _n_(528435, "Exception", lambda: Exception) as e:
            _l_(528446)

            _c_(528438, _n_(528436, "print", lambda: print), _n_(528437, "e", lambda: e))                                                                                                                                        
            _l_(528439)                                                                                                                                        
            _c_(528444, _n_(528440, "abort", lambda: abort), 400, _c_(528443, _n_(528441, "str", lambda: str), _n_(528442, "e", lambda: e))) 
            _l_(528445) 