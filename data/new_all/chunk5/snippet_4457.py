# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57447541/ask-about-this-error-type-error-cant-mix-string-and-bytes-in-path-components
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class threading_one(_n_(665864, "QThread", lambda: QThread), _n_(665865, "QMessageBox", lambda: QMessageBox)):
    _l_(665932)

    signal = _c_(665866, pyqtSignal)
    _l_(665867)
    count_pro = _c_(665869, pyqtSignal, _n_(665868, "int", lambda: int))
    _l_(665870)
    cha_name = _c_(665872, pyqtSignal, _n_(665871, "str", lambda: str))
    _l_(665873)

    def __init__(self):
        _l_(665879)

        _c_(665877, _a_(665875, _n_(665874, "QThread", lambda: QThread), "__init__"), _n_(665876, "self", lambda: self))
        _l_(665878)

    def progress_count(self, total, recvd, ratio, rate, eta):
        _l_(665900)

        read_data = _n_(665880, "recvd", lambda: recvd)
        _l_(665881)
        if _n_(665882, "total", lambda: total) > 0:
            _l_(665899)

            download_percentage = _n_(665883, "read_data", lambda: read_data) * 100 / _n_(665884, "total", lambda: total)
            _l_(665885)
            _c_(665890, _a_(665888, _a_(665887, _n_(665886, "self", lambda: self), "count_pro"), "emit"), _n_(665889, "download_percentage", lambda: download_percentage))
            _l_(665891)
            if _n_(665892, "download_percentage", lambda: download_percentage) >= 100:
                _l_(665898)

                _c_(665896, _a_(665895, _a_(665894, _n_(665893, "self", lambda: self), "signal"), "emit"))
                _l_(665897)

    def run(self):
        _l_(665931)


        video = _c_(665905, _a_(665902, _n_(665901, "pafy", lambda: pafy), "new"), _a_(665904, _n_(665903, "self", lambda: self), "url"))
        _l_(665906)
        stream = _c_(665909, _a_(665908, _n_(665907, "video", lambda: video), "getbest"), preftype='mp4')
        _l_(665910)
        _c_(665916, _a_(665913, _a_(665912, _n_(665911, "self", lambda: self), "cha_name"), "emit"), _a_(665915, _n_(665914, "video", lambda: video), "title"))
        _l_(665917)
        _c_(665924, _a_(665919, _n_(665918, "stream", lambda: stream), "download"), filepath=_a_(665921, _n_(665920, "self", lambda: self), "save"), callback=_a_(665923, _n_(665922, "self", lambda: self), "progress_count"))
        _l_(665925)
        _c_(665929, _a_(665928, _a_(665927, _n_(665926, "self", lambda: self), "signal"), "emit"))
        _l_(665930)


class MainApp(_n_(665933, "QMainWindow", lambda: QMainWindow), _n_(665934, "Ui_MainWindow", lambda: Ui_MainWindow)):
    _l_(666089)

    def __init__(self, parent=None):
        _l_(665955)

        _c_(665940, _a_(665938, _n_(665935, "super", lambda: super)(_n_(665936, "MainApp", lambda: MainApp), _n_(665937, "self", lambda: self)), "__init__"), _n_(665939, "parent", lambda: parent))
        _l_(665941)
        _c_(665945, _a_(665943, _n_(665942, "self", lambda: self), "setupUi"), _n_(665944, "self", lambda: self))
        _l_(665946)
        _c_(665949, _a_(665948, _n_(665947, "self", lambda: self), "Handel_Screen"))
        _l_(665950)
        _c_(665953, _a_(665952, _n_(665951, "self", lambda: self), "Handel_Button"))
        _l_(665954)

    def Handel_Screen(self):
        _l_(665960)

        _c_(665958, _a_(665957, _n_(665956, "self", lambda: self), "setWindowTitle"), "Test Download Program")
        _l_(665959)

    def Handel_Button(self):
        _l_(666005)

        _c_(665967, _a_(665964, _a_(665963, _a_(665962, _n_(665961, "self", lambda: self), "pushButton"), "clicked"), "connect"), _a_(665966, _n_(665965, "self", lambda: self), "download_video"))
        _l_(665968)
        _c_(665975, _a_(665972, _a_(665971, _a_(665970, _n_(665969, "self", lambda: self), "pushButton_2"), "clicked"), "connect"), _a_(665974, _n_(665973, "self", lambda: self), "Browse_Location"))
        _l_(665976)

        _n_(665977, "self", lambda: self).down_single = _c_(665979, _n_(665978, "threading_one", lambda: threading_one))
        _l_(665980)
        _c_(665987, _a_(665984, _a_(665983, _a_(665982, _n_(665981, "self", lambda: self), "down_single"), "signal"), "connect"), _a_(665986, _n_(665985, "self", lambda: self), "finish"))
        _l_(665988)
        _c_(665995, _a_(665992, _a_(665991, _a_(665990, _n_(665989, "self", lambda: self), "down_single"), "count_pro"), "connect"), _a_(665994, _n_(665993, "self", lambda: self), "chang_progressBar"))
        _l_(665996)
        _c_(666003, _a_(666000, _a_(665999, _a_(665998, _n_(665997, "self", lambda: self), "down_single"), "cha_name"), "connect"), _a_(666002, _n_(666001, "self", lambda: self), "change_name_video"))
        _l_(666004)

    def chang_progressBar(self, value):
        _l_(666012)

        _c_(666010, _a_(666008, _a_(666007, _n_(666006, "self", lambda: self), "progressBar"), "setValue"), _n_(666009, "value", lambda: value))
        _l_(666011)

    def finish(self):
        _l_(666033)

        _c_(666016, _a_(666014, _n_(666013, "QMessageBox", lambda: QMessageBox), "information"), _n_(666015, "self", lambda: self), "Complete Download ...", "Your Download is Complete ...")
        _l_(666017)
        _c_(666021, _a_(666020, _a_(666019, _n_(666018, "self", lambda: self), "lineEdit"), "clear"))
        _l_(666022)
        _c_(666026, _a_(666025, _a_(666024, _n_(666023, "self", lambda: self), "progressBar"), "setValue"), 0)
        _l_(666027)
        _c_(666031, _a_(666030, _a_(666029, _n_(666028, "self", lambda: self), "pushButton"), "setEnabled"), True)
        _l_(666032)

    def Browse_Location(self):
        _l_(666045)

        save_lacation = _c_(666037, _a_(666035, _n_(666034, "QFileDialog", lambda: QFileDialog), "getExistingDirectory"), _n_(666036, "self", lambda: self), 'Select Location')
        _l_(666038)
        _c_(666043, _a_(666041, _a_(666040, _n_(666039, "self", lambda: self), "label"), "setText"), _n_(666042, "save_lacation", lambda: save_lacation))
        _l_(666044)

    def change_name_video(self, title):
        _l_(666052)

        _c_(666050, _a_(666048, _a_(666047, _n_(666046, "self", lambda: self), "label_2"), "setText"), _n_(666049, "title", lambda: title))
        _l_(666051)

    def download_video(self):
        _l_(666088)

        _a_(666054, _n_(666053, "self", lambda: self), "down_single").url = _c_(666058, _a_(666057, _a_(666056, _n_(666055, "self", lambda: self), "lineEdit"), "text"))
        _l_(666059)
        _a_(666061, _n_(666060, "self", lambda: self), "down_single").save = _c_(666065, _a_(666064, _a_(666063, _n_(666062, "self", lambda: self), "label"), "text"))
        _l_(666066)

        if _c_(666070, _a_(666069, _a_(666068, _n_(666067, "self", lambda: self), "lineEdit"), "text")) == "":
            _l_(666077)

            _c_(666074, _a_(666072, _n_(666071, "QMessageBox", lambda: QMessageBox), "warning"), _n_(666073, "self", lambda: self), " From System ! ", " Please put valid URL first  !! ")
            _l_(666075)
            aux = ""
            _l_(666076)
            return aux
        _c_(666081, _a_(666080, _a_(666079, _n_(666078, "self", lambda: self), "pushButton"), "setEnabled"), False)
        _l_(666082)
        _c_(666086, _a_(666085, _a_(666084, _n_(666083, "self", lambda: self), "down_single"), "start"))
        _l_(666087)


def main():
    _l_(666106)

    app = _c_(666093, _n_(666090, "QApplication", lambda: QApplication), _a_(666092, _n_(666091, "sys", lambda: sys), "argv"))
    _l_(666094)
    window = _c_(666096, _n_(666095, "MainApp", lambda: MainApp))
    _l_(666097)
    _c_(666100, _a_(666099, _n_(666098, "window", lambda: window), "show"))
    _l_(666101)
    _c_(666104, _a_(666103, _n_(666102, "app", lambda: app), "exec"))
    _l_(666105)


if _n_(666107, "__name__", lambda: __name__) == '__main__':
    _l_(666111)

    _c_(666109, _n_(666108, "main", lambda: main))
    _l_(666110)