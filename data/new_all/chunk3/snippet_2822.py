# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62032946/drf-creating-new-objects-from-nested-representation-raises-typeerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Article(_a_(544258, _n_(544257, "models", lambda: models), "Model")):
    _l_(544277)

    uuid = _c_(544260, _a_(544259, models, "UUIDField"), editable=False, unique=True)
    _l_(544261)
    company = _c_(544264, _a_(544262, models, "ForeignKey"), Company,
        on_delete=_a_(544263, models, "PROTECT"),
        related_name='article_company_id',
    )
    _l_(544265)
    articleType = _c_(544268, _a_(544266, models, "ForeignKey"), ArticleType,
        on_delete=_a_(544267, models, "PROTECT"),
        related_name='type',
    )    
    _l_(544269)    
    date_inserted = _c_(544271, _a_(544270, models, "DateField"))    
    _l_(544272)    
    def __str__(self):
        _l_(544276)

        aux = _a_(544274, _n_(544273, "self", lambda: self), "uuid")
        _l_(544275)
        return aux