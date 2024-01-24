# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56381315/attribute-errormodule-mysql-has-no-attribute-connector
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import mysql.connector
    _l_(567682)

except ImportError:
    pass
try:
    import random
    _l_(567684)

except ImportError:
    pass
first_names=['Jodee,Marielle,Phillip,Colby,Stephany,Dione,Grover,Napoleon,Nicholas,Alysa,Noma,Leta,Ciera,Donny,Buc,Iren,Renato,Glory,Stacia,Bennie,Soo,Mitzie,Kaci,Peggy,Hilma,Melva,Cindie,Miyoko,Melina,Cammy,Blanche,Rhea,Jill,Kellye,Ailene,Vida,Alva,Sau,Hollis,Oswaldo,Marty']
_l_(567685)
last_names=['Bula,Bibi,Rolf,Tayna,Ardith,Art,Jeannetta,Patrina,Ronny,Maida,Cleopatra,Sherry,Vincenza,Sheri,Sherlyn,Shayne,Geneva,Javier,Celine,Saran,Shari,Boris,Gwyneth,Summer,Maryellen,Rufina,Essie,Palma,Rafael,Cordell,Jude,Jenine,Manuel,Cleveland,Daphine,Lavina,Candi,Rossie,Brunilda,Gilberte,Nick,Hoyt,Lucius,Ardis,Tyler,Dwain,Caleb,Aide,Mckinley,Margurite']
_l_(567686)
mydb=_c_(567689, _a_(567688, _a_(567687, mysql, "connector"), "connect"), host='localhost',user='root',passwd='hariom21feb',database='test')
_l_(567690)
mycursor=_c_(567693, _a_(567692, _n_(567691, "mydb", lambda: mydb), "cursor"))
_l_(567694)
fkey=_c_(567697, _a_(567696, _n_(567695, "random", lambda: random), "randint"), 0,49)
_l_(567698)
lkey=_c_(567701, _a_(567700, _n_(567699, "random", lambda: random), "randint"), 0,49)
_l_(567702)
nkey=_c_(567705, _a_(567704, _n_(567703, "random", lambda: random), "randint"), 0,50)
_l_(567706)
for i in _c_(567709, _n_(567707, "range", lambda: range), _n_(567708, "nkey", lambda: nkey)):
    _l_(567724)

    query=('insert into test value(%s,%s,%s,%s,%s)')
    _l_(567710)
    tup=('L5W4NW',_c_(567713, _n_(567711, "first_names", lambda: first_names), _n_(567712, "fkey", lambda: fkey)),_c_(567716, _n_(567714, "last_names", lambda: last_names), _n_(567715, "lkey", lambda: lkey)),'2970','completed')
    _l_(567717)
    _c_(567722, _a_(567719, _n_(567718, "mycursor", lambda: mycursor), "execute"), _n_(567720, "query", lambda: query),_n_(567721, "tup", lambda: tup))
    _l_(567723)
_c_(567727, _a_(567726, _n_(567725, "mydb", lambda: mydb), "commit"))
_l_(567728)