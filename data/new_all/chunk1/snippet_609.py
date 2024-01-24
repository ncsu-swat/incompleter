# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/69766838/scheduling-airflow-taskgroup-throws-attributeerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def get_task_group(dag, task_group):
    _l_(382475)

    t1 = _c_(382439, _n_(382436, "DummyOperator", lambda: DummyOperator), task_id='t1', dag=_n_(382437, "dag", lambda: dag), task_group=_n_(382438, "task_group", lambda: task_group))
    _l_(382440)
    t2 = _c_(382444, _n_(382441, "DummyOperator", lambda: DummyOperator), task_id='t2', dag=_n_(382442, "dag", lambda: dag), task_group=_n_(382443, "task_group", lambda: task_group))
    _l_(382445)
    t3 = _c_(382449, _n_(382446, "DummyOperator", lambda: DummyOperator), task_id='t3', dag=_n_(382447, "dag", lambda: dag), task_group=_n_(382448, "task_group", lambda: task_group))
    _l_(382450)
    t4 = _c_(382454, _n_(382451, "DummyOperator", lambda: DummyOperator), task_id='t4', dag=_n_(382452, "dag", lambda: dag), task_group=_n_(382453, "task_group", lambda: task_group))
    _l_(382455)
    t5 = _c_(382459, _n_(382456, "DummyOperator", lambda: DummyOperator), task_id='t5', dag=_n_(382457, "dag", lambda: dag), task_group=_n_(382458, "task_group", lambda: task_group))
    _l_(382460)
    t_list = [_n_(382461, "t2", lambda: t2), _n_(382462, "t3", lambda: t3), _n_(382463, "t4", lambda: t4)]
    _l_(382464)
    _c_(382468, _a_(382466, _n_(382465, "t1", lambda: t1), "set_downstream"), _n_(382467, "t_list", lambda: t_list))
    _l_(382469)
    _c_(382473, _a_(382471, _n_(382470, "t5", lambda: t5), "set_upstream"), _n_(382472, "t_list", lambda: t_list))
    _l_(382474)


with _c_(382478, _n_(382476, "DAG", lambda: DAG), 'some_dag', default_args=_n_(382477, "args", lambda: args)) as dag:
    _l_(382524)

    with _c_(382481, _n_(382479, "TaskGroup", lambda: TaskGroup), group_id=f"run_model_tasks", dag=_n_(382480, "dag", lambda: dag)) as tg:
        _l_(382487)

        run_model_task_group = _c_(382485, _n_(382482, "get_task_group", lambda: get_task_group), _n_(382483, "dag", lambda: dag), _n_(382484, "tg", lambda: tg))
        _l_(382486)

    a1 = _c_(382490, _n_(382488, "DummyOperator", lambda: DummyOperator), task_id='a1', dag=_n_(382489, "dag", lambda: dag))
    _l_(382491)
    a2 = _c_(382494, _n_(382492, "DummyOperator", lambda: DummyOperator), task_id='a2', dag=_n_(382493, "dag", lambda: dag))
    _l_(382495)
    a3 = _c_(382498, _n_(382496, "DummyOperator", lambda: DummyOperator), task_id='a3', dag=_n_(382497, "dag", lambda: dag))
    _l_(382499)
    a4 = _c_(382502, _n_(382500, "DummyOperator", lambda: DummyOperator), task_id='a4', dag=_n_(382501, "dag", lambda: dag))
    _l_(382503)

    _c_(382507, _a_(382505, _n_(382504, "a1", lambda: a1), "set_downstream"), _n_(382506, "a2", lambda: a2))
    _l_(382508)
    _c_(382512, _a_(382510, _n_(382509, "a2", lambda: a2), "set_downstream"), _n_(382511, "run_model_task_group", lambda: run_model_task_group))
    _l_(382513)
    _c_(382517, _a_(382515, _n_(382514, "a3", lambda: a3), "set_upstream"), _n_(382516, "run_model_task_group", lambda: run_model_task_group))
    _l_(382518)
    _c_(382522, _a_(382520, _n_(382519, "a3", lambda: a3), "set_downstream"), _n_(382521, "a4", lambda: a4))
    _l_(382523)