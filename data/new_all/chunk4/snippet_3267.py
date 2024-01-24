# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/76424247/typeerror-selenium-webdriver-remote-webdriver-webdriver-find-element-argument
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from selenium.webdriver.common.by import By
    _l_(607233)

except ImportError:
    pass


class CheckoutPage:
    _l_(607271)

    def __init__(self, driver):
        _l_(607237)

        _n_(607234, "self", lambda: self).driver = _n_(607235, "driver", lambda: driver)
        _l_(607236)

    cardTitles = (_a_(607239, _n_(607238, "By", lambda: By), "XPATH"), "//div[@class='card h-100']/div/h4/a")
    _l_(607240)
    cardFooter = (_a_(607242, _n_(607241, "By", lambda: By), "CSS_SELECTOR"), ".card-footer button")
    _l_(607243)
    checkoutButton = (_a_(607245, _n_(607244, "By", lambda: By), "CSS_SELECTOR"), "nav-link btn btn-primary")
    _l_(607246)

    def getcardTitles(self):
        _l_(607254)

        aux = _c_(607252, _a_(607249, _a_(607248, _n_(607247, "self", lambda: self), "driver"), "find_elements"), *_a_(607251, _n_(607250, "CheckoutPage", lambda: CheckoutPage), "cardTitles"))
        _l_(607253)
        return aux

    def getcardFooter(self):
        _l_(607262)

        aux = _c_(607260, _a_(607257, _a_(607256, _n_(607255, "self", lambda: self), "driver"), "find_elements"), *_a_(607259, _n_(607258, "CheckoutPage", lambda: CheckoutPage), "cardFooter"))
        _l_(607261)
        return aux

    def checkoutButton(self):
        _l_(607270)

        aux = _c_(607268, _a_(607265, _a_(607264, _n_(607263, "self", lambda: self), "driver"), "find_element"), *_a_(607267, _n_(607266, "CheckoutPage", lambda: CheckoutPage), "checkoutButton"))
        _l_(607269)
        return aux