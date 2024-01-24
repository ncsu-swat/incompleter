# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62016881/python-flask-sqlalchemy-attributeerror-table-object-has-no-attribute-added
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from datetime import datetime
    _l_(647902)

except ImportError:
    pass
try:
    from TasMar import  db, login_manager
    _l_(647904)

except ImportError:
    pass
try:
    from flask import  current_app
    _l_(647906)

except ImportError:
    pass
try:
    from flask_login import UserMixin
    _l_(647908)

except ImportError:
    pass

@_a_(647910, _n_(647909, "login_manager", lambda: login_manager), "user_loader")
def load_user(user_id):
    _l_(647919)

    aux = _c_(647917, _a_(647913, _a_(647912, _n_(647911, "User", lambda: User), "query"), "get"), _c_(647916, _n_(647914, "int", lambda: int), _n_(647915, "user_id", lambda: user_id)))
    _l_(647918)
    return aux

class User(_a_(647921, _n_(647920, "db", lambda: db), "Model"), _n_(647922, "UserMixin", lambda: UserMixin)):
    _l_(647976)

    __tablename__ = 'tm_user'
    _l_(647923)
    id = _c_(647928, _a_(647925, _n_(647924, "db", lambda: db), "Column"), _a_(647927, _n_(647926, "db", lambda: db), "Integer"), primary_key=True)
    _l_(647929)
    username = _c_(647935, _a_(647931, _n_(647930, "db", lambda: db), "Column"), _c_(647934, _a_(647933, _n_(647932, "db", lambda: db), "String"), 20),unique=True, nullable=False)
    _l_(647936)
    email = _c_(647942, _a_(647938, _n_(647937, "db", lambda: db), "Column"), _c_(647941, _a_(647940, _n_(647939, "db", lambda: db), "String"), 120),unique=True, nullable=False)
    _l_(647943)
    image_file = _c_(647949, _a_(647945, _n_(647944, "db", lambda: db), "Column"), _c_(647948, _a_(647947, _n_(647946, "db", lambda: db), "String"), 20), nullable=False, default='default.jpg')
    _l_(647950)
    password=  _c_(647956, _a_(647952, _n_(647951, "db", lambda: db), "Column"), _c_(647955, _a_(647954, _n_(647953, "db", lambda: db), "String"), 120), nullable=False)
    _l_(647957)

    #foreign keys accessing this table's primary keys
    added = _c_(647960, _a_(647959, _n_(647958, "db", lambda: db), "relationship"), 'Tasks', lazy=True, foreign_keys='tm_task.added_by')
    _l_(647961)
    assigned = _c_(647964, _a_(647963, _n_(647962, "db", lambda: db), "relationship"), 'Tasks', lazy=True, foreign_keys='tm_task.assigned_to')
    _l_(647965)

    def __repr__(self):
        _l_(647975)

        aux = _c_(647973, _a_(647966, "User('{}','{}','{}')", "format"), _a_(647968, _n_(647967, "self", lambda: self), "username"),_a_(647970, _n_(647969, "self", lambda: self), "email"),_a_(647972, _n_(647971, "self", lambda: self), "image_file"))
        _l_(647974)
        return aux


class Tasks(_a_(647978, _n_(647977, "db", lambda: db), "Model")):
    _l_(648085)

    __tablename__ = 'tm_task'
    _l_(647979)
    task_id = _c_(647984, _a_(647981, _n_(647980, "db", lambda: db), "Column"), _a_(647983, _n_(647982, "db", lambda: db), "Integer"), primary_key=True)
    _l_(647985)
    parent_id = _c_(647993, _a_(647987, _n_(647986, "db", lambda: db), "Column"), _a_(647989, _n_(647988, "db", lambda: db), "Integer"), _c_(647992, _a_(647991, _n_(647990, "db", lambda: db), "ForeignKey"), 'tm_task.task_id'),nullable=True)
    _l_(647994)
    descr = _c_(648000, _a_(647996, _n_(647995, "db", lambda: db), "Column"), _c_(647999, _a_(647998, _n_(647997, "db", lambda: db), "String"), 500), nullable=False)
    _l_(648001)
    added_on = _c_(648008, _a_(648003, _n_(648002, "db", lambda: db), "Column"), _a_(648005, _n_(648004, "db", lambda: db), "DateTime"), nullable=False, default=_a_(648007, _n_(648006, "datetime", lambda: datetime), "utcnow"))
    _l_(648009)
    added_by = _c_(648017, _a_(648011, _n_(648010, "db", lambda: db), "Column"), _a_(648013, _n_(648012, "db", lambda: db), "Integer"), _c_(648016, _a_(648015, _n_(648014, "db", lambda: db), "ForeignKey"), 'tm_user.id'),nullable=False)
    _l_(648018)
    assigned_to = _c_(648026, _a_(648020, _n_(648019, "db", lambda: db), "Column"), _a_(648022, _n_(648021, "db", lambda: db), "Integer"), _c_(648025, _a_(648024, _n_(648023, "db", lambda: db), "ForeignKey"), 'tm_user.id'),nullable=False)
    _l_(648027)
    last_updated = _c_(648034, _a_(648029, _n_(648028, "db", lambda: db), "Column"), _a_(648031, _n_(648030, "db", lambda: db), "DateTime"), nullable=False, default=_a_(648033, _n_(648032, "datetime", lambda: datetime), "utcnow"))
    _l_(648035)
    remark = _c_(648040, _a_(648037, _n_(648036, "db", lambda: db), "Column"), _a_(648039, _n_(648038, "db", lambda: db), "Text"))
    _l_(648041)


    parent = _c_(648044, _a_(648043, _n_(648042, "db", lambda: db), "relationship"), 'Tasks', remote_side=[task_id]) #self referential
    _l_(648045) #self referential
    status = _c_(648053, _a_(648047, _n_(648046, "db", lambda: db), "Column"), _a_(648049, _n_(648048, "db", lambda: db), "Integer"), _c_(648052, _a_(648051, _n_(648050, "db", lambda: db), "ForeignKey"), 'tm_status.id'),nullable=False)
    _l_(648054)
    type = _c_(648062, _a_(648056, _n_(648055, "db", lambda: db), "Column"), _a_(648058, _n_(648057, "db", lambda: db), "Integer"), _c_(648061, _a_(648060, _n_(648059, "db", lambda: db), "ForeignKey"), 'tm_type.id'),nullable=False)
    _l_(648063)
    urgency = _c_(648071, _a_(648065, _n_(648064, "db", lambda: db), "Column"), _a_(648067, _n_(648066, "db", lambda: db), "Integer"), _c_(648070, _a_(648069, _n_(648068, "db", lambda: db), "ForeignKey"), 'tm_urgency.id'),nullable=False)
    _l_(648072)

    def __repr__(self):
        _l_(648084)

        aux = _c_(648082, _a_(648073, "Tasks('{}','{}','{}','{}')", "format"), _a_(648075, _n_(648074, "self", lambda: self), "descr"),_a_(648077, _n_(648076, "self", lambda: self), "added_on"),_a_(648079, _n_(648078, "self", lambda: self), "added_by"),_a_(648081, _n_(648080, "self", lambda: self), "assigned_to"))
        _l_(648083)
        return aux

class tm_status(_a_(648087, _n_(648086, "db", lambda: db), "Model")):
    _l_(648112)

    __tablename__ = 'tm_status'
    _l_(648088)
    id = _c_(648093, _a_(648090, _n_(648089, "db", lambda: db), "Column"), _a_(648092, _n_(648091, "db", lambda: db), "Integer"), primary_key=True)
    _l_(648094)
    status = _c_(648100, _a_(648096, _n_(648095, "db", lambda: db), "Column"), _c_(648099, _a_(648098, _n_(648097, "db", lambda: db), "String"), 20),unique=True,nullable=False)
    _l_(648101)
    status_f = _c_(648104, _a_(648103, _n_(648102, "db", lambda: db), "relationship"), 'Tasks', lazy=True, foreign_keys='tm_task.status')
    _l_(648105)

    def __repr__(self):
        _l_(648111)

        aux = _c_(648109, _a_(648106, "tm_status('{}')", "format"), _a_(648108, _n_(648107, "self", lambda: self), "status"))
        _l_(648110)
        return aux

class tm_type(_a_(648114, _n_(648113, "db", lambda: db), "Model")):
    _l_(648139)

    __tablename__ = 'tm_type'
    _l_(648115)
    id = _c_(648120, _a_(648117, _n_(648116, "db", lambda: db), "Column"), _a_(648119, _n_(648118, "db", lambda: db), "Integer"), primary_key=True)
    _l_(648121)
    type = _c_(648127, _a_(648123, _n_(648122, "db", lambda: db), "Column"), _c_(648126, _a_(648125, _n_(648124, "db", lambda: db), "String"), 20),unique=True,nullable=False)
    _l_(648128)
    type_f = _c_(648131, _a_(648130, _n_(648129, "db", lambda: db), "relationship"), 'Tasks', lazy=True, foreign_keys='tm_task.type')
    _l_(648132)

    def __repr__(self):
        _l_(648138)

        aux = _c_(648136, _a_(648133, "tm_type('{}')", "format"), _a_(648135, _n_(648134, "self", lambda: self), "type"))
        _l_(648137)
        return aux

class tm_urgency(_a_(648141, _n_(648140, "db", lambda: db), "Model")):
    _l_(648166)

    __tablename__ = 'tm_urgency'
    _l_(648142)
    id = _c_(648147, _a_(648144, _n_(648143, "db", lambda: db), "Column"), _a_(648146, _n_(648145, "db", lambda: db), "Integer"), primary_key=True)
    _l_(648148)
    urgency = _c_(648154, _a_(648150, _n_(648149, "db", lambda: db), "Column"), _c_(648153, _a_(648152, _n_(648151, "db", lambda: db), "String"), 20),unique=True,nullable=False)
    _l_(648155)
    urgency_f = _c_(648158, _a_(648157, _n_(648156, "db", lambda: db), "relationship"), 'Tasks', lazy=True, foreign_keys='tm_task.urgency')
    _l_(648159)

    def __repr__(self):
        _l_(648165)

        aux = _c_(648163, _a_(648160, "tm_urgency('{}')", "format"), _a_(648162, _n_(648161, "self", lambda: self), "urgency"))
        _l_(648164)
        return aux