# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/71795534/traceback-most-recent-call-last-attributeerror-nonetype-object-has-no-attr
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
  from tkinter import *
  _l_(356733)

except ImportError:
  pass
try:
  import pandas as pd
  _l_(356735)

except ImportError:
  pass


def send_info():
  _l_(356903)

  path = 'Registers.form.xlsx'
  _l_(356736)
  df1 = _c_(356740, _a_(356738, _n_(356737, "pd", lambda: pd), "read_excel"), _n_(356739, "path", lambda: path))
  _l_(356741)
  SeriesA = _n_(356742, "df1", lambda: df1)['firstname']
  _l_(356743)
  SeriesB = _n_(356744, "df1", lambda: df1)['secondname']
  _l_(356745)
  SeriesC = _n_(356746, "df1", lambda: df1)['thirdname']
  _l_(356747)
  SeriesD = _n_(356748, "df1", lambda: df1)['age']
  _l_(356749)
  SeriesE = _n_(356750, "df1", lambda: df1)['phonenumber']
  _l_(356751)
  SeriesF = _n_(356752, "df1", lambda: df1)['Departmentname']
  _l_(356753)
  SeriesG = _n_(356754, "df1", lambda: df1)['familymembers']
  _l_(356755)
  SeriesH = _n_(356756, "df1", lambda: df1)['bookingdate']
  _l_(356757)
  A = _c_(356762, _a_(356759, _n_(356758, "pd", lambda: pd), "Series"), _a_(356761, _n_(356760, "firstname", lambda: firstname), "get"))
  _l_(356763)
  B = _c_(356768, _a_(356765, _n_(356764, "pd", lambda: pd), "Series"), _a_(356767, _n_(356766, "secondname", lambda: secondname), "get"))
  _l_(356769)
  C = _c_(356774, _a_(356771, _n_(356770, "pd", lambda: pd), "Series"), _a_(356773, _n_(356772, "thirdname", lambda: thirdname), "get"))
  _l_(356775)
  D = _c_(356780, _a_(356777, _n_(356776, "pd", lambda: pd), "Series"), _a_(356779, _n_(356778, "age", lambda: age), "get"))
  _l_(356781)
  E = _c_(356786, _a_(356783, _n_(356782, "pd", lambda: pd), "Series"), _a_(356785, _n_(356784, "phonenumber", lambda: phonenumber), "get"))
  _l_(356787)
  F = _c_(356792, _a_(356789, _n_(356788, "pd", lambda: pd), "Series"), _a_(356791, _n_(356790, "Departmentname", lambda: Departmentname), "get"))
  _l_(356793)
  G = _c_(356798, _a_(356795, _n_(356794, "pd", lambda: pd), "Series"), _a_(356797, _n_(356796, "familymembers", lambda: familymembers), "get"))
  _l_(356799)
  H = _c_(356804, _a_(356801, _n_(356800, "pd", lambda: pd), "Series"), _a_(356803, _n_(356802, "bookingdate", lambda: bookingdate), "get"))
  _l_(356805)
  SeriesA = _c_(356809, _a_(356807, _n_(356806, "SeriesA", lambda: SeriesA), "append"), _n_(356808, "A", lambda: A))
  _l_(356810)
  SeriesB = _c_(356814, _a_(356812, _n_(356811, "SeriesA", lambda: SeriesA), "append"), _n_(356813, "B", lambda: B))
  _l_(356815)
  SeriesC = _c_(356819, _a_(356817, _n_(356816, "SeriesA", lambda: SeriesA), "append"), _n_(356818, "C", lambda: C))
  _l_(356820)
  SeriesD = _c_(356824, _a_(356822, _n_(356821, "SeriesA", lambda: SeriesA), "append"), _n_(356823, "D", lambda: D))
  _l_(356825)
  SeriesE = _c_(356829, _a_(356827, _n_(356826, "SeriesA", lambda: SeriesA), "append"), _n_(356828, "E", lambda: E))
  _l_(356830)
  SeriesF = _c_(356834, _a_(356832, _n_(356831, "SeriesA", lambda: SeriesA), "append"), _n_(356833, "F", lambda: F))
  _l_(356835)
  SeriesG = _c_(356839, _a_(356837, _n_(356836, "SeriesA", lambda: SeriesA), "append"), _n_(356838, "G", lambda: G))
  _l_(356840)
  SeriesH = _c_(356844, _a_(356842, _n_(356841, "SeriesA", lambda: SeriesA), "append"), _n_(356843, "H", lambda: H))
  _l_(356845)
  df2 = _c_(356856, _a_(356847, _n_(356846, "pd", lambda: pd), "DataFrame"), {"firstname": _n_(356848, "SeriesA", lambda: SeriesA), "secondnamer": _n_(356849, "SeriesB", lambda: SeriesB), "thirdname": _n_(356850, "SeriesC", lambda: SeriesC), "age": _n_(356851, "SeriesD", lambda: SeriesD), "phonenumber": _n_(356852, "SeriesE", lambda: SeriesE), "Departmentname": _n_(356853, "SeriesF", lambda: SeriesF), "familymembers": _n_(356854, "SeriesG", lambda: SeriesG), "bookingdate": _n_(356855, "SeriesH", lambda: SeriesH)})
  _l_(356857)
  _c_(356861, _a_(356859, _n_(356858, "df2", lambda: df2), "to_excel"), _n_(356860, "path", lambda: path), index=False)
  _l_(356862)











  _c_(356866, _a_(356864, _n_(356863, "firstname_entry", lambda: firstname_entry), "delete"), 0, _n_(356865, "END", lambda: END))
  _l_(356867)
  _c_(356871, _a_(356869, _n_(356868, "secondname_entry", lambda: secondname_entry), "delete"), 0, _n_(356870, "END", lambda: END))
  _l_(356872)
  _c_(356876, _a_(356874, _n_(356873, "thirdname_entry", lambda: thirdname_entry), "delete"), 0, _n_(356875, "END", lambda: END))
  _l_(356877)
  _c_(356881, _a_(356879, _n_(356878, "age_entry", lambda: age_entry), "delete"), 0, _n_(356880, "END", lambda: END))
  _l_(356882)
  _c_(356886, _a_(356884, _n_(356883, "phonenumber_entry", lambda: phonenumber_entry), "delete"), 0, _n_(356885, "END", lambda: END))
  _l_(356887)
  _c_(356891, _a_(356889, _n_(356888, "Departmentname_entry", lambda: Departmentname_entry), "delete"), 0, _n_(356890, "END", lambda: END))
  _l_(356892)
  _c_(356896, _a_(356894, _n_(356893, "familymembers_entry", lambda: familymembers_entry), "delete"), 0, _n_(356895, "END", lambda: END))
  _l_(356897)
  _c_(356901, _a_(356899, _n_(356898, "bookingdate_entry", lambda: bookingdate_entry), "delete"), 0, _n_(356900, "END", lambda: END))
  _l_(356902)
screen = _c_(356905, _n_(356904, "Tk", lambda: Tk))
_l_(356906)
_c_(356909, _a_(356908, _n_(356907, "screen", lambda: screen), "geometry"), "1080x1080")
_l_(356910)
_c_(356913, _a_(356912, _n_(356911, "screen", lambda: screen), "title"), "مديرية شؤون البطاقة الوطنية")
_l_(356914)
welcome_text = _c_(356916, _n_(356915, "Label", lambda: Label), text="أهلا وسهلا بكم في الحجز الالكتروني للبطاقة الموحدة ", fg="white", bg="green",height=2 ,width=1080)
_l_(356917)
_c_(356920, _a_(356919, _n_(356918, "welcome_text", lambda: welcome_text), "grid"))
_l_(356921)
 
firstname_text = _c_(356925, _a_(356924, _c_(356923, _n_(356922, "Label", lambda: Label), text = "الاسم الاول * ",), "grid"), row=0)
_l_(356926)
secondname_text = _c_(356930, _a_(356929, _c_(356928, _n_(356927, "Label", lambda: Label), text = "الاسم الثاني * ",), "grid"), row=1)
_l_(356931)
thirdname_text = _c_(356935, _a_(356934, _c_(356933, _n_(356932, "Label", lambda: Label), text = "الاسم الثالث * ",), "grid"), row=2)
_l_(356936)
age_text = _c_(356940, _a_(356939, _c_(356938, _n_(356937, "Label", lambda: Label), text = "العمر * ",), "grid"), row=3)
_l_(356941)
phonenumber_text = _c_(356945, _a_(356944, _c_(356943, _n_(356942, "Label", lambda: Label), text = "رقم الهاتف * ",), "grid"), row=4)
_l_(356946)
Departmentname_text = _c_(356950, _a_(356949, _c_(356948, _n_(356947, "Label", lambda: Label), text = "اسم دائرة الاحوال المدنية * ",), "grid"), row=5)
_l_(356951)
familymembers_text = _c_(356955, _a_(356954, _c_(356953, _n_(356952, "Label", lambda: Label), text = "عدد افراد الاسرة * ",), "grid"), row=6)
_l_(356956)
bookingdate_text = _c_(356960, _a_(356959, _c_(356958, _n_(356957, "Label", lambda: Label), text = "موعد تاريخ الحجز المطلوب * ",), "grid"), row=7)
_l_(356961)

_c_(356964, _a_(356963, _n_(356962, "firstname_text", lambda: firstname_text), "place"), x = 540, y = 70)
_l_(356965)
_c_(356968, _a_(356967, _n_(356966, "secondname_text", lambda: secondname_text), "place"), x = 540, y = 130)
_l_(356969)
_c_(356972, _a_(356971, _n_(356970, "thirdname_text", lambda: thirdname_text), "place"), x = 540, y = 190)
_l_(356973)
_c_(356976, _a_(356975, _n_(356974, "age_text", lambda: age_text), "place"), x = 540, y = 250)
_l_(356977)
_c_(356980, _a_(356979, _n_(356978, "phonenumber_text", lambda: phonenumber_text), "place"), x = 540, y = 310)
_l_(356981)
_c_(356984, _a_(356983, _n_(356982, "Departmentname_text", lambda: Departmentname_text), "place"), x = 540, y = 370)
_l_(356985)
_c_(356988, _a_(356987, _n_(356986, "familymembers_text", lambda: familymembers_text), "place"), x = 540, y = 430)
_l_(356989)
_c_(356992, _a_(356991, _n_(356990, "bookingdate_text", lambda: bookingdate_text), "place"), x = 540, y = 490)
_l_(356993)



firstname = _c_(356995, _n_(356994, "StringVar", lambda: StringVar))
_l_(356996)
secondname = _c_(356998, _n_(356997, "StringVar", lambda: StringVar))
_l_(356999)
thirdname = _c_(357001, _n_(357000, "StringVar", lambda: StringVar))
_l_(357002)
age = _c_(357004, _n_(357003, "StringVar", lambda: StringVar))
_l_(357005)
phonenumber = _c_(357007, _n_(357006, "StringVar", lambda: StringVar))
_l_(357008)
Departmentname = _c_(357010, _n_(357009, "StringVar", lambda: StringVar))
_l_(357011)
familymembers = _c_(357013, _n_(357012, "StringVar", lambda: StringVar))
_l_(357014)
bookingdate = _c_(357016, _n_(357015, "StringVar", lambda: StringVar))
_l_(357017)

firstname_entry = _c_(357020, _n_(357018, "Entry", lambda: Entry), textvariable = _n_(357019, "firstname", lambda: firstname), width = "40")
_l_(357021)
secondname_entry = _c_(357024, _n_(357022, "Entry", lambda: Entry), textvariable = _n_(357023, "secondname", lambda: secondname), width = "40")
_l_(357025)
thirdname_entry = _c_(357028, _n_(357026, "Entry", lambda: Entry), textvariable = _n_(357027, "thirdname", lambda: thirdname), width = "40")
_l_(357029)
age_entry = _c_(357032, _n_(357030, "Entry", lambda: Entry), textvariable = _n_(357031, "age", lambda: age), width = "40")
_l_(357033)
phonenumber_entry = _c_(357036, _n_(357034, "Entry", lambda: Entry), textvariable = _n_(357035, "phonenumber", lambda: phonenumber), width = "40")
_l_(357037)
Departmentname_entry = _c_(357040, _n_(357038, "Entry", lambda: Entry), textvariable = _n_(357039, "Departmentname", lambda: Departmentname), width = "40")
_l_(357041)
familymembers_entry = _c_(357044, _n_(357042, "Entry", lambda: Entry), textvariable = _n_(357043, "familymembers", lambda: familymembers), width = "40")
_l_(357045)
bookingdate_entry = _c_(357048, _n_(357046, "Entry", lambda: Entry), textvariable = _n_(357047, "bookingdate", lambda: bookingdate), width = "40")
_l_(357049)

_c_(357052, _a_(357051, _n_(357050, "firstname_entry", lambda: firstname_entry), "place"), x = 450, y = 100)
_l_(357053)
_c_(357056, _a_(357055, _n_(357054, "secondname_entry", lambda: secondname_entry), "place"), x = 450, y = 160)
_l_(357057)
_c_(357060, _a_(357059, _n_(357058, "thirdname_entry", lambda: thirdname_entry), "place"), x = 450, y = 220)
_l_(357061)
_c_(357064, _a_(357063, _n_(357062, "age_entry", lambda: age_entry), "place"), x = 450, y = 280)
_l_(357065)
_c_(357068, _a_(357067, _n_(357066, "phonenumber_entry", lambda: phonenumber_entry), "place"), x = 450, y = 340)
_l_(357069)
_c_(357072, _a_(357071, _n_(357070, "Departmentname_entry", lambda: Departmentname_entry), "place"), x = 450, y = 400)
_l_(357073)
_c_(357076, _a_(357075, _n_(357074, "familymembers_entry", lambda: familymembers_entry), "place"), x = 450, y = 460)
_l_(357077)
_c_(357080, _a_(357079, _n_(357078, "bookingdate_entry", lambda: bookingdate_entry), "place"), x = 450, y = 520)
_l_(357081)

_c_(357084, _a_(357083, _n_(357082, "firstname_entry", lambda: firstname_entry), "grid"), row=0,column=1)
_l_(357085)
_c_(357088, _a_(357087, _n_(357086, "secondname_entry", lambda: secondname_entry), "grid"), row=1,column=1)
_l_(357089)
_c_(357092, _a_(357091, _n_(357090, "thirdname_entry", lambda: thirdname_entry), "grid"), row=2,column=1)
_l_(357093)
_c_(357096, _a_(357095, _n_(357094, "age_entry", lambda: age_entry), "grid"), row=3,column=1)
_l_(357097)
_c_(357100, _a_(357099, _n_(357098, "phonenumber_entry", lambda: phonenumber_entry), "grid"), row=4,column=1)
_l_(357101)
_c_(357104, _a_(357103, _n_(357102, "Departmentname_entry", lambda: Departmentname_entry), "grid"), row=5,column=1)
_l_(357105)
_c_(357108, _a_(357107, _n_(357106, "familymembers_entry", lambda: familymembers_entry), "grid"), row=6,column=1)
_l_(357109)
_c_(357112, _a_(357111, _n_(357110, "bookingdate_entry", lambda: bookingdate_entry), "grid"), row=7,column=1)
_l_(357113)


register = _c_(357119, _a_(357118, _c_(357117, _n_(357114, "Button", lambda: Button), _n_(357115, "screen", lambda: screen),text = "Register", width = "60", height = "2", command = _n_(357116, "send_info", lambda: send_info), bg = "grey"), "grid"), row=3,column=1, pady=4)
_l_(357120)
_c_(357123, _a_(357122, _n_(357121, "register", lambda: register), "place"), x = 360, y = 600)
_l_(357124)

_c_(357127, _a_(357126, _n_(357125, "screen", lambda: screen), "mainloop"))
_l_(357128)