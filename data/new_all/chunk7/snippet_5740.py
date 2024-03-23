# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/44996255/typeerror-object-of-type-nonetype-has-no-len-when-iterating-through-files
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(335509)

except ImportError:
    pass
try:
    import time
    _l_(335511)

except ImportError:
    pass
try:
    import getpass
    _l_(335513)

except ImportError:
    pass
try:
    from selenium import webdriver
    _l_(335515)

except ImportError:
    pass
try:
    from selenium.webdriver.common.keys import Keys
    _l_(335517)

except ImportError:
    pass


def Quora_bot():
    _l_(335561)


    username = None
    _l_(335518)
    password = None
    _l_(335519)

    chromedriver  = 'F:\All  Folders\chromedriver\shit.exe'
    _l_(335520)

#Uncomment this block if you don't want images to load(makes the procss a little bit faster)
    '''
    chromeOptions = webdriver.ChromeOptions()
    prefs = {"profile.managed_default_content_settings.images":2}
    chromeOptions.add_experimental_option("prefs",prefs)
    browser = webdriver.Chrome(chromedriver, chrome_options=chromeOptions)
    '''
    _l_(335521)

    browser = _c_(335525, _a_(335523, _n_(335522, "webdriver", lambda: webdriver), "Chrome"), _n_(335524, "chromedriver", lambda: chromedriver))
    _l_(335526)
    _c_(335529, _a_(335528, _n_(335527, "browser", lambda: browser), "get"), "http://www.quora.com")       # Quora home page
    _l_(335530)       # Quora home page
    _c_(335533, _a_(335532, _n_(335531, "time", lambda: time), "sleep"), 10)
    _l_(335534)

    # Logging into Quora
    form = _c_(335537, _a_(335536, _n_(335535, "browser", lambda: browser), "find_element_by_class_name"), 'regular_login')
    _l_(335538)
    email = _c_(335541, _a_(335540, _n_(335539, "form", lambda: form), "find_element_by_name"), "email")
    _l_(335542)
    password = _c_(335545, _a_(335544, _n_(335543, "form", lambda: form), "find_element_by_name"), "password")
    _l_(335546)
    button_element = _c_(335549, _a_(335548, _n_(335547, "browser", lambda: browser), "find_element_by_xpath"), "//*[@value='Login']")
    _l_(335550)
    _c_(335554, _a_(335552, _n_(335551, "email", lambda: email), "send_keys"), _n_(335553, "username", lambda: username))
    _l_(335555)
    _c_(335559, _a_(335557, _n_(335556, "password", lambda: password), "send_keys"), _n_(335558, "password", lambda: password))
    _l_(335560)


with _c_(335563, _n_(335562, "open", lambda: open), 'newfile.txt') as u:
    _l_(335568)

    for line in _n_(335564, "u", lambda: u):
        _l_(335567)

        rr = _n_(335565, "line", lambda: line)
        _l_(335566)


with _c_(335570, _n_(335569, "open", lambda: open), 'password.txt') as p:
    _l_(335575)

    for linee in _n_(335571, "p", lambda: p):
        _l_(335574)

        pp = _n_(335572, "linee", lambda: linee)
        _l_(335573)

_c_(335577, _n_(335576, "Quora_bot", lambda: Quora_bot))
_l_(335578)
username = _n_(335579, "rr", lambda: rr)
_l_(335580)
password = _n_(335581, "pp", lambda: pp)
_l_(335582)