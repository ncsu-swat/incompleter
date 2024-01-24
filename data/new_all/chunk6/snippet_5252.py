# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/37044191/nameerror-name-var-not-defined-in-if-statement
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
for index, row in _c_(357327, _a_(357326, _n_(357325, "dfcodes", lambda: dfcodes), "iterrows")):
    _l_(357424)

    # for each security code identify those with 3 down candles and narrowing raneg for first 3 days of 6 day set
    scode=_n_(357328, "row", lambda: row)['Security_Code']
    _l_(357329)

    tdate='2016-01-15'
    _l_(357330)
    df=_c_(357334, _n_(357331, "fetch_last", lambda: fetch_last), _n_(357332, "scode", lambda: scode),_n_(357333, "tdate", lambda: tdate),6)
    _l_(357335)
    dfreverse=_c_(357338, _a_(357337, _n_(357336, "df", lambda: df), "sort"), 'TradeDate', ascending=True)
    _l_(357339)

    #look for 3 consecutive down candles with narrowing range and then 2 up candles
    dfdownbars=_c_(357342, _a_(357341, _n_(357340, "dfreverse", lambda: dfreverse), "head"), 5)
    _l_(357343)
    ncnt=1
    _l_(357344)

    for index,row in _c_(357347, _a_(357346, _n_(357345, "dfdownbars", lambda: dfdownbars), "iterrows")):
        _l_(357422)

        otmp = _n_(357348, "row", lambda: row)['Opening_Price']
        _l_(357349)
        ctmp = _n_(357350, "row", lambda: row)['Closing_Price']
        _l_(357351)
        rtmp = _c_(357355, _n_(357352, "abs", lambda: abs), _n_(357353, "row", lambda: row)['Opening_Price'] - _n_(357354, "row", lambda: row)['Closing_Price'])
        _l_(357356)
        dtmp = _n_(357357, "row", lambda: row)['TradeDate']
        _l_(357358)
        if _n_(357359, "ctmp", lambda: ctmp)<_n_(357360, "otmp", lambda: otmp) and _n_(357361, "ncnt", lambda: ncnt)==1:
            _l_(357421)

            o1 = _n_(357362, "otmp", lambda: otmp)
            _l_(357363)
            c1 = _n_(357364, "ctmp", lambda: ctmp)
            _l_(357365)
            r1 = _n_(357366, "rtmp", lambda: rtmp)
            _l_(357367)
            d1 = _n_(357368, "dtmp", lambda: dtmp)
            _l_(357369)
            ncnt+=1
            _l_(357370)
        elif _n_(357371, "ctmp", lambda: ctmp)<_n_(357372, "otmp", lambda: otmp) and _n_(357373, "otmp", lambda: otmp)<_n_(357374, "o1", lambda: o1) and _n_(357375, "ctmp", lambda: ctmp)<_n_(357376, "c1", lambda: c1) and _n_(357377, "rtmp", lambda: rtmp)<=_n_(357378, "r1", lambda: r1) and _n_(357379, "ncnt", lambda: ncnt)==2:
            _l_(357420)

            o2 = _n_(357380, "otmp", lambda: otmp)
            _l_(357381)
            c2 = _n_(357382, "ctmp", lambda: ctmp)
            _l_(357383)
            r2 = _n_(357384, "rtmp", lambda: rtmp)
            _l_(357385)
            d2 = _n_(357386, "dtmp", lambda: dtmp)
            _l_(357387)
            ncnt += 1
            _l_(357388)
        elif _n_(357389, "ctmp", lambda: ctmp)<_n_(357390, "otmp", lambda: otmp) and _n_(357391, "otmp", lambda: otmp)<_n_(357392, "o2", lambda: o2) and _n_(357393, "rtmp", lambda: rtmp)<=_n_(357394, "r2", lambda: r2) and _n_(357395, "ncnt", lambda: ncnt)==3:
            _l_(357419)

            o3 = _n_(357396, "otmp", lambda: otmp)
            _l_(357397)
            c3 = _n_(357398, "ctmp", lambda: ctmp)
            _l_(357399)
            r3 = _n_(357400, "rtmp", lambda: rtmp)
            _l_(357401)
            d3 = _n_(357402, "dtmp", lambda: dtmp)
            _l_(357403)
            ncnt += 1
            _l_(357404)
        elif _n_(357405, "ctmp", lambda: ctmp) > _n_(357406, "otmp", lambda: otmp) and _n_(357407, "ctmp", lambda: ctmp) > _n_(357408, "c3", lambda: c3) and _n_(357409, "ncnt", lambda: ncnt)==4:
            _l_(357418)

            o4 = _n_(357410, "otmp", lambda: otmp)
            _l_(357411)
            c4 = _n_(357412, "ctmp", lambda: ctmp)
            _l_(357413)
            r4 = _n_(357414, "rtmp", lambda: rtmp)
            _l_(357415)
            ncnt += 1
            _l_(357416)
        else:
            break
            _l_(357417)

    cnt -= 1
    _l_(357423)