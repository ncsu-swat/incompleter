# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65701682/django-models-in-admin-return-typeerror-bad-operand-type-for-unary-str
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class CurrencyManagementAssetsModel(_a_(461849, _n_(461848, "models", lambda: models), "Model")):
    _l_(461882)

    RequestId = _c_(461851, _a_(461850, models, "IntegerField"), blank=False)
    _l_(461852)
    CbnInstitutionCode = _c_(461854, _a_(461853, models, "CharField"), max_length=5, blank=False)
    _l_(461855)
    SortCode = _c_(461857, _a_(461856, models, "CharField"), max_length=10, blank=False)
    _l_(461858)
    Count = _c_(461860, _a_(461859, models, "IntegerField"), blank=False)
    _l_(461861)
    AssetClassificationId = _c_(461863, _a_(461862, models, "IntegerField"), blank=False)
    _l_(461864)
    AssetTypeId = _c_(461866, _a_(461865, models, "IntegerField"), blank=False)
    _l_(461867)
    ValueOfCurrencyDistributed = _c_(461869, _a_(461868, models, "DecimalField"), max_digits='20', decimal_places='10', 
    blank=False)
    _l_(461870)
    VaultCapacity = _c_(461872, _a_(461871, models, "DecimalField"), max_digits='20', decimal_places='10', blank=False)
    _l_(461873)
    Year = _c_(461875, _a_(461874, models, "IntegerField"), blank=False)
    _l_(461876)
    HalfOftheYear = _c_(461878, _a_(461877, models, "IntegerField"), blank=False)
    _l_(461879)

    class Meta:
        _l_(461881)

        verbose_name = 'Currency Management Assets'
        _l_(461880)