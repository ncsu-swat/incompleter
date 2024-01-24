# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/70727382/how-would-i-fix-the-attribute-error-bytes-object-has-no-attribute-encode-d
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
z = _c_(640694, _a_(640693, _c_(640692, _a_(640691, _n_(640690, "priv", lambda: priv), "to_string")), "encode"), 'hex')
_l_(640695)
url = ("https://etherscan.io/address/%s"%_n_(640696, "address", lambda: address))
_l_(640697)

html = _a_(640702, _c_(640701, _a_(640699, _n_(640698, "requests", lambda: requests), "get"), _n_(640700, "url", lambda: url), headers={'User-agent': 'Mozilla/5.0'}), "text")
_l_(640703)
soup = _c_(640706, _n_(640704, "BeautifulSoup", lambda: BeautifulSoup), _n_(640705, "html", lambda: html), "html.parser")
_l_(640707)
table = _c_(640710, _a_(640709, _n_(640708, "soup", lambda: soup), "find"), "div", {"class": "col-md-6"})
_l_(640711)
value = _c_(640719, _a_(640718, _c_(640717, _a_(640716, _a_(640715, _c_(640714, _a_(640713, _n_(640712, "table", lambda: table), "findAll"), 'td')[1], "text"), "split"), ' ')[0], "strip"))
_l_(640720)


dosya3 = _c_(640722, _n_(640721, "open", lambda: open), "eth-adresler.txt", "a")
_l_(640723)
_c_(640734, _a_(640725, _n_(640724, "dosya3", lambda: dosya3), "write"), _c_(640728, _n_(640726, "str", lambda: str), _n_(640727, "i", lambda: i))+" "+"PRV Key = "+_n_(640729, "z", lambda: z)+"  ADR = 0x"+_n_(640730, "address", lambda: address)+" "+_c_(640733, _n_(640731, "str", lambda: str), _n_(640732, "value", lambda: value)) + "\n")
_l_(640735)
_c_(640738, _a_(640737, _n_(640736, "time", lambda: time), "sleep"), 0.2)
_l_(640739)


tp = 1+_c_(640742, _n_(640740, "float", lambda: float), _n_(640741, "value", lambda: value))
_l_(640743)
if _n_(640744, "tp", lambda: tp) > 1:
    _l_(640795)

    _c_(640746, _n_(640745, "print", lambda: print), "--------------------")
    _l_(640747)
    _c_(640749, _n_(640748, "print", lambda: print), "-----BULUNDU--------")
    _l_(640750)
    _c_(640753, _n_(640751, "print", lambda: print), "Private Key     = "+_n_(640752, "z", lambda: z))
    _l_(640754)
    _c_(640757, _n_(640755, "print", lambda: print), "Adres           = 0x"+_n_(640756, "address", lambda: address))
    _l_(640758)
    _c_(640763, _n_(640759, "print", lambda: print), "Ether Miktar    = "+_c_(640762, _n_(640760, "str", lambda: str), _n_(640761, "value", lambda: value)))
    _l_(640764)
    _c_(640766, _n_(640765, "print", lambda: print), "--------------------")
    _l_(640767)

    dosya4=_c_(640769, _n_(640768, "open", lambda: open), "BULUNAN.txt","a")
    _l_(640770)
    _c_(640778, _a_(640772, _n_(640771, "dosya4", lambda: dosya4), "write"), _n_(640773, "z", lambda: z)+" "+"0x"+_n_(640774, "address", lambda: address)+" "+_c_(640777, _n_(640775, "str", lambda: str), _n_(640776, "value", lambda: value))+ "\n")
    _l_(640779)
    _c_(640782, _a_(640781, _n_(640780, "dosya4", lambda: dosya4), "close"))
    _l_(640783)
else:
    _c_(640793, _n_(640784, "print", lambda: print), _c_(640787, _n_(640785, "str", lambda: str), _n_(640786, "i", lambda: i)) + " " + "private key = " + _n_(640788, "z", lambda: z) + " " + "Adress = 0x" + _n_(640789, "address", lambda: address) + "  " + _c_(640792, _n_(640790, "str", lambda: str), _n_(640791, "value", lambda: value)))
    _l_(640794)

i = _n_(640796, "i", lambda: i) + 1
_l_(640797)