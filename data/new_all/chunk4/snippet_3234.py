# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/76945050/qml-and-pyside6-typeerror-cannot-read-property-x-of-null
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from pathlib import Path
    _l_(623933)

except ImportError:
    pass
try:
    from PySide6.QtCore import QObject, QStringListModel
    _l_(623935)

except ImportError:
    pass
try:
    from PySide6.QtQml import QQmlApplicationEngine
    _l_(623937)

except ImportError:
    pass
try:
    from date_range_dialog import DateRangeDialog
    _l_(623939)

except ImportError:
    pass


class DialogManager(_n_(623940, "QObject", lambda: QObject)):
    _l_(624059)

    _engine: _n_(623941, "QQmlApplicationEngine", lambda: QQmlApplicationEngine)
    _l_(623942)

    def __init__(self):
        _l_(623952)

        _c_(623946, _a_(623944, _n_(623943, "QObject", lambda: QObject), "__init__"), _n_(623945, "self", lambda: self))
        _l_(623947)
        _n_(623948, "self", lambda: self)._engine = _c_(623950, _n_(623949, "QQmlApplicationEngine", lambda: QQmlApplicationEngine))
        _l_(623951)

    def loadDialog(
            self,
            name: _n_(623953, "str", lambda: str),
            width: _n_(623954, "float", lambda: float),
            height: _n_(623955, "float", lambda: float),
            startDates: _n_(623956, "list", lambda: list)[_n_(623957, "str", lambda: str)],
            endDates: _n_(623958, "list", lambda: list)[_n_(623959, "str", lambda: str)]
    ):
        _l_(624007)

        dialog = _c_(623961, _n_(623960, "DateRangeDialog", lambda: DateRangeDialog))
        _l_(623962)
        _n_(623963, "dialog", lambda: dialog).width = _n_(623964, "width", lambda: width)
        _l_(623965)
        _n_(623966, "dialog", lambda: dialog).height = _n_(623967, "height", lambda: height)
        _l_(623968)
        _n_(623969, "dialog", lambda: dialog).startDateModel = _c_(623972, _n_(623970, "QStringListModel", lambda: QStringListModel), _n_(623971, "startDates", lambda: startDates))
        _l_(623973)
        _n_(623974, "dialog", lambda: dialog).endDateModel = _c_(623977, _n_(623975, "QStringListModel", lambda: QStringListModel), _n_(623976, "endDates", lambda: endDates))
        _l_(623978)

        _c_(623982, _a_(623980, _n_(623979, "self", lambda: self), "_setRootContext"), _n_(623981, "dialog", lambda: dialog))
        _l_(623983)
        _c_(623987, _a_(623985, _n_(623984, "self", lambda: self), "_loadQmlFile"), _n_(623986, "name", lambda: name))
        _l_(623988)

        root = _c_(623991, _a_(623990, _n_(623989, "self", lambda: self), "_getQQmlEngineRoot"))
        _l_(623992)
        try:
            _l_(624006)

            _c_(623998, _a_(623995, _a_(623994, _n_(623993, "root", lambda: root), "outputDateRange"), "connect"), _a_(623997, _n_(623996, "dialog", lambda: dialog), "outputDateRange"))
            _l_(623999)
        except _n_(624000, "AttributeError", lambda: AttributeError) as e:
            _l_(624005)

            _c_(624003, _n_(624001, "print", lambda: print), _n_(624002, "e", lambda: e))
            _l_(624004)

    def _setRootContext(self, dialog: _n_(624008, "DateRangeDialog", lambda: DateRangeDialog)):
        _l_(624017)

        _c_(624015, _a_(624013, _c_(624012, _a_(624011, _a_(624010, _n_(624009, "self", lambda: self), "_engine"), "rootContext")), "setContextProperty"), "dialog", _n_(624014, "dialog", lambda: dialog))
        _l_(624016)

    def _loadQmlFile(self, qmlName: _n_(624018, "str", lambda: str)) -> None:
        _l_(624031)

        qmlFile = _a_(624022, _c_(624021, _n_(624019, "Path", lambda: Path), _n_(624020, "__file__", lambda: __file__)), "parent") / f"{_n_(624023, 'qmlName', lambda: qmlName)}.qml"
        _l_(624024)
        _c_(624029, _a_(624027, _a_(624026, _n_(624025, "self", lambda: self), "_engine"), "load"), _n_(624028, "qmlFile", lambda: qmlFile))
        _l_(624030)

    def _getQQmlEngineRoot(self) -> _n_(624032, "QObject", lambda: QObject):
        _l_(624058)

        if not _c_(624036, _a_(624035, _a_(624034, _n_(624033, "self", lambda: self), "_engine"), "rootObjects")):
            _l_(624040)

            raise _c_(624038, _n_(624037, "AttributeError", lambda: AttributeError), "Root objects for QQmlApplicationEngine not found")
            _l_(624039)

        root = _c_(624042, _n_(624041, "QObject", lambda: QObject))
        _l_(624043)
        for rootObject in _c_(624047, _a_(624046, _a_(624045, _n_(624044, "self", lambda: self), "_engine"), "rootObjects")):
            _l_(624055)

            if _c_(624050, _a_(624049, _n_(624048, "rootObject", lambda: rootObject), "inherits"), "QWindow"):
                _l_(624054)

                root = _n_(624051, "rootObject", lambda: rootObject)
                _l_(624052)
                break
                _l_(624053)
        aux = _n_(624056, "root", lambda: root)
        _l_(624057)

        return aux