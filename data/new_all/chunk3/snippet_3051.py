# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/50411547/peewee-attributeerror-when-select-with-more-than-one-join
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import peewee as pw
    _l_(547931)

except ImportError:
    pass


# Conection to mydbname database
dbn = 'mydbname'
_l_(547932)
user = 'myusername'
_l_(547933)
pwd = '******'
_l_(547934)
host = 'localhost'
_l_(547935)
prt = 3306
_l_(547936)

db = _c_(547944, _a_(547938, _n_(547937, "pw", lambda: pw), "MySQLDatabase"), _n_(547939, "dbn", lambda: dbn), user=_n_(547940, "user", lambda: user),
                  password=_n_(547941, "pwd", lambda: pwd),  host=_n_(547942, "host", lambda: host), port=_n_(547943, "prt", lambda: prt))
_l_(547945)


class MySqlDbModel(_a_(547947, _n_(547946, "pw", lambda: pw), "Model")):
    _l_(547951)

    class Meta:
        _l_(547950)

        database = _n_(547948, "db", lambda: db)
        _l_(547949)


class AgeCitas(_n_(547952, "MySqlDbModel", lambda: MySqlDbModel)):
    _l_(547989)

    CIT_ID = _c_(547955, _a_(547954, _n_(547953, "pw", lambda: pw), "BigIntegerField"))
    _l_(547956)
    AGE_ID = _c_(547959, _a_(547958, _n_(547957, "pw", lambda: pw), "BigIntegerField"))
    _l_(547960)
    FECHAHORA = _c_(547963, _a_(547962, _n_(547961, "pw", lambda: pw), "DateTimeField"))
    _l_(547964)
    ACT_ID = _c_(547967, _a_(547966, _n_(547965, "pw", lambda: pw), "BigIntegerField"))
    _l_(547968)
    PAC_ID = _c_(547971, _a_(547970, _n_(547969, "pw", lambda: pw), "BigIntegerField"))
    _l_(547972)
    ASIGNADA = _c_(547975, _a_(547974, _n_(547973, "pw", lambda: pw), "CharField"))
    _l_(547976)
    IND_ID = _c_(547979, _a_(547978, _n_(547977, "pw", lambda: pw), "BigIntegerField"))
    _l_(547980)
    ACUDIO = _c_(547983, _a_(547982, _n_(547981, "pw", lambda: pw), "DoubleField"))
    _l_(547984)
    ORDEN = _c_(547987, _a_(547986, _n_(547985, "pw", lambda: pw), "DoubleField"))
    _l_(547988)

class Meta:
    _l_(547991)

    table_name = 'AGE_CITAS'
    _l_(547990)


class AgeAgendas(_n_(547992, "MySqlDbModel", lambda: MySqlDbModel)):
    _l_(548021)

    AGE_ID = _c_(547995, _a_(547994, _n_(547993, "pw", lambda: pw), "DecimalField"))
    _l_(547996)
    CODIGO = _c_(547999, _a_(547998, _n_(547997, "pw", lambda: pw), "CharField"))
    _l_(548000)
    CEN_ID = _c_(548003, _a_(548002, _n_(548001, "pw", lambda: pw), "DecimalField"))
    _l_(548004)
    PER_ID = _c_(548007, _a_(548006, _n_(548005, "pw", lambda: pw), "DecimalField"))
    _l_(548008)
    NPR_ID = _c_(548011, _a_(548010, _n_(548009, "pw", lambda: pw), "DecimalField"))
    _l_(548012)
    DESCRIPCION = _c_(548015, _a_(548014, _n_(548013, "pw", lambda: pw), "CharField"))
    _l_(548016)
    COLOR = _c_(548019, _a_(548018, _n_(548017, "pw", lambda: pw), "CharField"))
    _l_(548020)

class Meta:
    _l_(548023)

    table_name = 'AGE_AGENDAS'
    _l_(548022)


class StkPersonas(_n_(548024, "MySqlDbModel", lambda: MySqlDbModel)):
    _l_(548089)

    PER_ID = _c_(548027, _a_(548026, _n_(548025, "pw", lambda: pw), "BigIntegerField"))
    _l_(548028)
    DOCUMENTO = _c_(548031, _a_(548030, _n_(548029, "pw", lambda: pw), "CharField"))
    _l_(548032)
    NOMBRE = _c_(548035, _a_(548034, _n_(548033, "pw", lambda: pw), "CharField"))
    _l_(548036)
    APELLIDO1 = _c_(548039, _a_(548038, _n_(548037, "pw", lambda: pw), "CharField"))
    _l_(548040)
    APELLIDO2 = _c_(548043, _a_(548042, _n_(548041, "pw", lambda: pw), "CharField"))
    _l_(548044)
    FECHA_ALTA = _c_(548047, _a_(548046, _n_(548045, "pw", lambda: pw), "DateTimeField"))
    _l_(548048)
    FECHA_BAJA = _c_(548051, _a_(548050, _n_(548049, "pw", lambda: pw), "DateTimeField"))
    _l_(548052)
    EMAIL = _c_(548055, _a_(548054, _n_(548053, "pw", lambda: pw), "CharField"))
    _l_(548056)
    TELEFONO1 = _c_(548059, _a_(548058, _n_(548057, "pw", lambda: pw), "CharField"))
    _l_(548060)
    TELEFONO2 = _c_(548063, _a_(548062, _n_(548061, "pw", lambda: pw), "CharField"))
    _l_(548064)
    TELEFONO3 = _c_(548067, _a_(548066, _n_(548065, "pw", lambda: pw), "CharField"))
    _l_(548068)
    TELEFONO4 = _c_(548071, _a_(548070, _n_(548069, "pw", lambda: pw), "CharField"))
    _l_(548072)
    SEXO = _c_(548075, _a_(548074, _n_(548073, "pw", lambda: pw), "CharField"))
    _l_(548076)
    NACIMIENTO = _c_(548079, _a_(548078, _n_(548077, "pw", lambda: pw), "DateTimeField"))
    _l_(548080)
    ES_PACIENTE = _c_(548083, _a_(548082, _n_(548081, "pw", lambda: pw), "CharField"))
    _l_(548084)
    ES_PROFESIONAL = _c_(548087, _a_(548086, _n_(548085, "pw", lambda: pw), "CharField"))
    _l_(548088)

class Meta:
    _l_(548091)

    table_name = 'STK_PERSONAS'
    _l_(548090)