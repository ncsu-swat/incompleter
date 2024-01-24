# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/27453945/where-is-this-typeerror-coming-from
#New User for EPM#
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(693963)

except ImportError:
    pass
try:
    import platform
    _l_(693965)

except ImportError:
    pass
try:
    import sys
    _l_(693967)

except ImportError:
    pass
try:
    from math import *
    _l_(693969)

except ImportError:
    pass
try:
    from PyQt4 import QtCore, QtGui
    _l_(693971)

except ImportError:
    pass
__version__ = '1.0.0'
_l_(693972)



class NewUser(_a_(693974, _n_(693973, "QtGui", lambda: QtGui), "QDialog")):
    _l_(694387)

    def __init__(self, parent):
        _l_(693986)

        _c_(693980, _a_(693978, _n_(693975, "super", lambda: super)(_n_(693976, "NewUser", lambda: NewUser), _n_(693977, "self", lambda: self)), "__init__"), _n_(693979, "parent", lambda: parent))
        _l_(693981)

        _c_(693984, _a_(693983, _n_(693982, "self", lambda: self), "initUi"))
        _l_(693985)

    def initUi(self):
        _l_(694211)


        global name, email, setPass, passRepeat, nameEdit, emailEdit
        _l_(693987)
        global setPassEdit, passRepeatEdit, ccIssueEdit, dbIssueEdit
        _l_(693988)
        global pinEdit, ccIssueChkBx1, ccIssueChkBx2, adminChkBx
        _l_(693989)
        global saveBtn, cancelBtn
        _l_(693990)

        name = _c_(693994, _a_(693992, _n_(693991, "QtGui", lambda: QtGui), "QLabel"), 'Name: ', _n_(693993, "self", lambda: self))
        _l_(693995)
        email = _c_(693999, _a_(693997, _n_(693996, "QtGui", lambda: QtGui), "QLabel"), 'Email: ', _n_(693998, "self", lambda: self))
        _l_(694000)
        setPass = _c_(694004, _a_(694002, _n_(694001, "QtGui", lambda: QtGui), "QLabel"), 'Set Password: ', _n_(694003, "self", lambda: self))
        _l_(694005)
        passRepeat = _c_(694009, _a_(694007, _n_(694006, "QtGui", lambda: QtGui), "QLabel"), 'Repeat Password', _n_(694008, "self", lambda: self))
        _l_(694010)

        nameEdit = _c_(694014, _a_(694012, _n_(694011, "QtGui", lambda: QtGui), "QLineEdit"), _n_(694013, "self", lambda: self))
        _l_(694015)
        emailEdit = _c_(694019, _a_(694017, _n_(694016, "QtGui", lambda: QtGui), "QLineEdit"), _n_(694018, "self", lambda: self))
        _l_(694020)
        setPassEdit = _c_(694024, _a_(694022, _n_(694021, "QtGui", lambda: QtGui), "QLineEdit"), _n_(694023, "self", lambda: self))
        _l_(694025)
        passRepeatEdit = _c_(694029, _a_(694027, _n_(694026, "QtGui", lambda: QtGui), "QLineEdit"), _n_(694028, "self", lambda: self))
        _l_(694030)
        ccIssueEdit = _c_(694034, _a_(694032, _n_(694031, "QtGui", lambda: QtGui), "QLineEdit"), _n_(694033, "self", lambda: self))
        _l_(694035)
        dbIssueEdit = _c_(694039, _a_(694037, _n_(694036, "QtGui", lambda: QtGui), "QLineEdit"), _n_(694038, "self", lambda: self))
        _l_(694040)
        pinEdit = _c_(694044, _a_(694042, _n_(694041, "QtGui", lambda: QtGui), "QLineEdit"), 'PIN', _n_(694043, "self", lambda: self))
        _l_(694045)
        cvcEdit = _c_(694049, _a_(694047, _n_(694046, "QtGui", lambda: QtGui), "QLineEdit"), 'CVC', _n_(694048, "self", lambda: self))
        _l_(694050)

        ccIssueChkBx1 = _c_(694054, _a_(694052, _n_(694051, "QtGui", lambda: QtGui), "QCheckBox"), 'Credit Card Issued', _n_(694053, "self", lambda: self))
        _l_(694055)
        ccIssueChkBx2 = _c_(694059, _a_(694057, _n_(694056, "QtGui", lambda: QtGui), "QCheckBox"), 'Debit Card Issued', _n_(694058, "self", lambda: self))
        _l_(694060)
        adminChkBx = _c_(694064, _a_(694062, _n_(694061, "QtGui", lambda: QtGui), "QCheckBox"), 'Make Admin', _n_(694063, "self", lambda: self))
        _l_(694065)

        saveBtn = _c_(694069, _a_(694067, _n_(694066, "QtGui", lambda: QtGui), "QPushButton"), 'Save and Close', _n_(694068, "self", lambda: self))
        _l_(694070)
        cancelBtn = _c_(694074, _a_(694072, _n_(694071, "QtGui", lambda: QtGui), "QPushButton"), 'Cancel', _n_(694073, "self", lambda: self))
        _l_(694075)

        ui = _c_(694078, _a_(694077, _n_(694076, "QtGui", lambda: QtGui), "QGridLayout"))
        _l_(694079)

        _c_(694083, _a_(694081, _n_(694080, "ui", lambda: ui), "addWidget"), _n_(694082, "name", lambda: name), 1, 0)
        _l_(694084)
        _c_(694088, _a_(694086, _n_(694085, "ui", lambda: ui), "addWidget"), _n_(694087, "email", lambda: email), 2, 0)
        _l_(694089)
        _c_(694093, _a_(694091, _n_(694090, "ui", lambda: ui), "addWidget"), _n_(694092, "setPass", lambda: setPass), 3, 0)
        _l_(694094)
        _c_(694098, _a_(694096, _n_(694095, "ui", lambda: ui), "addWidget"), _n_(694097, "passRepeat", lambda: passRepeat), 4, 0)
        _l_(694099)
        _c_(694103, _a_(694101, _n_(694100, "ui", lambda: ui), "addWidget"), _n_(694102, "nameEdit", lambda: nameEdit), 1, 1, 1, 4)
        _l_(694104)
        _c_(694108, _a_(694106, _n_(694105, "ui", lambda: ui), "addWidget"), _n_(694107, "emailEdit", lambda: emailEdit), 2, 1, 1, 4)
        _l_(694109)
        _c_(694113, _a_(694111, _n_(694110, "ui", lambda: ui), "addWidget"), _n_(694112, "setPassEdit", lambda: setPassEdit), 3, 1, 1, 4)
        _l_(694114)
        _c_(694118, _a_(694116, _n_(694115, "ui", lambda: ui), "addWidget"), _n_(694117, "passRepeatEdit", lambda: passRepeatEdit), 4, 1, 1, 4)
        _l_(694119)
        _c_(694123, _a_(694121, _n_(694120, "ui", lambda: ui), "addWidget"), _n_(694122, "ccIssueEdit", lambda: ccIssueEdit), 5, 1, 1, 3)
        _l_(694124)
        _c_(694128, _a_(694126, _n_(694125, "ui", lambda: ui), "addWidget"), _n_(694127, "cvcEdit", lambda: cvcEdit), 5, 4, 1, 1)
        _l_(694129)
        _c_(694133, _a_(694131, _n_(694130, "ui", lambda: ui), "addWidget"), _n_(694132, "dbIssueEdit", lambda: dbIssueEdit), 6, 1, 1, 3)
        _l_(694134)
        _c_(694138, _a_(694136, _n_(694135, "ui", lambda: ui), "addWidget"), _n_(694137, "pinEdit", lambda: pinEdit), 6, 4, 1, 1)
        _l_(694139)
        _c_(694143, _a_(694141, _n_(694140, "ui", lambda: ui), "addWidget"), _n_(694142, "ccIssueChkBx1", lambda: ccIssueChkBx1), 5, 0)
        _l_(694144)
        _c_(694148, _a_(694146, _n_(694145, "ui", lambda: ui), "addWidget"), _n_(694147, "ccIssueChkBx2", lambda: ccIssueChkBx2), 6, 0)
        _l_(694149)
        _c_(694153, _a_(694151, _n_(694150, "ui", lambda: ui), "addWidget"), _n_(694152, "adminChkBx", lambda: adminChkBx), 7, 4)
        _l_(694154)
        _c_(694158, _a_(694156, _n_(694155, "ui", lambda: ui), "addWidget"), _n_(694157, "saveBtn", lambda: saveBtn), 7, 0)
        _l_(694159)
        _c_(694163, _a_(694161, _n_(694160, "ui", lambda: ui), "addWidget"), _n_(694162, "cancelBtn", lambda: cancelBtn), 7, 1)
        _l_(694164)

        _c_(694170, _a_(694167, _a_(694166, _n_(694165, "ccIssueChkBx1", lambda: ccIssueChkBx1), "stateChanged"), "connect"), _a_(694169, _n_(694168, "self", lambda: self), "ccEn"))
        _l_(694171)
        _c_(694177, _a_(694174, _a_(694173, _n_(694172, "ccIssueChkBx2", lambda: ccIssueChkBx2), "stateChanged"), "connect"), _a_(694176, _n_(694175, "self", lambda: self), "dbEn"))
        _l_(694178)

        _c_(694184, _a_(694181, _a_(694180, _n_(694179, "saveBtn", lambda: saveBtn), "clicked"), "connect"), _a_(694183, _n_(694182, "self", lambda: self), "save"))
        _l_(694185)

        _c_(694188, _a_(694187, _n_(694186, "self", lambda: self), "ccEn"))
        _l_(694189)
        _c_(694192, _a_(694191, _n_(694190, "self", lambda: self), "dbEn"))
        _l_(694193)

        _c_(694197, _a_(694195, _n_(694194, "self", lambda: self), "setLayout"), _n_(694196, "ui", lambda: ui))
        _l_(694198)
        _c_(694201, _a_(694200, _n_(694199, "self", lambda: self), "resize"), 400, 300)
        _l_(694202)
        _c_(694205, _a_(694204, _n_(694203, "self", lambda: self), "center"))
        _l_(694206)
        _c_(694209, _a_(694208, _n_(694207, "self", lambda: self), "show"))
        _l_(694210)

    def ccEn(self):
        _l_(694224)


        if _c_(694214, _a_(694213, _n_(694212, "ccIssueChkBx1", lambda: ccIssueChkBx1), "isChecked")):
            _l_(694223)

            _c_(694217, _a_(694216, _n_(694215, "ccIssueEdit", lambda: ccIssueEdit), "setEnabled"), True)
            _l_(694218)
        else:
            _c_(694221, _a_(694220, _n_(694219, "ccIssueEdit", lambda: ccIssueEdit), "setEnabled"), False)
            _l_(694222)

    def dbEn(self):
        _l_(694245)


        if _c_(694227, _a_(694226, _n_(694225, "ccIssueChkBx2", lambda: ccIssueChkBx2), "isChecked")):
            _l_(694244)

            _c_(694230, _a_(694229, _n_(694228, "dbIssueEdit", lambda: dbIssueEdit), "setEnabled"), True)
            _l_(694231)
            _c_(694234, _a_(694233, _n_(694232, "pinEdit", lambda: pinEdit), "setEnabled"), True)
            _l_(694235)
        else:
            _c_(694238, _a_(694237, _n_(694236, "dbIssueEdit", lambda: dbIssueEdit), "setEnabled"), False)
            _l_(694239)
            _c_(694242, _a_(694241, _n_(694240, "pinEdit", lambda: pinEdit), "setEnabled"), False)
            _l_(694243)

    def save(self, userName, userEmail, userPass, userCC=None, userCVC=None,
            userDB=None, userPin=None, isAdmin=False):
        _l_(694361)


        userName = _c_(694249, _a_(694248, _a_(694247, _n_(694246, "self", lambda: self), "nameEdit"), "text"))
        _l_(694250)
        userEmail = _c_(694254, _a_(694253, _a_(694252, _n_(694251, "self", lambda: self), "emailEdit"), "text"))
        _l_(694255)

        if _c_(694259, _a_(694258, _a_(694257, _n_(694256, "self", lambda: self), "setPassEdit"), "text")) == _c_(694263, _a_(694262, _a_(694261, _n_(694260, "self", lambda: self), "passRepeatEdit"), "text")):
            _l_(694270)

            userPass = _c_(694267, _a_(694266, _a_(694265, _n_(694264, "self", lambda: self), "setPassEdit"), "text"))
            _l_(694268)
        else:
            pass #Throw error here
            _l_(694269) #Throw error here

        if _c_(694274, _a_(694273, _a_(694272, _n_(694271, "self", lambda: self), "ccIssueChkBx1"), "isChecked")):
            _l_(694316)

            if _c_(694278, _n_(694275, "len", lambda: len), _a_(694277, _n_(694276, "self", lambda: self), "ccIssueEdit")) == 15 and _c_(694282, _n_(694279, "len", lambda: len), _a_(694281, _n_(694280, "self", lambda: self), "cvcEdit")) == 4:
                _l_(694315)

                userCC = _c_(694286, _a_(694285, _a_(694284, _n_(694283, "self", lambda: self), "ccIssueEdit"), "text"))
                _l_(694287)
                userCVC = _c_(694291, _a_(694290, _a_(694289, _n_(694288, "self", lambda: self), "cvcEdit"), "text"))
                _l_(694292)
                ccType = 'AMEX'
                _l_(694293)
            elif _c_(694297, _n_(694294, "len", lambda: len), _a_(694296, _n_(694295, "self", lambda: self), "ccIssueEdit")) == 16 and _c_(694301, _n_(694298, "len", lambda: len), _a_(694300, _n_(694299, "self", lambda: self), "cvcEdit")) == 3:
                _l_(694314)

                userCC = _c_(694305, _a_(694304, _a_(694303, _n_(694302, "self", lambda: self), "ccIssueEdit"), "text"))
                _l_(694306)
                userCVC = _c_(694310, _a_(694309, _a_(694308, _n_(694307, "self", lambda: self), "cvcEdit"), "text"))
                _l_(694311)
                ccType = 'MC/Visa'
                _l_(694312)
            else:
                pass #Throw error here
                _l_(694313) #Throw error here

        if _c_(694320, _a_(694319, _a_(694318, _n_(694317, "self", lambda: self), "ccIssueChkBx2"), "isChecked")):
            _l_(694341)

            if _c_(694324, _n_(694321, "len", lambda: len), _a_(694323, _n_(694322, "self", lambda: self), "dbIssueEdit")) == 16 and _c_(694328, _n_(694325, "len", lambda: len), _a_(694327, _n_(694326, "self", lambda: self), "pinEdit")) == 4:
                _l_(694340)

                userDB = _c_(694332, _a_(694331, _a_(694330, _n_(694329, "self", lambda: self), "dbIssueEdit"), "text"))
                _l_(694333)
                userPin = _c_(694337, _a_(694336, _a_(694335, _n_(694334, "self", lambda: self), "pinEdit"), "text"))
                _l_(694338)
            else:
                pass #Throw error here
                _l_(694339) #Throw error here

        if _c_(694345, _a_(694344, _a_(694343, _n_(694342, "self", lambda: self), "adminChkBx"), "isChecked")):
            _l_(694347)

            isAdmin = True
            _l_(694346)

        userSave = _c_(694359, _a_(694349, _n_(694348, "newUser", lambda: newUser), "Save"), _n_(694350, "userName", lambda: userName), _n_(694351, "userEmail", lambda: userEmail), _n_(694352, "userPass", lambda: userPass), _n_(694353, "userCC", lambda: userCC), _n_(694354, "userCVC", lambda: userCVC),
            _n_(694355, "ccType", lambda: ccType), _n_(694356, "userDB", lambda: userDB), _n_(694357, "userPin", lambda: userPin), _n_(694358, "isAdmin", lambda: isAdmin))
        _l_(694360)

    def center(self):
        _l_(694386)


        qr = _c_(694364, _a_(694363, _n_(694362, "self", lambda: self), "frameGeometry"))
        _l_(694365)
        cp = _c_(694372, _a_(694371, _c_(694370, _a_(694369, _c_(694368, _a_(694367, _n_(694366, "QtGui", lambda: QtGui), "QDesktopWidget")), "availableGeometry")), "center"))
        _l_(694373)
        _c_(694377, _a_(694375, _n_(694374, "qr", lambda: qr), "moveCenter"), _n_(694376, "cp", lambda: cp))
        _l_(694378)
        _c_(694384, _a_(694380, _n_(694379, "self", lambda: self), "move"), _c_(694383, _a_(694382, _n_(694381, "qr", lambda: qr), "topLeft")))
        _l_(694385)



class Save(_n_(694388, "object", lambda: object)):
    _l_(694433)

    '''Creates a User Object'''
    _l_(694389)

    def __init__(self, userName, userEmail, userPass, userCC, userCVC, ccType,
        userDB, userPin, isAdmin):
        _l_(694394)


        _c_(694392, _a_(694391, _n_(694390, "self", lambda: self), "create"))
        _l_(694393)

    def create(self):
        _l_(694432)


        list = [_n_(694395, "userName", lambda: userName), _n_(694396, "userEmail", lambda: userEmail), _n_(694397, "userPass", lambda: userPass), _n_(694398, "userCC", lambda: userCC), _n_(694399, "userCVC", lambda: userCVC), _n_(694400, "ccType", lambda: ccType), _n_(694401, "userDB", lambda: userDB),
            _n_(694402, "userPin", lambda: userPin), _n_(694403, "isAdmin", lambda: isAdmin)]
        _l_(694404)

        dirName = _c_(694408, _n_(694405, "str", lambda: str), _a_(694407, _n_(694406, "self", lambda: self), "userName"))
        _l_(694409)
        _c_(694413, _a_(694411, _n_(694410, "os", lambda: os), "mkdir"), _n_(694412, "dirName", lambda: dirName))
        _l_(694414)
        _c_(694418, _a_(694416, _n_(694415, "os", lambda: os), "chdir"), _n_(694417, "dirName", lambda: dirName))
        _l_(694419)

        fileName = _c_(694421, _n_(694420, "open", lambda: open), 'profile.txt', 'wb')
        _l_(694422)
        for i in _n_(694423, "list", lambda: list):
            _l_(694431)

            _c_(694429, _a_(694425, _n_(694424, "fileName", lambda: fileName), "write"), _c_(694428, _n_(694426, "str", lambda: str), _n_(694427, "i", lambda: i)))
            _l_(694430)