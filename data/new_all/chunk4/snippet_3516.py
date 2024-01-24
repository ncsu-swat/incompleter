# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/73092421/python-flask-typeerror-int-argument-must-be-a-string-a-bytes-like-object-or
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from flask_sqlalchemy import SQLAlchemy
    _l_(587176)

except ImportError:
    pass
try:
    from sqlalchemy.sql.schema import ForeignKey
    _l_(587178)

except ImportError:
    pass
try:
    from flask_login import UserMixin
    _l_(587180)

except ImportError:
    pass

db = _c_(587182, _n_(587181, "SQLAlchemy", lambda: SQLAlchemy)) 
_l_(587183) 

class UserModel(_n_(587184, "UserMixin", lambda: UserMixin),_a_(587186, _n_(587185, "db", lambda: db), "Model")):
    _l_(587237)

    __tablename__ = 'users'
    _l_(587187)

    id = _c_(587192, _a_(587189, _n_(587188, "db", lambda: db), "Column"), _a_(587191, _n_(587190, "db", lambda: db), "Integer"), primary_key=True, autoincrement=True)
    _l_(587193)
    roll_num = _c_(587198, _a_(587195, _n_(587194, "db", lambda: db), "Column"), _a_(587197, _n_(587196, "db", lambda: db), "Integer"), nullable=False, unique=True)
    _l_(587199)
    name = _c_(587205, _a_(587201, _n_(587200, "db", lambda: db), "Column"), _c_(587204, _a_(587203, _n_(587202, "db", lambda: db), "String"), 80),nullable=False)
    _l_(587206)
    email = _c_(587212, _a_(587208, _n_(587207, "db", lambda: db), "Column"), _c_(587211, _a_(587210, _n_(587209, "db", lambda: db), "String"), 120), nullable=False, unique=True)
    _l_(587213)
    password = _c_(587219, _a_(587215, _n_(587214, "db", lambda: db), "Column"), _c_(587218, _a_(587217, _n_(587216, "db", lambda: db), "String")), nullable=False)
    _l_(587220)
    admin =  _c_(587225, _a_(587222, _n_(587221, "db", lambda: db), "Column"), _a_(587224, _n_(587223, "db", lambda: db), "Integer"),default=0)
    _l_(587226)
    votes = _c_(587229, _a_(587228, _n_(587227, "db", lambda: db), "relationship"), 'VotesModel', backref='voter', lazy=True)
    _l_(587230)

    def __repr__(self):
        _l_(587236)

        aux = f"User('{_a_(587232, _n_(587231, 'self', lambda: self), 'name')}', '{_a_(587234, _n_(587233, 'self', lambda: self), 'roll_num')}')"
        _l_(587235)
        return aux

class VotesModel(_a_(587239, _n_(587238, "db", lambda: db), "Model")):
    _l_(587277)

    __tablename__ = 'votes'
    _l_(587240)

    id = _c_(587245, _a_(587242, _n_(587241, "db", lambda: db), "Column"), _a_(587244, _n_(587243, "db", lambda: db), "Integer"), primary_key=True, autoincrement=True)
    _l_(587246)
    roll_num = _c_(587251, _a_(587248, _n_(587247, "db", lambda: db), "Column"), _a_(587250, _n_(587249, "db", lambda: db), "Integer"), nullable=False, unique=True)
    _l_(587252)
    voter_id = _c_(587259, _a_(587254, _n_(587253, "db", lambda: db), "Column"), _a_(587256, _n_(587255, "db", lambda: db), "Integer"), _c_(587258, _n_(587257, "ForeignKey", lambda: ForeignKey), 'users.id'))
    _l_(587260)
    post_1 = _c_(587265, _a_(587262, _n_(587261, "db", lambda: db), "Column"), _a_(587264, _n_(587263, "db", lambda: db), "Integer"), nullable=False )
    _l_(587266)
    post_2 = _c_(587271, _a_(587268, _n_(587267, "db", lambda: db), "Column"), _a_(587270, _n_(587269, "db", lambda: db), "Integer"), nullable=False)
    _l_(587272)

    def __repr__(self):
        _l_(587276)

        aux = f"Voter('{_a_(587274, _n_(587273, 'self', lambda: self), 'roll_num')}')"
        _l_(587275)
        return aux

class CandidateModel(_a_(587279, _n_(587278, "db", lambda: db), "Model")):
    _l_(587359)

    __tablename__ = 'candidates'
    _l_(587280)

    id = _c_(587285, _a_(587282, _n_(587281, "db", lambda: db), "Column"), _a_(587284, _n_(587283, "db", lambda: db), "Integer"), primary_key=True, autoincrement=True)
    _l_(587286)
    roll_num = _c_(587291, _a_(587288, _n_(587287, "db", lambda: db), "Column"), _a_(587290, _n_(587289, "db", lambda: db), "Integer"), nullable=False, unique=True)
    _l_(587292)
    first_name = _c_(587298, _a_(587294, _n_(587293, "db", lambda: db), "Column"), _c_(587297, _a_(587296, _n_(587295, "db", lambda: db), "String"), 80), nullable=False)
    _l_(587299)
    last_name = _c_(587305, _a_(587301, _n_(587300, "db", lambda: db), "Column"), _c_(587304, _a_(587303, _n_(587302, "db", lambda: db), "String"), 80))
    _l_(587306)
    batch = _c_(587312, _a_(587308, _n_(587307, "db", lambda: db), "Column"), _c_(587311, _a_(587310, _n_(587309, "db", lambda: db), "String"), 120), nullable=False)
    _l_(587313)
    course = _c_(587319, _a_(587315, _n_(587314, "db", lambda: db), "Column"), _c_(587318, _a_(587317, _n_(587316, "db", lambda: db), "String"), 120), nullable=False)
    _l_(587320)
    department = _c_(587326, _a_(587322, _n_(587321, "db", lambda: db), "Column"), _c_(587325, _a_(587324, _n_(587323, "db", lambda: db), "String"), 120), nullable=False)
    _l_(587327)
    post = _c_(587333, _a_(587329, _n_(587328, "db", lambda: db), "Column"), _c_(587332, _a_(587331, _n_(587330, "db", lambda: db), "String"), 80), nullable=False)
    _l_(587334)
    pic_path = _c_(587340, _a_(587336, _n_(587335, "db", lambda: db), "Column"), _c_(587339, _a_(587338, _n_(587337, "db", lambda: db), "String"), 120), default='images/default.png')
    _l_(587341)
    agenda =  _c_(587347, _a_(587343, _n_(587342, "db", lambda: db), "Column"), _c_(587346, _a_(587345, _n_(587344, "db", lambda: db), "String"), 300), default="No agenda")
    _l_(587348)

    def __repr__(self):
        _l_(587358)

        aux = f"Candidate('{_a_(587350, _n_(587349, 'self', lambda: self), 'first_name')}','{_a_(587352, _n_(587351, 'self', lambda: self), 'batch')}','{_a_(587354, _n_(587353, 'self', lambda: self), 'course')}','{_a_(587356, _n_(587355, 'self', lambda: self), 'department')}')"
        _l_(587357)
        return aux