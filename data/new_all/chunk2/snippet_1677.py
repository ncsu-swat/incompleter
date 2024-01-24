# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64341578/attributeerror-choosebook-object-has-no-attribute-txtrd
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class ChooseBook():
    _l_(468788)


    bookprice=2
    _l_(468438)
    def getqty(self, sv):
        _l_(468469)

        if _c_(468442, _a_(468441, _a_(468440, _n_(468439, "self", lambda: self), "txtbookqty"), "get"))=="":
            _l_(468468)

            _n_(468443, "self", lambda: self).qty=0
            _l_(468444)
        else:
        
            _n_(468445, "self", lambda: self).qty=_c_(468451, _n_(468446, "int", lambda: int), _c_(468450, _a_(468449, _a_(468448, _n_(468447, "self", lambda: self), "sv"), "get")))
            _l_(468452)
            _c_(468457, _a_(468455, _a_(468454, _n_(468453, "self", lambda: self), "txtbookprice"), "delete"), 0,_n_(468456, "END", lambda: END))
            _l_(468458)
            #print(self.qty)
            _c_(468466, _a_(468461, _a_(468460, _n_(468459, "self", lambda: self), "txtbookprice"), "insert"), 0,_a_(468463, _n_(468462, "self", lambda: self), "qty")*_a_(468465, _n_(468464, "self", lambda: self), "bookprice"))
            _l_(468467)

    def on_CPOname_change(self,value,op,op2):
        _l_(468486)

        stname=_c_(468473, _a_(468472, _a_(468471, _n_(468470, "self", lambda: self), "comboBookname"), "get"))
        _l_(468474)
        name=_n_(468475, "stname", lambda: stname)[1:-1]
        _l_(468476)
        book_data=_c_(468479, _n_(468477, "Fun_Select", lambda: Fun_Select), "SELECT book_price FROM book_record WHERE book_name='"+_n_(468478, "name", lambda: name)+"'")
        _l_(468480)
        #print(book_data)
        _n_(468481, "self", lambda: self).bookprice=_c_(468484, _n_(468482, "int", lambda: int), _n_(468483, "book_data", lambda: book_data)[0][0])
        _l_(468485)

    def on_date_change(self,day):
        _l_(468547)

        if _c_(468490, _a_(468489, _a_(468488, _n_(468487, "self", lambda: self), "txtdaysborrowed"), "get"))=="":
            _l_(468546)

            _n_(468491, "self", lambda: self).dayadd=0
            _l_(468492)

        else:
            _n_(468493, "self", lambda: self).dayadd=_c_(468499, _n_(468494, "int", lambda: int), _c_(468498, _a_(468497, _a_(468496, _n_(468495, "self", lambda: self), "day"), "get")))
            _l_(468500)
            date=_c_(468504, _a_(468503, _a_(468502, _n_(468501, "self", lambda: self), "txtborrowdate"), "get"))
            _l_(468505)
            _n_(468506, "self", lambda: self).dayindate=_c_(468509, _n_(468507, "int", lambda: int), _n_(468508, "date", lambda: date)[8:10])
            _l_(468510)
            _n_(468511, "self", lambda: self).yearindate=_c_(468514, _n_(468512, "int", lambda: int), _n_(468513, "date", lambda: date)[0:4])
            _l_(468515)
            _n_(468516, "self", lambda: self).monthindate=_c_(468519, _n_(468517, "int", lambda: int), _n_(468518, "date", lambda: date)[5:7])
            _l_(468520)
            if _a_(468522, _n_(468521, "self", lambda: self), "dayindate")+_a_(468524, _n_(468523, "self", lambda: self), "dayadd") > 31:
                _l_(468534)

                _n_(468525, "self", lambda: self).monthindate=_a_(468527, _n_(468526, "self", lambda: self), "monthindate")+1
                _l_(468528)
                if _a_(468530, _n_(468529, "self", lambda: self), "monthindate") > 12:
                    _l_(468533)

                    _n_(468531, "self", lambda: self).yearindate+=1
                    _l_(468532)
            _c_(468544, _a_(468537, _a_(468536, _n_(468535, "self", lambda: self), "txtrd"), "insert"), 0,_a_(468539, _n_(468538, "self", lambda: self), "dayindate")+'-'+_a_(468541, _n_(468540, "self", lambda: self), "monthindate")+'-'+_a_(468543, _n_(468542, "self", lambda: self), "yearindate"))
            _l_(468545)
            


    def __init__(self):
        _l_(468787)


        
        
        today_date=_c_(468551, _a_(468550, _a_(468549, _n_(468548, "datetime", lambda: datetime), "date"), "today"))
        _l_(468552)
        win=_c_(468554, _n_(468553, "Tk", lambda: Tk))
        _l_(468555)
        _c_(468558, _a_(468557, _n_(468556, "win", lambda: win), "title"), "Choose book type")
        _l_(468559)
        _c_(468562, _a_(468561, _n_(468560, "win", lambda: win), "geometry"), "600x800")
        _l_(468563)
        v=_c_(468565, _n_(468564, "StringVar", lambda: StringVar))
        _l_(468566)
        d=_c_(468568, _n_(468567, "StringVar", lambda: StringVar))
        _l_(468569)
        _c_(468574, _a_(468571, _n_(468570, "v", lambda: v), "trace"), 'w', _a_(468573, _n_(468572, "self", lambda: self), "on_CPOname_change"))
        _l_(468575)
        _n_(468576, "self", lambda: self).day=_c_(468578, _n_(468577, "StringVar", lambda: StringVar))
        _l_(468579)
        _c_(468589, _a_(468582, _a_(468581, _n_(468580, "self", lambda: self), "day"), "trace"), 'w',lambda name, index, mode, day=_a_(468584, _n_(468583, "self", lambda: self), "day"): _c_(468588, _a_(468586, _n_(468585, "self", lambda: self), "on_date_change"), _n_(468587, "day", lambda: day)))
        _l_(468590)
        _n_(468591, "self", lambda: self).sv = _c_(468593, _n_(468592, "StringVar", lambda: StringVar))
        _l_(468594)
        _c_(468604, _a_(468597, _a_(468596, _n_(468595, "self", lambda: self), "sv"), "trace"), "w", lambda name, index, mode, sv=_a_(468599, _n_(468598, "self", lambda: self), "sv"): _c_(468603, _a_(468601, _n_(468600, "self", lambda: self), "getqty"), _n_(468602, "sv", lambda: sv)))
        _l_(468605)

        _c_(468610, _a_(468609, _c_(468608, _n_(468606, "Label", lambda: Label), _n_(468607, "win", lambda: win),text="Choose Book Name"), "grid"), row=0,column=0,padx="1.5c",pady="1c")
        _l_(468611)
        _c_(468616, _a_(468615, _c_(468614, _n_(468612, "Label", lambda: Label), _n_(468613, "win", lambda: win),text="Enter Book Quantity"), "grid"), row=1,column=0,padx="1.5c",pady="1c")
        _l_(468617)
        _c_(468622, _a_(468621, _c_(468620, _n_(468618, "Label", lambda: Label), _n_(468619, "win", lambda: win),text="Total Book Price"), "grid"), row=2,column=0,padx="1.5c",pady="1c")
        _l_(468623)
        _c_(468628, _a_(468627, _c_(468626, _n_(468624, "Label", lambda: Label), _n_(468625, "win", lambda: win),text="Borrowed Date"), "grid"), row=3,column=0,padx="1.5c",pady="1c")
        _l_(468629)
        _c_(468634, _a_(468633, _c_(468632, _n_(468630, "Label", lambda: Label), _n_(468631, "win", lambda: win),text="Days borrowed"), "grid"), row=4,column=0,padx="1.5c",pady="1c")
        _l_(468635)
        _c_(468640, _a_(468639, _c_(468638, _n_(468636, "Label", lambda: Label), _n_(468637, "win", lambda: win),text="Return Date"), "grid"), row=5,column=0,padx="1.5c",pady="1c")
        _l_(468641)
        _c_(468646, _a_(468645, _c_(468644, _n_(468642, "Label", lambda: Label), _n_(468643, "win", lambda: win),text="Choose Employee Name"), "grid"), row=6,column=0,padx="1.5c",pady="1c")
        _l_(468647)
        _c_(468652, _a_(468651, _c_(468650, _n_(468648, "Label", lambda: Label), _n_(468649, "win", lambda: win),text="Choose Customer Name"), "grid"), row=7,column=0,padx="1.5c",pady="1c")
        _l_(468653)
        
        #bookname
        _n_(468654, "self", lambda: self).comboBookname=_c_(468659, _a_(468656, _n_(468655, "ttk", lambda: ttk), "Combobox"), _n_(468657, "win", lambda: win), textvar=_n_(468658, "v", lambda: v))
        _l_(468660)
        _a_(468662, _n_(468661, "self", lambda: self), "comboBookname")["values"]=_c_(468664, _n_(468663, "Fun_Select", lambda: Fun_Select), "SELECT book_name FROM book_record")
        _l_(468665)
        _c_(468669, _a_(468668, _a_(468667, _n_(468666, "self", lambda: self), "comboBookname"), "grid"), row=0,column=1,pady="1c")
        _l_(468670)
        #bookqty
        _n_(468671, "self", lambda: self).txtbookqty=_c_(468676, _n_(468672, "Entry", lambda: Entry), _n_(468673, "win", lambda: win),textvariable=_a_(468675, _n_(468674, "self", lambda: self), "sv"))
        _l_(468677)
        _c_(468681, _a_(468680, _a_(468679, _n_(468678, "self", lambda: self), "txtbookqty"), "grid"), row=1,column=1,pady="1c")
        _l_(468682)
        #bookprice
        _n_(468683, "self", lambda: self).txtbookprice=_c_(468686, _n_(468684, "Entry", lambda: Entry), _n_(468685, "win", lambda: win))
        _l_(468687)
        _c_(468691, _a_(468690, _a_(468689, _n_(468688, "self", lambda: self), "txtbookprice"), "grid"), row=2,column=1,pady="1c")
        _l_(468692)
        #borrowdate
        _n_(468693, "self", lambda: self).txtborrowdate=_c_(468698, _n_(468694, "Entry", lambda: Entry), _n_(468695, "win", lambda: win),textvariable=_n_(468696, "d", lambda: d),state=_n_(468697, "DISABLED", lambda: DISABLED))
        _l_(468699)
        _c_(468703, _a_(468701, _n_(468700, "d", lambda: d), "set"), _n_(468702, "today_date", lambda: today_date))
        _l_(468704)
        _c_(468708, _a_(468707, _a_(468706, _n_(468705, "self", lambda: self), "txtborrowdate"), "grid"), row=3,column=1,pady="1c")
        _l_(468709)
        #daysborrowed
        _n_(468710, "self", lambda: self).txtdaysborrowed=_c_(468715, _n_(468711, "Entry", lambda: Entry), _n_(468712, "win", lambda: win),textvariable=_a_(468714, _n_(468713, "self", lambda: self), "day"))
        _l_(468716)
        _c_(468720, _a_(468719, _a_(468718, _n_(468717, "self", lambda: self), "day"), "set"), 0)
        _l_(468721)
        _c_(468725, _a_(468724, _a_(468723, _n_(468722, "self", lambda: self), "txtdaysborrowed"), "grid"), row=4,column=1,pady="1c")
        _l_(468726)
        #returndate
        _n_(468727, "self", lambda: self).txtrd=_c_(468730, _n_(468728, "Entry", lambda: Entry), _n_(468729, "win", lambda: win))
        _l_(468731)
        _c_(468735, _a_(468734, _a_(468733, _n_(468732, "self", lambda: self), "txtrd"), "grid"), row=5,column=1,pady="1c")
        _l_(468736)
        #employeename
        _n_(468737, "self", lambda: self).comboEmployeename=_c_(468741, _a_(468739, _n_(468738, "ttk", lambda: ttk), "Combobox"), _n_(468740, "win", lambda: win))
        _l_(468742)
        _a_(468744, _n_(468743, "self", lambda: self), "comboEmployeename")["values"]=_c_(468746, _n_(468745, "Fun_Select", lambda: Fun_Select), "SELECT employee_name FROM employees")
        _l_(468747)
        _c_(468751, _a_(468750, _a_(468749, _n_(468748, "self", lambda: self), "comboEmployeename"), "grid"), row=6,column=1,pady="1c")
        _l_(468752)
        #customername
        _n_(468753, "self", lambda: self).comboCustomername=_c_(468757, _a_(468755, _n_(468754, "ttk", lambda: ttk), "Combobox"), _n_(468756, "win", lambda: win))
        _l_(468758)
        _a_(468760, _n_(468759, "self", lambda: self), "comboCustomername")["values"]=_c_(468762, _n_(468761, "Fun_Select", lambda: Fun_Select), "SELECT customer_name FROM customers")
        _l_(468763)
        _c_(468767, _a_(468766, _a_(468765, _n_(468764, "self", lambda: self), "comboCustomername"), "grid"), row=7,column=1,pady="1c")
        _l_(468768)
        
        

        _c_(468775, _a_(468774, _c_(468773, _n_(468769, "Button", lambda: Button), _n_(468770, "win", lambda: win),text="Exit",width=10,command=_a_(468772, _n_(468771, "win", lambda: win), "destroy")), "grid"), row=8,column=0,padx="1.5c",pady="1c")
        _l_(468776)
        _c_(468781, _a_(468780, _c_(468779, _n_(468777, "Button", lambda: Button), _n_(468778, "win", lambda: win),text="Save",width=10,command=None), "grid"), row=8,column=1,padx="1.5c",pady="1c")
        _l_(468782)
                                    
        _c_(468785, _a_(468784, _n_(468783, "win", lambda: win), "mainloop"))
        _l_(468786)
_c_(468790, _n_(468789, "ChooseBook", lambda: ChooseBook))
_l_(468791)