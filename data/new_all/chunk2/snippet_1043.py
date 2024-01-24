# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/50707750/django-admin-stackedinline-not-loading-add-another-model-uncaught-typeerror-ca
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_c_(456031, _a_(456028, _n_(456027, "admin", lambda: admin), "register"), _a_(456030, _n_(456029, "models", lambda: models), "Paper"))
class PaperAdmin(_n_(456032, "BaseLiteratureAdmin", lambda: BaseLiteratureAdmin)):
    _l_(456061)


    class EditedPaperAdminInline(_a_(456033, admin, "StackedInline")):
        _l_(456037)

        model = _a_(456034, models, "EditedPaper")
        _l_(456035)
        extra = 0
        _l_(456036)

    class SupplementaryInformationAdminInline(_a_(456038, admin, "StackedInline")):
        _l_(456042)

        model = _a_(456039, models, "SupplementaryInformation")
        _l_(456040)
        extra = 0
        _l_(456041)

    class PaperNotesAdminInline(BaseNotesAdminInline):
        _l_(456049)

        exclude = _c_(456047, _n_(456043, "tuple", lambda: tuple), (_n_(456044, "i", lambda: i) for i in _a_(456045, BaseNotesAdminInline, "exclude") if _n_(456046, "i", lambda: i) != 'paper'))
        _l_(456048)

    class ReferencedPaperInline(_a_(456050, admin, "StackedInline")):
        _l_(456059)

        model = _a_(456053, _a_(456052, _a_(456051, models, "Paper"), "referenced_papers"), "through")
        _l_(456054)
        extra = 0
        _l_(456055)
        fk_name = 'from_paper'
        _l_(456056)
        verbose_name = "Referenced Paper"
        _l_(456057)
        verbose_name_plural = "Referenced Papers"
        _l_(456058)

    inlines = (
        EditedPaperAdminInline, # problem
        PaperNotesAdminInline, # ok single/together
        ReferencedPaperInline, # ok single/together
        SupplementaryInformationAdminInline, # problem
        
    )
    _l_(456060)