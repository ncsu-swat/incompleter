# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/68092717/i-am-trying-to-append-a-dictionary-to-a-list-but-it-showing-me-name-error-and-t
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Category:
    _l_(542214)

    ledger =[]
    _l_(542176)
    
    def __init__(self,category):
        _l_(542181)

        _c_(542179, _n_(542177, "print", lambda: print), _n_(542178, "category", lambda: category))
        _l_(542180)
       

    def deposit(self,amount,description):
        _l_(542213)

        
        _n_(542182, "self", lambda: self).amount=_n_(542183, "amount", lambda: amount)
        _l_(542184)
        _n_(542185, "self", lambda: self).description=_n_(542186, "description", lambda: description)
        _l_(542187)
        if not _n_(542188, "description", lambda: description):
            _l_(542212)

            aux = ""
            _l_(542189)
            return aux
        else:
        
            dect={"amount":_a_(542191, _n_(542190, "self", lambda: self), "amount"),"description":_a_(542193, _n_(542192, "self", lambda: self), "description")}
            _l_(542194)
            _c_(542197, _n_(542195, "print", lambda: print), _n_(542196, "dect", lambda: dect))
            _l_(542198)
            _c_(542202, _a_(542200, _n_(542199, "ledger", lambda: ledger), "append"), _n_(542201, "dect", lambda: dect))
            _l_(542203)
            _n_(542204, "self", lambda: self).ledger=_n_(542205, "ledger", lambda: ledger)
            _l_(542206)
            _c_(542210, _n_(542207, "print", lambda: print), _a_(542209, _n_(542208, "self", lambda: self), "ledger"))
            _l_(542211)
food=_c_(542216, _n_(542215, "Category", lambda: Category), "food")
_l_(542217)
_c_(542220, _a_(542219, _n_(542218, "food", lambda: food), "deposit"), 1000,"initial deposit")
_l_(542221)