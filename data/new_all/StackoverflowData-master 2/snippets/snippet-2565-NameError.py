#Source: https://stackoverflow.com/questions/71414030/typeerror-int-object-is-not-subscriptable-on-identical-code
def databaseMR10():
    dbMR10 = ('path/to/database')
    return(dbMR10)
#only one file by name

database10 = glob.glob('path/to/database')
db10 = max(database10, key = os.path.getctime)
#multiple files only take latest

def getData():
    conn = sqlite3.connect(db10)
    cur = conn.cursor()
    cur.execute('''SELECT Itn, Delay, Code, Temp, Humi, Time, Date FROM READING''')
    data = cur.fetchall()
    for row in data:
        Itn = str(row[0])
        Delay = str(row[1])
        Code = str(row[2])
        Temp = str(row[3])
        Humi = str(row[4])
        Time = str(row[5])
        Date = str(row[6])
    conn.close()
    return(Itn, Delay, Code, Temp, Humi, Time, Date)
    #no issues returns data
    
def getMRData():
    dbMR10 = databaseMR10()
    conn = sqlite3.connect(dbMR10)
    cur = conn.cursor()
    cur.execute('''SELECT Itn, Delay, Code, Temp, Humi, Time, Date FROM MR_READING''')
    data = cur.fetchone()
    for row in data:
        ItnMR = str(row[0]) #problem line 
        DelayMR = str(row[1])
        CodeMR = str(row[2])
        TempMR = str(row[3])
        HumiMR = str(row[4])
        TimeMR = str(row[5])
        DateMR = str(row[6])
    conn.close()
    return(ItnMR, DelayMR, CodeMR, TempMR, HumiMR, TimeMR, DateMR)
    #ItnMR = str(row[0])    TypeError: 'int' object is not subscriptable