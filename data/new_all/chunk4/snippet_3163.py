# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/34421005/mysql-date-range-pull-using-python-typeerrorunhashable-type-bytearray
# Establish a MySQL connection
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from mysql.connector import MySQLConnection, Error
    _l_(616885)

except ImportError:
    pass
try:
    from python_mysql_dbconfig import read_db_config
    _l_(616887)

except ImportError:
    pass
db_config = _c_(616889, _n_(616888, "read_db_config", lambda: read_db_config))
_l_(616890)
conn = _c_(616893, _n_(616891, "MySQLConnection", lambda: MySQLConnection), **_n_(616892, "db_config", lambda: db_config))
_l_(616894)
cursor = _c_(616897, _a_(616896, _n_(616895, "conn", lambda: conn), "cursor"), raw=True)
_l_(616898)
try:
    import xlsxwriter
    _l_(616900)

except ImportError:
    pass
try:
    from xlsxwriter.workbook import Workbook
    _l_(616902)

except ImportError:
    pass
try:
    import os
    _l_(616904)

except ImportError:
    pass
try:
    import subprocess
    _l_(616906)

except ImportError:
    pass
try:
    import glob
    _l_(616908)

except ImportError:
    pass
try:
    import datetime
    _l_(616910)

except ImportError:
    pass
try:
    from datetime import datetime
    _l_(616912)

except ImportError:
    pass
try:
    import dateutil.parser
    _l_(616914)

except ImportError:
    pass

#creates the path needed for output files
path = 'C:/Python34/output_files/'
_l_(616915)

#creates the workbook
output_filename = _c_(616917, _n_(616916, "input", lambda: input), 'output filename:')
_l_(616918)
workbook = _c_(616923, _a_(616920, _n_(616919, "xlsxwriter", lambda: xlsxwriter), "Workbook"), _n_(616921, "path", lambda: path) + _n_(616922, "output_filename", lambda: output_filename) + '.xlsx')
_l_(616924)
worksheet = _c_(616927, _a_(616926, _n_(616925, "workbook", lambda: workbook), "add_worksheet"))
_l_(616928)

#formatting definitions
bold    = _c_(616931, _a_(616930, _n_(616929, "workbook", lambda: workbook), "add_format"), {'bold': True})
_l_(616932)
date_format = _c_(616935, _a_(616934, _n_(616933, "workbook", lambda: workbook), "add_format"), {'num_format': 'yyyy-mm-dd hh:mm:ss'})
_l_(616936)
timeShape =  '%Y-%m-%d %H:%M:%S'
_l_(616937)

#actual query


query = (
    "SELECT sent_time, delivered_time, OBJ, id1_active, id2_active, id3_active, id1_inactive, id2_inactive, id3_inactive, location_active, location_inactive FROM table1 "
    "WHERE sent_time BETWEEN %s AND %s"
)
_l_(616938)
userIn = _c_(616943, _a_(616940, _a_(616939, dateutil, "parser"), "parse"), _c_(616942, _n_(616941, "input", lambda: input), 'start date:'))
_l_(616944)
userEnd = _c_(616949, _a_(616946, _a_(616945, dateutil, "parser"), "parse"), _c_(616948, _n_(616947, "input", lambda: input), 'end date:'))
_l_(616950)


# Execute sql Query
_c_(616956, _a_(616952, _n_(616951, "cursor", lambda: cursor), "execute"), _n_(616953, "query", lambda: query),(_n_(616954, "userIn", lambda: userIn), _n_(616955, "userEnd", lambda: userEnd)))
_l_(616957)
result = _c_(616960, _a_(616959, _n_(616958, "cursor", lambda: cursor), "fetchall"))
_l_(616961)


#sets up the header row
_c_(616965, _a_(616963, _n_(616962, "worksheet", lambda: worksheet), "write"), 'A1','sent_time',_n_(616964, "bold", lambda: bold))
_l_(616966)
_c_(616970, _a_(616968, _n_(616967, "worksheet", lambda: worksheet), "write"), 'B1', 'delivered_time',_n_(616969, "bold", lambda: bold))
_l_(616971)
_c_(616975, _a_(616973, _n_(616972, "worksheet", lambda: worksheet), "write"), 'C1', 'customer_name',_n_(616974, "bold", lambda: bold))
_l_(616976)
_c_(616980, _a_(616978, _n_(616977, "worksheet", lambda: worksheet), "write"), 'D1', 'id1_active',_n_(616979, "bold", lambda: bold))
_l_(616981)
_c_(616985, _a_(616983, _n_(616982, "worksheet", lambda: worksheet), "write"), 'E1', 'id2_active',_n_(616984, "bold", lambda: bold))
_l_(616986)
_c_(616990, _a_(616988, _n_(616987, "worksheet", lambda: worksheet), "write"), 'F1', 'id3_active',_n_(616989, "bold", lambda: bold))
_l_(616991)
_c_(616995, _a_(616993, _n_(616992, "worksheet", lambda: worksheet), "write"), 'G1', 'id1_inactive',_n_(616994, "bold", lambda: bold))
_l_(616996)
_c_(617000, _a_(616998, _n_(616997, "worksheet", lambda: worksheet), "write"), 'H1', 'id2_inactive',_n_(616999, "bold", lambda: bold))
_l_(617001)
_c_(617005, _a_(617003, _n_(617002, "worksheet", lambda: worksheet), "write"), 'I1', 'id3_inactive',_n_(617004, "bold", lambda: bold))
_l_(617006)
_c_(617010, _a_(617008, _n_(617007, "worksheet", lambda: worksheet), "write"), 'J1', 'location_active',_n_(617009, "bold", lambda: bold))
_l_(617011)
_c_(617015, _a_(617013, _n_(617012, "worksheet", lambda: worksheet), "write"), 'K1', 'location_inactive',_n_(617014, "bold", lambda: bold))
_l_(617016)
_c_(617019, _a_(617018, _n_(617017, "worksheet", lambda: worksheet), "autofilter"), 'A1:K1')  #dropdown menu created for filtering
_l_(617020)  #dropdown menu created for filtering


#print into client to see that you have results
_c_(617022, _n_(617021, "print", lambda: print), "     sent_time     ", "        delivered_time     ", "OBJ", "\t   id1_active  ", "   id2_active  ", "    id3_active  ", "\t", " id1_inactive ", " id2_inactive ", "  id3_inactive ", "\tlocation_active", "\tlocation_inactive")
_l_(617023)
for row in _n_(617024, "result", lambda: result):
    _l_(617029)

    _c_(617027, _n_(617025, "print", lambda: print), *_n_(617026, "row", lambda: row), sep='\t')
    _l_(617028)


# Create a For loop to iterate through each row in the XLS file, starting at row 2 to skip the headers
for r, row in _c_(617032, _n_(617030, "enumerate", lambda: enumerate), _n_(617031, "result", lambda: result), start=1):
    _l_(617105)

    for c, col in _c_(617035, _n_(617033, "enumerate", lambda: enumerate), _n_(617034, "row", lambda: row)):
        _l_(617104)

        _c_(617041, _a_(617037, _n_(617036, "worksheet", lambda: worksheet), "write_datetime"), _n_(617038, "r", lambda: r),0,_n_(617039, "row", lambda: row)[0], _n_(617040, "date_format", lambda: date_format))
        _l_(617042)
        _c_(617048, _a_(617044, _n_(617043, "worksheet", lambda: worksheet), "write_datetime"), _n_(617045, "r", lambda: r),1, _n_(617046, "row", lambda: row)[1], _n_(617047, "date_format", lambda: date_format))
        _l_(617049)
        _c_(617054, _a_(617051, _n_(617050, "worksheet", lambda: worksheet), "write"), _n_(617052, "r", lambda: r),2, _n_(617053, "row", lambda: row)[2])
        _l_(617055)
        _c_(617060, _a_(617057, _n_(617056, "worksheet", lambda: worksheet), "write"), _n_(617058, "r", lambda: r),3, _n_(617059, "row", lambda: row)[3])
        _l_(617061)
        _c_(617066, _a_(617063, _n_(617062, "worksheet", lambda: worksheet), "write"), _n_(617064, "r", lambda: r),4, _n_(617065, "row", lambda: row)[4])
        _l_(617067)
        _c_(617072, _a_(617069, _n_(617068, "worksheet", lambda: worksheet), "write"), _n_(617070, "r", lambda: r),5, _n_(617071, "row", lambda: row)[5])
        _l_(617073)
        _c_(617078, _a_(617075, _n_(617074, "worksheet", lambda: worksheet), "write"), _n_(617076, "r", lambda: r),6, _n_(617077, "row", lambda: row)[6])
        _l_(617079)
        _c_(617084, _a_(617081, _n_(617080, "worksheet", lambda: worksheet), "write"), _n_(617082, "r", lambda: r),7, _n_(617083, "row", lambda: row)[7])
        _l_(617085)
        _c_(617090, _a_(617087, _n_(617086, "worksheet", lambda: worksheet), "write"), _n_(617088, "r", lambda: r),8, _n_(617089, "row", lambda: row)[8])
        _l_(617091)
        _c_(617096, _a_(617093, _n_(617092, "worksheet", lambda: worksheet), "write"), _n_(617094, "r", lambda: r),9, _n_(617095, "row", lambda: row)[9])
        _l_(617097)
        _c_(617102, _a_(617099, _n_(617098, "worksheet", lambda: worksheet), "write"), _n_(617100, "r", lambda: r),10, _n_(617101, "row", lambda: row)[10])
        _l_(617103)




#close out everything and save
_c_(617108, _a_(617107, _n_(617106, "cursor", lambda: cursor), "close"))
_l_(617109)
_c_(617112, _a_(617111, _n_(617110, "workbook", lambda: workbook), "close"))
_l_(617113)
_c_(617116, _a_(617115, _n_(617114, "conn", lambda: conn), "close"))
_l_(617117)

#print number of rows and bye-bye message
_c_(617119, _n_(617118, "print", lambda: print), "- - - - - - - - - - - - -")
_l_(617120)
rows = _c_(617123, _n_(617121, "len", lambda: len), _n_(617122, "result", lambda: result))
_l_(617124)
_c_(617129, _n_(617125, "print", lambda: print), "I just imported "+ _c_(617128, _n_(617126, "str", lambda: str), _n_(617127, "rows", lambda: rows)) + " rows from MySQL!")
_l_(617130)
_c_(617132, _n_(617131, "print", lambda: print), "")
_l_(617133)
_c_(617135, _n_(617134, "print", lambda: print), "Good to Go!!!")
_l_(617136)
_c_(617138, _n_(617137, "print", lambda: print), "")
_l_(617139)


#CONVERTS JUST CREATED FILE TO CSV

# set path to folder containing xlsx files

out_path ='C:/Python34/csv_files'
_l_(617140)
_c_(617144, _a_(617142, _n_(617141, "os", lambda: os), "chdir"), _n_(617143, "path", lambda: path))
_l_(617145)


# find the file with extension .xlsx
xlsx = _c_(617149, _a_(617147, _n_(617146, "glob", lambda: glob), "glob"), _n_(617148, "output_filename", lambda: output_filename) + '.xlsx')
_l_(617150)

# create output filenames with extension .csv
csvs = [_c_(617153, _a_(617152, _n_(617151, "x", lambda: x), "replace"), '.xlsx','.csv') for x in _n_(617154, "xlsx", lambda: xlsx)]
_l_(617155)

# zip into a list of tuples
in_out = _c_(617159, _n_(617156, "zip", lambda: zip), _n_(617157, "xlsx", lambda: xlsx),_n_(617158, "csvs", lambda: csvs))
_l_(617160)

# loop through each file, calling the in2csv utility from subprocess
for xl,csv in _n_(617161, "in_out", lambda: in_out):
    _l_(617183)

    out = _c_(617164, _n_(617162, "open", lambda: open), _n_(617163, "csv", lambda: csv),'w')
    _l_(617165)
    command = 'c:/python34/scripts/in2csv %s\\%s' % (_n_(617166, "path", lambda: path),_n_(617167, "xl", lambda: xl))
    _l_(617168)
    proc = _c_(617173, _a_(617170, _n_(617169, "subprocess", lambda: subprocess), "Popen"), _n_(617171, "command", lambda: command),stdout=_n_(617172, "out", lambda: out))
    _l_(617174)
    _c_(617177, _a_(617176, _n_(617175, "proc", lambda: proc), "wait"))
    _l_(617178)
    _c_(617181, _a_(617180, _n_(617179, "out", lambda: out), "close"))
    _l_(617182)

_c_(617186, _n_(617184, "print", lambda: print), 'XLSX and CSV files named ' + _n_(617185, "output_filename", lambda: output_filename) + ' were created')
_l_(617187)