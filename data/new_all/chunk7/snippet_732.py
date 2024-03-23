# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/70434952/attributeerror-str-object-has-no-attribute-descendants-error-with-automati
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
PATH = (r"C:\Users\gustavo.vieira\Desktop\python\drivers\msedgedriver.exe")
_l_(393033)
funds_list = ['VINLAND MACRO MASTER FUNDO DE INVESTIMENTO MULTIMERCADO']
_l_(393034)
url = 'https://cvmweb.cvm.gov.br/SWB/Sistemas/SCW/CPublica/CConsolFdo/FormBuscaParticFdo.aspx'
_l_(393035)


for i in _n_(393036, "funds_lista", lambda: funds_lista):
    _l_(393087)

    driver = _c_(393040, _a_(393038, _n_(393037, "webdriver", lambda: webdriver), "Edge"), _n_(393039, "PATH", lambda: PATH))
    _l_(393041)
    _c_(393045, _a_(393043, _n_(393042, "driver", lambda: driver), "get"), _n_(393044, "url", lambda: url))
    _l_(393046)
    search = _c_(393049, _a_(393048, _n_(393047, "driver", lambda: driver), "find_element_by_name"), "txtCNPJNome")
    _l_(393050)
    _c_(393054, _a_(393052, _n_(393051, "search", lambda: search), "send_keys"), _n_(393053, "i", lambda: i))
    _l_(393055)
    _c_(393060, _a_(393057, _n_(393056, "search", lambda: search), "send_keys"), _a_(393059, _n_(393058, "Keys", lambda: Keys), "RETURN"))
    _l_(393061)
    _c_(393067, _a_(393066, _c_(393065, _a_(393063, _n_(393062, "driver", lambda: driver), "find_element_by_link_text"), _n_(393064, "i", lambda: i)), "click"))
    _l_(393068)
    font = _c_(393073, _a_(393072, _c_(393071, _a_(393070, _n_(393069, "driver", lambda: driver), "find_element_by_link_text"), 'Composição da Carteira'), "click"))
    _l_(393074)
    soup = _c_(393077, _n_(393075, "BeautifulSoup", lambda: BeautifulSoup), _n_(393076, "font", lambda: font))
    _l_(393078)
    rows = _c_(393081, _a_(393080, _n_(393079, "soup", lambda: soup), "find_all"), "tr")
    _l_(393082)
    _c_(393085, _n_(393083, "print", lambda: print), _n_(393084, "rows", lambda: rows))
    _l_(393086)