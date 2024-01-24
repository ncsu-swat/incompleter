# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/66003120/airflow-2-0-attributeerror-myoperator-object-has-no-attribute-kwargs
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from datetime import timedelta
    _l_(472689)

except ImportError:
    pass
try:
    from airflow import DAG
    _l_(472691)

except ImportError:
    pass
try:
    from airflow.utils.dates import days_ago
    _l_(472693)

except ImportError:
    pass
try:
    from operators.custom import MyOperator
    _l_(472695)

except ImportError:
    pass

args = {
    'owner': 'airflow',
}
_l_(472696)

with _c_(472703, _n_(472697, "DAG", lambda: DAG), dag_id='ex_operator',
    default_args=_n_(472698, "args", lambda: args),
    schedule_interval='0 0 * * *',
    start_date=_c_(472700, _n_(472699, "days_ago", lambda: days_ago), 1),
    dagrun_timeout=_c_(472702, _n_(472701, "timedelta", lambda: timedelta), minutes=60)
) as dag:
    _l_(472707)


    custom_ops = _c_(472705, _n_(472704, "MyOperator", lambda: MyOperator), task_id = 'myop_id',
        name = 'me',
        params = {
            'lib': 'rainy'
        }
    )
    _l_(472706)