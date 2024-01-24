# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/77393069/python-attributeerror-webdriver-object-has-no-attribute-launch-app
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pytest
    _l_(609775)

except ImportError:
    pass
try:
    import allure
    _l_(609777)

except ImportError:
    pass
try:
    from allure_commons.types import AttachmentType
    _l_(609779)

except ImportError:
    pass
try:
    from appium import webdriver
    _l_(609781)

except ImportError:
    pass
try:
    from appium.webdriver.common.appiumby import AppiumBy
    _l_(609783)

except ImportError:
    pass
try:
    from appium.options.android import UiAutomator2Options
    _l_(609785)

except ImportError:
    pass

appium_server = "http://localhost:4723/wd/hub"
_l_(609786)

desired_cap = {

    # Emulator - Android
    "deviceName": "Nexus 4 API 30",
    "platformName": "Android",
    "platformVersion": "11.0",
    "udid": "emulator-5554",
    "appPackage": "com.epf.mip.uat",
    "appActivity": "com.epf.mip.uat.MainActivity"
}
_l_(609787)

# Converts capabilities to AppiumOptions instance
capabilities_options = _c_(609792, _a_(609790, _c_(609789, _n_(609788, "UiAutomator2Options", lambda: UiAutomator2Options)), "load_capabilities"), _n_(609791, "desired_cap", lambda: desired_cap))
_l_(609793)

@_c_(609796, _a_(609795, _n_(609794, "pytest", lambda: pytest), "hookimpl"), hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    _l_(609811)

    outcome = yield
    _l_(609797)
    rep = _c_(609800, _a_(609799, _n_(609798, "outcome", lambda: outcome), "get_result"))
    _l_(609801)
    _c_(609807, _n_(609802, "setattr", lambda: setattr), _n_(609803, "item", lambda: item), "rep_" + _a_(609805, _n_(609804, "rep", lambda: rep), "when"), _n_(609806, "rep", lambda: rep))
    _l_(609808)
    aux = _n_(609809, "rep", lambda: rep)
    _l_(609810)
    return aux


@_c_(609814, _a_(609813, _n_(609812, "pytest", lambda: pytest), "fixture"))
def appium_android_driver(request):
    _l_(609844)

    _c_(609816, _n_(609815, "print", lambda: print), "Initializing Appium Android Driver")
    _l_(609817)
    driver = _c_(609822, _a_(609819, _n_(609818, "webdriver", lambda: webdriver), "Remote"), command_executor=_n_(609820, "appium_server", lambda: appium_server), options=_n_(609821, "capabilities_options", lambda: capabilities_options))
    _l_(609823)

    yield _n_(609824, "driver", lambda: driver)
    _l_(609825)

    if _a_(609829, _a_(609828, _a_(609827, _n_(609826, "request", lambda: request), "node"), "rep_call"), "failed"):
        _l_(609839)

        _c_(609837, _a_(609831, _n_(609830, "allure", lambda: allure), "attach"), _c_(609834, _a_(609833, _n_(609832, "driver", lambda: driver), "get_screenshot_as_png")), name="Screen Before Error",  attachment_type=_a_(609836, _n_(609835, "AttachmentType", lambda: AttachmentType), "PNG"))
        _l_(609838)

    _c_(609842, _a_(609841, _n_(609840, "driver", lambda: driver), "quit"))
    _l_(609843)