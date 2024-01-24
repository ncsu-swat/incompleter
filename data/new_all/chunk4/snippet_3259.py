# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/76626739/python-typeerror-cant-instantiate-abstract-class-with-abstract-methods
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class ChromaProductRetriever(_n_(593011, "BaseRetriever", lambda: BaseRetriever), _n_(593012, "BaseModel", lambda: BaseModel)):
    _l_(593049)

    vectorstore: VectorStore
    _l_(593013)
 
    class Config:
        _l_(593015)

        arbitrary_types_allowed = True
        _l_(593014)
 
    def combine_metadata(self, doc) -> _n_(593016, "str", lambda: str):
        _l_(593024)

        metadata = _a_(593018, _n_(593017, "doc", lambda: doc), "metadata")
        _l_(593019)
        aux = (
           "Item Name: " + _n_(593020, "metadata", lambda: metadata)["item_name"] + ". " +
           "Item Description: " + _n_(593021, "metadata", lambda: metadata)["bullet_point"] + ". " +
           "Item Keywords: " + _n_(593022, "metadata", lambda: metadata)["item_keywords"] + "."
        )
        _l_(593023)
        return aux
 
    def get_relevant_documents(self, query):
        _l_(593048)

        docs = []
        _l_(593025)
        for doc in _c_(593030, _a_(593028, _a_(593027, _n_(593026, "self", lambda: self), "vectorstore"), "similarity_search"), _n_(593029, "query", lambda: query)):
            _l_(593045)

            content = _c_(593034, _a_(593032, _n_(593031, "self", lambda: self), "combine_metadata"), _n_(593033, "doc", lambda: doc))
            _l_(593035)
            _c_(593043, _a_(593037, _n_(593036, "docs", lambda: docs), "append"), _c_(593042, _n_(593038, "Document", lambda: Document), page_content=_n_(593039, "content", lambda: content),
                metadata=_a_(593041, _n_(593040, "doc", lambda: doc), "metadata")
            ))
            _l_(593044)
        aux = _n_(593046, "docs", lambda: docs)
        _l_(593047)
 
        return aux