# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53332704/xcom-pull-returns-a-nameerror-on-ti
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
default_args = {
    'owner': 'me',
    'start_date': _c_(401950, _a_(401949, _n_(401948, "dt", lambda: dt), "datetime"), 2017, 10, 30),
    'retries': 1,
    'retry_delay': _c_(401953, _a_(401952, _n_(401951, "dt", lambda: dt), "timedelta"), minutes=10),
    'provide_context' : True,
}
_l_(401954)



def get_last_date(**kwargs):
    _l_(401960)

    _c_(401957, _a_(401956, _n_(401955, "kwargs", lambda: kwargs)['ti'], "xcom_push"), key='last_date', value='2018-11-15')
    _l_(401958)
    aux = True
    _l_(401959)
    return aux



with _c_(401963, _n_(401961, "DAG", lambda: DAG), 'ga_mysql_dag2',
         default_args=_n_(401962, "default_args", lambda: default_args),
         schedule_interval=None,
         catchup=False,
         ) as dag:
    _l_(401985)


    last_date_task = _c_(401966, _n_(401964, "PythonOperator", lambda: PythonOperator), task_id='last_date_task', python_callable=_n_(401965, "get_last_date", lambda: get_last_date), provide_context=True)
    _l_(401967)

    ga_wh_task = _c_(401980, _n_(401968, "GoogleAnalyticsReportingToMySqlOperator", lambda: GoogleAnalyticsReportingToMySqlOperator), task_id='ga_wh_task', google_analytics_conn_id='google_analytics', key_file=_n_(401969, "key_file", lambda: key_file),\
                                        view_id=_n_(401970, "view_id", lambda: view_id), until=_n_(401971, "until", lambda: until), dimensions=_n_(401972, "dimensions", lambda: dimensions), metrics=_n_(401973, "metrics", lambda: metrics), database=_n_(401974, "database", lambda: database),\
                                        table = _n_(401975, "table", lambda: table), mysql_conn_id = _n_(401976, "mysql_conn_id", lambda: mysql_conn_id),
                                        provide_context=True, since={{_c_(401979, _a_(401978, _n_(401977, "ti", lambda: ti), "xcom_pull"), task_ids="last_date_task", key='last_date')}})
    _l_(401981)
    sleep = _c_(401983, _n_(401982, "BashOperator", lambda: BashOperator), task_id='sleep', bash_command='sleep 10')
    _l_(401984)

# Dependencies
_n_(401986, "last_date_task", lambda: last_date_task) >> _n_(401987, "ga_warehouse_task", lambda: ga_warehouse_task) >> _n_(401988, "sleep", lambda: sleep)
_l_(401989)