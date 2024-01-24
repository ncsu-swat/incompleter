# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65006689/gensim-taggeddocument-list-generates-typeerror-nonetype-object-is-not-iterabl
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class doc2vec_model(_n_(581671, "Doc2Vec", lambda: Doc2Vec)):
    _l_(581746)

    
    def train(self,path):
        _l_(581687)

        _n_(581672, "self", lambda: self)._path = _n_(581673, "path", lambda: path)
        _l_(581674)
        _c_(581677, _a_(581676, _n_(581675, "self", lambda: self), "_tagged_documents"))
        _l_(581678)

        _c_(581685, _a_(581682, _n_(581679, "super", lambda: super)(_n_(581680, "Doc2Vec", lambda: Doc2Vec), _n_(581681, "self", lambda: self)), "__init__"), _a_(581684, _n_(581683, "self", lambda: self), "_docs"), min_count = 100, 
                                     vector_size=300, 
                                     epochs = 20, 
                                     negative = 5, 
                                     workers=20, 
                                     sample = 1e-5,
                                     alpha=0.01,
                                     min_alpha=0.0001)
        _l_(581686)

    def _tagged_documents(self,):
        _l_(581745)

        _n_(581688, "self", lambda: self).file_l = [_n_(581689, "name", lambda: name) for name in _c_(581694, _a_(581691, _n_(581690, "glob", lambda: glob), "iglob"), _a_(581693, _n_(581692, "self", lambda: self), "_path"), recursive=True)]
        _l_(581695)
        _n_(581696, "self", lambda: self)._docs = [] 
        _l_(581697) 
        for f_id, path in _c_(581701, _n_(581698, "enumerate", lambda: enumerate), _a_(581700, _n_(581699, "self", lambda: self), "file_l")):
            _l_(581744)

            with _c_(581704, _n_(581702, "open", lambda: open), _n_(581703, "path", lambda: path),'r') as f:
                _l_(581743)

                docu = _c_(581707, _a_(581706, _n_(581705, "f", lambda: f), "read"))
                _l_(581708)
                docu = _c_(581711, _n_(581709, "norm_string", lambda: norm_string), _n_(581710, "docu", lambda: docu))
                _l_(581712)
                docu = _c_(581715, _a_(581714, _n_(581713, "docu", lambda: docu), "split"), ' ')
                _l_(581716)
                chunk_size = 200 
                _l_(581717) 
                chunk_l = [_n_(581718, "docu", lambda: docu)[_n_(581719, "i", lambda: i):_n_(581720, "i", lambda: i)+_n_(581721, "chunk_size", lambda: chunk_size)] for i in _c_(581727, _n_(581722, "range", lambda: range), 0,_c_(581725, _n_(581723, "len", lambda: len), _n_(581724, "docu", lambda: docu)),_n_(581726, "chunk_size", lambda: chunk_size))]
                _l_(581728)
                for c_id, docu_chunk in _c_(581731, _n_(581729, "enumerate", lambda: enumerate), _n_(581730, "chunk_l", lambda: chunk_l)):
                    _l_(581742)

                    _c_(581740, _a_(581734, _a_(581733, _n_(581732, "self", lambda: self), "_docs"), "append"), _c_(581739, _n_(581735, "TaggedDocument", lambda: TaggedDocument), words=_n_(581736, "docu_chunk", lambda: docu_chunk), tags=(f'DOC_{_n_(581737, "f_id", lambda: f_id)}_{_n_(581738, "c_id", lambda: c_id)}',)))
                    _l_(581741)