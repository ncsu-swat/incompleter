# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/51426359/django-typeerror-nonetype-object-is-not-iterable-dont-understand-why-obje
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.db import models
    _l_(473724)

except ImportError:
    pass
try:
    from django.conf import settings
    _l_(473726)

except ImportError:
    pass
try:
    from django.db.models import Q
    _l_(473728)

except ImportError:
    pass

class ThreadManager(_a_(473730, _n_(473729, "models", lambda: models), "Manager")):
    _l_(473835)

    def by_user(self, user):
        _l_(473759)

        qlookup = _c_(473733, _n_(473731, "Q", lambda: Q), first=_n_(473732, "user", lambda: user)) | _c_(473736, _n_(473734, "Q", lambda: Q), second=_n_(473735, "user", lambda: user))
        _l_(473737)
        qlookup2 = _c_(473740, _n_(473738, "Q", lambda: Q), first=_n_(473739, "user", lambda: user)) & _c_(473743, _n_(473741, "Q", lambda: Q), second=_n_(473742, "user", lambda: user))
        _l_(473744)
        qs = _c_(473755, _a_(473754, _c_(473753, _a_(473751, _c_(473750, _a_(473748, _c_(473747, _a_(473746, _n_(473745, "self", lambda: self), "get_queryset")), "filter"), _n_(473749, "qlookup", lambda: qlookup)), "exclude"), _n_(473752, "qlookup2", lambda: qlookup2)), "distinct"))
        _l_(473756)
        aux = _n_(473757, "qs", lambda: qs)
        _l_(473758)
        return aux

    def get_or_new(self, user, other_username):
        _l_(473834)

        username = _a_(473761, _n_(473760, "user", lambda: user), "username")
        _l_(473762)
        if _n_(473763, "username", lambda: username) == _n_(473764, "other_username", lambda: other_username):
            _l_(473766)

            aux = None
            _l_(473765)
            return aux
        qlookup1 = _c_(473769, _n_(473767, "Q", lambda: Q), first__username=_n_(473768, "username", lambda: username)) & _c_(473772, _n_(473770, "Q", lambda: Q), second__username=_n_(473771, "other_username", lambda: other_username))
        _l_(473773)
        qlookup2 = _c_(473776, _n_(473774, "Q", lambda: Q), first__username=_n_(473775, "other_username", lambda: other_username)) & _c_(473779, _n_(473777, "Q", lambda: Q), second__username=_n_(473778, "username", lambda: username))
        _l_(473780)
        qs = _c_(473789, _a_(473788, _c_(473787, _a_(473784, _c_(473783, _a_(473782, _n_(473781, "self", lambda: self), "get_queryset")), "filter"), _n_(473785, "qlookup1", lambda: qlookup1) | _n_(473786, "qlookup2", lambda: qlookup2)), "distinct"))
        _l_(473790)
        if _c_(473793, _a_(473792, _n_(473791, "qs", lambda: qs), "count")) == 1:
            _l_(473833)

            aux = _c_(473796, _a_(473795, _n_(473794, "qs", lambda: qs), "first")), False
            _l_(473797)
            return aux
        elif _c_(473800, _a_(473799, _n_(473798, "qs", lambda: qs), "count")) > 1:
            _l_(473832)

            aux = _c_(473805, _a_(473804, _c_(473803, _a_(473802, _n_(473801, "qs", lambda: qs), "order_by"), 'timestamp'), "first")), False
            _l_(473806)
            return aux
        else:
            Klass = _a_(473808, _n_(473807, "user", lambda: user), "__class__")
            _l_(473809)
            user2 = _c_(473814, _a_(473812, _a_(473811, _n_(473810, "Klass", lambda: Klass), "objects"), "get"), username=_n_(473813, "other_username", lambda: other_username))
            _l_(473815)
            if _n_(473816, "user", lambda: user) != _n_(473817, "user2", lambda: user2):
                _l_(473830)

                obj = _c_(473822, _a_(473819, _n_(473818, "self", lambda: self), "model"), first=_n_(473820, "user", lambda: user),
                        second=_n_(473821, "user2", lambda: user2)
                    )
                _l_(473823)
                _c_(473826, _a_(473825, _n_(473824, "obj", lambda: obj), "save"))
                _l_(473827)
                aux = _n_(473828, "obj", lambda: obj), True
                _l_(473829)
                return aux
            aux = None, False
            _l_(473831)
            return aux


class Thread(_a_(473837, _n_(473836, "models", lambda: models), "Model")):
    _l_(473881)

    first        = _c_(473844, _a_(473839, _n_(473838, "models", lambda: models), "ForeignKey"), _a_(473841, _n_(473840, "settings", lambda: settings), "AUTH_USER_MODEL"), on_delete=_a_(473843, _n_(473842, "models", lambda: models), "CASCADE"), related_name='chat_thread_first')
    _l_(473845)
    second       = _c_(473852, _a_(473847, _n_(473846, "models", lambda: models), "ForeignKey"), _a_(473849, _n_(473848, "settings", lambda: settings), "AUTH_USER_MODEL"), on_delete=_a_(473851, _n_(473850, "models", lambda: models), "CASCADE"), related_name='chat_thread_second')
    _l_(473853)
    updated      = _c_(473856, _a_(473855, _n_(473854, "models", lambda: models), "DateTimeField"), auto_now=True)
    _l_(473857)
    timestamp    = _c_(473860, _a_(473859, _n_(473858, "models", lambda: models), "DateTimeField"), auto_now_add=True)
    _l_(473861)

    objects      = _c_(473863, _n_(473862, "ThreadManager", lambda: ThreadManager))
    _l_(473864)

    @_n_(473865, "property", lambda: property)
    def room_group_name(self):
        _l_(473869)

        aux = f'chat_{_a_(473867, _n_(473866, "self", lambda: self), "id")}'
        _l_(473868)
        return aux

    def broadcast(self, msg=None):
        _l_(473880)

        if _n_(473870, 'msg', lambda: msg) is not None:
            _l_(473878)

            _c_(473875, _n_(473871, 'broadcast_msg_to_chat', lambda: broadcast_msg_to_chat), _n_(473872, 'msg', lambda: msg), group_name=_a_(473874, _n_(473873, 'self', lambda: self), 'room_group_name'), user='admin')
            _l_(473876)
            aux = True
            _l_(473877)
            return aux
        aux = False
        _l_(473879)
        return aux


class ChatMessage(_a_(473883, _n_(473882, 'models', lambda: models), 'Model')):
    _l_(473907)

    thread      = _c_(473889, _a_(473885, _n_(473884, 'models', lambda: models), 'ForeignKey'), _n_(473886, 'Thread', lambda: Thread), null=True, blank=True, on_delete=_a_(473888, _n_(473887, 'models', lambda: models), 'SET_NULL'))
    _l_(473890)
    user        = _c_(473897, _a_(473892, _n_(473891, 'models', lambda: models), 'ForeignKey'), _a_(473894, _n_(473893, 'settings', lambda: settings), 'AUTH_USER_MODEL'), verbose_name='sender', on_delete=_a_(473896, _n_(473895, 'models', lambda: models), 'CASCADE'))
    _l_(473898)
    message     = _c_(473901, _a_(473900, _n_(473899, 'models', lambda: models), 'TextField'))
    _l_(473902)
    timestamp   = _c_(473905, _a_(473904, _n_(473903, 'models', lambda: models), 'DateTimeField'), auto_now_add=True)
    _l_(473906)