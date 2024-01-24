# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65724638/nameerror-name-contact-value-is-not-defined-in-serializers-py
#
# TABLE: CONTACT_METHOD (COME)
#
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class ContactMethod(_a_(565159, _n_(565158, "models", lambda: models), "Model")):
    _l_(565224)

    # attributes:
    contact_value = _c_(565161, _a_(565160, models, "CharField"), db_column = 'CONTACT_VALUE', max_length = 255, null=True, blank=True, verbose_name = 'Contact Value')
    _l_(565162)
    effective_period_from = _c_(565164, _a_(565163, models, "DateTimeField"), db_column = 'EFFECTIVE_PERIOD_FROM', null=True, blank=True, verbose_name = 'Effective Period From')
    _l_(565165)
    effective_period_to = _c_(565167, _a_(565166, models, "DateTimeField"), db_column = 'EFFECTIVE_PERIOD_TO', null=True, blank=True, verbose_name = 'Effective Period To')
    _l_(565168)
    extension_number = _c_(565170, _a_(565169, models, "CharField"), db_column = 'EXTENSION_NUMBER', max_length = 255, null=True, blank=True, verbose_name = 'Extension Number')
    _l_(565171)
    notes = _c_(565173, _a_(565172, models, "TextField"), db_column = 'NOTES', max_length = 1000, null=True, blank=True, verbose_name = 'Notes')
    _l_(565174)
    created_at = _c_(565176, _a_(565175, models, "DateTimeField"), db_column = 'CREATED_AT', verbose_name = 'Created At', editable = False, auto_now_add=True)
    _l_(565177)
    created_by = _c_(565179, _a_(565178, models, "CharField"), db_column = 'CREATED_BY', max_length = 255, verbose_name = 'Created By', editable = False)
    _l_(565180)
    updated_at = _c_(565182, _a_(565181, models, "DateTimeField"), db_column = 'UPDATED_AT', verbose_name = 'Updated At', editable = False, auto_now=True)
    _l_(565183)
    updated_by = _c_(565185, _a_(565184, models, "CharField"), db_column = 'UPDATED_BY', max_length = 255, verbose_name = 'Updated By', editable = False)
    _l_(565186)

    # primary & foreign keys:
    id = _c_(565188, _a_(565187, models, "BigAutoField"), db_column = 'ID', primary_key = True)
    _l_(565189)
    # COME_REF_CMTY_FK: ref CONTACT_METHOD_TYPE 
    contact_method_type_id = _c_(565192, _a_(565190, models, "ForeignKey"), ContactMethodTypeLv, on_delete = _a_(565191, models, "DO_NOTHING"), db_column = 'CONTACT_METHOD_TYPE_ID', verbose_name = 'Contact Method Type')
    _l_(565193)

    def __str__(self):
        _l_(565217)

        aux = f'contact_value={_a_(565195, _n_(565194, "self", lambda: self), "contact_value")} | effective_period_from={_a_(565197, _n_(565196, "self", lambda: self), "effective_period_from")} | effective_period_to={_a_(565199, _n_(565198, "self", lambda: self), "effective_period_to")} | extension_number={_a_(565201, _n_(565200, "self", lambda: self), "extension_number")} | notes={_a_(565203, _n_(565202, "self", lambda: self), "notes")} | id={_a_(565205, _n_(565204, "self", lambda: self), "id")} | contact_method_type_id={_a_(565207, _n_(565206, "self", lambda: self), "contact_method_type_id")} | created_at={_a_(565209, _n_(565208, "self", lambda: self), "created_at")} | created_by={_a_(565211, _n_(565210, "self", lambda: self), "created_by")} | updated_at={_a_(565213, _n_(565212, "self", lambda: self), "updated_at")} | updated_by={_a_(565215, _n_(565214, "self", lambda: self), "updated_by")}'
        _l_(565216)
        return aux

    class Meta:
        _l_(565223)

        #abstract = True
        managed = False
        _l_(565218)
        db_table = 'CONTACT_METHOD'
        _l_(565219)
        verbose_name = 'Contact Method'
        _l_(565220)
        verbose_name_plural = 'Contact Methods'
        _l_(565221)
        ordering = (
            'id',
            )
        _l_(565222)