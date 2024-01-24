# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/50348992/django-attributeerror-module-clients-has-no-attribute-models
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.db import models
    _l_(577581)

except ImportError:
    pass
try:
    import datetime
    _l_(577583)

except ImportError:
    pass
try:
    import calendar
    _l_(577585)

except ImportError:
    pass
try:
    import clients.models
    _l_(577587)

except ImportError:
    pass
try:
    from django.core.urlresolvers import reverse
    _l_(577589)

except ImportError:
    pass


# Create your models here.


class PartnerInfo(_a_(577591, _n_(577590, "models", lambda: models), "Model")):
    _l_(577608)

    name = _c_(577594, _a_(577593, _n_(577592, "models", lambda: models), "CharField"), max_length=100)
    _l_(577595)
    email = _c_(577598, _a_(577597, _n_(577596, "models", lambda: models), "CharField"), max_length=100)
    _l_(577599)
    phone = _c_(577602, _a_(577601, _n_(577600, "models", lambda: models), "IntegerField"))
    _l_(577603)
    price = _c_(577606, _a_(577605, _n_(577604, "models", lambda: models), "IntegerField"))
    _l_(577607)


class NewPartnerLead(_a_(577610, _n_(577609, "models", lambda: models), "Model"), _n_(577611, "LeadStage", lambda: LeadStage)):
    _l_(577627)

    new_name = _c_(577614, _a_(577613, _n_(577612, "models", lambda: models), "CharField"), max_length=50)
    _l_(577615)
    email = _c_(577618, _a_(577617, _n_(577616, "models", lambda: models), "CharField"), max_length=50)
    _l_(577619)
    phone_num = _c_(577622, _a_(577621, _n_(577620, "models", lambda: models), "IntegerField"))
    _l_(577623)
    lead_stage = _c_(577625, _a_(577624, LeadStage, "lead_stage"))
    _l_(577626)


class Booking(_a_(577629, _n_(577628, "models", lambda: models), "Model"), _n_(577630, "ClientLead", lambda: ClientLead)):
    _l_(577664)

    number_of_bookings = _c_(577633, _a_(577632, _n_(577631, "models", lambda: models), "IntegerField"))
    _l_(577634)
    clients_name = _c_(577636, _a_(577635, ClientLead, "client_name"))
    _l_(577637)
    clients_phone = _c_(577639, _a_(577638, ClientLead, "phone_number"))
    _l_(577640)
    clients_email = _c_(577642, _a_(577641, ClientLead, "email_address"))
    _l_(577643)

    class BookingDetail(_n_(577644, "Booking", lambda: Booking)):
        _l_(577663)

        start_date = _c_(577648, _a_(577647, _a_(577646, _n_(577645, "datetime", lambda: datetime), "datetime"), "date"))
        _l_(577649)
        end_date = _c_(577653, _a_(577652, _a_(577651, _n_(577650, "datetime", lambda: datetime), "datetime"), "date"))
        _l_(577654)
        destination = _c_(577657, _a_(577656, _n_(577655, "models", lambda: models), "CharField"), max_length=50)
        _l_(577658)

        @static
        def number_of_days(self, start_date, end_date):
            _l_(577662)

            aux = _n_(577659, "end_date", lambda: end_date)-_n_(577660, "start_date", lambda: start_date)
            _l_(577661)

            return aux


class Payment(_a_(577666, _n_(577665, "models", lambda: models), "Model"), _a_(577668, _n_(577667, "PartnerInfo", lambda: PartnerInfo), "price"), _a_(577671, _a_(577670, _n_(577669, "Booking", lambda: Booking), "BookingDetail"), "number_of_days")):
    _l_(577689)

    cash_out = _c_(577674, _a_(577673, _n_(577672, "models", lambda: models), "IntegerField"))
    _l_(577675)

    @static
    def client_payment(self, number_of_days, price):
        _l_(577679)

        aux = _n_(577676, "price", lambda: price)*_n_(577677, "number_of_days", lambda: number_of_days)
        _l_(577678)
        return aux

    @static
    def provider_cut(self, client_payment):
        _l_(577684)

        provider_cut = 0.8*_n_(577680, "client_payment", lambda: client_payment)
        _l_(577681)
        aux = _n_(577682, "provider_cut", lambda: provider_cut)
        _l_(577683)
        return aux

    @static
    def balance(self, provider_cut):
        _l_(577688)

        _n_(577685, "provider_cut", lambda: provider_cut)-_n_(577686, "cash_out", lambda: cash_out)
        _l_(577687)

class Action(_n_(577690, "Actions", lambda: Actions)):
    _l_(577697)

    status = _c_(577692, _a_(577691, Actions, "status"))
    _l_(577693)
    action = _c_(577695, _a_(577694, Actions, "action"))
    _l_(577696)