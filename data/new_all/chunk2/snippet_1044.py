# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/50707750/django-admin-stackedinline-not-loading-add-another-model-uncaught-typeerror-ca
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
inlines = (
        _n_(437688, "PaperNotesAdminInline", lambda: PaperNotesAdminInline), # ok single/together
        _n_(437689, "ReferencedPaperInline", lambda: ReferencedPaperInline), # ok single/together
        _n_(437690, "EditedPaperAdminInline", lambda: EditedPaperAdminInline), # problem
        _n_(437691, "SupplementaryInformationAdminInline", lambda: SupplementaryInformationAdminInline), # problem
        
    )
_l_(437692)