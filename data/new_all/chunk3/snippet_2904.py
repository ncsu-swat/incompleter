# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58902206/get-form-in-modeladmin-causing-typeerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class AdminMemoForm(_a_(550029, _n_(550028, "forms", lambda: forms), "ModelForm")):
    _l_(550033)

    """
    Memo creation form, related to:

    :model: 'memos.Memo',
    """
    class Meta:
        _l_(550032)

        model = Memo
        _l_(550030)
        fields = (
            'title',
            'content',
            'important',
            'word_file',
            'receiver',
            'read',
            'unread',
        )
        _l_(550031)