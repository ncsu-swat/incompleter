# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/73591649/how-to-fix-nameerror-when-i-call-a-function-from-another-file
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
        from selenium import webdriver
        _l_(567845)

except ImportError:
        pass
try:
        from selenium.webdriver.support.ui import WebDriverWait
        _l_(567847)

except ImportError:
        pass
try:
        from selenium.webdriver.common.by import By
        _l_(567849)

except ImportError:
        pass
try:
        from selenium.webdriver.support import expected_conditions as EC
        _l_(567851)

except ImportError:
        pass
try:
        import undetected_chromedriver.v2 as uc
        _l_(567853)

except ImportError:
        pass

if _n_(567854, "__name__", lambda: __name__) == '__main__':
        _l_(567920)


        options = _c_(567857, _a_(567856, _n_(567855, "uc", lambda: uc), "ChromeOptions"))
        _l_(567858)
        _c_(567861, _a_(567860, _n_(567859, "options", lambda: options), "add_argument"), "--ignore-certificate-error")
        _l_(567862)
        _c_(567865, _a_(567864, _n_(567863, "options", lambda: options), "add_argument"), "--ignore-ssl-errors")
        _l_(567866)
        # e.g. Chrome path in Mac =/Users/x/Library/xx/Chrome/Default/
        # options.add_argument( "--user-data-dir=<Your chrome profile>")
        driver = _c_(567870, _a_(567868, _n_(567867, "uc", lambda: uc), "Chrome"), options=_n_(567869, "options", lambda: options))
        _l_(567871)
        url='https://accounts.google.com/servicelogin'
        _l_(567872)
        _c_(567876, _a_(567874, _n_(567873, "driver", lambda: driver), "get"), _n_(567875, "url", lambda: url))
        _l_(567877)
        # add email
        _c_(567885, _a_(567883, _c_(567882, _a_(567879, _n_(567878, "driver", lambda: driver), "find_element"), _a_(567881, _n_(567880, "By", lambda: By), "XPATH"), '//*[@id="identifierId"]'), "send_keys"), _n_(567884, "gmail_uid", lambda: gmail_uid))
        _l_(567886)
        _c_(567893, _a_(567892, _c_(567891, _a_(567888, _n_(567887, "driver", lambda: driver), "find_element"), _a_(567890, _n_(567889, "By", lambda: By), "XPATH"), '//*[@id="identifierNext"]/div/button/span'), "click"))
        _l_(567894)
       
        _c_(567902, _a_(567900, _c_(567899, _a_(567896, _n_(567895, "driver", lambda: driver), "find_element"), _a_(567898, _n_(567897, "By", lambda: By), "XPATH"), '//*[@id="password"]/div[1]/div/div[1]/input'), "send_keys"), _n_(567901, "gmail_pwd", lambda: gmail_pwd))
        _l_(567903)
        _c_(567910, _a_(567909, _c_(567908, _a_(567905, _n_(567904, "driver", lambda: driver), "find_element"), _a_(567907, _n_(567906, "By", lambda: By), "XPATH"), '//*[@id="passwordNext"]/div/button/span'), "click"))
        _l_(567911)
       

        def my_custom_function(url):
                _l_(567919)


                get_url = _c_(567915, _a_(567913, _n_(567912, "driver", lambda: driver), "get"), _n_(567914, "url", lambda: url))
                _l_(567916)
                aux = _n_(567917, "get_url", lambda: get_url)
                _l_(567918)

                return aux