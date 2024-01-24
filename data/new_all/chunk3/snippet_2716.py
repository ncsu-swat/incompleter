# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65724638/nameerror-name-contact-value-is-not-defined-in-serializers-py
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from rest_framework import serializers
    _l_(549674)

except ImportError:
    pass
try:
    from .models import (
        ContactMethod,
        ContactMethodType,
        CountryType,
        GenderType,
        Organisation,
        OrganisationType,
        Party,
        PartyContact,
        PartyContactType,
        PartyIdentifierType,
        PartyRelationship,
        PartyType,
        Person,
        RoleType,
        RoleTypeRelationship,
        )
    _l_(549676)

except ImportError:
    pass

#
# TABLE: CONTACT_METHOD (COME)
#
class ContactMethodSerializer(_a_(549678, _n_(549677, "serializers", lambda: serializers), "ModelSerializer")):
    _l_(549685)


    class Meta:
        _l_(549684)

        # the model for Serializer
        model = _n_(549679, "ContactMethod", lambda: ContactMethod)
        _l_(549680)
        # field names for serialization
        fields = (
            contact_value,
            effective_period_from,
            effective_period_to,
            extension_number,
            notes,
            _n_(549681, "id", lambda: id),
            contact_method_type_id,
            created_at,
            created_by,
            updated_at,
            updated_by,
            )
        _l_(549682)
        ...
        _l_(549683)