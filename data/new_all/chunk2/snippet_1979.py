# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/73741857/attributeerror-function-object-has-no-attribute-read-excel
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def load():
    _l_(439893)

    path=_c_(439882, _a_(439881, _n_(439880, "filedialog", lambda: filedialog), "askopenfilename"))
    _l_(439883)
    df=_c_(439887, _a_(439885, _n_(439884, "pd", lambda: pd), "read_excel"), _n_(439886, "path", lambda: path))
    _l_(439888)
    _c_(439891, _n_(439889, "print", lambda: print), _n_(439890, "df", lambda: df))
    _l_(439892)
def save():
    _l_(439981)

    mese = _c_(439896, _a_(439895, _n_(439894, "entry2", lambda: entry2), "get"))
    _l_(439897)
    altezza = _c_(439900, _a_(439899, _n_(439898, "entry3", lambda: entry3), "get"))
    _l_(439901)
    peso = _c_(439904, _a_(439903, _n_(439902, "entry4", lambda: entry4), "get"))
    _l_(439905)
    mmagra = _c_(439908, _a_(439907, _n_(439906, "entry5", lambda: entry5), "get"))
    _l_(439909)
    mgrassa = _c_(439912, _a_(439911, _n_(439910, "entry6", lambda: entry6), "get"))
    _l_(439913)
    utente = _c_(439916, _a_(439915, _n_(439914, "entry7", lambda: entry7), "get"))
    _l_(439917)
    wb = _c_(439919, _n_(439918, "Workbook", lambda: Workbook))
    _l_(439920)
    ws = _a_(439922, _n_(439921, "wb", lambda: wb), "active")
    _l_(439923)
    _n_(439924, "ws", lambda: ws)['A1'] = "Mese"
    _l_(439925)
    _n_(439926, "ws", lambda: ws)['B1'] = "Altezza"
    _l_(439927)
    _n_(439928, "ws", lambda: ws)['C1'] = "Peso"
    _l_(439929)
    _n_(439930, "ws", lambda: ws)['D1'] = "Massa Magra"
    _l_(439931)
    _n_(439932, "ws", lambda: ws)['E1'] = "Massa Grassa"
    _l_(439933)
    _n_(439934, "ws", lambda: ws)['F1'] = "Utente"
    _l_(439935)
    _n_(439936, "ws", lambda: ws)['A2'] = _n_(439937, "mese", lambda: mese)
    _l_(439938)
    _n_(439939, "ws", lambda: ws)['B2'] = _n_(439940, "altezza", lambda: altezza)
    _l_(439941)
    _n_(439942, "ws", lambda: ws)['C2'] = _n_(439943, "peso", lambda: peso)
    _l_(439944)
    _n_(439945, "ws", lambda: ws)['D2'] = _n_(439946, "mmagra", lambda: mmagra)
    _l_(439947)
    _n_(439948, "ws", lambda: ws)['E2'] = _n_(439949, "mgrassa", lambda: mgrassa)
    _l_(439950)
    _n_(439951, "ws", lambda: ws)['F2'] = _n_(439952, "utente", lambda: utente)
    _l_(439953)
    _c_(439956, _a_(439955, _n_(439954, "wb", lambda: wb), "save"), r'C:\Users\lricci\Desktop\SERVER\web\Gym Tracker\Gym Tracker v1.0\track.xlsx')
    _l_(439957)
    _c_(439959, _n_(439958, "showinfo", lambda: showinfo), "Salvataggio")
    _l_(439960)
    file1 = _c_(439963, _a_(439962, _n_(439961, "pd", lambda: pd), "read_excel"), "track.xlsx")
    _l_(439964)
    file2 = _c_(439967, _a_(439966, _n_(439965, "pd", lambda: pd), "read_excel"), "trackn.xlsx")
    _l_(439968)
    all = [_n_(439969, "file1", lambda: file1), _n_(439970, "file2", lambda: file2)]
    _l_(439971)
    append = _c_(439975, _a_(439973, _n_(439972, "pd", lambda: pd), "concat"), _n_(439974, "all", lambda: all))
    _l_(439976)
    _c_(439979, _a_(439978, _n_(439977, "append", lambda: append), "to_excel"), "track.xlsx", index=False)
    _l_(439980)
def delete():
    _l_(440018)

    _c_(439986, _a_(439983, _n_(439982, "entry2", lambda: entry2), "delete"), 0, _a_(439985, _n_(439984, "tk", lambda: tk), "END"))
    _l_(439987)
    _c_(439992, _a_(439989, _n_(439988, "entry3", lambda: entry3), "delete"), 0, _a_(439991, _n_(439990, "tk", lambda: tk), "END"))
    _l_(439993)
    _c_(439998, _a_(439995, _n_(439994, "entry4", lambda: entry4), "delete"), 0, _a_(439997, _n_(439996, "tk", lambda: tk), "END"))
    _l_(439999)
    _c_(440004, _a_(440001, _n_(440000, "entry5", lambda: entry5), "delete"), 0, _a_(440003, _n_(440002, "tk", lambda: tk), "END"))
    _l_(440005)
    _c_(440010, _a_(440007, _n_(440006, "entry6", lambda: entry6), "delete"), 0, _a_(440009, _n_(440008, "tk", lambda: tk), "END"))
    _l_(440011)
    _c_(440016, _a_(440013, _n_(440012, "entry7", lambda: entry7), "delete"), 0, _a_(440015, _n_(440014, "tk", lambda: tk), "END"))
    _l_(440017)

# Main frame
windows = _c_(440021, _a_(440020, _n_(440019, "tk", lambda: tk), "Tk"))
_l_(440022)
_c_(440025, _a_(440024, _n_(440023, "windows", lambda: windows), "geometry"), "400x350")
_l_(440026)
_c_(440029, _a_(440028, _n_(440027, "windows", lambda: windows), "title"), "Gym Tracker")
_l_(440030)
_c_(440033, _a_(440032, _n_(440031, "windows", lambda: windows), "resizable"), False, False)
_l_(440034)

#Frame 2
frame1 = _c_(440039, _a_(440038, _c_(440037, _n_(440035, "Frame", lambda: Frame), _n_(440036, "windows", lambda: windows), width=150, height=30, highlightcolor="white",highlightbackground="black", highlightthickness=1), "place"), x=120, y=2)
_l_(440040)
label1= _c_(440045, _a_(440044, _c_(440043, _n_(440041, "Label", lambda: Label), _n_(440042, "windows", lambda: windows), text="GYM TRACKER"), "place"), x=150, y=7)
_l_(440046)
frame2 = _c_(440051, _a_(440050, _c_(440049, _n_(440047, "Frame", lambda: Frame), _n_(440048, "windows", lambda: windows), width=500, height=1, highlightcolor="white",highlightbackground="black", highlightthickness=1), "place"), x=2, y=45)
_l_(440052)

# Combobox Mese
label2 = _c_(440057, _a_(440056, _c_(440055, _n_(440053, "Label", lambda: Label), _n_(440054, "windows", lambda: windows), text="Mese"), "place"), x=110, y=60)
_l_(440058)
combobox = _c_(440063, _a_(440062, _c_(440061, _n_(440059, "Combobox", lambda: Combobox), _n_(440060, "windows", lambda: windows), values=['Gennaio', 'Febbraio', 'Marzo', 'Aprile', 'Maggio', 'Giugno','Luglio', 'Agosto', 'Settembre', 'Ottobre', 'Novembre', 'Dicembre']), "place"), x=200, y=60)
_l_(440064)
entry2 = _c_(440068, _a_(440066, _n_(440065, "tk", lambda: tk), "Entry"), _n_(440067, "windows", lambda: windows))
_l_(440069)

label3 = _c_(440074, _a_(440073, _c_(440072, _n_(440070, "Label", lambda: Label), _n_(440071, "windows", lambda: windows), text="Altezza"), "place"), x=110, y=90)
_l_(440075)
textbox1 = _c_(440080, _a_(440079, _c_(440078, _n_(440076, "Text", lambda: Text), _n_(440077, "windows", lambda: windows), width=17, height=1), "place"), x=200, y=90)
_l_(440081)
entry3 = _c_(440085, _a_(440083, _n_(440082, "tk", lambda: tk), "Entry"), _n_(440084, "windows", lambda: windows))
_l_(440086)

label4 = _c_(440091, _a_(440090, _c_(440089, _n_(440087, "Label", lambda: Label), _n_(440088, "windows", lambda: windows), text="Peso"), "place"), x=110, y=120)
_l_(440092)
textbox = _c_(440097, _a_(440096, _c_(440095, _n_(440093, "Text", lambda: Text), _n_(440094, "windows", lambda: windows), width=17, height=1), "place"), x=200, y=120)
_l_(440098)
entry4 = _c_(440102, _a_(440100, _n_(440099, "tk", lambda: tk), "Entry"), _n_(440101, "windows", lambda: windows))
_l_(440103)

label5 = _c_(440108, _a_(440107, _c_(440106, _n_(440104, "Label", lambda: Label), _n_(440105, "windows", lambda: windows), text="Massa Magra"), "place"), x=110, y=150)
_l_(440109)
textbox = _c_(440114, _a_(440113, _c_(440112, _n_(440110, "Text", lambda: Text), _n_(440111, "windows", lambda: windows), width=17, height=1), "place"), x=200, y=150)
_l_(440115)
entry5 = _c_(440119, _a_(440117, _n_(440116, "tk", lambda: tk), "Entry"), _n_(440118, "windows", lambda: windows))
_l_(440120)

label6 = _c_(440125, _a_(440124, _c_(440123, _n_(440121, "Label", lambda: Label), _n_(440122, "windows", lambda: windows), text="Massa Grassa"), "place"), x=110, y=180)
_l_(440126)
textbox = _c_(440131, _a_(440130, _c_(440129, _n_(440127, "Text", lambda: Text), _n_(440128, "windows", lambda: windows), width=17, height=1), "place"), x=200, y=180)
_l_(440132)
entry6 = _c_(440136, _a_(440134, _n_(440133, "tk", lambda: tk), "Entry"), _n_(440135, "windows", lambda: windows))
_l_(440137)
# Combobox Utente
label7 = _c_(440142, _a_(440141, _c_(440140, _n_(440138, "Label", lambda: Label), _n_(440139, "windows", lambda: windows), text="Utente"), "place"), x=110, y=210)
_l_(440143)
combobox = _c_(440148, _a_(440147, _c_(440146, _n_(440144, "Combobox", lambda: Combobox), _n_(440145, "windows", lambda: windows), values=['Erika', 'Lorenzo']), "place"), x=200, y=210)
_l_(440149)
entry7 = _c_(440153, _a_(440151, _n_(440150, "tk", lambda: tk), "Entry"), _n_(440152, "windows", lambda: windows))
_l_(440154)

# Bottoni
b1 = _c_(440161, _a_(440160, _c_(440159, _a_(440156, _n_(440155, "tk", lambda: tk), "Button"), _n_(440157, "windows", lambda: windows), text="Elimina", command=_n_(440158, "delete", lambda: delete) ,width=8, height=1), "place"), x=170, y=310)
_l_(440162)
b2 = _c_(440169, _a_(440168, _c_(440167, _a_(440164, _n_(440163, "tk", lambda: tk), "Button"), _n_(440165, "windows", lambda: windows), text="Load", width=8, height=1,command=_n_(440166, "load", lambda: load)), "place"), x=300, y=310)
_l_(440170)
b3 = _c_(440177, _a_(440176, _c_(440175, _a_(440172, _n_(440171, "tk", lambda: tk), "Button"), _n_(440173, "windows", lambda: windows), text="Salva", width=8, height=1, command=_n_(440174, "save", lambda: save)), "place"), x=50, y=310)
_l_(440178)
_c_(440181, _a_(440180, _n_(440179, "windows", lambda: windows), "mainloop"))
_l_(440182)