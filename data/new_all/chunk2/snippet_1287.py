# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55509211/how-to-resolve-object-of-type-attributeerror-is-not-json-serializable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Invite_Key(_a_(453065, _n_(453064, "models", lambda: models), "Model")):
    _l_(453143)

    STATUS_CHOICES = (
        ('valid', 'valid'),
        ('not_valid', 'not_valid'),
        ('banned', 'banned'),
    )
    _l_(453066)

    # Foreign keys
    user_submitter = _c_(453070, _a_(453067, models, "ForeignKey"), _a_(453068, settings, "AUTH_USER_MODEL"),
        on_delete=_a_(453069, models, "CASCADE"),
        null=True,
        blank=True,
        related_name='user_submitter'
    )
    _l_(453071)

    user_receiver = _c_(453075, _a_(453072, models, "ForeignKey"), _a_(453073, settings, "AUTH_USER_MODEL"),
        on_delete=_a_(453074, models, "CASCADE"),
        null=True,
        blank=True,
        related_name='user_receiver'
    )
    _l_(453076)

    uuid = _c_(453078, _a_(453077, models, "UUIDField"), default=generate_ulid_as_uuid, editable=False, unique=True, null=False)
    _l_(453079)
    open_uuid = _c_(453081, _a_(453080, models, "UUIDField"), default=uuid1, editable=False, unique=True, null=False)
    _l_(453082)
    reason = _c_(453084, _a_(453083, models, "TextField"), validators=[bad_words, bad_words_inline, test_test])
    _l_(453085)

    # Now are choices
    status = _c_(453087, _a_(453086, models, "CharField"), max_length=14, choices=STATUS_CHOICES, default="valid")
    _l_(453088)

    # Now below are boolean
    is_taken = _c_(453090, _a_(453089, models, "BooleanField"), default=False)
    _l_(453091)
    is_locked = _c_(453093, _a_(453092, models, "BooleanField"), default=False)
    _l_(453094)

    claim_date = _c_(453096, _a_(453095, models, "DateField"), editable=True, null=True, blank=True)
    _l_(453097)
    expire_date = _c_(453099, _a_(453098, models, "DateField"), editable=True, null=True, blank=True)
    _l_(453100)

    # Now these are the time stamps
    created_at = _c_(453102, _a_(453101, models, "DateTimeField"), auto_now_add=True, editable=False)
    _l_(453103)
    updated_at = _c_(453105, _a_(453104, models, "DateTimeField"), auto_now=True, editable=False)
    _l_(453106)

    def __str__(self):
        _l_(453112)

        aux = _c_(453110, _n_(453107, "str", lambda: str), _a_(453109, _n_(453108, "self", lambda: self), "uuid"))
        _l_(453111)
        return aux

    # An instance of our object temp used for later
    def __init__(self, *args, **kwargs):
        _l_(453123)

        _c_(453119, _a_(453116, _n_(453113, "super", lambda: super)(_n_(453114, "Invite_Key", lambda: Invite_Key), _n_(453115, "self", lambda: self)), "__init__"), *_n_(453117, "args", lambda: args), **_n_(453118, "kwargs", lambda: kwargs))
        _l_(453120)
        _n_(453121, "self", lambda: self).temp = ''
        _l_(453122)

    # We can set attributes onSave of our data to the table
    def save(self, *args, **kwargs):
        _l_(453142)

        if not _a_(453125, _n_(453124, "self", lambda: self), "id"):
            _l_(453133)

            # for expire date
            _n_(453126, "self", lambda: self).expire_date = _c_(453129, _a_(453128, _n_(453127, "datetime", lambda: datetime), "now")) + _c_(453131, _n_(453130, "timedelta", lambda: timedelta), days=7)
            _l_(453132)

        _c_(453140, _a_(453137, _n_(453134, "super", lambda: super)(_n_(453135, "Invite_Key", lambda: Invite_Key), _n_(453136, "self", lambda: self)), "save"), *_n_(453138, "args", lambda: args), **_n_(453139, "kwargs", lambda: kwargs))
        _l_(453141)