# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/50603012/python-attributeerror-nonetype-object-has-no-attribute-execute
## Third party Library Imports
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
  import pandas as pd
  _l_(572876)

except ImportError:
  pass
try:
  import psycopg2
  _l_(572878)

except ImportError:
  pass
try:
  import airflow
  _l_(572880)

except ImportError:
  pass
try:
  from airflow import DAG
  _l_(572882)

except ImportError:
  pass
try:
  from airflow.operators.python_operator import PythonOperator
  _l_(572884)

except ImportError:
  pass
try:
  from airflow.operators.bash_operator import BashOperator
  _l_(572886)

except ImportError:
  pass
try:
  from datetime import datetime, timedelta
  _l_(572888)

except ImportError:
  pass
try:
  from sqlalchemy import create_engine
  _l_(572890)

except ImportError:
  pass
try:
  import io
  _l_(572892)

except ImportError:
  pass

# Following are defaults which can be overridden later on
default_args = {
'owner': 'airflow',
'depends_on_past': False,
'start_date': _c_(572894, _n_(572893, "datetime", lambda: datetime), 2018, 5, 29, 12),
'email': ['airflow@airflow.com']
}
_l_(572895)

dag = _c_(572898, _n_(572896, "DAG", lambda: DAG), 'sample1', default_args=_n_(572897, "default_args", lambda: default_args))
_l_(572899)

## Login to DB

def db_log(**kwargs):
  _l_(572921)

  global db_con
  _l_(572900)
  try:
    _l_(572920)

    db_con = _c_(572903, _a_(572902, _n_(572901, "psycopg2", lambda: psycopg2), "connect"), " dbname = 'name' user = 'user' password = 'pass' host = 'host' port = '5439'")
    _l_(572904)
  except:
    _l_(572919)

    _c_(572906, _n_(572905, "print", lambda: print), "I am unable to connect")
    _l_(572907)
    _c_(572909, _n_(572908, "print", lambda: print), 'Connection Task Complete')
    _l_(572910)
    task_instance = _n_(572911, "kwargs", lambda: kwargs)['task_instance']
    _l_(572912)
    _c_(572915, _a_(572914, _n_(572913, "task_instance", lambda: task_instance), "xcom_push"), key="dwh_connection" , value = "dwh_connection")
    _l_(572916)
    aux = _n_(572917, "dwh_connection", lambda: (dwh_connection))
    _l_(572918)
    return aux



t1 = _c_(572925, _n_(572922, "PythonOperator", lambda: PythonOperator), task_id='DWH_Connect',
  python_callable=_n_(572923, "data_warehouse_login", lambda: data_warehouse_login),provide_context=True,
  dag=_n_(572924, "dag", lambda: dag))
_l_(572926)

#######################

def insert_data(**kwargs):
  _l_(572939)

  task_instance = _n_(572927, "kwargs", lambda: kwargs)['task_instance']
  _l_(572928)
  db_con_xcom = _c_(572931, _a_(572930, _n_(572929, "task_instance", lambda: task_instance), "xcom_pull"), key="dwh_connection", task_ids='DWH_Connect')
  _l_(572932)
  cur = _n_(572933, "db_con_xcom", lambda: db_con_xcom)
  _l_(572934)
  _c_(572937, _a_(572936, _n_(572935, "cur", lambda: cur), "execute"), """insert into tbl_1 select limit 2 """)
  _l_(572938)


##########################################

t2 = _c_(572943, _n_(572940, "PythonOperator", lambda: PythonOperator), task_id='DWH_Connect1',
  python_callable=_n_(572941, "insert_data", lambda: insert_data),provide_context=True,dag=_n_(572942, "dag", lambda: dag))
_l_(572944)

_n_(572945, "t1", lambda: t1) >> _n_(572946, "t2", lambda: t2)
_l_(572947)