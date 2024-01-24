# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56621969/attribute-error-with-list-of-stock-tickers
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
file = 'techtickerlist.csv'
_l_(458561)
with _c_(458564, _n_(458562, "open", lambda: open), _n_(458563, "file", lambda: file)) as f:
    _l_(458578)

    reader = _c_(458568, _a_(458566, _n_(458565, "csv", lambda: csv), "reader"), _n_(458567, "f", lambda: f))
    _l_(458569)
    technologyTickers = []
    _l_(458570)
    for row in _n_(458571, "reader", lambda: reader):
        _l_(458577)

        _c_(458575, _a_(458573, _n_(458572, "technologyTickers", lambda: technologyTickers), "append"), _n_(458574, "row", lambda: row)[0])
        _l_(458576)

def scrape(stock_list, interested, technicals):
    _l_(458664)

    SuggestedStocks = []
    _l_(458579)
    for each_stock in _n_(458580, "stock_list", lambda: stock_list):
        _l_(458659)

        try:
            _l_(458658)

            technicals = _c_(458583, _n_(458581, "scrape_yahoo", lambda: scrape_yahoo), _n_(458582, "each_stock", lambda: each_stock))
            _l_(458584)
            condition_1 = _c_(458595, _n_(458585, "float", lambda: float), _c_(458594, _a_(458593, _c_(458592, _a_(458591, _c_(458590, _a_(458589, _c_(458588, _a_(458587, _n_(458586, "technicals", lambda: technicals), "get"), 'Return on Equity',0), "replace"), '%',''), "replace"), 'N/A','-100'), "replace"), ',','')) > 25
            _l_(458596)
            condition_2 = _c_(458605, _n_(458597, "float", lambda: float), _c_(458604, _a_(458603, _c_(458602, _a_(458601, _c_(458600, _a_(458599, _n_(458598, "technicals", lambda: technicals), "get"), 'Trailing P/E',0), "replace"), 'N/A','0'), "replace"), ',','')) < 25
            _l_(458606)
            condition_3 = _c_(458613, _n_(458607, "float", lambda: float), _c_(458612, _a_(458611, _c_(458610, _a_(458609, _n_(458608, "technicals", lambda: technicals), "get"), 'Price/Book',0), "replace"), 'N/A','100')) <8
            _l_(458614)
            condition_4 = _c_(458621, _n_(458615, "float", lambda: float), _c_(458620, _a_(458619, _c_(458618, _a_(458617, _n_(458616, "technicals", lambda: technicals), "get"), 'Beta (3Y Monthly)',0), "replace"), 'N/A','100')) <1.1
            _l_(458622)
            if _n_(458623, "condition_1", lambda: condition_1) and _n_(458624, "condition_2", lambda: condition_2) and _n_(458625, "condition_3", lambda: condition_3) and _n_(458626, "condition_4", lambda: condition_4):
                _l_(458651)

                _c_(458629, _n_(458627, "print", lambda: print), _n_(458628, "each_stock", lambda: each_stock))
                _l_(458630)
                _c_(458634, _a_(458632, _n_(458631, "SuggestedStocks", lambda: SuggestedStocks), "append"), _n_(458633, "each_stock", lambda: each_stock))  
                _l_(458635)  
                for ind in _n_(458636, "interested", lambda: interested):
                    _l_(458643)

                    _c_(458641, _n_(458637, "print", lambda: print), _n_(458638, "ind", lambda: ind) + ": "+ _n_(458639, "technicals", lambda: technicals)[_n_(458640, "ind", lambda: ind)])         
                    _l_(458642)         
                _c_(458645, _n_(458644, "print", lambda: print), "------")
                _l_(458646)
                _c_(458649, _a_(458648, _n_(458647, "time", lambda: time), "sleep"), 1)   
                _l_(458650)   
        except _n_(458652, "ValueError", lambda: ValueError):
            _l_(458657)

            _c_(458654, _n_(458653, "print", lambda: print), 'Value Error')
            _l_(458655)
            aux = ""
            _l_(458656)
            return aux
    #return technicals
    _c_(458662, _n_(458660, "print", lambda: print), _n_(458661, "SuggestedStocks", lambda: SuggestedStocks))
    _l_(458663)


def main():
    _l_(458679)


    stock_list = _n_(458665, "technologyTickers", lambda: technologyTickers)
    _l_(458666)
    interested = ['Return on Equity', 'Revenue', 'Quarterly Revenue Growth','Trailing P/E', 'Beta (3Y Monthly)','Price/Book']
    _l_(458667)
    technicals = {}
    _l_(458668)

    tech = _c_(458673, _n_(458669, "scrape", lambda: scrape), _n_(458670, "stock_list", lambda: stock_list), _n_(458671, "interested", lambda: interested), _n_(458672, "technicals", lambda: technicals))
    _l_(458674)
    _c_(458677, _n_(458675, "print", lambda: print), _n_(458676, "tech", lambda: tech))
    _l_(458678)