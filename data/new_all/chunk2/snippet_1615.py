# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/70477075/i-keep-getting-this-error-when-i-want-to-query-data-from-a-model-in-mysql-databa
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Lga(_a_(425885, _n_(425884, "models", lambda: models), "Model")):
    _l_(425913)

    uniqueid = _c_(425887, _a_(425886, models, "AutoField"), primary_key=True)
    _l_(425888)
    lga_id = _c_(425890, _a_(425889, models, "IntegerField"))
    _l_(425891)
    lga_name = _c_(425893, _a_(425892, models, "CharField"), max_length=50)
    _l_(425894)
    state_id = _c_(425896, _a_(425895, models, "IntegerField"))
    _l_(425897)
    lga_description = _c_(425899, _a_(425898, models, "TextField"), blank=True, null=True)
    _l_(425900)
    entered_by_user = _c_(425902, _a_(425901, models, "CharField"), max_length=50)
    _l_(425903)
    date_entered = _c_(425905, _a_(425904, models, "DateTimeField"))
    _l_(425906)
    user_ip_address = _c_(425908, _a_(425907, models, "CharField"), max_length=50)
    _l_(425909)

    class Meta:
        _l_(425912)

        managed = False
        _l_(425910)
        db_table = 'lga'
        _l_(425911)