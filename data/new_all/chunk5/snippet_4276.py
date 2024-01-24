# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60360550/sqlalchemy-multiple-nested-queries-with-filters-from-one-table-attributeerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Sale(_a_(654038, _n_(654037, "db", lambda: db), "Model")):
    _l_(654132)

    id = _c_(654041, _a_(654039, db, "Column"), _a_(654040, db, "Integer"), primary_key=True)
    _l_(654042)
    vente_no = _c_(654046, _a_(654043, db, "Column"), _c_(654045, _a_(654044, db, "String"), 50))
    _l_(654047)
    lampshade = _c_(654051, _a_(654048, db, "Column"), _c_(654050, _a_(654049, db, "String"), 30))
    _l_(654052)
    brocante = _c_(654056, _a_(654053, db, "Column"), _c_(654055, _a_(654054, db, "String"), 30))
    _l_(654057)
    buyer = _c_(654061, _a_(654058, db, "Column"), _c_(654060, _a_(654059, db, "String"), 255))
    _l_(654062)
    pays = _c_(654066, _a_(654063, db, "Column"), _c_(654065, _a_(654064, db, "String"), 255))
    _l_(654067)
    QT = _c_(654070, _a_(654068, db, "Column"), _a_(654069, db, "Integer"))
    _l_(654071)
    prix_de_vente = _c_(654074, _a_(654072, db, "Column"), _a_(654073, db, "Float"))
    _l_(654075)
    poste = _c_(654078, _a_(654076, db, "Column"), _a_(654077, db, "Float"))
    _l_(654079)
    total = _c_(654082, _a_(654080, db, "Column"), _a_(654081, db, "Float"))
    _l_(654083)
    bordeaux = _c_(654086, _a_(654084, db, "Column"), _a_(654085, db, "Integer"))
    _l_(654087)
    amazon = _c_(654091, _a_(654088, db, "Column"), _c_(654090, _a_(654089, db, "String"), 255))
    _l_(654092)
    bordeaux_euros = _c_(654095, _a_(654093, db, "Column"), _a_(654094, db, "Float"))
    _l_(654096)
    bordeaux_comm = _c_(654099, _a_(654097, db, "Column"), _a_(654098, db, "Float"))
    _l_(654100)
    amazon_euros = _c_(654103, _a_(654101, db, "Column"), _a_(654102, db, "Float"))
    _l_(654104)
    amazon_comm = _c_(654107, _a_(654105, db, "Column"), _a_(654106, db, "Float"))
    _l_(654108)
    PID = _c_(654113, _a_(654109, db, "Column"), _a_(654110, db, "Integer"), _c_(654112, _a_(654111, db, "ForeignKey"), "period.id"))
    _l_(654114)
    date = _c_(654117, _a_(654115, db, "Column"), _a_(654116, db, "Date"))
    _l_(654118)
    description = _c_(654121, _a_(654119, db, "Column"), _c_(654120, String, 255))
    _l_(654122)

    P_id = _c_(654124, _a_(654123, db, "relationship"), "Period")
    _l_(654125)

    def __repr__(self):
        _l_(654131)

        aux = _c_(654129, _a_(654126, '{}', "format"), _a_(654128, _n_(654127, "self", lambda: self), "id"))
        _l_(654130)
        return aux