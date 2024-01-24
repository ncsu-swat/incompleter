# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/50194562/django-2-0-2-problems-with-modelform-creation-attributeerror-str-object-has
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Rischi(_a_(571655, _n_(571654, "models", lambda: models), "Model")):
    _l_(571717)

    RISCHIO = (
        ('Nullo', 'Nullo'),
        ('Irrilevante', 'Irrilevante'),
        ('Basso', 'Basso'),
        ('Medio', 'Medio'),
        ('Alto', 'Alto'),
        )
    _l_(571656)
    azienda = _c_(571659, _a_(571657, models, "ForeignKey"), 'azienda.Azienda',
        on_delete=_a_(571658, models, "CASCADE"),
        )
    _l_(571660)
    foto = _c_(571662, _a_(571661, models, "ImageField"), upload_to='rischi', blank=True)
    _l_(571663)
    attivita = _c_(571666, _a_(571664, models, "ForeignKey"), Attivita,
        blank=True,
        null=True,
        on_delete=_a_(571665, models, "CASCADE"),
        )
    _l_(571667)
    luogo = _c_(571670, _a_(571668, models, "ForeignKey"), Luoghi,
        blank=True,
        null=True,
        on_delete=_a_(571669, models, "CASCADE"),
        )
    _l_(571671)
    macchina = _c_(571674, _a_(571672, models, "ForeignKey"), Macchine,
        blank=True,
        null=True,
        on_delete=_a_(571673, models, "CASCADE"),
        )
    _l_(571675)
    sostanza = _c_(571678, _a_(571676, models, "ForeignKey"), Sostanze,
        blank=True,
        null=True,
        on_delete=_a_(571677, models, "CASCADE"),
        )
    _l_(571679)
    fonte_rischio = _c_(571682, _a_(571680, models, "ForeignKey"), Fonte_rischio,
        on_delete=_a_(571681, models, "CASCADE")
        )
    _l_(571683)
    pericolo = _c_(571685, _a_(571684, models, "CharField"), max_length=200)
    _l_(571686)
    mansione = _c_(571688, _a_(571687, models, "ManyToManyField"), 'mansione.Mansione'
        )
    _l_(571689)
    livello_rischio = _c_(571691, _a_(571690, models, "CharField"), max_length=200)
    _l_(571692)
    rischio = _c_(571694, _a_(571693, models, "CharField"), max_length=200, choices=RISCHIO)
    _l_(571695)
    allegato = _c_(571697, _a_(571696, models, "ManyToManyField"), Allegati,
        blank=True,
        )
    _l_(571698)
    note = _c_(571700, _a_(571699, models, "TextField"), blank=True)
    _l_(571701)
    data_di_creazione = _c_(571703, _a_(571702, models, "DateField"), auto_now_add=True)
    _l_(571704)
    data_di_modifica = _c_(571706, _a_(571705, models, "DateField"), auto_now=True)
    _l_(571707)

    def __str__(self):
        _l_(571716)

        aux = _a_(571710, _a_(571709, _n_(571708, "self", lambda: self), "fonte_rischio"), "nome") + ", id: "+ _c_(571714, _n_(571711, "str", lambda: str), _a_(571713, _n_(571712, "self", lambda: self), "pk"))
        _l_(571715)
        return aux