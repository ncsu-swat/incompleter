# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/71075086/attribute-error-when-using-api-to-access-google-calendar
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
credentials = _c_(642249, _a_(642246, _a_(642245, _n_(642244, "service_account", lambda: service_account), "Credentials"), "from_service_account_file"), _n_(642247, "SERVICE_ACCOUNT_FILE", lambda: SERVICE_ACCOUNT_FILE), scopes=_n_(642248, "SCOPES", lambda: SCOPES))
_l_(642250)
credentials = _c_(642254, _a_(642252, _n_(642251, "credentials", lambda: credentials), "with_subject"), _n_(642253, "SUBJECT_EMAIL", lambda: SUBJECT_EMAIL))
_l_(642255)
calendar_service = _c_(642260, _a_(642258, _a_(642257, _n_(642256, "googleapiclient", lambda: googleapiclient), "discovery"), "build"), 'calendar', 'v3', _n_(642259, "credentials", lambda: credentials))
_l_(642261)
events = _c_(642268, _a_(642267, _c_(642266, _a_(642265, _c_(642264, _a_(642263, _n_(642262, "calendar_service", lambda: calendar_service), "events")), "list"), calendarId='primary'), "execute"))
_l_(642269)