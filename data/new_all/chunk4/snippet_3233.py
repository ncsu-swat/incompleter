# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/76945050/qml-and-pyside6-typeerror-cannot-read-property-x-of-null
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import sys
    _l_(600125)

except ImportError:
    pass
try:
    from PySide6.QtWidgets import QApplication
    _l_(600127)

except ImportError:
    pass
try:
    from dialog_manager import DialogManager
    _l_(600129)

except ImportError:
    pass
try:
    import style_rc
    _l_(600131)

except ImportError:
    pass


def main() -> None:
    _l_(600151)

    app = _c_(600135, _n_(600132, "QApplication", lambda: QApplication), _a_(600134, _n_(600133, "sys", lambda: sys), "argv"))
    _l_(600136)
    dialogManager = _c_(600138, _n_(600137, "DialogManager", lambda: DialogManager))
    _l_(600139)
    _c_(600142, _a_(600141, _n_(600140, "dialogManager", lambda: dialogManager), "loadDialog"), name="DateRangeDialog",
            width=800, 
            height=180, 
            startDates=["14/08/23", "15/08/23"], 
            endDates=["15/08/23"]
    )
    _l_(600143)

    _c_(600149, _a_(600145, _n_(600144, "sys", lambda: sys), "exit"), _c_(600148, _a_(600147, _n_(600146, "app", lambda: app), "exec")))
    _l_(600150)


if _n_(600152, "__name__", lambda: __name__) == "__main__":
    _l_(600156)

    _c_(600154, _n_(600153, "main", lambda: main))
    _l_(600155)