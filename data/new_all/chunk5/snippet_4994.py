# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/27453945/where-is-this-typeerror-coming-from
#New User for EPM#
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(669705)

except ImportError:
    pass
try:
    import platform
    _l_(669707)

except ImportError:
    pass
try:
    import sys
    _l_(669709)

except ImportError:
    pass
try:
    from math import *
    _l_(669711)

except ImportError:
    pass
try:
    from PyQt4 import QtCore, QtGui
    _l_(669713)

except ImportError:
    pass
__version__ = '1.0.0'
_l_(669714)



class NewUser(_a_(669716, _n_(669715, "QtGui", lambda: QtGui), "QDialog")):
    _l_(670129)

    def __init__(self, parent):
        _l_(669728)

        _c_(669722, _a_(669720, _n_(669717, "super", lambda: super)(_n_(669718, "NewUser", lambda: NewUser), _n_(669719, "self", lambda: self)), "__init__"), _n_(669721, "parent", lambda: parent))
        _l_(669723)

        _c_(669726, _a_(669725, _n_(669724, "self", lambda: self), "initUi"))
        _l_(669727)

    def initUi(self):
        _l_(669953)


        global name, email, setPass, passRepeat, nameEdit, emailEdit
        _l_(669729)
        global setPassEdit, passRepeatEdit, ccIssueEdit, dbIssueEdit
        _l_(669730)
        global pinEdit, ccIssueChkBx1, ccIssueChkBx2, adminChkBx
        _l_(669731)
        global saveBtn, cancelBtn
        _l_(669732)

        name = _c_(669736, _a_(669734, _n_(669733, "QtGui", lambda: QtGui), "QLabel"), 'Name: ', _n_(669735, "self", lambda: self))
        _l_(669737)
        email = _c_(669741, _a_(669739, _n_(669738, "QtGui", lambda: QtGui), "QLabel"), 'Email: ', _n_(669740, "self", lambda: self))
        _l_(669742)
        setPass = _c_(669746, _a_(669744, _n_(669743, "QtGui", lambda: QtGui), "QLabel"), 'Set Password: ', _n_(669745, "self", lambda: self))
        _l_(669747)
        passRepeat = _c_(669751, _a_(669749, _n_(669748, "QtGui", lambda: QtGui), "QLabel"), 'Repeat Password', _n_(669750, "self", lambda: self))
        _l_(669752)

        nameEdit = _c_(669756, _a_(669754, _n_(669753, "QtGui", lambda: QtGui), "QLineEdit"), _n_(669755, "self", lambda: self))
        _l_(669757)
        emailEdit = _c_(669761, _a_(669759, _n_(669758, "QtGui", lambda: QtGui), "QLineEdit"), _n_(669760, "self", lambda: self))
        _l_(669762)
        setPassEdit = _c_(669766, _a_(669764, _n_(669763, "QtGui", lambda: QtGui), "QLineEdit"), _n_(669765, "self", lambda: self))
        _l_(669767)
        passRepeatEdit = _c_(669771, _a_(669769, _n_(669768, "QtGui", lambda: QtGui), "QLineEdit"), _n_(669770, "self", lambda: self))
        _l_(669772)
        ccIssueEdit = _c_(669776, _a_(669774, _n_(669773, "QtGui", lambda: QtGui), "QLineEdit"), _n_(669775, "self", lambda: self))
        _l_(669777)
        dbIssueEdit = _c_(669781, _a_(669779, _n_(669778, "QtGui", lambda: QtGui), "QLineEdit"), _n_(669780, "self", lambda: self))
        _l_(669782)
        pinEdit = _c_(669786, _a_(669784, _n_(669783, "QtGui", lambda: QtGui), "QLineEdit"), 'PIN', _n_(669785, "self", lambda: self))
        _l_(669787)
        cvcEdit = _c_(669791, _a_(669789, _n_(669788, "QtGui", lambda: QtGui), "QLineEdit"), 'CVC', _n_(669790, "self", lambda: self))
        _l_(669792)

        ccIssueChkBx1 = _c_(669796, _a_(669794, _n_(669793, "QtGui", lambda: QtGui), "QCheckBox"), 'Credit Card Issued', _n_(669795, "self", lambda: self))
        _l_(669797)
        ccIssueChkBx2 = _c_(669801, _a_(669799, _n_(669798, "QtGui", lambda: QtGui), "QCheckBox"), 'Debit Card Issued', _n_(669800, "self", lambda: self))
        _l_(669802)
        adminChkBx = _c_(669806, _a_(669804, _n_(669803, "QtGui", lambda: QtGui), "QCheckBox"), 'Make Admin', _n_(669805, "self", lambda: self))
        _l_(669807)

        saveBtn = _c_(669811, _a_(669809, _n_(669808, "QtGui", lambda: QtGui), "QPushButton"), 'Save and Close', _n_(669810, "self", lambda: self))
        _l_(669812)
        cancelBtn = _c_(669816, _a_(669814, _n_(669813, "QtGui", lambda: QtGui), "QPushButton"), 'Cancel', _n_(669815, "self", lambda: self))
        _l_(669817)

        ui = _c_(669820, _a_(669819, _n_(669818, "QtGui", lambda: QtGui), "QGridLayout"))
        _l_(669821)

        _c_(669825, _a_(669823, _n_(669822, "ui", lambda: ui), "addWidget"), _n_(669824, "name", lambda: name), 1, 0)
        _l_(669826)
        _c_(669830, _a_(669828, _n_(669827, "ui", lambda: ui), "addWidget"), _n_(669829, "email", lambda: email), 2, 0)
        _l_(669831)
        _c_(669835, _a_(669833, _n_(669832, "ui", lambda: ui), "addWidget"), _n_(669834, "setPass", lambda: setPass), 3, 0)
        _l_(669836)
        _c_(669840, _a_(669838, _n_(669837, "ui", lambda: ui), "addWidget"), _n_(669839, "passRepeat", lambda: passRepeat), 4, 0)
        _l_(669841)
        _c_(669845, _a_(669843, _n_(669842, "ui", lambda: ui), "addWidget"), _n_(669844, "nameEdit", lambda: nameEdit), 1, 1, 1, 4)
        _l_(669846)
        _c_(669850, _a_(669848, _n_(669847, "ui", lambda: ui), "addWidget"), _n_(669849, "emailEdit", lambda: emailEdit), 2, 1, 1, 4)
        _l_(669851)
        _c_(669855, _a_(669853, _n_(669852, "ui", lambda: ui), "addWidget"), _n_(669854, "setPassEdit", lambda: setPassEdit), 3, 1, 1, 4)
        _l_(669856)
        _c_(669860, _a_(669858, _n_(669857, "ui", lambda: ui), "addWidget"), _n_(669859, "passRepeatEdit", lambda: passRepeatEdit), 4, 1, 1, 4)
        _l_(669861)
        _c_(669865, _a_(669863, _n_(669862, "ui", lambda: ui), "addWidget"), _n_(669864, "ccIssueEdit", lambda: ccIssueEdit), 5, 1, 1, 3)
        _l_(669866)
        _c_(669870, _a_(669868, _n_(669867, "ui", lambda: ui), "addWidget"), _n_(669869, "cvcEdit", lambda: cvcEdit), 5, 4, 1, 1)
        _l_(669871)
        _c_(669875, _a_(669873, _n_(669872, "ui", lambda: ui), "addWidget"), _n_(669874, "dbIssueEdit", lambda: dbIssueEdit), 6, 1, 1, 3)
        _l_(669876)
        _c_(669880, _a_(669878, _n_(669877, "ui", lambda: ui), "addWidget"), _n_(669879, "pinEdit", lambda: pinEdit), 6, 4, 1, 1)
        _l_(669881)
        _c_(669885, _a_(669883, _n_(669882, "ui", lambda: ui), "addWidget"), _n_(669884, "ccIssueChkBx1", lambda: ccIssueChkBx1), 5, 0)
        _l_(669886)
        _c_(669890, _a_(669888, _n_(669887, "ui", lambda: ui), "addWidget"), _n_(669889, "ccIssueChkBx2", lambda: ccIssueChkBx2), 6, 0)
        _l_(669891)
        _c_(669895, _a_(669893, _n_(669892, "ui", lambda: ui), "addWidget"), _n_(669894, "adminChkBx", lambda: adminChkBx), 7, 4)
        _l_(669896)
        _c_(669900, _a_(669898, _n_(669897, "ui", lambda: ui), "addWidget"), _n_(669899, "saveBtn", lambda: saveBtn), 7, 0)
        _l_(669901)
        _c_(669905, _a_(669903, _n_(669902, "ui", lambda: ui), "addWidget"), _n_(669904, "cancelBtn", lambda: cancelBtn), 7, 1)
        _l_(669906)

        _c_(669912, _a_(669909, _a_(669908, _n_(669907, "ccIssueChkBx1", lambda: ccIssueChkBx1), "stateChanged"), "connect"), _a_(669911, _n_(669910, "self", lambda: self), "ccEn"))
        _l_(669913)
        _c_(669919, _a_(669916, _a_(669915, _n_(669914, "ccIssueChkBx2", lambda: ccIssueChkBx2), "stateChanged"), "connect"), _a_(669918, _n_(669917, "self", lambda: self), "dbEn"))
        _l_(669920)

        _c_(669926, _a_(669923, _a_(669922, _n_(669921, "saveBtn", lambda: saveBtn), "clicked"), "connect"), _a_(669925, _n_(669924, "self", lambda: self), "save"))
        _l_(669927)

        _c_(669930, _a_(669929, _n_(669928, "self", lambda: self), "ccEn"))
        _l_(669931)
        _c_(669934, _a_(669933, _n_(669932, "self", lambda: self), "dbEn"))
        _l_(669935)

        _c_(669939, _a_(669937, _n_(669936, "self", lambda: self), "setLayout"), _n_(669938, "ui", lambda: ui))
        _l_(669940)
        _c_(669943, _a_(669942, _n_(669941, "self", lambda: self), "resize"), 400, 300)
        _l_(669944)
        _c_(669947, _a_(669946, _n_(669945, "self", lambda: self), "center"))
        _l_(669948)
        _c_(669951, _a_(669950, _n_(669949, "self", lambda: self), "show"))
        _l_(669952)

    def ccEn(self):
        _l_(669966)


        if _c_(669956, _a_(669955, _n_(669954, "ccIssueChkBx1", lambda: ccIssueChkBx1), "isChecked")):
            _l_(669965)

            _c_(669959, _a_(669958, _n_(669957, "ccIssueEdit", lambda: ccIssueEdit), "setEnabled"), True)
            _l_(669960)
        else:
            _c_(669963, _a_(669962, _n_(669961, "ccIssueEdit", lambda: ccIssueEdit), "setEnabled"), False)
            _l_(669964)

    def dbEn(self):
        _l_(669987)


        if _c_(669969, _a_(669968, _n_(669967, "ccIssueChkBx2", lambda: ccIssueChkBx2), "isChecked")):
            _l_(669986)

            _c_(669972, _a_(669971, _n_(669970, "dbIssueEdit", lambda: dbIssueEdit), "setEnabled"), True)
            _l_(669973)
            _c_(669976, _a_(669975, _n_(669974, "pinEdit", lambda: pinEdit), "setEnabled"), True)
            _l_(669977)
        else:
            _c_(669980, _a_(669979, _n_(669978, "dbIssueEdit", lambda: dbIssueEdit), "setEnabled"), False)
            _l_(669981)
            _c_(669984, _a_(669983, _n_(669982, "pinEdit", lambda: pinEdit), "setEnabled"), False)
            _l_(669985)

    def save(self, userName, userEmail, userPass, userCC=None, userCVC=None,
            userDB=None, userPin=None, isAdmin=False):
        _l_(670103)


        userName = _c_(669991, _a_(669990, _a_(669989, _n_(669988, "self", lambda: self), "nameEdit"), "text"))
        _l_(669992)
        userEmail = _c_(669996, _a_(669995, _a_(669994, _n_(669993, "self", lambda: self), "emailEdit"), "text"))
        _l_(669997)

        if _c_(670001, _a_(670000, _a_(669999, _n_(669998, "self", lambda: self), "setPassEdit"), "text")) == _c_(670005, _a_(670004, _a_(670003, _n_(670002, "self", lambda: self), "passRepeatEdit"), "text")):
            _l_(670012)

            userPass = _c_(670009, _a_(670008, _a_(670007, _n_(670006, "self", lambda: self), "setPassEdit"), "text"))
            _l_(670010)
        else:
            pass #Throw error here
            _l_(670011) #Throw error here

        if _c_(670016, _a_(670015, _a_(670014, _n_(670013, "self", lambda: self), "ccIssueChkBx1"), "isChecked")):
            _l_(670058)

            if _c_(670020, _n_(670017, "len", lambda: len), _a_(670019, _n_(670018, "self", lambda: self), "ccIssueEdit")) == 15 and _c_(670024, _n_(670021, "len", lambda: len), _a_(670023, _n_(670022, "self", lambda: self), "cvcEdit")) == 4:
                _l_(670057)

                userCC = _c_(670028, _a_(670027, _a_(670026, _n_(670025, "self", lambda: self), "ccIssueEdit"), "text"))
                _l_(670029)
                userCVC = _c_(670033, _a_(670032, _a_(670031, _n_(670030, "self", lambda: self), "cvcEdit"), "text"))
                _l_(670034)
                ccType = 'AMEX'
                _l_(670035)
            elif _c_(670039, _n_(670036, "len", lambda: len), _a_(670038, _n_(670037, "self", lambda: self), "ccIssueEdit")) == 16 and _c_(670043, _n_(670040, "len", lambda: len), _a_(670042, _n_(670041, "self", lambda: self), "cvcEdit")) == 3:
                _l_(670056)

                userCC = _c_(670047, _a_(670046, _a_(670045, _n_(670044, "self", lambda: self), "ccIssueEdit"), "text"))
                _l_(670048)
                userCVC = _c_(670052, _a_(670051, _a_(670050, _n_(670049, "self", lambda: self), "cvcEdit"), "text"))
                _l_(670053)
                ccType = 'MC/Visa'
                _l_(670054)
            else:
                pass #Throw error here
                _l_(670055) #Throw error here

        if _c_(670062, _a_(670061, _a_(670060, _n_(670059, "self", lambda: self), "ccIssueChkBx2"), "isChecked")):
            _l_(670083)

            if _c_(670066, _n_(670063, "len", lambda: len), _a_(670065, _n_(670064, "self", lambda: self), "dbIssueEdit")) == 16 and _c_(670070, _n_(670067, "len", lambda: len), _a_(670069, _n_(670068, "self", lambda: self), "pinEdit")) == 4:
                _l_(670082)

                userDB = _c_(670074, _a_(670073, _a_(670072, _n_(670071, "self", lambda: self), "dbIssueEdit"), "text"))
                _l_(670075)
                userPin = _c_(670079, _a_(670078, _a_(670077, _n_(670076, "self", lambda: self), "pinEdit"), "text"))
                _l_(670080)
            else:
                pass #Throw error here
                _l_(670081) #Throw error here

        if _c_(670087, _a_(670086, _a_(670085, _n_(670084, "self", lambda: self), "adminChkBx"), "isChecked")):
            _l_(670089)

            isAdmin = True
            _l_(670088)

        userSave = _c_(670101, _a_(670091, _n_(670090, "newUser", lambda: newUser), "Save"), _n_(670092, "userName", lambda: userName), _n_(670093, "userEmail", lambda: userEmail), _n_(670094, "userPass", lambda: userPass), _n_(670095, "userCC", lambda: userCC), _n_(670096, "userCVC", lambda: userCVC),
            _n_(670097, "ccType", lambda: ccType), _n_(670098, "userDB", lambda: userDB), _n_(670099, "userPin", lambda: userPin), _n_(670100, "isAdmin", lambda: isAdmin))
        _l_(670102)

    def center(self):
        _l_(670128)


        qr = _c_(670106, _a_(670105, _n_(670104, "self", lambda: self), "frameGeometry"))
        _l_(670107)
        cp = _c_(670114, _a_(670113, _c_(670112, _a_(670111, _c_(670110, _a_(670109, _n_(670108, "QtGui", lambda: QtGui), "QDesktopWidget")), "availableGeometry")), "center"))
        _l_(670115)
        _c_(670119, _a_(670117, _n_(670116, "qr", lambda: qr), "moveCenter"), _n_(670118, "cp", lambda: cp))
        _l_(670120)
        _c_(670126, _a_(670122, _n_(670121, "self", lambda: self), "move"), _c_(670125, _a_(670124, _n_(670123, "qr", lambda: qr), "topLeft")))
        _l_(670127)



class Save(_n_(670130, "object", lambda: object)):
    _l_(670175)

    '''Creates a User Object'''
    _l_(670131)

    def __init__(self, userName, userEmail, userPass, userCC, userCVC, ccType,
        userDB, userPin, isAdmin):
        _l_(670136)


        _c_(670134, _a_(670133, _n_(670132, "self", lambda: self), "create"))
        _l_(670135)

    def create(self):
        _l_(670174)


        list = [_n_(670137, "userName", lambda: userName), _n_(670138, "userEmail", lambda: userEmail), _n_(670139, "userPass", lambda: userPass), _n_(670140, "userCC", lambda: userCC), _n_(670141, "userCVC", lambda: userCVC), _n_(670142, "ccType", lambda: ccType), _n_(670143, "userDB", lambda: userDB),
            _n_(670144, "userPin", lambda: userPin), _n_(670145, "isAdmin", lambda: isAdmin)]
        _l_(670146)

        dirName = _c_(670150, _n_(670147, "str", lambda: str), _a_(670149, _n_(670148, "self", lambda: self), "userName"))
        _l_(670151)
        _c_(670155, _a_(670153, _n_(670152, "os", lambda: os), "mkdir"), _n_(670154, "dirName", lambda: dirName))
        _l_(670156)
        _c_(670160, _a_(670158, _n_(670157, "os", lambda: os), "chdir"), _n_(670159, "dirName", lambda: dirName))
        _l_(670161)

        fileName = _c_(670163, _n_(670162, "open", lambda: open), 'profile.txt', 'wb')
        _l_(670164)
        for i in _n_(670165, "list", lambda: list):
            _l_(670173)

            _c_(670171, _a_(670167, _n_(670166, "fileName", lambda: fileName), "write"), _c_(670170, _n_(670168, "str", lambda: str), _n_(670169, "i", lambda: i)))
            _l_(670172)