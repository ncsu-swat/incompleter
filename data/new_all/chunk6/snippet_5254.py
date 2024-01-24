# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/37044191/nameerror-name-var-not-defined-in-if-statement
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
for index, row in _c_(366173, _a_(366172, _n_(366171, "dfcodes", lambda: dfcodes), "iterrows")):
    _l_(366256)

    # for each security code identify those with 3 down candles and narrowing raneg for first 3 days of 6 day set
    scode=_n_(366174, "row", lambda: row)['Security_Code']
    _l_(366175)

    tdate='2016-01-15'
    _l_(366176)
    df=_c_(366180, _n_(366177, "fetch_last", lambda: fetch_last), _n_(366178, "scode", lambda: scode),_n_(366179, "tdate", lambda: tdate),6)
    _l_(366181)
    dfreverse=_c_(366184, _a_(366183, _n_(366182, "df", lambda: df), "sort"), 'TradeDate', ascending=True)
    _l_(366185)

    #look for 3 consecutive down candles with narrowing range and then 2 up candles
    dfdownbars=_c_(366188, _a_(366187, _n_(366186, "dfreverse", lambda: dfreverse), "head"), 5)
    _l_(366189)
    ncnt=1
    _l_(366190)

    for index,row in _c_(366193, _a_(366192, _n_(366191, "dfdownbars", lambda: dfdownbars), "iterrows")):
        _l_(366255)

        otmp = _n_(366194, "row", lambda: row)['Opening_Price']
        _l_(366195)
        ctmp = _n_(366196, "row", lambda: row)['Closing_Price']
        _l_(366197)
        rtmp = _c_(366201, _n_(366198, "abs", lambda: abs), _n_(366199, "row", lambda: row)['Opening_Price'] - _n_(366200, "row", lambda: row)['Closing_Price'])
        _l_(366202)
        dtmp = _n_(366203, "row", lambda: row)['TradeDate']
        _l_(366204)
        if _n_(366205, "ctmp", lambda: ctmp)<_n_(366206, "otmp", lambda: otmp) and _n_(366207, "ncnt", lambda: ncnt)==1:
            _l_(366254)

            o1 = _n_(366208, "otmp", lambda: otmp)
            _l_(366209)
            c1 = _n_(366210, "ctmp", lambda: ctmp)
            _l_(366211)
            r1 = _n_(366212, "rtmp", lambda: rtmp)
            _l_(366213)
            d1 = _n_(366214, "dtmp", lambda: dtmp)
            _l_(366215)
            ncnt+=1
            _l_(366216)
        elif _n_(366217, "ctmp", lambda: ctmp)<_n_(366218, "otmp", lambda: otmp) and _n_(366219, "otmp", lambda: otmp)<_n_(366220, "o1", lambda: o1) and _n_(366221, "ctmp", lambda: ctmp)<_n_(366222, "c1", lambda: c1) and _n_(366223, "rtmp", lambda: rtmp)<=_n_(366224, "r1", lambda: r1) and _n_(366225, "ncnt", lambda: ncnt)==2:
            _l_(366253)

            o2 = _n_(366226, "otmp", lambda: otmp)
            _l_(366227)
            c2 = _n_(366228, "ctmp", lambda: ctmp)
            _l_(366229)
            r2 = _n_(366230, "rtmp", lambda: rtmp)
            _l_(366231)
            d2 = _n_(366232, "dtmp", lambda: dtmp)
            _l_(366233)
            ncnt += 1
            _l_(366234)
        elif _n_(366235, "ctmp", lambda: ctmp)<_n_(366236, "otmp", lambda: otmp) and _n_(366237, "otmp", lambda: otmp)<_n_(366238, "o2", lambda: o2) and _n_(366239, "rtmp", lambda: rtmp)<=_n_(366240, "r2", lambda: r2) and _n_(366241, "ncnt", lambda: ncnt)==3:
            _l_(366252)

            o3 = _n_(366242, "otmp", lambda: otmp)
            _l_(366243)
            c3 = _n_(366244, "ctmp", lambda: ctmp)
            _l_(366245)
            r3 = _n_(366246, "rtmp", lambda: rtmp)
            _l_(366247)
            d3 = _n_(366248, "dtmp", lambda: dtmp)
            _l_(366249)
            ncnt += 1
            _l_(366250)
        else:
            break
            _l_(366251)