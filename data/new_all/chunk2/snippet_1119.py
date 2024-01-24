# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/44207149/django-save-to-db-typeerror-int-argument-must-be-a-string-a-bytes-like-obje
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class InstagramAccount(_a_(475661, _n_(475660, "models", lambda: models), "Model")):
    _l_(475685)

    username = _c_(475663, _a_(475662, models, "CharField"), max_length=45, primary_key=True)
    _l_(475664)
    password = _c_(475666, _a_(475665, models, "CharField"), max_length=45)
    _l_(475667)
    account_id_account = _c_(475670, _a_(475668, models, "ForeignKey"), Account, _a_(475669, models, "DO_NOTHING"), db_column='account_id_account')
    _l_(475671)
    expired_date = _c_(475673, _a_(475672, models, "DateTimeField"), null=False)
    _l_(475674)
    history_of_payments = _c_(475676, _a_(475675, models, "TextField"), blank=True, null=True)
    _l_(475677)
    account_type = _c_(475679, _a_(475678, models, "TextField"), default='trial')
    _l_(475680)

    class Meta:
        _l_(475684)

        managed = False
        _l_(475681)
        db_table = 'instagram_account'
        _l_(475682)
        unique_together = (('account_id_account', 'username'),)
        _l_(475683)

class Proxy(_a_(475687, _n_(475686, "models", lambda: models), "Model")):
    _l_(475728)

    id_proxy = _c_(475689, _a_(475688, models, "AutoField"), primary_key=True)
    _l_(475690)
    proxy = _c_(475692, _a_(475691, models, "CharField"), max_length=45, blank=False, null=False)
    _l_(475693)
    meta = _c_(475695, _a_(475694, models, "TextField"), null=True)
    _l_(475696)
    start_date = _c_(475698, _a_(475697, models, "DateTimeField"), null=False)
    _l_(475699)
    end_date = _c_(475701, _a_(475700, models, "DateTimeField"), null=True)
    _l_(475702)
    country = _c_(475704, _a_(475703, models, "CharField"), max_length=45, null=False)
    _l_(475705)
    period = _c_(475707, _a_(475706, models, "PositiveIntegerField"))
    _l_(475708)
    price = _c_(475711, _a_(475709, models, "FloatField"), validators=[_c_(475710, MinValueValidator, 0.0), ])
    _l_(475712)
    # It can confuse, but our proxy provider have it own id for proxy
    proxy_provider_id = _c_(475714, _a_(475713, models, "PositiveIntegerField"))
    _l_(475715)
    ip = _c_(475717, _a_(475716, models, "CharField"), max_length=45, null=False, blank=False)
    _l_(475718)
    account = _c_(475722, _a_(475719, models, "ForeignKey"), _n_(475720, "InstagramAccount", lambda: InstagramAccount), _a_(475721, models, "DO_NOTHING"),
                                db_column='instagram_account_account_id_account')
    _l_(475723)

    class Meta:
        _l_(475727)

        managed = False
        _l_(475724)
        db_table = 'proxy'
        _l_(475725)
        unique_together = (('id_proxy', 'account'),)
        _l_(475726)