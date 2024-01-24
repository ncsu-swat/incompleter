# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/74576161/selenium-cant-find-a-submit-button-on-login-attributeerror-webdriver-objec
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_c_(358251, _a_(358250, _n_(358249, "driver", lambda: driver), "get"), 'https://app.quantdata.us/login')
_l_(358252)

cookies = _c_(358255, _a_(358254, _n_(358253, "driver", lambda: driver), "get_cookies"))
_l_(358256)
_c_(358259, _a_(358258, _n_(358257, "driver", lambda: driver), "implicitly_wait"), 20)
_l_(358260)

_c_(358266, _a_(358264, _c_(358263, _a_(358262, _n_(358261, "driver", lambda: driver), "find_element"), "id","username"), "send_keys"), _n_(358265, "username", lambda: username))#works
_l_(358267)#works
_c_(358273, _a_(358271, _c_(358270, _a_(358269, _n_(358268, "driver", lambda: driver), "find_element"), "id","password"), "send_keys"), _n_(358272, "password", lambda: password))#works
_l_(358274)#works


_c_(358279, _a_(358278, _c_(358277, _a_(358276, _n_(358275, "driver", lambda: driver), "find_element"), "id","submit"), "click")) #not working 
_l_(358280) #not working 
_c_(358285, _a_(358284, _c_(358283, _a_(358282, _n_(358281, "driver", lambda: driver), "findElement"), "class","submit"), "click"));#notworking
_l_(358286)#notworking
_c_(358291, _a_(358290, _c_(358289, _a_(358288, _n_(358287, "driver", lambda: driver), "find_element"), "xpath","//*[@id=__next]/div[1]/div[2]/div[2]/div/form/button"), "click"))#not working
_l_(358292)#not working
_c_(358297, _a_(358296, _c_(358295, _a_(358294, _n_(358293, "driver", lambda: driver), "find_element_by_css_selector"), 'button[type=submit]'), "submit")) #not working 
_l_(358298) #not working 
 
_c_(358303, _a_(358302, _c_(358301, _a_(358300, _n_(358299, "driver", lambda: driver), "find_element"), "id","submit"), "click")) #not working 
_l_(358304) #not working 
_c_(358309, _a_(358308, _c_(358307, _a_(358306, _n_(358305, "driver", lambda: driver), "findElement"), "class","submit"), "click"));#notworking
_l_(358310)#notworking
_c_(358315, _a_(358314, _c_(358313, _a_(358312, _n_(358311, "driver", lambda: driver), "find_element"), "xpath","//*[@id=__next]/div[1]/div[2]/div[2]/div/form/button"), "click"))#not working
_l_(358316)#not working
_c_(358321, _a_(358320, _c_(358319, _a_(358318, _n_(358317, "driver", lambda: driver), "find_element_by_css_selector"), 'button[type=submit]'), "submit")) #not working 
_l_(358322) #not working 