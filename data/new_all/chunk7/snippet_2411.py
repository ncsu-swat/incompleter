# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/44884830/typeerror-must-be-str-not-int-in-python-3
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(550779)

except ImportError:
    pass
try:
    import time
    _l_(550781)

except ImportError:
    pass
try:
    import getpass
    _l_(550783)

except ImportError:
    pass
try:
    from selenium import webdriver
    _l_(550785)

except ImportError:
    pass
try:
    from selenium.webdriver.common.keys import Keys
    _l_(550787)

except ImportError:
    pass

while True:
    _l_(550834)

    chromedriver  = 'F:\All  Folders\chromedriver\chrome.exe'
    _l_(550788)

#Uncomment this block if you don't want images to load(makes the procss a little bit faster)
    '''
    chromeOptions = webdriver.ChromeOptions()
    prefs = {"profile.managed_default_content_settings.images":2}
    chromeOptions.add_experimental_option("prefs",prefs)
    browser = webdriver.Chrome(chromedriver, chrome_options=chromeOptions)
    '''
    _l_(550789)

    browser = _c_(550793, _a_(550791, _n_(550790, "webdriver", lambda: webdriver), "Chrome"), _n_(550792, "chromedriver", lambda: chromedriver))
    _l_(550794)
    _c_(550797, _a_(550796, _n_(550795, "browser", lambda: browser), "get"), "http://www.website.com")       # website's home page
    _l_(550798)       # website's home page
    _c_(550801, _a_(550800, _n_(550799, "time", lambda: time), "sleep"), 10)
    _l_(550802)

    # Logging into website
    form = _c_(550805, _a_(550804, _n_(550803, "browser", lambda: browser), "find_element_by_class_name"), 'regular_login')
    _l_(550806)
    email = _c_(550809, _a_(550808, _n_(550807, "form", lambda: form), "find_element_by_name"), "email")
    _l_(550810)
    password = _c_(550813, _a_(550812, _n_(550811, "form", lambda: form), "find_element_by_name"), "password")
    _l_(550814)
    button_element = _c_(550817, _a_(550816, _n_(550815, "browser", lambda: browser), "find_element_by_xpath"), "//*[@value='Login']")
    _l_(550818)

    #List of emails
    email_list = ['na23b9@gmail.com', '25g65b@gmail.si', 'gfdebfk@gmail.jp']
    _l_(550819)
    for emails, emails in _c_(550822, _n_(550820, "enumerate", lambda: enumerate), _n_(550821, "email_list", lambda: email_list)):
        _l_(550833)

        _c_(550826, _a_(550824, _n_(550823, "email", lambda: email), "send_keys"), _n_(550825, "emails", lambda: emails))
        _l_(550827)
        emails = _n_(550828, "emails", lambda: emails) + 1
        _l_(550829)
        _c_(550831, _n_(550830, "print", lambda: print), "success")
        _l_(550832)