# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/74576161/selenium-cant-find-a-submit-button-on-login-attributeerror-webdriver-objec
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_c_(353163, _a_(353162, _n_(353161, "driver", lambda: driver), "get"), 'https://app.quantdata.us/login')
_l_(353164)

cookies = _c_(353167, _a_(353166, _n_(353165, "driver", lambda: driver), "get_cookies"))
_l_(353168)
_c_(353171, _a_(353170, _n_(353169, "driver", lambda: driver), "implicitly_wait"), 20)
_l_(353172)

_c_(353178, _a_(353176, _c_(353175, _a_(353174, _n_(353173, "driver", lambda: driver), "find_element"), "id","username"), "send_keys"), _n_(353177, "username", lambda: username))#works
_l_(353179)#works
_c_(353185, _a_(353183, _c_(353182, _a_(353181, _n_(353180, "driver", lambda: driver), "find_element"), "id","password"), "send_keys"), _n_(353184, "password", lambda: password))#works
_l_(353186)#works


_c_(353191, _a_(353190, _c_(353189, _a_(353188, _n_(353187, "driver", lambda: driver), "find_element"), "id","submit"), "click")) #not working 
_l_(353192) #not working 
_c_(353197, _a_(353196, _c_(353195, _a_(353194, _n_(353193, "driver", lambda: driver), "findElement"), "class","submit"), "click"));#notworking
_l_(353198)#notworking
_c_(353203, _a_(353202, _c_(353201, _a_(353200, _n_(353199, "driver", lambda: driver), "find_element"), "xpath","//*[@id=__next]/div[1]/div[2]/div[2]/div/form/button"), "click"))#not working
_l_(353204)#not working
_c_(353209, _a_(353208, _c_(353207, _a_(353206, _n_(353205, "driver", lambda: driver), "find_element_by_css_selector"), 'button[type=submit]'), "submit")) #not working 
_l_(353210) #not working 
 
_c_(353215, _a_(353214, _c_(353213, _a_(353212, _n_(353211, "driver", lambda: driver), "find_element"), "id","submit"), "click")) #not working 
_l_(353216) #not working 
_c_(353221, _a_(353220, _c_(353219, _a_(353218, _n_(353217, "driver", lambda: driver), "findElement"), "class","submit"), "click"));#notworking
_l_(353222)#notworking
_c_(353227, _a_(353226, _c_(353225, _a_(353224, _n_(353223, "driver", lambda: driver), "find_element"), "xpath","//*[@id=__next]/div[1]/div[2]/div[2]/div/form/button"), "click"))#not working
_l_(353228)#not working
_c_(353233, _a_(353232, _c_(353231, _a_(353230, _n_(353229, "driver", lambda: driver), "find_element_by_css_selector"), 'button[type=submit]'), "submit")) #not working 
_l_(353234) #not working 