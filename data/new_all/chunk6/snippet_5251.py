# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/37044191/nameerror-name-var-not-defined-in-if-statement
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
for index, row in _c_(361239, _a_(361238, _n_(361237, "dfcodes", lambda: dfcodes), "iterrows")):
    _l_(361322)

    # for each security code identify those with 3 down candles and narrowing raneg for first 3 days of 6 day set
    scode=_n_(361240, "row", lambda: row)['Security_Code']
    _l_(361241)

    tdate='2016-01-15'
    _l_(361242)
    df=_c_(361246, _n_(361243, "fetch_last", lambda: fetch_last), _n_(361244, "scode", lambda: scode),_n_(361245, "tdate", lambda: tdate),6)
    _l_(361247)
    dfreverse=_c_(361250, _a_(361249, _n_(361248, "df", lambda: df), "sort"), 'TradeDate', ascending=True)
    _l_(361251)

    #look for 3 consecutive down candles with narrowing range and then 2 up candles
    dfdownbars=_c_(361254, _a_(361253, _n_(361252, "dfreverse", lambda: dfreverse), "head"), 5)
    _l_(361255)
    ncnt=1
    _l_(361256)

    for index,row in _c_(361259, _a_(361258, _n_(361257, "dfdownbars", lambda: dfdownbars), "iterrows")):
        _l_(361321)

        otmp = _n_(361260, "row", lambda: row)['Opening_Price']
        _l_(361261)
        ctmp = _n_(361262, "row", lambda: row)['Closing_Price']
        _l_(361263)
        rtmp = _c_(361267, _n_(361264, "abs", lambda: abs), _n_(361265, "row", lambda: row)['Opening_Price'] - _n_(361266, "row", lambda: row)['Closing_Price'])
        _l_(361268)
        dtmp = _n_(361269, "row", lambda: row)['TradeDate']
        _l_(361270)
        if _n_(361271, "ctmp", lambda: ctmp)<_n_(361272, "otmp", lambda: otmp) and _n_(361273, "ncnt", lambda: ncnt)==1:
            _l_(361320)

            o1 = _n_(361274, "otmp", lambda: otmp)
            _l_(361275)
            c1 = _n_(361276, "ctmp", lambda: ctmp)
            _l_(361277)
            r1 = _n_(361278, "rtmp", lambda: rtmp)
            _l_(361279)
            d1 = _n_(361280, "dtmp", lambda: dtmp)
            _l_(361281)
            ncnt+=1
            _l_(361282)
        elif _n_(361283, "ctmp", lambda: ctmp)<_n_(361284, "otmp", lambda: otmp) and _n_(361285, "otmp", lambda: otmp)<_n_(361286, "o1", lambda: o1) and _n_(361287, "ctmp", lambda: ctmp)<_n_(361288, "c1", lambda: c1) and _n_(361289, "rtmp", lambda: rtmp)<=_n_(361290, "r1", lambda: r1) and _n_(361291, "ncnt", lambda: ncnt)==2:
            _l_(361319)

            o2 = _n_(361292, "otmp", lambda: otmp)
            _l_(361293)
            c2 = _n_(361294, "ctmp", lambda: ctmp)
            _l_(361295)
            r2 = _n_(361296, "rtmp", lambda: rtmp)
            _l_(361297)
            d2 = _n_(361298, "dtmp", lambda: dtmp)
            _l_(361299)
            ncnt += 1
            _l_(361300)
        elif _n_(361301, "ctmp", lambda: ctmp)<_n_(361302, "otmp", lambda: otmp) and _n_(361303, "otmp", lambda: otmp)<_n_(361304, "o2", lambda: o2) and _n_(361305, "rtmp", lambda: rtmp)<=_n_(361306, "r2", lambda: r2) and _n_(361307, "ncnt", lambda: ncnt)==3:
            _l_(361318)

            o3 = _n_(361308, "otmp", lambda: otmp)
            _l_(361309)
            c3 = _n_(361310, "ctmp", lambda: ctmp)
            _l_(361311)
            r3 = _n_(361312, "rtmp", lambda: rtmp)
            _l_(361313)
            d3 = _n_(361314, "dtmp", lambda: dtmp)
            _l_(361315)
            ncnt += 1
            _l_(361316)
        else:
            break
            _l_(361317)