# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58340342/pandas-groupby-typeerror-not-supported-between-instances-of-seriesgroupby
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
group = _c_(398235, _a_(398234, _n_(398233, "df", lambda: df), "groupby"), ['Id',  'Name'])
_l_(398236)
conditions = [
    ((_n_(398237, "group", lambda: group)["Balance"]>0) & (_n_(398238, "group", lambda: group)['Value']>0) & (_n_(398239, "group", lambda: group)['L_Date']<=_n_(398240, "group", lambda: group)['c_date'])),
    ((_n_(398241, "group", lambda: group)["Balance"]==0) & (_n_(398242, "group", lambda: group)['Value']==0) & (_n_(398243, "group", lambda: group)['L_Date']<=_n_(398244, "group", lambda: group)['c_date']))]
_l_(398245)
choices = ['Good', 'Bad']
_l_(398246)
_n_(398247, "df", lambda: df)['outcome'] = _c_(398252, _a_(398249, _n_(398248, "np", lambda: np), "select"), _n_(398250, "conditions", lambda: conditions), _n_(398251, "choices", lambda: choices), default='Normal')
_l_(398253)