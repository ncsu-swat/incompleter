# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/37044191/nameerror-name-var-not-defined-in-if-statement
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
for index, row in _c_(359316, _a_(359315, _n_(359314, "dfcodes", lambda: dfcodes), "iterrows")):
    _l_(359413)

    # for each security code identify those with 3 down candles and narrowing raneg for first 3 days of 6 day set
    scode=_n_(359317, "row", lambda: row)['Security_Code']
    _l_(359318)

    tdate='2016-01-15'
    _l_(359319)
    df=_c_(359323, _n_(359320, "fetch_last", lambda: fetch_last), _n_(359321, "scode", lambda: scode),_n_(359322, "tdate", lambda: tdate),6)
    _l_(359324)
    dfreverse=_c_(359327, _a_(359326, _n_(359325, "df", lambda: df), "sort"), 'TradeDate', ascending=True)
    _l_(359328)

    #look for 3 consecutive down candles with narrowing range and then 2 up candles
    dfdownbars=_c_(359331, _a_(359330, _n_(359329, "dfreverse", lambda: dfreverse), "head"), 5)
    _l_(359332)
    ncnt=1
    _l_(359333)

    for index,row in _c_(359336, _a_(359335, _n_(359334, "dfdownbars", lambda: dfdownbars), "iterrows")):
        _l_(359411)

        otmp = _n_(359337, "row", lambda: row)['Opening_Price']
        _l_(359338)
        ctmp = _n_(359339, "row", lambda: row)['Closing_Price']
        _l_(359340)
        rtmp = _c_(359344, _n_(359341, "abs", lambda: abs), _n_(359342, "row", lambda: row)['Opening_Price'] - _n_(359343, "row", lambda: row)['Closing_Price'])
        _l_(359345)
        dtmp = _n_(359346, "row", lambda: row)['TradeDate']
        _l_(359347)
        if _n_(359348, "ctmp", lambda: ctmp)<_n_(359349, "otmp", lambda: otmp) and _n_(359350, "ncnt", lambda: ncnt)==1:
            _l_(359410)

            o1 = _n_(359351, "otmp", lambda: otmp)
            _l_(359352)
            c1 = _n_(359353, "ctmp", lambda: ctmp)
            _l_(359354)
            r1 = _n_(359355, "rtmp", lambda: rtmp)
            _l_(359356)
            d1 = _n_(359357, "dtmp", lambda: dtmp)
            _l_(359358)
            ncnt+=1
            _l_(359359)
        elif _n_(359360, "ctmp", lambda: ctmp)<_n_(359361, "otmp", lambda: otmp) and _n_(359362, "otmp", lambda: otmp)<_n_(359363, "o1", lambda: o1) and _n_(359364, "ctmp", lambda: ctmp)<_n_(359365, "c1", lambda: c1) and _n_(359366, "rtmp", lambda: rtmp)<=_n_(359367, "r1", lambda: r1) and _n_(359368, "ncnt", lambda: ncnt)==2:
            _l_(359409)

            o2 = _n_(359369, "otmp", lambda: otmp)
            _l_(359370)
            c2 = _n_(359371, "ctmp", lambda: ctmp)
            _l_(359372)
            r2 = _n_(359373, "rtmp", lambda: rtmp)
            _l_(359374)
            d2 = _n_(359375, "dtmp", lambda: dtmp)
            _l_(359376)
            ncnt += 1
            _l_(359377)
        elif _n_(359378, "ctmp", lambda: ctmp)<_n_(359379, "otmp", lambda: otmp) and _n_(359380, "otmp", lambda: otmp)<_n_(359381, "o2", lambda: o2) and _n_(359382, "rtmp", lambda: rtmp)<=_n_(359383, "r2", lambda: r2) and _n_(359384, "ncnt", lambda: ncnt)==3:
            _l_(359408)

            o3 = _n_(359385, "otmp", lambda: otmp)
            _l_(359386)
            c3 = _n_(359387, "ctmp", lambda: ctmp)
            _l_(359388)
            r3 = _n_(359389, "rtmp", lambda: rtmp)
            _l_(359390)
            d3 = _n_(359391, "dtmp", lambda: dtmp)
            _l_(359392)
            ncnt += 1
            _l_(359393)
        elif _n_(359394, "ctmp", lambda: ctmp) > _n_(359395, "otmp", lambda: otmp) and _n_(359396, "ctmp", lambda: ctmp) > _n_(359397, "c3", lambda: c3) and _n_(359398, "ncnt", lambda: ncnt)==4:
            _l_(359407)

            o4 = _n_(359399, "otmp", lambda: otmp)
            _l_(359400)
            c4 = _n_(359401, "ctmp", lambda: ctmp)
            _l_(359402)
            r4 = _n_(359403, "rtmp", lambda: rtmp)
            _l_(359404)
            ncnt += 1
            _l_(359405)
        else:
            break
            _l_(359406)

    cnt -= 1
    _l_(359412)