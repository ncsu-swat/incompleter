# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/74899727/attributeerror-webdriver-object-has-no-attribute-find-element-by-id
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
driver = _c_(672134, _a_(672133, _n_(672132, "webdriver", lambda: webdriver), "Firefox"))
_l_(672135)
_c_(672138, _a_(672137, _n_(672136, "driver", lambda: driver), "get"), 'https://mahmoud-magdy.com/register')
_l_(672139)
_c_(672145, _a_(672143, _c_(672142, _a_(672141, _n_(672140, "driver", lambda: driver), "find_element_by_id"), 'first_name'), "send_keys"), _n_(672144, "monster", lambda: monster))
_l_(672146)
_c_(672152, _a_(672150, _c_(672149, _a_(672148, _n_(672147, "driver", lambda: driver), "find_element_by_id"), 'last_name'), "send_keys"), _n_(672151, "monster", lambda: monster))
_l_(672153)
_c_(672159, _a_(672157, _c_(672156, _a_(672155, _n_(672154, "driver", lambda: driver), "find_element_by_name"), 'phone'), "send_keys"), _n_(672158, "phone", lambda: phone))
_l_(672160)
_c_(672166, _a_(672164, _c_(672163, _a_(672162, _n_(672161, "driver", lambda: driver), "find_element_by_name"), 'father_phone'), "send_keys"), _n_(672165, "father_phone", lambda: father_phone))
_l_(672167)
_c_(672173, _a_(672171, _c_(672170, _a_(672169, _n_(672168, "driver", lambda: driver), "find_element_by_name"), 'email'), "send_keys"), _n_(672172, "email", lambda: email))
_l_(672174)
_c_(672180, _a_(672178, _c_(672177, _a_(672176, _n_(672175, "driver", lambda: driver), "find_element_by_name"), 'password'), "send_keys"), _n_(672179, "password", lambda: password))
_l_(672181)
_c_(672187, _a_(672185, _c_(672184, _a_(672183, _n_(672182, "driver", lambda: driver), "find_element_by_name"), 'password_confirmation'), "send_keys"), _n_(672186, "password_confirmation", lambda: password_confirmation))
_l_(672188)
_c_(672193, _a_(672192, _c_(672191, _a_(672190, _n_(672189, "driver", lambda: driver), "find_element_by_css_selector"), 'button[type="submit"]'), "click"))
_l_(672194)
_c_(672197, _n_(672195, "print", lambda: print), _n_(672196, "phone", lambda: phone))
_l_(672198)
_c_(672201, _a_(672200, _n_(672199, "driver", lambda: driver), "quit"))
_l_(672202)