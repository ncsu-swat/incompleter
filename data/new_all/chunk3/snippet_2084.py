# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65149626/how-to-correct-typeerror-execute-takes-from-2-to-4-positional-arguments-but-5
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
if _n_(578852, "user_input", lambda: user_input)==2:
    _l_(578893)

    number=_c_(578856, _n_(578853, "int", lambda: int), _c_(578855, _n_(578854, "input", lambda: input), "Enter number of tickets you want to book-"))
    _l_(578857)
    for b in _c_(578860, _n_(578858, "range", lambda: range), 0,_n_(578859, "number", lambda: number)):
        _l_(578892)

        passengername=_c_(578862, _n_(578861, "input", lambda: input), "Enter name of passenger-")
        _l_(578863)
        starting_station=_c_(578865, _n_(578864, "input", lambda: input), "Enter name of station from where passenger will board train-")
        _l_(578866)
        destination=_c_(578868, _n_(578867, "input", lambda: input), "Enter name of station passenger wishes to reach-")
        _l_(578869)
                    
        _c_(578871, _n_(578870, "print", lambda: print), "Ticket Booked!")
        _l_(578872)
        mydb=_c_(578876, _a_(578875, _a_(578874, _n_(578873, "mysql", lambda: mysql), "connector"), "connect"), host="localhost",user="root",passwd="",database="railways")
        _l_(578877)
        mycursor=_c_(578880, _a_(578879, _n_(578878, "mydb", lambda: mydb), "cursor"))
        _l_(578881)
        _c_(578886, _a_(578883, _n_(578882, "mycursor", lambda: mycursor), "execute"), "select train_no from route_fare where from_station=%s",(_n_(578884, "starting_station", lambda: starting_station),), " and to_station=%s",(_n_(578885, "destination", lambda: destination),))
        _l_(578887)
        for w in _n_(578888, "mycursor", lambda: mycursor):
            _l_(578891)

            train_number_p=_n_(578889, "w", lambda: w)
            _l_(578890)