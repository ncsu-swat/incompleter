# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/54028479/typeerror-printboardpg-object-does-not-support-indexing
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import csv
    _l_(676762)

except ImportError:
    pass
try:
    import re
    _l_(676764)

except ImportError:
    pass
try:
    import datetime
    _l_(676766)

except ImportError:
    pass
try:
    from task import Task
    _l_(676768)

except ImportError:
    pass
try:
    from task_list import TaskList
    _l_(676770)

except ImportError:
    pass


class Worklog():
    _l_(676922)

    def __init__(self):
        _l_(676784)

        _n_(676771, "self", lambda: self).filename = "work_log.csv"
        _l_(676772)
        _n_(676773, "self", lambda: self).tasklist = _c_(676775, _n_(676774, "TaskList", lambda: TaskList))
        _l_(676776)
        _c_(676782, _a_(676779, _a_(676778, _n_(676777, "self", lambda: self), "tasklist"), "read_task_from_file"), _a_(676781, _n_(676780, "self", lambda: self), "filename"))
        _l_(676783)

    def search_by_date(self):
        _l_(676797)

        for d, i in _c_(676790, _n_(676785, "enumerate", lambda: enumerate), _c_(676789, _a_(676788, _a_(676787, _n_(676786, "self", lambda: self), "tasklist"), "dates"))):
            _l_(676796)

            _c_(676794, _n_(676791, "print", lambda: print), _n_(676792, "d", lambda: d)+1, ':', _n_(676793, "i", lambda: i))
            _l_(676795)

    def search_by_time(self):
        _l_(676799)

        pass
        _l_(676798)

    def exact_search(self):
        _l_(676801)

        pass
        _l_(676800)

    def pattern_search(self):
        _l_(676803)

        pass
        _l_(676802)

    def add_task(self):
        _l_(676839)

        task = _c_(676805, _n_(676804, "Task", lambda: Task))
        _l_(676806)
        _c_(676809, _a_(676808, _n_(676807, "task", lambda: task), "input_task"))
        _l_(676810)
        _c_(676813, _a_(676812, _n_(676811, "task", lambda: task), "input_minutes"))
        _l_(676814)
        _c_(676817, _a_(676816, _n_(676815, "task", lambda: task), "input_notes"))
        _l_(676818)
        _n_(676819, "task", lambda: task).date = _c_(676823, _a_(676822, _a_(676821, _n_(676820, "datetime", lambda: datetime), "date"), "today"))
        _l_(676824)
        _c_(676829, _a_(676827, _a_(676826, _n_(676825, "self", lambda: self), "tasklist"), "app_task"), _n_(676828, "task", lambda: task))
        _l_(676830)
        _c_(676837, _a_(676833, _a_(676832, _n_(676831, "self", lambda: self), "tasklist"), "save_task_to_file"), _a_(676835, _n_(676834, "self", lambda: self), "filename"),_n_(676836, "task", lambda: task))
        _l_(676838)

    def lookup_task(self):
        _l_(676891)

        if _c_(676844, _n_(676840, "len", lambda: len), _a_(676843, _a_(676842, _n_(676841, "self", lambda: self), "tasklist"), "task_list")) == 0:
            _l_(676890)

            _c_(676846, _n_(676845, "print", lambda: print), "Your task log is empty.\n")
            _l_(676847)
            _c_(676849, _n_(676848, "input", lambda: input), "Hit Enter to add a new task.")
            _l_(676850)
        else:
            while True:
                _l_(676889)

                lookup = _c_(676852, _n_(676851, "input", lambda: input), "Lookup by Date(D), Time(T), Exact Search(E) or Pattern(P): ")
                _l_(676853)
                _c_(676856, _a_(676855, _n_(676854, "lookup", lambda: lookup), "lower"))
                _l_(676857)

                if _n_(676858, "lookup", lambda: lookup) == 'd':
                    _l_(676888)

                    _c_(676861, _a_(676860, _n_(676859, "self", lambda: self), "search_by_date"))
                    _l_(676862)
                    break
                    _l_(676863)
                elif _n_(676864, "lookup", lambda: lookup) == 't':
                    _l_(676887)

                    _c_(676867, _a_(676866, _n_(676865, "self", lambda: self), "search_by_time"))
                    _l_(676868)
                    break
                    _l_(676869)
                elif _n_(676870, "lookup", lambda: lookup) == 'e':
                    _l_(676886)

                    _c_(676873, _a_(676872, _n_(676871, "self", lambda: self), "exact_search"))
                    _l_(676874)
                    break
                    _l_(676875)
                elif _n_(676876, "lookup", lambda: lookup) == 'p':
                    _l_(676885)

                    _c_(676879, _a_(676878, _n_(676877, "self", lambda: self), "pattern_search"))
                    _l_(676880)
                    break
                    _l_(676881)
                else:
                    _c_(676883, _n_(676882, "print", lambda: print), "Sorry invalid option. Please try again")
                    _l_(676884)

    def start_message(self):
        _l_(676921)

        while True:
            _l_(676920)


            q = _c_(676897, _n_(676892, "input", lambda: input), _c_(676896, _a_(676895, _c_(676894, _a_(676893, "Add New Task(1) or Lookup Task(2) or Quit(3): ", "strip")), "lower")))
            _l_(676898)

            if _n_(676899, "q", lambda: q) == "1":
                _l_(676919)

                _c_(676902, _a_(676901, _n_(676900, "self", lambda: self), "add_task"))
                _l_(676903)

            elif _n_(676904, "q", lambda: q) == "2":
                _l_(676918)

                _c_(676907, _a_(676906, _n_(676905, "self", lambda: self), "lookup_task"))
                _l_(676908)

            elif _n_(676909, "q", lambda: q) == "3":
                _l_(676917)

                aux = ""
                _l_(676912)
                exit(aux)

            else:
                _c_(676914, _n_(676913, "print", lambda: print), "Sorry that's an invalid entry. Please try again.")
                _l_(676915)
                continue
                _l_(676916)

if _n_(676923, "__name__", lambda: __name__) == '__main__':
    _l_(676931)

    log = _c_(676925, _n_(676924, "Worklog", lambda: Worklog))
    _l_(676926)
    _c_(676929, _a_(676928, _n_(676927, "log", lambda: log), "start_message"))
    _l_(676930)