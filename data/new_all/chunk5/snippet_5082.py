# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/74899727/attributeerror-webdriver-object-has-no-attribute-find-element-by-id
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
driver = _c_(662937, _a_(662936, _n_(662935, "webdriver", lambda: webdriver), "Firefox"))
_l_(662938)
_c_(662941, _a_(662940, _n_(662939, "driver", lambda: driver), "get"), 'https://mahmoud-magdy.com/register')
_l_(662942)
_c_(662948, _a_(662946, _c_(662945, _a_(662944, _n_(662943, "driver", lambda: driver), "find_element_by_id"), 'first_name'), "send_keys"), _n_(662947, "monster", lambda: monster))
_l_(662949)
_c_(662955, _a_(662953, _c_(662952, _a_(662951, _n_(662950, "driver", lambda: driver), "find_element_by_id"), 'last_name'), "send_keys"), _n_(662954, "monster", lambda: monster))
_l_(662956)
_c_(662962, _a_(662960, _c_(662959, _a_(662958, _n_(662957, "driver", lambda: driver), "find_element_by_name"), 'phone'), "send_keys"), _n_(662961, "phone", lambda: phone))
_l_(662963)
_c_(662969, _a_(662967, _c_(662966, _a_(662965, _n_(662964, "driver", lambda: driver), "find_element_by_name"), 'father_phone'), "send_keys"), _n_(662968, "father_phone", lambda: father_phone))
_l_(662970)
_c_(662976, _a_(662974, _c_(662973, _a_(662972, _n_(662971, "driver", lambda: driver), "find_element_by_name"), 'email'), "send_keys"), _n_(662975, "email", lambda: email))
_l_(662977)
_c_(662983, _a_(662981, _c_(662980, _a_(662979, _n_(662978, "driver", lambda: driver), "find_element_by_name"), 'password'), "send_keys"), _n_(662982, "password", lambda: password))
_l_(662984)
_c_(662990, _a_(662988, _c_(662987, _a_(662986, _n_(662985, "driver", lambda: driver), "find_element_by_name"), 'password_confirmation'), "send_keys"), _n_(662989, "password_confirmation", lambda: password_confirmation))
_l_(662991)
_c_(662996, _a_(662995, _c_(662994, _a_(662993, _n_(662992, "driver", lambda: driver), "find_element_by_css_selector"), 'button[type="submit"]'), "click"))
_l_(662997)
_c_(663000, _n_(662998, "print", lambda: print), _n_(662999, "phone", lambda: phone))
_l_(663001)
_c_(663004, _a_(663003, _n_(663002, "driver", lambda: driver), "quit"))
_l_(663005)