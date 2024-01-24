# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/74706590/attributeerror-type-object-adminsignupform-has-no-attribute-as-view-why-is
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class User(_n_(424783, "AbstractUser", lambda: AbstractUser)):
    _l_(424793)

    is_student = _c_(424785, _a_(424784, models, "BooleanField"), default=False)
    _l_(424786)
    is_teacher = _c_(424788, _a_(424787, models, "BooleanField"), default=False)
    _l_(424789)
    is_admin = _c_(424791, _a_(424790, models, "BooleanField"), default=False)
    _l_(424792)

class Admin(_a_(424795, _n_(424794, "models", lambda: models), "Model")):
    _l_(424809)

    admin = _c_(424799, _a_(424796, models, "OneToOneField"), _n_(424797, "User", lambda: User), on_delete=_a_(424798, models, "CASCADE"))
    _l_(424800)
    bio = _c_(424802, _a_(424801, models, "TextField"))
    _l_(424803)
    
    def __str__(self):
        _l_(424808)

        aux = f'{_a_(424806, _a_(424805, _n_(424804, "self", lambda: self), "user"), "username")} Admin'
        _l_(424807)
        return aux
class Student(_a_(424811, _n_(424810, 'models', lambda: models), 'Model')):
    _l_(424847)

    user = _c_(424815, _a_(424812, models, 'OneToOneField'), _n_(424813, 'User', lambda: User), on_delete=_a_(424814, models, 'CASCADE'), primary_key=True)
    _l_(424816)
    quizzes = _c_(424818, _a_(424817, models, 'ManyToManyField'), Quiz, through='TakenQuiz')
    _l_(424819)
    interests = _c_(424821, _a_(424820, models, 'ManyToManyField'), Subject, related_name='interested_students')
    _l_(424822)

    def get_unanswered_questions(self, quiz):
        _l_(424841)

        answered_questions = _c_(424829, _a_(424828, _c_(424827, _a_(424825, _a_(424824, _n_(424823, 'self', lambda: self), 'quiz_answers'), 'filter'), answer__question__quiz=_n_(424826, 'quiz', lambda: quiz)), 'values_list'), 'answer__question__pk', flat=True)
        _l_(424830)
        questions = _c_(424837, _a_(424836, _c_(424835, _a_(424833, _a_(424832, _n_(424831, 'quiz', lambda: quiz), 'questions'), 'exclude'), pk__in=_n_(424834, 'answered_questions', lambda: answered_questions)), 'order_by'), 'text')
        _l_(424838)
        aux = _n_(424839, 'questions', lambda: questions)
        _l_(424840)
        return aux

    def __str__(self):
        _l_(424846)

        aux = _a_(424844, _a_(424843, _n_(424842, 'self', lambda: self), 'user'), 'username')
        _l_(424845)
        return aux