# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53689831/exception-in-tkinter-callback-with-typeerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from Tkinter import *
    _l_(674867)

except ImportError:
    pass
try:
    import tkMessageBox
    _l_(674869)

except ImportError:
    pass
course = _c_(674871, _n_(674870, "list", lambda: list))
_l_(674872)

class Course:
    _l_(675108)


    course = _c_(674874, _n_(674873, "list", lambda: list))
    _l_(674875)
    def __init__(self, longName, shortName, professor):
        _l_(674885)

        _n_(674876, "self", lambda: self).longName = _n_(674877, "longName", lambda: longName)
        _l_(674878)
        _n_(674879, "self", lambda: self).shortName = _n_(674880, "shortName", lambda: shortName)
        _l_(674881)
        _n_(674882, "self", lambda: self).professor = _n_(674883, "professor", lambda: professor)
        _l_(674884)

    @_n_(674886, "staticmethod", lambda: staticmethod)
    def importCourses():
        _l_(674915)

        n=0
        _l_(674887)
        _n_(674888, "course", lambda: course)[:] = []
        _l_(674889)
        with _c_(674891, _n_(674890, "open", lambda: open), 'Courses.txt', 'r') as f:
            _l_(674914)

            for line in _n_(674892, "f", lambda: f):
                _l_(674913)

                if _n_(674893, "line", lambda: line) == '\n':
                    _l_(674895)

                    continue
                    _l_(674894)
                longName, shortName, professor = _c_(674900, _a_(674899, _c_(674898, _a_(674897, _n_(674896, "line", lambda: line), "rstrip"), "\n\r"), "split"), '-')
                _l_(674901)
                _c_(674909, _a_(674903, _n_(674902, "course", lambda: course), "append"), _c_(674908, _n_(674904, "Course", lambda: Course), _n_(674905, "longName", lambda: longName), _n_(674906, "shortName", lambda: shortName), _n_(674907, "professor", lambda: professor)))
                _l_(674910)
                n=_n_(674911, "n", lambda: n)+1
                _l_(674912)
    @_n_(674916, "classmethod", lambda: classmethod)
    def createCourse(cls, newLongName, newShortName, newProfessor):
        _l_(674949)

        with _c_(674918, _n_(674917, "open", lambda: open), 'Courses.txt', 'r') as g:
            _l_(674923)

            lines = _c_(674921, _a_(674920, _n_(674919, "g", lambda: g), "readlines"))
            _l_(674922)
        with _c_(674925, _n_(674924, "open", lambda: open), 'Courses.txt', 'a') as f:
            _l_(674944)

            for line in _n_(674926, "lines", lambda: lines):
                _l_(674936)

                if ('-' + _n_(674927, "newShortName", lambda: newShortName) + '-') in _n_(674928, "line", lambda: line):
                    _l_(674935)

                    _c_(674932, _a_(674930, _n_(674929, "tkMessageBox", lambda: tkMessageBox), "showinfo"), "Oops!", "There is already a Course with the name " + _n_(674931, "newShortName", lambda: newShortName) + '.')
                    _l_(674933)
                    aux = ""
                    _l_(674934)
                    return aux
            _c_(674942, _a_(674938, _n_(674937, "f", lambda: f), "write"), _n_(674939, "newLongName", lambda: newLongName) + '-' + _n_(674940, "newShortName", lambda: newShortName) + '-' + _n_(674941, "newProfessor", lambda: newProfessor))
            _l_(674943)
        _c_(674947, _a_(674946, _n_(674945, "Course", lambda: Course), "importCourses"))
        _l_(674948)
    @_n_(674950, "staticmethod", lambda: staticmethod)

    def createCourseEntry(self):
        _l_(675035)

        createCourseEntryWindow = _c_(674953, _n_(674951, "Toplevel", lambda: Toplevel), _n_(674952, "self", lambda: self))
        _l_(674954)
        newCourseSNameLabel = _c_(674957, _n_(674955, "Label", lambda: Label), _n_(674956, "createCourseEntryWindow", lambda: createCourseEntryWindow), text="Course Short Name:")
        _l_(674958)
        _c_(674961, _a_(674960, _n_(674959, "newCourseSNameLabel", lambda: newCourseSNameLabel), "grid"), row=0,column=0)
        _l_(674962)
        newCourseLNameLabel = _c_(674965, _n_(674963, "Label", lambda: Label), _n_(674964, "createCourseEntryWindow", lambda: createCourseEntryWindow), text="Course Long Name:")
        _l_(674966)
        _c_(674969, _a_(674968, _n_(674967, "newCourseLNameLabel", lambda: newCourseLNameLabel), "grid"), row=1,column=0)
        _l_(674970)
        newCourseProfessorLabel = _c_(674973, _n_(674971, "Label", lambda: Label), _n_(674972, "createCourseEntryWindow", lambda: createCourseEntryWindow), text="Course Professor:")
        _l_(674974)
        _c_(674977, _a_(674976, _n_(674975, "newCourseProfessorLabel", lambda: newCourseProfessorLabel), "grid"), row=2,column=0)
        _l_(674978)
        newCourseSNameEntry = _c_(674981, _n_(674979, "Entry", lambda: Entry), _n_(674980, "createCourseEntryWindow", lambda: createCourseEntryWindow))
        _l_(674982)
        _c_(674985, _a_(674984, _n_(674983, "newCourseSNameEntry", lambda: newCourseSNameEntry), "grid"), row=0,column=1)
        _l_(674986)
        newCourseLNameEntry = _c_(674989, _n_(674987, "Entry", lambda: Entry), _n_(674988, "createCourseEntryWindow", lambda: createCourseEntryWindow))
        _l_(674990)
        _c_(674993, _a_(674992, _n_(674991, "newCourseLNameEntry", lambda: newCourseLNameEntry), "grid"), row=1,column=1)
        _l_(674994)
        newCourseProfessorEntry = _c_(674997, _n_(674995, "Entry", lambda: Entry), _n_(674996, "createCourseEntryWindow", lambda: createCourseEntryWindow))
        _l_(674998)
        _c_(675001, _a_(675000, _n_(674999, "newCourseProfessorEntry", lambda: newCourseProfessorEntry), "grid"), row=2,column=1)
        _l_(675002)

        createNewCourseButton = _c_(675017, _n_(675003, "Button", lambda: Button), _n_(675004, "createCourseEntryWindow", lambda: createCourseEntryWindow), text="Create", 
                      command=_c_(675016, _a_(675006, _n_(675005, "Course", lambda: Course), "createCourse"), _c_(675009, _a_(675008, _n_(675007, "newCourseSNameEntry", lambda: newCourseSNameEntry), "get")),_c_(675012, _a_(675011, _n_(675010, "newCourseLNameEntry", lambda: newCourseLNameEntry), "get")),_c_(675015, _a_(675014, _n_(675013, "newCourseProfessorEntry", lambda: newCourseProfessorEntry), "get"))))
        _l_(675018)
        _c_(675021, _a_(675020, _n_(675019, "createNewCourseButton", lambda: createNewCourseButton), "grid"), row=3,column=0)
        _l_(675022)
        cancelCreation = _c_(675029, _n_(675023, "Button", lambda: Button), _n_(675024, "createCourseEntryWindow", lambda: createCourseEntryWindow), text="Cancel", command=lambda win=_n_(675025, "top", lambda: top): _c_(675028, _a_(675027, _n_(675026, "win", lambda: win), "destroy")))
        _l_(675030)
        _c_(675033, _a_(675032, _n_(675031, "cancelCreation", lambda: cancelCreation), "grid"), row=3,column=1)
        _l_(675034)

    def deleteCourse(deleteShortName):
        _l_(675060)

        with _c_(675037, _n_(675036, "open", lambda: open), 'Courses.txt', 'r') as f:
            _l_(675042)

            lines = _c_(675040, _a_(675039, _n_(675038, "f", lambda: f), "readlines"))
            _l_(675041)
        with _c_(675044, _n_(675043, "open", lambda: open), 'Courses.txt', 'w') as g:
            _l_(675055)

            for line in _n_(675045, "lines", lambda: lines):
                _l_(675054)

                if ('-'+_n_(675046, "deleteShortName", lambda: deleteShortName)+'-') not in _n_(675047, "line", lambda: line):
                    _l_(675053)

                    _c_(675051, _a_(675049, _n_(675048, "g", lambda: g), "write"), _n_(675050, "line", lambda: line))
                    _l_(675052)
        _c_(675058, _a_(675057, _n_(675056, "Course", lambda: Course), "importCourses"))
        _l_(675059)

    def deleteCourseEntry(self):
        _l_(675107)

        deleteCourseEntryWindow = _c_(675063, _n_(675061, "TopLevel", lambda: TopLevel), _n_(675062, "self", lambda: self))
        _l_(675064)
        deleteCourseLabel = _c_(675067, _n_(675065, "Label", lambda: Label), _n_(675066, "deleteCourseEntryWindow", lambda: deleteCourseEntryWindow), text="Course Short Name:")
        _l_(675068)
        _c_(675071, _a_(675070, _n_(675069, "deleteCourseLabel", lambda: deleteCourseLabel), "grid"), row=0, column=0)
        _l_(675072)
        deleteCourseSNameEntry = _c_(675075, _n_(675073, "Entry", lambda: Entry), _n_(675074, "deleteCourseEntryWindow", lambda: deleteCourseEntryWindow))
        _l_(675076)
        _c_(675079, _a_(675078, _n_(675077, "deleteCourseSNameEntry", lambda: deleteCourseSNameEntry), "grid"), row=0,column=1)
        _l_(675080)

        deleteCourseButton = _c_(675089, _n_(675081, "Button", lambda: Button), _n_(675082, "deleteCourseEntryWindow", lambda: deleteCourseEntryWindow), text="Delete", 
                      command=_c_(675088, _a_(675084, _n_(675083, "Course", lambda: Course), "deleteCourse"), _c_(675087, _a_(675086, _n_(675085, "deleteCourseSNameEntry", lambda: deleteCourseSNameEntry), "get"))))
        _l_(675090)
        _c_(675093, _a_(675092, _n_(675091, "deleteCourseButton", lambda: deleteCourseButton), "grid"), row=1,column=0)
        _l_(675094)
        cancelDeletion = _c_(675101, _n_(675095, "Button", lambda: Button), _n_(675096, "deleteCourseEntryWindow", lambda: deleteCourseEntryWindow), text="Cancel", command=lambda win=_n_(675097, "top", lambda: top): _c_(675100, _a_(675099, _n_(675098, "win", lambda: win), "destroy")))
        _l_(675102)
        _c_(675105, _a_(675104, _n_(675103, "cancelDeletion", lambda: cancelDeletion), "grid"), row=1,column=1)
        _l_(675106)


_c_(675111, _a_(675110, _n_(675109, "Course", lambda: Course), "importCourses"))
_l_(675112)
# Course.deleteCourse('LIT2380')
#Course.createCourse('Literature by Women','LIT2380','Alexandra Asbille')

root = _c_(675114, _n_(675113, "Tk", lambda: Tk))
_l_(675115)

createCourseWindowButton = _c_(675120, _n_(675116, "Button", lambda: Button), _n_(675117, "root", lambda: root), text= 'Create Course', relief='solid', command=_a_(675119, _n_(675118, "Course", lambda: Course), "createCourseEntry"))
_l_(675121)
_c_(675124, _a_(675123, _n_(675122, "createCourseWindowButton", lambda: createCourseWindowButton), "grid"), row=0, column=0)
_l_(675125)
deleteCourseWindowButton = _c_(675130, _n_(675126, "Button", lambda: Button), _n_(675127, "root", lambda: root), text= 'Delete Course', relief='solid', command=_a_(675129, _n_(675128, "Course", lambda: Course), "deleteCourseEntry"))
_l_(675131)
_c_(675134, _a_(675133, _n_(675132, "deleteCourseWindowButton", lambda: deleteCourseWindowButton), "grid"), row=0, column=1)
_l_(675135)

courseSNameLabels = _c_(675137, _n_(675136, "list", lambda: list))
_l_(675138)
courseLNameLabels = _c_(675140, _n_(675139, "list", lambda: list))
_l_(675141)
courseProfessorLabels = _c_(675143, _n_(675142, "list", lambda: list))
_l_(675144)

for x in _c_(675149, _n_(675145, "range", lambda: range), 0,_c_(675148, _n_(675146, "len", lambda: len), _n_(675147, "course", lambda: course))):
    _l_(675160)

    _c_(675158, _a_(675151, _n_(675150, "courseSNameLabels", lambda: courseSNameLabels), "append"), _c_(675157, _n_(675152, "Label", lambda: Label), _n_(675153, "root", lambda: root), text= _a_(675156, _n_(675154, "course", lambda: course)[_n_(675155, "x", lambda: x)], "shortName"), relief='solid'))
    _l_(675159)
for x in _c_(675165, _n_(675161, "range", lambda: range), 0,_c_(675164, _n_(675162, "len", lambda: len), _n_(675163, "course", lambda: course))):
    _l_(675176)

    _c_(675174, _a_(675167, _n_(675166, "courseLNameLabels", lambda: courseLNameLabels), "append"), _c_(675173, _n_(675168, "Label", lambda: Label), _n_(675169, "root", lambda: root), text= _a_(675172, _n_(675170, "course", lambda: course)[_n_(675171, "x", lambda: x)], "longName"), relief='solid'))
    _l_(675175)
for x in _c_(675181, _n_(675177, "range", lambda: range), 0,_c_(675180, _n_(675178, "len", lambda: len), _n_(675179, "course", lambda: course))):
    _l_(675192)

    _c_(675190, _a_(675183, _n_(675182, "courseProfessorLabels", lambda: courseProfessorLabels), "append"), _c_(675189, _n_(675184, "Label", lambda: Label), _n_(675185, "root", lambda: root), text= _a_(675188, _n_(675186, "course", lambda: course)[_n_(675187, "x", lambda: x)], "professor"), relief='solid'))
    _l_(675191)

m=1
_l_(675193)
for y in _n_(675194, "courseSNameLabels", lambda: courseSNameLabels):
    _l_(675202)

    _c_(675198, _a_(675196, _n_(675195, "y", lambda: y), "grid"), row=_n_(675197, "m", lambda: m))
    _l_(675199)
    m=_n_(675200, "m", lambda: m)+1
    _l_(675201)
m=1
_l_(675203)
for y in _n_(675204, "courseLNameLabels", lambda: courseLNameLabels):
    _l_(675212)

    _c_(675208, _a_(675206, _n_(675205, "y", lambda: y), "grid"), row=_n_(675207, "m", lambda: m), column=1)
    _l_(675209)
    m=_n_(675210, "m", lambda: m)+1
    _l_(675211)
m=1
_l_(675213)
for y in _n_(675214, "courseProfessorLabels", lambda: courseProfessorLabels):
    _l_(675222)

    _c_(675218, _a_(675216, _n_(675215, "y", lambda: y), "grid"), row=_n_(675217, "m", lambda: m), column=2)
    _l_(675219)
    m=_n_(675220, "m", lambda: m)+1
    _l_(675221)
_c_(675225, _a_(675224, _n_(675223, "root", lambda: root), "mainloop"))
_l_(675226)