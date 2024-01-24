# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/32928255/attributeerror-at-authentication-django-1-8
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class UserProfile(_a_(658095, _n_(658094, "models", lambda: models), "Model")):
    _l_(658121)

    user = _c_(658097, _a_(658096, models, "OneToOneField"), User)
    _l_(658098)
    date_of_birth = _c_(658100, _a_(658099, models, "DateField"))
    _l_(658101)
    phone_number = _c_(658103, _a_(658102, models, "CharField"), max_length=30)
    _l_(658104)
    height = _c_(658106, _a_(658105, models, "FloatField"))
    _l_(658107)
    weight = _c_(658109, _a_(658108, models, "FloatField"))
    _l_(658110)
    medical_information = _c_(658112, _a_(658111, models, "ForeignKey"), MedicalInformation, null=True)
    _l_(658113)
    emergency_contact = _c_(658115, _a_(658114, models, "ForeignKey"), EmergencyContact, null=True)
    _l_(658116)
    status = _c_(658118, _a_(658117, models, "ForeignKey"), UserStatus, null=True)
    _l_(658119)
    REQUIRED_FIELDS = ['weight', 'height', 'date_of_birth', 'phone_number', 'email', 'first_name', 'last_name']
    _l_(658120)