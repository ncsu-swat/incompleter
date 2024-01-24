# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/28795573/error-attributeerror-application-object-has-no-attribute-message
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from tkinter import ttk
    _l_(429616)

except ImportError:
    pass
try:
    from tkinter import *
    _l_(429618)

except ImportError:
    pass
try:
    import math
    _l_(429620)

except ImportError:
    pass

root = _c_(429622, _n_(429621, "Tk", lambda: Tk))
_l_(429623)

class Application(_n_(429624, "Frame", lambda: Frame)):
    _l_(430634)

    def __init__(self, master = None):
        _l_(429639)

        _c_(429629, _a_(429626, _n_(429625, "Frame", lambda: Frame), "__init__"), _n_(429627, "self", lambda: self), _n_(429628, "master", lambda: master))
        _l_(429630)
        _c_(429633, _a_(429632, _n_(429631, "self", lambda: self), "grid"))
        _l_(429634)
        _c_(429637, _a_(429636, _n_(429635, "self", lambda: self), "create_widgets"))
        _l_(429638)

    def create_widgets(self):
        _l_(430073)


        _n_(429640, "self", lambda: self).title = _c_(429642, _n_(429641, "StringVar", lambda: StringVar))
        _l_(429643)
        _c_(429647, _a_(429646, _a_(429645, _n_(429644, "self", lambda: self), "title"), "set"), 'Operator Aid: Depressurisation Rate')#~~~TITLE
        _l_(429648)#~~~TITLE
        _n_(429649, "self", lambda: self).titleField = _c_(429654, _n_(429650, "Label", lambda: Label), _n_(429651, "self", lambda: self), textvariable = _a_(429653, _n_(429652, "self", lambda: self), "title"))
        _l_(429655)
        _c_(429659, _a_(429658, _a_(429657, _n_(429656, "self", lambda: self), "titleField"), "grid"), row = 0, column = 0, columnspan = 4, stick = 'nsew')
        _l_(429660)

        _n_(429661, "self", lambda: self).pressure = _c_(429664, _n_(429662, "Label", lambda: Label), _n_(429663, "self", lambda: self), text = 'Pressure/ Bar')#~~~PRESSURE HEADING
        _l_(429665)#~~~PRESSURE HEADING
        _c_(429669, _a_(429668, _a_(429667, _n_(429666, "self", lambda: self), "pressure"), "grid"), row = 1, column = 0, columnspan = 2, stick = 'nsew')
        _l_(429670)

        _n_(429671, "self", lambda: self).time = _c_(429674, _n_(429672, "Label", lambda: Label), _n_(429673, "self", lambda: self), text = 'Time/ Minutes')#~~~TIME HEADING
        _l_(429675)#~~~TIME HEADING
        _c_(429679, _a_(429678, _a_(429677, _n_(429676, "self", lambda: self), "time"), "grid"), row = 1, column = 2, columnspan = 2, stick = 'nsew')
        _l_(429680)

        _n_(429681, "self", lambda: self).est_tLabel = _c_(429684, _n_(429682, "Label", lambda: Label), _n_(429683, "self", lambda: self), text = 'Estimated Time at 2 Bar: ')
        _l_(429685)
        _c_(429689, _a_(429688, _a_(429687, _n_(429686, "self", lambda: self), "est_tLabel"), "grid"), row = 7, column = 0, stick = 'e')
        _l_(429690)

        _n_(429691, "self", lambda: self).est_cLabel = _c_(429694, _n_(429692, "Label", lambda: Label), _n_(429693, "self", lambda: self), text = 'Estimated Category: ')
        _l_(429695)
        _c_(429699, _a_(429698, _a_(429697, _n_(429696, "self", lambda: self), "est_cLabel"), "grid"), row = 8, column = 0, stick = 'e')
        _l_(429700)

        #~~~PRESSURE ENTRY~~~
        _n_(429701, "self", lambda: self).p1Entry = _c_(429703, _n_(429702, "StringVar", lambda: StringVar))
        _l_(429704)
        _c_(429708, _a_(429707, _a_(429706, _n_(429705, "self", lambda: self), "p1Entry"), "set"), '')
        _l_(429709)
        _n_(429710, "self", lambda: self).p1Entry = _c_(429715, _n_(429711, "Entry", lambda: Entry), _n_(429712, "self", lambda: self), textvariable = _a_(429714, _n_(429713, "self", lambda: self), "p1Entry"))
        _l_(429716)
        _c_(429720, _a_(429719, _a_(429718, _n_(429717, "self", lambda: self), "p1Entry"), "grid"), row = 2, column = 0, stick = 'nsew')
        _l_(429721)

        _n_(429722, "self", lambda: self).p2Entry = _c_(429724, _n_(429723, "StringVar", lambda: StringVar))
        _l_(429725)
        _c_(429729, _a_(429728, _a_(429727, _n_(429726, "self", lambda: self), "p2Entry"), "set"), '')
        _l_(429730)
        _n_(429731, "self", lambda: self).p2Entry = _c_(429736, _n_(429732, "Entry", lambda: Entry), _n_(429733, "self", lambda: self), textvariable = _a_(429735, _n_(429734, "self", lambda: self), "p2Entry"))
        _l_(429737)
        _c_(429741, _a_(429740, _a_(429739, _n_(429738, "self", lambda: self), "p2Entry"), "grid"), row = 3, column = 0, stick = 'nsew')
        _l_(429742)

        _n_(429743, "self", lambda: self).p3Entry = _c_(429745, _n_(429744, "StringVar", lambda: StringVar))
        _l_(429746)
        _c_(429750, _a_(429749, _a_(429748, _n_(429747, "self", lambda: self), "p3Entry"), "set"), '')
        _l_(429751)
        _n_(429752, "self", lambda: self).p3Entry = _c_(429757, _n_(429753, "Entry", lambda: Entry), _n_(429754, "self", lambda: self), textvariable = _a_(429756, _n_(429755, "self", lambda: self), "p3Entry"))
        _l_(429758)
        _c_(429762, _a_(429761, _a_(429760, _n_(429759, "self", lambda: self), "p3Entry"), "grid"), row = 4, column = 0, stick = 'nsew')
        _l_(429763)

        _n_(429764, "self", lambda: self).p4Entry = _c_(429766, _n_(429765, "StringVar", lambda: StringVar))
        _l_(429767)
        _c_(429771, _a_(429770, _a_(429769, _n_(429768, "self", lambda: self), "p4Entry"), "set"), '')
        _l_(429772)
        _n_(429773, "self", lambda: self).p4Entry = _c_(429778, _n_(429774, "Entry", lambda: Entry), _n_(429775, "self", lambda: self), textvariable = _a_(429777, _n_(429776, "self", lambda: self), "p4Entry"))
        _l_(429779)
        _c_(429783, _a_(429782, _a_(429781, _n_(429780, "self", lambda: self), "p4Entry"), "grid"), row = 5, column = 0, stick = 'nsew')
        _l_(429784)

        _n_(429785, "self", lambda: self).p5Entry = _c_(429787, _n_(429786, "StringVar", lambda: StringVar))
        _l_(429788)
        _c_(429792, _a_(429791, _a_(429790, _n_(429789, "self", lambda: self), "p5Entry"), "set"), '')
        _l_(429793)
        _n_(429794, "self", lambda: self).p5Entry = _c_(429799, _n_(429795, "Entry", lambda: Entry), _n_(429796, "self", lambda: self), textvariable = _a_(429798, _n_(429797, "self", lambda: self), "p5Entry"))
        _l_(429800)
        _c_(429804, _a_(429803, _a_(429802, _n_(429801, "self", lambda: self), "p5Entry"), "grid"), row = 6, column = 0, stick = 'nsew')
        _l_(429805)

        #~~~TIME ENTRY~~~
        _n_(429806, "self", lambda: self).t1Entry = _c_(429808, _n_(429807, "StringVar", lambda: StringVar))
        _l_(429809)
        _c_(429813, _a_(429812, _a_(429811, _n_(429810, "self", lambda: self), "t1Entry"), "set"), '')
        _l_(429814)
        _n_(429815, "self", lambda: self).t1Entry = _c_(429820, _n_(429816, "Entry", lambda: Entry), _n_(429817, "self", lambda: self), textvariable = _a_(429819, _n_(429818, "self", lambda: self), "t1Entry"))
        _l_(429821)
        _c_(429825, _a_(429824, _a_(429823, _n_(429822, "self", lambda: self), "t1Entry"), "grid"), row = 2, column = 2, stick = 'nsew')
        _l_(429826)

        _n_(429827, "self", lambda: self).t2Entry = _c_(429829, _n_(429828, "StringVar", lambda: StringVar))
        _l_(429830)
        _c_(429834, _a_(429833, _a_(429832, _n_(429831, "self", lambda: self), "t2Entry"), "set"), '')
        _l_(429835)
        _n_(429836, "self", lambda: self).t2Entry = _c_(429841, _n_(429837, "Entry", lambda: Entry), _n_(429838, "self", lambda: self), textvariable = _a_(429840, _n_(429839, "self", lambda: self), "t2Entry"))
        _l_(429842)
        _c_(429846, _a_(429845, _a_(429844, _n_(429843, "self", lambda: self), "t2Entry"), "grid"), row = 3, column = 2, stick = 'nsew')
        _l_(429847)

        _n_(429848, "self", lambda: self).t3Entry = _c_(429850, _n_(429849, "StringVar", lambda: StringVar))
        _l_(429851)
        _c_(429855, _a_(429854, _a_(429853, _n_(429852, "self", lambda: self), "t3Entry"), "set"), '')
        _l_(429856)
        _n_(429857, "self", lambda: self).t3Entry = _c_(429862, _n_(429858, "Entry", lambda: Entry), _n_(429859, "self", lambda: self), textvariable = _a_(429861, _n_(429860, "self", lambda: self), "t3Entry"))
        _l_(429863)
        _c_(429867, _a_(429866, _a_(429865, _n_(429864, "self", lambda: self), "t3Entry"), "grid"), row = 4, column = 2, stick = 'nsew')
        _l_(429868)

        _n_(429869, "self", lambda: self).t4Entry = _c_(429871, _n_(429870, "StringVar", lambda: StringVar))
        _l_(429872)
        _c_(429876, _a_(429875, _a_(429874, _n_(429873, "self", lambda: self), "t4Entry"), "set"), '')
        _l_(429877)
        _n_(429878, "self", lambda: self).t4Entry = _c_(429883, _n_(429879, "Entry", lambda: Entry), _n_(429880, "self", lambda: self), textvariable = _a_(429882, _n_(429881, "self", lambda: self), "t4Entry"))
        _l_(429884)
        _c_(429888, _a_(429887, _a_(429886, _n_(429885, "self", lambda: self), "t4Entry"), "grid"), row = 5, column = 2, stick = 'nsew')
        _l_(429889)

        _n_(429890, "self", lambda: self).t5Entry = _c_(429892, _n_(429891, "StringVar", lambda: StringVar))
        _l_(429893)
        _c_(429897, _a_(429896, _a_(429895, _n_(429894, "self", lambda: self), "t5Entry"), "set"), '')
        _l_(429898)
        _n_(429899, "self", lambda: self).t5Entry = _c_(429904, _n_(429900, "Entry", lambda: Entry), _n_(429901, "self", lambda: self), textvariable = _a_(429903, _n_(429902, "self", lambda: self), "t5Entry"))
        _l_(429905)
        _c_(429909, _a_(429908, _a_(429907, _n_(429906, "self", lambda: self), "t5Entry"), "grid"), row = 6, column = 2, stick = 'nsew')
        _l_(429910)

        #~~~ESTIMATED PRESSURE AND CATEGORY ENTRY~~~

        _n_(429911, "self", lambda: self).est_tEntry = _c_(429913, _n_(429912, "StringVar", lambda: StringVar))
        _l_(429914)
        _c_(429918, _a_(429917, _a_(429916, _n_(429915, "self", lambda: self), "est_tEntry"), "set"), '')
        _l_(429919)
        _n_(429920, "self", lambda: self).est_tEntry = _c_(429925, _n_(429921, "Entry", lambda: Entry), _n_(429922, "self", lambda: self), textvariable = _a_(429924, _n_(429923, "self", lambda: self), "est_tEntry"))
        _l_(429926)
        _c_(429930, _a_(429929, _a_(429928, _n_(429927, "self", lambda: self), "est_tEntry"), "grid"), row = 7, column = 1, stick = 'nsew')
        _l_(429931)

        _n_(429932, "self", lambda: self).est_cEntry = _c_(429934, _n_(429933, "StringVar", lambda: StringVar))
        _l_(429935)
        _c_(429939, _a_(429938, _a_(429937, _n_(429936, "self", lambda: self), "est_cEntry"), "set"), '')
        _l_(429940)
        _n_(429941, "self", lambda: self).est_cEntry = _c_(429946, _n_(429942, "Entry", lambda: Entry), _n_(429943, "self", lambda: self), textvariable = _a_(429945, _n_(429944, "self", lambda: self), "est_cEntry"))
        _l_(429947)
        _c_(429951, _a_(429950, _a_(429949, _n_(429948, "self", lambda: self), "est_cEntry"), "grid"), row = 8, column = 1, stick = 'nsew')
        _l_(429952)

        #~~~PRESSURE BUTTONS~~~
        _n_(429953, "self", lambda: self).p1Button = _c_(429958, _n_(429954, "Button", lambda: Button), _n_(429955, "self", lambda: self), text = 'ENTER', command = _a_(429957, _n_(429956, "self", lambda: self), "submitp1"))
        _l_(429959)
        _c_(429963, _a_(429962, _a_(429961, _n_(429960, "self", lambda: self), "p1Button"), "grid"), row = 2, column = 1, stick = 'nsew')
        _l_(429964)

        _n_(429965, "self", lambda: self).p2Button = _c_(429970, _n_(429966, "Button", lambda: Button), _n_(429967, "self", lambda: self), text = 'ENTER', command = _a_(429969, _n_(429968, "self", lambda: self), "submitp2"))
        _l_(429971)
        _c_(429975, _a_(429974, _a_(429973, _n_(429972, "self", lambda: self), "p2Button"), "grid"), row = 3, column = 1, stick = 'nsew')
        _l_(429976)

        _n_(429977, "self", lambda: self).p3Button = _c_(429982, _n_(429978, "Button", lambda: Button), _n_(429979, "self", lambda: self), text = 'ENTER', command = _a_(429981, _n_(429980, "self", lambda: self), "submitp3"))
        _l_(429983)
        _c_(429987, _a_(429986, _a_(429985, _n_(429984, "self", lambda: self), "p3Button"), "grid"), row = 4, column = 1, stick = 'nsew')
        _l_(429988)

        _n_(429989, "self", lambda: self).p4Button = _c_(429994, _n_(429990, "Button", lambda: Button), _n_(429991, "self", lambda: self), text = 'ENTER', command = _a_(429993, _n_(429992, "self", lambda: self), "submitp4"))
        _l_(429995)
        _c_(429999, _a_(429998, _a_(429997, _n_(429996, "self", lambda: self), "p4Button"), "grid"), row = 5, column = 1, stick = 'nsew')
        _l_(430000)

        _n_(430001, "self", lambda: self).p5Button = _c_(430006, _n_(430002, "Button", lambda: Button), _n_(430003, "self", lambda: self), text = 'ENTER', command = _a_(430005, _n_(430004, "self", lambda: self), "submitp5"))
        _l_(430007)
        _c_(430011, _a_(430010, _a_(430009, _n_(430008, "self", lambda: self), "p5Button"), "grid"), row = 6, column = 1, stick = 'nsew')
        _l_(430012)

        #~~~TIME BUTTONS~~~
        _n_(430013, "self", lambda: self).t1Button = _c_(430018, _n_(430014, "Button", lambda: Button), _n_(430015, "self", lambda: self), text = 'ENTER', command = _a_(430017, _n_(430016, "self", lambda: self), "submitt1"))
        _l_(430019)
        _c_(430023, _a_(430022, _a_(430021, _n_(430020, "self", lambda: self), "t1Button"), "grid"), row = 2, column = 3, stick = 'nsew')
        _l_(430024)

        _n_(430025, "self", lambda: self).t2Button = _c_(430030, _n_(430026, "Button", lambda: Button), _n_(430027, "self", lambda: self), text = 'ENTER', command = _a_(430029, _n_(430028, "self", lambda: self), "submitt2"))
        _l_(430031)
        _c_(430035, _a_(430034, _a_(430033, _n_(430032, "self", lambda: self), "t2Button"), "grid"), row = 3, column = 3, stick = 'nsew')
        _l_(430036)

        _n_(430037, "self", lambda: self).t3Button = _c_(430042, _n_(430038, "Button", lambda: Button), _n_(430039, "self", lambda: self), text = 'ENTER', command = _a_(430041, _n_(430040, "self", lambda: self), "submitt3"))
        _l_(430043)
        _c_(430047, _a_(430046, _a_(430045, _n_(430044, "self", lambda: self), "t3Button"), "grid"), row = 4, column = 3, stick = 'nsew')
        _l_(430048)

        _n_(430049, "self", lambda: self).t4Button = _c_(430054, _n_(430050, "Button", lambda: Button), _n_(430051, "self", lambda: self), text = 'ENTER', command = _a_(430053, _n_(430052, "self", lambda: self), "submitt4"))
        _l_(430055)
        _c_(430059, _a_(430058, _a_(430057, _n_(430056, "self", lambda: self), "t4Button"), "grid"), row = 5, column = 3, stick = 'nsew')
        _l_(430060)

        _n_(430061, "self", lambda: self).t5Button = _c_(430066, _n_(430062, "Button", lambda: Button), _n_(430063, "self", lambda: self), text = 'ENTER', command = _a_(430065, _n_(430064, "self", lambda: self), "submitt5"))
        _l_(430067)
        _c_(430071, _a_(430070, _a_(430069, _n_(430068, "self", lambda: self), "t5Button"), "grid"), row = 6, column = 3, stick = 'nsew')
        _l_(430072)

    def submitp1(self):
        _l_(430116)

        words = _c_(430077, _a_(430076, _a_(430075, _n_(430074, "self", lambda: self), "p1Entry"), "get"))
        _l_(430078)
        try:
            _l_(430096)

            p1 = _c_(430081, _n_(430079, "float", lambda: float), _n_(430080, "words", lambda: words))
            _l_(430082)
        except (_n_(430083, "ValueError", lambda: ValueError), _n_(430084, "TypeError", lambda: TypeError)):
            _l_(430095)

            _c_(430087, _a_(430086, _n_(430085, "self", lambda: self), "change_message"), 'ERROR')
            _l_(430088)
            _c_(430092, _a_(430090, _n_(430089, "self", lambda: self), "p1Entry"), 0, _n_(430091, "END", lambda: END))
            _l_(430093)
            aux = ""
            _l_(430094)
            return aux
        _c_(430099, _a_(430098, _n_(430097, "self", lambda: self), "change_message"), 'clear')
        _l_(430100)
        _c_(430105, _a_(430103, _a_(430102, _n_(430101, "self", lambda: self), "est_tEntry"), "delete"), 0, _n_(430104, "END", lambda: END))
        _l_(430106)
        _c_(430114, _a_(430109, _a_(430108, _n_(430107, "self", lambda: self), "est_tEntry"), "insert"), 0, '%.2f' % _c_(430113, _a_(430111, _n_(430110, "self", lambda: self), "Calc_1"), _n_(430112, "p1", lambda: p1)))
        _l_(430115)


    def submitp2(self):
        _l_(430159)

        words = _c_(430120, _a_(430119, _a_(430118, _n_(430117, "self", lambda: self), "p2Entry"), "get"))
        _l_(430121)
        try:
            _l_(430139)

            p2 = _c_(430124, _n_(430122, "float", lambda: float), _n_(430123, "words", lambda: words))
            _l_(430125)
        except (_n_(430126, "ValueError", lambda: ValueError), _n_(430127, "TypeError", lambda: TypeError)):
            _l_(430138)

            _c_(430130, _a_(430129, _n_(430128, "self", lambda: self), "change_message"), 'ERROR')
            _l_(430131)
            _c_(430135, _a_(430133, _n_(430132, "self", lambda: self), "p2Entry"), 0, _n_(430134, "END", lambda: END))
            _l_(430136)
            aux = ""
            _l_(430137)
            return aux
        _c_(430142, _a_(430141, _n_(430140, "self", lambda: self), "change_message"), 'clear')
        _l_(430143)
        _c_(430148, _a_(430146, _a_(430145, _n_(430144, "self", lambda: self), "est_tEntry"), "delete"), 0, _n_(430147, "END", lambda: END))
        _l_(430149)
        _c_(430157, _a_(430152, _a_(430151, _n_(430150, "self", lambda: self), "est_tEntry"), "insert"), 0, '%.2f' % _c_(430156, _a_(430154, _n_(430153, "self", lambda: self), "Calc_1"), _n_(430155, "p2", lambda: p2)))
        _l_(430158)

    def submitp3(self):
        _l_(430202)

        words = _c_(430163, _a_(430162, _a_(430161, _n_(430160, "self", lambda: self), "p3Entry"), "get"))
        _l_(430164)
        try:
            _l_(430182)

            p3 = _c_(430167, _n_(430165, "float", lambda: float), _n_(430166, "words", lambda: words))
            _l_(430168)
        except (_n_(430169, "ValueError", lambda: ValueError), _n_(430170, "TypeError", lambda: TypeError)):
            _l_(430181)

            _c_(430173, _a_(430172, _n_(430171, "self", lambda: self), "change_message"), 'ERROR')
            _l_(430174)
            _c_(430178, _a_(430176, _n_(430175, "self", lambda: self), "p3Entry"), 0, _n_(430177, "END", lambda: END))
            _l_(430179)
            aux = ""
            _l_(430180)
            return aux
        _c_(430185, _a_(430184, _n_(430183, "self", lambda: self), "change_message"), 'clear')
        _l_(430186)
        _c_(430191, _a_(430189, _a_(430188, _n_(430187, "self", lambda: self), "est_tEntry"), "delete"), 0, _n_(430190, "END", lambda: END))
        _l_(430192)
        _c_(430200, _a_(430195, _a_(430194, _n_(430193, "self", lambda: self), "est_tEntry"), "insert"), 0, '%.2f' % _c_(430199, _a_(430197, _n_(430196, "self", lambda: self), "Calc_2"), _n_(430198, "p3", lambda: p3)))
        _l_(430201)

    def submitp4(self):
        _l_(430245)

        words = _c_(430206, _a_(430205, _a_(430204, _n_(430203, "self", lambda: self), "p4Entry"), "get"))
        _l_(430207)
        try:
            _l_(430225)

            p4 = _c_(430210, _n_(430208, "float", lambda: float), _n_(430209, "words", lambda: words))
            _l_(430211)
        except (_n_(430212, "ValueError", lambda: ValueError), _n_(430213, "TypeError", lambda: TypeError)):
            _l_(430224)

            _c_(430216, _a_(430215, _n_(430214, "self", lambda: self), "change_message"), 'ERROR')
            _l_(430217)
            _c_(430221, _a_(430219, _n_(430218, "self", lambda: self), "p4Entry"), 0, _n_(430220, "END", lambda: END))
            _l_(430222)
            aux = ""
            _l_(430223)
            return aux
        _c_(430228, _a_(430227, _n_(430226, "self", lambda: self), "change_message"), 'clear')
        _l_(430229)
        _c_(430234, _a_(430232, _a_(430231, _n_(430230, "self", lambda: self), "est_tEntry"), "delete"), 0, _n_(430233, "END", lambda: END))
        _l_(430235)
        _c_(430243, _a_(430238, _a_(430237, _n_(430236, "self", lambda: self), "est_tEntry"), "insert"), 0, '%.2f' % _c_(430242, _a_(430240, _n_(430239, "self", lambda: self), "Calc_3"), _n_(430241, "p4", lambda: p4)))
        _l_(430244)

    def submitp5(self):
        _l_(430288)

        words = _c_(430249, _a_(430248, _a_(430247, _n_(430246, "self", lambda: self), "p5Entry"), "get"))
        _l_(430250)
        try:
            _l_(430268)

            p5 = _c_(430253, _n_(430251, "float", lambda: float), _n_(430252, "words", lambda: words))
            _l_(430254)
        except (_n_(430255, "ValueError", lambda: ValueError), _n_(430256, "TypeError", lambda: TypeError)):
            _l_(430267)

            _c_(430259, _a_(430258, _n_(430257, "self", lambda: self), "change_message"), 'ERROR')
            _l_(430260)
            _c_(430264, _a_(430262, _n_(430261, "self", lambda: self), "p5Entry"), 0, _n_(430263, "END", lambda: END))
            _l_(430265)
            aux = ""
            _l_(430266)
            return aux
        _c_(430271, _a_(430270, _n_(430269, "self", lambda: self), "change_message"), 'clear')
        _l_(430272)
        _c_(430277, _a_(430275, _a_(430274, _n_(430273, "self", lambda: self), "est_tEntry"), "delete"), 0, _n_(430276, "END", lambda: END))
        _l_(430278)
        _c_(430286, _a_(430281, _a_(430280, _n_(430279, "self", lambda: self), "est_tEntry"), "insert"), 0, '%.2f' % _c_(430285, _a_(430283, _n_(430282, "self", lambda: self), "Calc_4"), _n_(430284, "p5", lambda: p5)))
        _l_(430287)

    def submitt1(self):
        _l_(430331)

        words = _c_(430292, _a_(430291, _a_(430290, _n_(430289, "self", lambda: self), "t1Entry"), "get"))
        _l_(430293)
        try:
            _l_(430311)

            t1 = _c_(430296, _n_(430294, "float", lambda: float), _n_(430295, "words", lambda: words))
            _l_(430297)
        except (_n_(430298, "ValueError", lambda: ValueError), _n_(430299, "TypeError", lambda: TypeError)):
            _l_(430310)

            _c_(430302, _a_(430301, _n_(430300, "self", lambda: self), "change_message"), 'ERROR')
            _l_(430303)
            _c_(430307, _a_(430305, _n_(430304, "self", lambda: self), "t1Entry"), 0, _n_(430306, "END", lambda: END))
            _l_(430308)
            aux = ""
            _l_(430309)
            return aux
        _c_(430314, _a_(430313, _n_(430312, "self", lambda: self), "change_message"), 'clear')
        _l_(430315)
        _c_(430320, _a_(430318, _a_(430317, _n_(430316, "self", lambda: self), "est_tEntry"), "delete"), 0, _n_(430319, "END", lambda: END))
        _l_(430321)
        _c_(430329, _a_(430324, _a_(430323, _n_(430322, "self", lambda: self), "est_tEntry"), "insert"), 0, '%.2f' % _c_(430328, _a_(430326, _n_(430325, "self", lambda: self), "Calc_1"), _n_(430327, "t1", lambda: t1)))
        _l_(430330)

    def submitt2(self):
        _l_(430374)

        words = _c_(430335, _a_(430334, _a_(430333, _n_(430332, "self", lambda: self), "t2Entry"), "get"))
        _l_(430336)
        try:
            _l_(430354)

            t2 = _c_(430339, _n_(430337, "float", lambda: float), _n_(430338, "words", lambda: words))
            _l_(430340)
        except (_n_(430341, "ValueError", lambda: ValueError), _n_(430342, "TypeError", lambda: TypeError)):
            _l_(430353)

            _c_(430345, _a_(430344, _n_(430343, "self", lambda: self), "change_message"), 'ERROR')
            _l_(430346)
            _c_(430350, _a_(430348, _n_(430347, "self", lambda: self), "t2Entry"), 0, _n_(430349, "END", lambda: END))
            _l_(430351)
            aux = ""
            _l_(430352)
            return aux
        _c_(430357, _a_(430356, _n_(430355, "self", lambda: self), "change_message"), 'clear')
        _l_(430358)
        _c_(430363, _a_(430361, _a_(430360, _n_(430359, "self", lambda: self), "est_tEntry"), "delete"), 0, _n_(430362, "END", lambda: END))
        _l_(430364)
        _c_(430372, _a_(430367, _a_(430366, _n_(430365, "self", lambda: self), "est_tEntry"), "insert"), 0, '%.2f' % _c_(430371, _a_(430369, _n_(430368, "self", lambda: self), "Calc_1"), _n_(430370, "t2", lambda: t2)))
        _l_(430373)

    def submitt3(self):
        _l_(430417)

        words = _c_(430378, _a_(430377, _a_(430376, _n_(430375, "self", lambda: self), "t3Entry"), "get"))
        _l_(430379)
        try:
            _l_(430397)

            t3 = _c_(430382, _n_(430380, "float", lambda: float), _n_(430381, "words", lambda: words))
            _l_(430383)
        except (_n_(430384, "ValueError", lambda: ValueError), _n_(430385, "TypeError", lambda: TypeError)):
            _l_(430396)

            _c_(430388, _a_(430387, _n_(430386, "self", lambda: self), "change_message"), 'ERROR')
            _l_(430389)
            _c_(430393, _a_(430391, _n_(430390, "self", lambda: self), "t3Entry"), 0, _n_(430392, "END", lambda: END))
            _l_(430394)
            aux = ""
            _l_(430395)
            return aux
        _c_(430400, _a_(430399, _n_(430398, "self", lambda: self), "change_message"), 'clear')
        _l_(430401)
        _c_(430406, _a_(430404, _a_(430403, _n_(430402, "self", lambda: self), "est_tEntry"), "delete"), 0, _n_(430405, "END", lambda: END))
        _l_(430407)
        _c_(430415, _a_(430410, _a_(430409, _n_(430408, "self", lambda: self), "est_tEntry"), "insert"), 0, '%.2f' % _c_(430414, _a_(430412, _n_(430411, "self", lambda: self), "Calc_2"), _n_(430413, "t3", lambda: t3)))
        _l_(430416)

    def submitt4(self):
        _l_(430460)

        words = _c_(430421, _a_(430420, _a_(430419, _n_(430418, "self", lambda: self), "t4Entry"), "get"))
        _l_(430422)
        try:
            _l_(430440)

            t4 = _c_(430425, _n_(430423, "float", lambda: float), _n_(430424, "words", lambda: words))
            _l_(430426)
        except (_n_(430427, "ValueError", lambda: ValueError), _n_(430428, "TypeError", lambda: TypeError)):
            _l_(430439)

            _c_(430431, _a_(430430, _n_(430429, "self", lambda: self), "change_message"), 'ERROR')
            _l_(430432)
            _c_(430436, _a_(430434, _n_(430433, "self", lambda: self), "t4Entry"), 0, _n_(430435, "END", lambda: END))
            _l_(430437)
            aux = ""
            _l_(430438)
            return aux
        _c_(430443, _a_(430442, _n_(430441, "self", lambda: self), "change_message"), 'clear')
        _l_(430444)
        _c_(430449, _a_(430447, _a_(430446, _n_(430445, "self", lambda: self), "est_tEntry"), "delete"), 0, _n_(430448, "END", lambda: END))
        _l_(430450)
        _c_(430458, _a_(430453, _a_(430452, _n_(430451, "self", lambda: self), "est_tEntry"), "insert"), 0, '%.2f' % _c_(430457, _a_(430455, _n_(430454, "self", lambda: self), "Calc_3"), _n_(430456, "t4", lambda: t4)))
        _l_(430459)

    def submitt5(self):
        _l_(430503)

        words = _c_(430464, _a_(430463, _a_(430462, _n_(430461, "self", lambda: self), "t5Entry"), "get"))
        _l_(430465)
        try:
            _l_(430483)

            t5 = _c_(430468, _n_(430466, "float", lambda: float), _n_(430467, "words", lambda: words))
            _l_(430469)
        except (_n_(430470, "ValueError", lambda: ValueError), _n_(430471, "TypeError", lambda: TypeError)):
            _l_(430482)

            _c_(430474, _a_(430473, _n_(430472, "self", lambda: self), "change_message"), 'ERROR')
            _l_(430475)
            _c_(430479, _a_(430477, _n_(430476, "self", lambda: self), "t5Entry"), 0, _n_(430478, "END", lambda: END))
            _l_(430480)
            aux = ""
            _l_(430481)
            return aux
        _c_(430486, _a_(430485, _n_(430484, "self", lambda: self), "change_message"), 'clear')
        _l_(430487)
        _c_(430492, _a_(430490, _a_(430489, _n_(430488, "self", lambda: self), "est_tEntry"), "delete"), 0, _n_(430491, "END", lambda: END))
        _l_(430493)
        _c_(430501, _a_(430496, _a_(430495, _n_(430494, "self", lambda: self), "est_tEntry"), "insert"), 0, '%.2f' % _c_(430500, _a_(430498, _n_(430497, "self", lambda: self), "Calc_4"), _n_(430499, "t5", lambda: t5)))
        _l_(430502)

    def change_message(self, status):
        _l_(430513)

        messages = {'error': 'I don\'t understand your input.', 'clear': ''}
        _l_(430504)
        _c_(430510, _a_(430507, _a_(430506, _n_(430505, "self", lambda: self), "message"), "set"), _n_(430508, "messages", lambda: messages)[_n_(430509, "status", lambda: status)])
        _l_(430511)
        aux = ""
        _l_(430512)
        return aux

#~~~CALCULATIONS~~~~~~~~~~~~~~~~~
    def Calc_1(self, pressure):
        _l_(430543)

        a1 = _c_(430517, _a_(430515, _n_(430514, "math", lambda: math), "log"), _n_(430516, "p1", lambda: p1)) - _c_(430521, _a_(430519, _n_(430518, "math", lambda: math), "log"), _n_(430520, "p2", lambda: p2))
        _l_(430522)
        b1 = _n_(430523, "t2", lambda: t2) - _n_(430524, "t1", lambda: t1)
        _l_(430525)
        k1 = _n_(430526, "a1", lambda: a1)/_n_(430527, "b1", lambda: b1)
        _l_(430528)
        p2bar = _c_(430532, _a_(430530, _n_(430529, "math", lambda: math), "log"), _n_(430531, "p1", lambda: p1)) - _c_(430535, _a_(430534, _n_(430533, "math", lambda: math), "log"), 2)
        _l_(430536)
        t2bar = (_n_(430537, "p2bar", lambda: p2bar) / _n_(430538, "k1", lambda: k1)) + _n_(430539, "t1", lambda: t1)
        _l_(430540)
        aux = _n_(430541, "t2bar", lambda: t2bar)
        _l_(430542)
        return aux

    def Calc_2(self, pressure):
        _l_(430573)

        a2 = _c_(430547, _a_(430545, _n_(430544, "math", lambda: math), "log"), _n_(430546, "p2", lambda: p2)) - _c_(430551, _a_(430549, _n_(430548, "math", lambda: math), "log"), _n_(430550, "p3", lambda: p3))
        _l_(430552)
        b2 = _n_(430553, "t3", lambda: t3) - _n_(430554, "t2", lambda: t2)
        _l_(430555)
        k2 = _n_(430556, "a2", lambda: a2)/_n_(430557, "b2", lambda: b2)
        _l_(430558)
        p2bar = _c_(430562, _a_(430560, _n_(430559, "math", lambda: math), "log"), _n_(430561, "p1", lambda: p1)) - _c_(430565, _a_(430564, _n_(430563, "math", lambda: math), "log"), 2)
        _l_(430566)
        t2bar = (_n_(430567, "p2bar", lambda: p2bar) / _n_(430568, "k2", lambda: k2)) + _n_(430569, "t1", lambda: t1)#~~~CHANGE IF YOU WANT EST. TIME FROM
        _l_(430570)#~~~CHANGE IF YOU WANT EST. TIME FROM
        aux = _n_(430571, "t2bar", lambda: t2bar)
        _l_(430572)
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~NOW RATHER THAN START
        return aux

    def Calc_3(self, pressure):
        _l_(430603)

        a3 = _c_(430577, _a_(430575, _n_(430574, "math", lambda: math), "log"), _n_(430576, "p3", lambda: p3)) - _c_(430581, _a_(430579, _n_(430578, "math", lambda: math), "log"), _n_(430580, "p4", lambda: p4))
        _l_(430582)
        b3 = _n_(430583, "t4", lambda: t4) - _n_(430584, "t3", lambda: t3)
        _l_(430585)
        k3 = _n_(430586, "a3", lambda: a3)/_n_(430587, "b3", lambda: b3)
        _l_(430588)
        p2bar = _c_(430592, _a_(430590, _n_(430589, "math", lambda: math), "log"), _n_(430591, "p3", lambda: p3)) - _c_(430595, _a_(430594, _n_(430593, "math", lambda: math), "log"), 2)
        _l_(430596)
        t2bar = (_n_(430597, "p2bar", lambda: p2bar) / _n_(430598, "k3", lambda: k3)) + _n_(430599, "t1", lambda: t1)#~~~CHANGE IF YOU WANT EST. TIME FROM
        _l_(430600)#~~~CHANGE IF YOU WANT EST. TIME FROM
        aux = _n_(430601, "t2bar", lambda: t2bar)
        _l_(430602)
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~NOW RATHER THAN START
        return aux

    def Calc_4(self, pressure):
        _l_(430633)

        a4 = _c_(430607, _a_(430605, _n_(430604, "math", lambda: math), "log"), _n_(430606, "p4", lambda: p4)) - _c_(430611, _a_(430609, _n_(430608, "math", lambda: math), "log"), _n_(430610, "p5", lambda: p5))
        _l_(430612)
        b4 = _n_(430613, "t5", lambda: t5) - _n_(430614, "t4", lambda: t4)
        _l_(430615)
        k4 = _n_(430616, "a4", lambda: a4)/_n_(430617, "b4", lambda: b4)
        _l_(430618)
        p2bar = _c_(430622, _a_(430620, _n_(430619, "math", lambda: math), "log"), _n_(430621, "p4", lambda: p4)) - _c_(430625, _a_(430624, _n_(430623, "math", lambda: math), "log"), 2)
        _l_(430626)
        t2bar = (_n_(430627, "p2bar", lambda: p2bar) / _n_(430628, "k4", lambda: k4)) + _n_(430629, "t1", lambda: t1)#~~~CHANGE IF YOU WANT EST. TIME FROM
        _l_(430630)#~~~CHANGE IF YOU WANT EST. TIME FROM
        aux = _n_(430631, "t2bar", lambda: t2bar)
        _l_(430632)
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~NOW RATHER THAN START
        return aux

#~~~MAIN~~~~~~~~~~~~~~~
def main():
    _l_(430648)

    app = _c_(430636, _n_(430635, "Application", lambda: Application))
    _l_(430637)
    _c_(430641, _a_(430640, _a_(430639, _n_(430638, "app", lambda: app), "master"), "title"), 'Operator Aid: Depressurisation Rate')
    _l_(430642)
    _c_(430645, _a_(430644, _n_(430643, "app", lambda: app), "mainloop"))
    _l_(430646)
    aux = 0
    _l_(430647)
    return aux

if _n_(430649, "__name__", lambda: __name__) == '__main__':
    _l_(430653)

    _c_(430651, _n_(430650, "main", lambda: main))
    _l_(430652)