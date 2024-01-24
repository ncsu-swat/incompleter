# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/54414067/attributeerror-in-object-has-no-attribute-tohtml-pyqt5
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import sys
    _l_(435716)

except ImportError:
    pass
try:
    import bs4 as bs
    _l_(435718)

except ImportError:
    pass
try:
    from PyQt5.QtCore import QUrl
    _l_(435720)

except ImportError:
    pass
try:
    from PyQt5.QtWidgets import QApplication
    _l_(435722)

except ImportError:
    pass
try:
    from PyQt5.QtWebEngineWidgets import QWebEnginePage, QWebEngineView
    _l_(435724)

except ImportError:
    pass


class Page(_n_(435725, "QWebEngineView", lambda: QWebEngineView)):
    _l_(435768)


    def __init__(self, url):
        _l_(435758)

        _n_(435726, "self", lambda: self).app = _c_(435730, _n_(435727, "QApplication", lambda: QApplication), _a_(435729, _n_(435728, "sys", lambda: sys), "argv"))
        _l_(435731)
        _c_(435735, _a_(435733, _n_(435732, "QWebEnginePage", lambda: QWebEnginePage), "__init__"), _n_(435734, "self", lambda: self))
        _l_(435736)
        _n_(435737, "self", lambda: self).html = ''
        _l_(435738)
        _c_(435744, _a_(435741, _a_(435740, _n_(435739, "self", lambda: self), "loadFinished"), "connect"), _a_(435743, _n_(435742, "self", lambda: self), "_on_load_finished"))
        _l_(435745)
        _c_(435751, _a_(435747, _n_(435746, "self", lambda: self), "load"), _c_(435750, _n_(435748, "QUrl", lambda: QUrl), _n_(435749, "url", lambda: url)))
        _l_(435752)
        _c_(435756, _a_(435755, _a_(435754, _n_(435753, "self", lambda: self), "app"), "exec_"))
        _l_(435757)

    def _on_load_finished(self):
        _l_(435767)

        _c_(435760, _n_(435759, "print", lambda: print), 'Load finished')
        _l_(435761)
        _c_(435765, _a_(435764, _a_(435763, _n_(435762, "self", lambda: self), "app"), "quit"))
        _l_(435766)


def main():
    _l_(435789)

    page = _c_(435772, _a_(435771, _c_(435770, _n_(435769, "Page", lambda: Page), 'https://pythonprogramming.net/parsememcparseface/'), "toHtml"))
    _l_(435773)
    soup = _c_(435778, _a_(435775, _n_(435774, "bs", lambda: bs), "BeautifulSoup"), _a_(435777, _n_(435776, "page", lambda: page), "html"), 'html.parser')
    _l_(435779)
    js_test = _c_(435782, _a_(435781, _n_(435780, "soup", lambda: soup), "find"), 'p', class_='jstest')
    _l_(435783)
    _c_(435787, _n_(435784, "print", lambda: print), _a_(435786, _n_(435785, "js_test", lambda: js_test), "text"))
    _l_(435788)

if _n_(435790, "__name__", lambda: __name__) == '__main__':
    _l_(435793)

_c_(435792, _n_(435791, "main", lambda: main)