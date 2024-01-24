# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/76424247/typeerror-selenium-webdriver-remote-webdriver-webdriver-find-element-argument
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import time
    _l_(583355)

except ImportError:
    pass
try:
    import pytest
    _l_(583357)

except ImportError:
    pass
try:
    from selenium import webdriver
    _l_(583359)

except ImportError:
    pass
try:
    from selenium.webdriver.chrome.service import Service
    _l_(583361)

except ImportError:
    pass
try:
    from selenium.webdriver.common.by import By
    _l_(583363)

except ImportError:
    pass
try:
    from selenium.webdriver.support import expected_conditions as EC
    _l_(583365)

except ImportError:
    pass
try:
    from selenium.webdriver.support.wait import WebDriverWait
    _l_(583367)

except ImportError:
    pass
try:
    from pageObjects.CheckoutPage import CheckoutPage
    _l_(583369)

except ImportError:
    pass
try:
    from pageObjects.ConfirmPage import ConfirmPage
    _l_(583371)

except ImportError:
    pass
try:
    from pageObjects.HomePage import HomePage
    _l_(583373)

except ImportError:
    pass
try:
    from utilities.BaseClass import BaseClass
    _l_(583375)

except ImportError:
    pass


class TestOne(_n_(583376, "BaseClass", lambda: BaseClass)):
    _l_(583494)

    def test_e2e(self):
        _l_(583493)

        homePage = _c_(583380, _n_(583377, "HomePage", lambda: HomePage), _a_(583379, _n_(583378, "self", lambda: self), "driver"))
        _l_(583381)
        _c_(583386, _a_(583385, _c_(583384, _a_(583383, _n_(583382, "homePage", lambda: homePage), "shopItems")), "click"))
        _l_(583387)

        checkoutPage = _c_(583391, _n_(583388, "CheckoutPage", lambda: CheckoutPage), _a_(583390, _n_(583389, "self", lambda: self), "driver"))
        _l_(583392)
        elements = _c_(583395, _a_(583394, _n_(583393, "checkoutPage", lambda: checkoutPage), "getcardTitles"))
        _l_(583396)
        confirmPage = _c_(583400, _n_(583397, "ConfirmPage", lambda: ConfirmPage), _a_(583399, _n_(583398, "self", lambda: self), "driver"))
        _l_(583401)
        i = -1
        _l_(583402)
        for ele in _n_(583403, "elements", lambda: elements):
            _l_(583416)

            i = _n_(583404, "i", lambda: i) + 1
            _l_(583405)
            if _a_(583407, _n_(583406, "ele", lambda: ele), "text") == "Blackberry":
                _l_(583415)

                _c_(583413, _a_(583412, _c_(583410, _a_(583409, _n_(583408, "checkoutPage", lambda: checkoutPage), "getcardFooter"))[_n_(583411, "i", lambda: i)], "click"))
                _l_(583414)
        # self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
        _c_(583421, _a_(583420, _c_(583419, _a_(583418, _n_(583417, "checkoutPage", lambda: checkoutPage), "checkoutButton")), "click"))
        _l_(583422)
        _c_(583425, _a_(583424, _n_(583423, "time", lambda: time), "sleep"), 5)
        _l_(583426)
        # self.driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-success']").click()
        _c_(583431, _a_(583430, _c_(583429, _a_(583428, _n_(583427, "confirmPage", lambda: confirmPage), "checkoutConfirm")), "click"))
        _l_(583432)
        _c_(583440, _a_(583439, _c_(583438, _a_(583435, _a_(583434, _n_(583433, "self", lambda: self), "driver"), "find_element"), _a_(583437, _n_(583436, "By", lambda: By), "ID"), "country"), "send_keys"), "Bangla")
        _l_(583441)
        wait = _c_(583445, _n_(583442, "WebDriverWait", lambda: WebDriverWait), _a_(583444, _n_(583443, "self", lambda: self), "driver"), 10)
        _l_(583446)
        _c_(583454, _a_(583448, _n_(583447, "wait", lambda: wait), "until"), _c_(583453, _a_(583450, _n_(583449, "EC", lambda: EC), "presence_of_element_located"), (_a_(583452, _n_(583451, "By", lambda: By), "CSS_SELECTOR"), "div[class='suggestions'] ul li a")))
        _l_(583455)
        _c_(583463, _a_(583462, _c_(583461, _a_(583458, _a_(583457, _n_(583456, "self", lambda: self), "driver"), "find_element"), _a_(583460, _n_(583459, "By", lambda: By), "CSS_SELECTOR"), "div[class='suggestions'] ul li a"), "click"))
        _l_(583464)
        _c_(583472, _a_(583471, _c_(583470, _a_(583467, _a_(583466, _n_(583465, "self", lambda: self), "driver"), "find_element"), _a_(583469, _n_(583468, "By", lambda: By), "XPATH"), "//label[@for='checkbox2']"), "click"))
        _l_(583473)
        _c_(583481, _a_(583480, _c_(583479, _a_(583476, _a_(583475, _n_(583474, "self", lambda: self), "driver"), "find_element"), _a_(583478, _n_(583477, "By", lambda: By), "XPATH"), "//input[@value='Purchase']"), "click"))
        _l_(583482)
        success = _a_(583489, _c_(583488, _a_(583485, _a_(583484, _n_(583483, "self", lambda: self), "driver"), "find_element"), _a_(583487, _n_(583486, "By", lambda: By), "XPATH"), "//div[@class='alert alert-success alert-dismissible']"), "text")
        _l_(583490)
        assert "Success! Thank you!" in _n_(583491, "success", lambda: success)
        _l_(583492)