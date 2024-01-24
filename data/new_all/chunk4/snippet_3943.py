# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65006689/gensim-taggeddocument-list-generates-typeerror-nonetype-object-is-not-iterabl
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class doc2vec_model(_n_(588016, "Doc2Vec", lambda: Doc2Vec)):
    _l_(588091)

    
    def train(self,path):
        _l_(588032)

        _n_(588017, "self", lambda: self)._path = _n_(588018, "path", lambda: path)
        _l_(588019)
        _c_(588022, _a_(588021, _n_(588020, "self", lambda: self), "_tagged_documents"))
        _l_(588023)

        _c_(588030, _a_(588027, _n_(588024, "super", lambda: super)(_n_(588025, "Doc2Vec", lambda: Doc2Vec), _n_(588026, "self", lambda: self)), "__init__"), _a_(588029, _n_(588028, "self", lambda: self), "_docs"), min_count = 100, 
                                     vector_size=300, 
                                     epochs = 20, 
                                     negative = 5, 
                                     workers=20, 
                                     sample = 1e-5,
                                     alpha=0.01,
                                     min_alpha=0.0001)
        _l_(588031)

    def _tagged_documents(self,):
        _l_(588090)

        _n_(588033, "self", lambda: self).file_l = [_n_(588034, "name", lambda: name) for name in _c_(588039, _a_(588036, _n_(588035, "glob", lambda: glob), "iglob"), _a_(588038, _n_(588037, "self", lambda: self), "_path"), recursive=True)]
        _l_(588040)
        _n_(588041, "self", lambda: self)._docs = [] 
        _l_(588042) 
        for f_id, path in _c_(588046, _n_(588043, "enumerate", lambda: enumerate), _a_(588045, _n_(588044, "self", lambda: self), "file_l")):
            _l_(588089)

            with _c_(588049, _n_(588047, "open", lambda: open), _n_(588048, "path", lambda: path),'r') as f:
                _l_(588088)

                docu = _c_(588052, _a_(588051, _n_(588050, "f", lambda: f), "read"))
                _l_(588053)
                docu = _c_(588056, _n_(588054, "norm_string", lambda: norm_string), _n_(588055, "docu", lambda: docu))
                _l_(588057)
                docu = _c_(588060, _a_(588059, _n_(588058, "docu", lambda: docu), "split"), ' ')
                _l_(588061)
                chunk_size = 200 
                _l_(588062) 
                chunk_l = [_n_(588063, "docu", lambda: docu)[_n_(588064, "i", lambda: i):_n_(588065, "i", lambda: i)+_n_(588066, "chunk_size", lambda: chunk_size)] for i in _c_(588072, _n_(588067, "range", lambda: range), 0,_c_(588070, _n_(588068, "len", lambda: len), _n_(588069, "docu", lambda: docu)),_n_(588071, "chunk_size", lambda: chunk_size))]
                _l_(588073)
                for c_id, docu_chunk in _c_(588076, _n_(588074, "enumerate", lambda: enumerate), _n_(588075, "chunk_l", lambda: chunk_l)):
                    _l_(588087)

                    _c_(588085, _a_(588079, _a_(588078, _n_(588077, "self", lambda: self), "_docs"), "append"), _c_(588084, _n_(588080, "TaggedDocument", lambda: TaggedDocument), words=_n_(588081, "docu_chunk", lambda: docu_chunk), tags=(f'DOC_{_n_(588082, "f_id", lambda: f_id)}_{_n_(588083, "c_id", lambda: c_id)}',)))
                    _l_(588086)