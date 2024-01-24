# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56174450/why-do-i-keep-getting-the-attributeerror-str-object-has-no-attribute-student
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
ONE = 1
_l_(460893)
TWO = 2
_l_(460894)
THREE = 3
_l_(460895)
FOUR = 4
_l_(460896)
FIVE = 5
_l_(460897)

TRUE = True
_l_(460898)
FALSE = False
_l_(460899)

COURSES_INPUT = 'courses-sample.txt'
_l_(460900)
STUDENTS_INPUT= 'students-sample.txt'
_l_(460901)
try:
    import student
    _l_(460903)

except ImportError:
    pass
try:
    import course
    _l_(460905)

except ImportError:
    pass



def main():
    _l_(460994)


    _c_(460907, _n_(460906, "process_students", lambda: process_students))
    _l_(460908)
    _c_(460910, _n_(460909, "process_courses", lambda: process_courses))
    _l_(460911)
    option = _c_(460913, _n_(460912, "get_option", lambda: get_option))
    _l_(460914)
    while _n_(460915, "option", lambda: option) != 5:
        _l_(460985)

        if _n_(460916, "option", lambda: option) == 1:
            _l_(460946)


            course_num = _c_(460918, _n_(460917, "input", lambda: input), 'please input course number of course you wish to add: ')
            _l_(460919)
            add_course = _c_(460923, _a_(460921, _n_(460920, "new_student", lambda: new_student), "add_course"), _n_(460922, "course_num", lambda: course_num))
            _l_(460924)
            while _n_(460925, "add_course", lambda: add_course) == _n_(460926, "FALSE", lambda: FALSE):
                _l_(460933)

                _c_(460928, _n_(460927, "print", lambda: print), 'The course requested for add does not exist. Please Try Again.')
                _l_(460929)
                course_num = _c_(460931, _n_(460930, "input", lambda: input), 'Please input course number of course you wish to add: ')
                _l_(460932)
            if _c_(460936, _a_(460935, _n_(460934, "new_course", lambda: new_course), "space_available")) == _n_(460937, "TRUE", lambda: TRUE):
                _l_(460945)

                _c_(460940, _a_(460939, _n_(460938, "new_course", lambda: new_course), "enroll_student"))
                _l_(460941)
            else:
                _c_(460943, _n_(460942, "print", lambda: print), 'Class requested does not have any seats available.')
                _l_(460944)

        if _n_(460947, "option", lambda: option) == 2:
            _l_(460969)

            course_num = _c_(460949, _n_(460948, "input", lambda: input), 'please input course number of course you wish to drop: ')
            _l_(460950)
            drop_course = _c_(460954, _a_(460952, _n_(460951, "new_student", lambda: new_student), "drop_course"), _n_(460953, "course_num", lambda: course_num))
            _l_(460955)
            while _n_(460956, "drop_course", lambda: drop_course) == _n_(460957, "FALSE", lambda: FALSE):
                _l_(460964)

                _c_(460959, _n_(460958, "print", lambda: print), 'The enrolled course requested for drop does not exist. Please Try Again.')
                _l_(460960)
                course_num = _c_(460962, _n_(460961, "input", lambda: input), 'Please input course number of course you wish to drop: ')
                _l_(460963)
            _c_(460967, _a_(460966, _n_(460965, "new_course", lambda: new_course), "drop_student"))
            _l_(460968)

        if _n_(460970, "option", lambda: option) == 3:
            _l_(460975)

            _c_(460973, _n_(460971, "print_student_info", lambda: print_student_info), _n_(460972, "student_dict", lambda: student_dict))
            _l_(460974)
        if _n_(460976, "option", lambda: option) == 4:
            _l_(460981)

            _c_(460979, _n_(460977, "print_course_schedule", lambda: print_course_schedule), _n_(460978, "course_dict", lambda: course_dict))
            _l_(460980)
        option = _c_(460983, _n_(460982, "get_option", lambda: get_option))
        _l_(460984)
    _c_(460988, _n_(460986, "write_updated", lambda: write_updated), 'students-updated.txt',_n_(460987, "student_dict", lambda: student_dict))
    _l_(460989)
    _c_(460992, _n_(460990, "write_updated", lambda: write_updated), 'courses-updated.txt',_n_(460991, "course_dict", lambda: course_dict))
    _l_(460993)



def print_menu():
    _l_(461013)

    _c_(460996, _n_(460995, "print", lambda: print), "1. Add course")
    _l_(460997)
    _c_(460999, _n_(460998, "print", lambda: print), "2. Drop course")
    _l_(461000)
    _c_(461002, _n_(461001, "print", lambda: print), "3. Print student's schedule")
    _l_(461003)
    _c_(461005, _n_(461004, "print", lambda: print), "4. Print course schedule")
    _l_(461006)
    _c_(461008, _n_(461007, "print", lambda: print), "5. Done")
    _l_(461009)
    _c_(461011, _n_(461010, "print", lambda: print), "")
    _l_(461012)

def get_option():
    _l_(461032)

    _c_(461015, _n_(461014, "print_menu", lambda: print_menu))
    _l_(461016)
    choice = _c_(461018, _n_(461017, "input", lambda: input), "What would you like to do? ")
    _l_(461019)
    while _n_(461020, "choice", lambda: choice) not in _c_(461022, _n_(461021, "range", lambda: range), 1,6):
        _l_(461029)

        _c_(461024, _n_(461023, "print_menu", lambda: print_menu))
        _l_(461025)
        choice = _c_(461027, _n_(461026, "input", lambda: input), "Choice is invalid. What would you like to do? ")
        _l_(461028)
    aux = _n_(461030, "choice", lambda: choice)
    _l_(461031)
    return aux

def process_students():
    _l_(461074)

    student_dict = {}
    _l_(461033)
    student_info = _c_(461036, _n_(461034, "open", lambda: open), _n_(461035, "STUDENTS_INPUT", lambda: STUDENTS_INPUT),"r")
    _l_(461037)
    for student in _n_(461038, "student_info", lambda: student_info):
        _l_(461069)

        info_list = _c_(461041, _a_(461040, _n_(461039, "student", lambda: student), "split"), ":")
        _l_(461042)
        new_id = _n_(461043, "info_list", lambda: info_list)[0]
        _l_(461044)
        first_name = _n_(461045, "info_list", lambda: info_list)[1]
        _l_(461046)
        last_name = _n_(461047, "info_list", lambda: info_list)[2]
        _l_(461048)
        course_list = _n_(461049, "info_list", lambda: info_list)[3:]
        _l_(461050)
        new_student = _c_(461057, _a_(461052, _n_(461051, "student", lambda: student), "Student"), _n_(461053, "new_id", lambda: new_id), _n_(461054, "first_name", lambda: first_name), _n_(461055, "last_name", lambda: last_name), _n_(461056, "course_list", lambda: course_list))
        _l_(461058)
        _c_(461063, _n_(461059, "print", lambda: print), _c_(461062, _a_(461061, _n_(461060, "new_student", lambda: new_student), "line_for_file")))
        _l_(461064)
        _n_(461065, "student_dict", lambda: student_dict)[_n_(461066, "new_eid", lambda: new_eid)] = _n_(461067, "new_student", lambda: new_student)
        _l_(461068)
    _c_(461072, _a_(461071, _n_(461070, "student_info", lambda: student_info), "close"))
    _l_(461073)

def process_courses():
    _l_(461113)

    course_dict = {}
    _l_(461075)
    course_info = _c_(461078, _n_(461076, "open", lambda: open), _n_(461077, "COURSES_INPUT", lambda: COURSES_INPUT),"r")
    _l_(461079)
    for course in _n_(461080, "course_info", lambda: course_info):
        _l_(461108)

        info_list = _c_(461083, _a_(461082, _n_(461081, "course", lambda: course), "split"), ";")
        _l_(461084)
        unique_num = _n_(461085, "info_list", lambda: info_list)[0]
        _l_(461086)
        class_name = _n_(461087, "info_list", lambda: info_list)[1]
        _l_(461088)
        prof = _n_(461089, "info_list", lambda: info_list)[2]
        _l_(461090)
        seats = _n_(461091, "info_list", lambda: info_list)[3]
        _l_(461092)
        capacity = _n_(461093, "info_list", lambda: info_list)[4]
        _l_(461094)
        new_course = _c_(461102, _a_(461096, _n_(461095, "course", lambda: course), "Course"), _n_(461097, "unique_num", lambda: unique_num), _n_(461098, "class_name", lambda: class_name), _n_(461099, "prof", lambda: prof), _n_(461100, "seats", lambda: seats), _n_(461101, "capacity", lambda: capacity))
        _l_(461103)
        _n_(461104, "course_dict", lambda: course_dict)[_n_(461105, "unique_num", lambda: unique_num)] = _n_(461106, "new_course", lambda: new_course)
        _l_(461107)
    _c_(461111, _a_(461110, _n_(461109, "course_info", lambda: course_info), "close"))
    _l_(461112)

def print_course_schedule(course_dict):
    _l_(461120)

    for value in _n_(461114, "course_dict", lambda: course_dict):
        _l_(461119)

        _c_(461117, _n_(461115, "print", lambda: print), _n_(461116, "value", lambda: value))
        _l_(461118)

def print_student_info(student_dict):
    _l_(461127)

    for value in _n_(461121, "student_dict", lambda: student_dict):
        _l_(461126)

        _c_(461124, _n_(461122, "print", lambda: print), _n_(461123, "value", lambda: value))
        _l_(461125)

def get_id():
    _l_(461139)

    eid = _c_(461129, _n_(461128, "input", lambda: input), "What is the UT EID? ")
    _l_(461130)
    while _n_(461131, "eid", lambda: eid) not in _n_(461132, "student_dict", lambda: student_dict):
        _l_(461136)

        eid = _c_(461134, _n_(461133, "input", lambda: input), "Invalid UT EID. Please re-enter: ")
        _l_(461135)
    aux = _n_(461137, "eid", lambda: eid)
    _l_(461138)
    return aux

def get_unique():
    _l_(461151)

    unique = _c_(461141, _n_(461140, "input", lambda: input), "What is the course unique number? ")
    _l_(461142)
    while _n_(461143, "unique", lambda: unique) not in _n_(461144, "course_dict", lambda: course_dict):
        _l_(461148)

        unique = _c_(461146, _n_(461145, "input", lambda: input), "Invalid unique number. Please re-enter: ")
        _l_(461147)
    aux = _n_(461149, "unique", lambda: unique)
    _l_(461150)
    return aux


def write_updated(filename,dictionary):
    _l_(461168)

    output_file = _c_(461154, _n_(461152, "open", lambda: open), _n_(461153, "filename", lambda: filename),'w')
    _l_(461155)

    for key in _n_(461156, "dictionary", lambda: dictionary):
        _l_(461163)

        _c_(461161, _a_(461158, _n_(461157, "output_file", lambda: output_file), "write"), _n_(461159, "dictionary", lambda: dictionary)[_n_(461160, "key", lambda: key)])
        _l_(461162)
    _c_(461166, _a_(461165, _n_(461164, "output_file", lambda: output_file), "close"))
    _l_(461167)
_c_(461170, _n_(461169, "main", lambda: main))
_l_(461171)