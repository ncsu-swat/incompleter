# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75353814/python-google-or-tools-surgical-booking-attributeerror-dataframe
from __future__ import print_function
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_l_(438947)
try:
    from ortools.sat.python import cp_model
    _l_(438949)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(438951)

except ImportError:
    pass
try:
    import sys
    _l_(438953)

except ImportError:
    pass
try:
    import math
    _l_(438955)

except ImportError:
    pass



#

# Parameters
targetOvertimeFrequency = 0.2
_l_(438956)
targetUndertimeFrequency = 0
_l_(438957)
undertimeCostWeight = 1
_l_(438958)
overtimeCostWeight = 1
_l_(438959)

arguments = _a_(438961, _n_(438960, "sys", lambda: sys), "argv")
_l_(438962)
excelInputFile = 'input.xlsx'
_l_(438963)
excelOutputFile = 'output.xlsx'
_l_(438964)

overtimeBlockLength = 15 # length of overtime blocks in minutes
_l_(438965) # length of overtime blocks in minutes
noOfNursesPerBlock = 2.5 # number of nurses per overtime block
_l_(438966) # number of nurses per overtime block
overtimeSalary = 75 # pay by block for overtime nurses
_l_(438967) # pay by block for overtime nurses

# Optional: get excel filenames from command line argument
if (_c_(438970, _n_(438968, "len", lambda: len), _n_(438969, "arguments", lambda: arguments)) > 1):
    _l_(438979)

    excelInputFile = _c_(438973, _n_(438971, "str", lambda: str), _n_(438972, "arguments", lambda: arguments)[1])
    _l_(438974)
    excelOutputFile = _c_(438977, _n_(438975, "str", lambda: str), _n_(438976, "arguments", lambda: arguments)[2])
    _l_(438978)


# Read data from an excel file
data = _c_(438983, _a_(438981, _n_(438980, "pd", lambda: pd), "read_excel"), r'' + _n_(438982, "excelInputFile", lambda: excelInputFile), header=4)
_l_(438984)
#
# Input data from excel sheet columns

dfP = _c_(438988, _a_(438986, _n_(438985, "pd", lambda: pd), "DataFrame"), _n_(438987, "data", lambda: data), columns=["Procedure"])
_l_(438989)
dfP = _c_(438994, _a_(438993, _a_(438992, _a_(438991, _n_(438990, "dfP", lambda: dfP), "iloc")[:, :], "values"), "tolist"))
_l_(438995)
dfP = [_n_(438996, "x", lambda: x) for y in _n_(438997, "dfP", lambda: dfP) for x in _n_(438998, "y", lambda: y)]
_l_(438999)

dfD = _c_(439003, _a_(439001, _n_(439000, "pd", lambda: pd), "DataFrame"), _n_(439002, "data", lambda: data), columns=["Date"])
_l_(439004)
dfD = _c_(439007, _a_(439006, _n_(439005, "dfD", lambda: dfD), "get_values"))
_l_(439008)
dfD = [_n_(439009, "x", lambda: x) for y in _n_(439010, "dfD", lambda: dfD) for x in _n_(439011, "y", lambda: y)]
_l_(439012)

dfE = _c_(439016, _a_(439014, _n_(439013, "pd", lambda: pd), "DataFrame"), _n_(439015, "data", lambda: data), columns=["Book Dur"])
_l_(439017)
dfE = _c_(439022, _a_(439021, _a_(439020, _a_(439019, _n_(439018, "dfE", lambda: dfE), "iloc")[:, :], "values"), "tolist"))
_l_(439023)
dfE = [_n_(439024, "x", lambda: x) for y in _n_(439025, "dfE", lambda: dfE) for x in _n_(439026, "y", lambda: y)]
_l_(439027)

dfA = _c_(439031, _a_(439029, _n_(439028, "pd", lambda: pd), "DataFrame"), _n_(439030, "data", lambda: data), columns=["Actual Dur"])
_l_(439032)
dfA = _c_(439037, _a_(439036, _a_(439035, _a_(439034, _n_(439033, "dfA", lambda: dfA), "iloc")[:, :], "values"), "tolist"))
_l_(439038)
dfA =  [_n_(439039, "x", lambda: x) for y in _n_(439040, "dfA", lambda: dfA) for x in _n_(439041, "y", lambda: y)]
_l_(439042)

rawProcedures = [] # a list of each procedure performed
_l_(439043) # a list of each procedure performed
procedureTypes = [] # a list of all theprocedure codes
_l_(439044) # a list of all theprocedure codes
rawDays = [] # a list of dates for each procedure performed
_l_(439045) # a list of dates for each procedure performed
days = [] # a list of the dates in the data
_l_(439046) # a list of the dates in the data
rawExpectedTimes = [] # a list of scheduled times for each procedure performed
_l_(439047) # a list of scheduled times for each procedure performed
rawActualTimes = [] # a list of actual times for each procedure performed
_l_(439048) # a list of actual times for each procedure performed

# Input data into arrays
for i in _c_(439053, _n_(439049, "range", lambda: range), _c_(439052, _n_(439050, "len", lambda: len), _n_(439051, "dfE", lambda: dfE))):
    _l_(439103)

    if _c_(439057, _n_(439054, "str", lambda: str), _n_(439055, "dfE", lambda: dfE)[_n_(439056, "i", lambda: i)]) != 'nan':
        _l_(439102)

        if _n_(439058, "dfD", lambda: dfD)[_n_(439059, "i", lambda: i)] not in _n_(439060, "days", lambda: days):
            _l_(439067)

            _c_(439065, _a_(439062, _n_(439061, "days", lambda: days), "append"), _n_(439063, "dfD", lambda: dfD)[_n_(439064, "i", lambda: i)])
            _l_(439066)
        _c_(439072, _a_(439069, _n_(439068, "rawExpectedTimes", lambda: rawExpectedTimes), "append"), _n_(439070, "dfE", lambda: dfE)[_n_(439071, "i", lambda: i)])
        _l_(439073)
        _c_(439078, _a_(439075, _n_(439074, "rawDays", lambda: rawDays), "append"), _n_(439076, "dfD", lambda: dfD)[_n_(439077, "i", lambda: i)])
        _l_(439079)
        _c_(439084, _a_(439081, _n_(439080, "rawActualTimes", lambda: rawActualTimes), "append"), _n_(439082, "dfA", lambda: dfA)[_n_(439083, "i", lambda: i)])
        _l_(439085)
        _c_(439090, _a_(439087, _n_(439086, "rawProcedures", lambda: rawProcedures), "append"), _n_(439088, "dfP", lambda: dfP)[_n_(439089, "i", lambda: i)])
        _l_(439091)
        if _n_(439092, "dfP", lambda: dfP)[_n_(439093, "i", lambda: i)] not in _n_(439094, "procedureTypes", lambda: procedureTypes):
            _l_(439101)

            _c_(439099, _a_(439096, _n_(439095, "procedureTypes", lambda: procedureTypes), "append"), _n_(439097, "dfP", lambda: dfP)[_n_(439098, "i", lambda: i)])
            _l_(439100)

_c_(439106, _a_(439105, _n_(439104, "procedureTypes", lambda: procedureTypes), "sort")) # sort procedure types alphabetically
_l_(439107) # sort procedure types alphabetically

proceduresPerDay = {_n_(439108, "w", lambda: w): [] for w in _n_(439109, "days", lambda: days)} # a map from a day to a list of procedures performed on that day
_l_(439110) # a map from a day to a list of procedures performed on that day
for i in _c_(439115, _n_(439111, "range", lambda: range), _c_(439114, _n_(439112, "len", lambda: len), _n_(439113, "rawDays", lambda: rawDays))):
    _l_(439124)

    _c_(439122, _a_(439119, _n_(439116, "proceduresPerDay", lambda: proceduresPerDay)[_n_(439117, "rawDays", lambda: rawDays)[_n_(439118, "i", lambda: i)]], "append"), _n_(439120, "rawProcedures", lambda: rawProcedures)[_n_(439121, "i", lambda: i)])
    _l_(439123)


expectedTimes = {_n_(439125, "w", lambda: w): [] for w in _n_(439126, "days", lambda: days)} # a map from a day to a list of booking times for that day
_l_(439127) # a map from a day to a list of booking times for that day
for i in _c_(439132, _n_(439128, "range", lambda: range), _c_(439131, _n_(439129, "len", lambda: len), _n_(439130, "rawDays", lambda: rawDays))):
    _l_(439141)

    _c_(439139, _a_(439136, _n_(439133, "expectedTimes", lambda: expectedTimes)[_n_(439134, "rawDays", lambda: rawDays)[_n_(439135, "i", lambda: i)]], "append"), _n_(439137, "rawExpectedTimes", lambda: rawExpectedTimes)[_n_(439138, "i", lambda: i)])
    _l_(439140)

actualTimes = {_n_(439142, "w", lambda: w): [] for w in _n_(439143, "days", lambda: days)} # a map from a day to a list of actual procedure times for that day
_l_(439144) # a map from a day to a list of actual procedure times for that day
for i in _c_(439149, _n_(439145, "range", lambda: range), _c_(439148, _n_(439146, "len", lambda: len), _n_(439147, "rawDays", lambda: rawDays))):
    _l_(439158)

    _c_(439156, _a_(439153, _n_(439150, "actualTimes", lambda: actualTimes)[_n_(439151, "rawDays", lambda: rawDays)[_n_(439152, "i", lambda: i)]], "append"), _n_(439154, "rawActualTimes", lambda: rawActualTimes)[_n_(439155, "i", lambda: i)])
    _l_(439157)

#    ­
# Pre-processing

originalBookTimes = {_n_(439159, "p", lambda: p): 0 for p in _n_(439160, "procedureTypes", lambda: procedureTypes)} # a map with average booking times for each procedue
_l_(439161) # a map with average booking times for each procedue
for p in _n_(439162, "procedureTypes", lambda: procedureTypes):
    _l_(439188)

    counter = 0
    _l_(439163)
    for i in _c_(439168, _n_(439164, "range", lambda: range), _c_(439167, _n_(439165, "len", lambda: len), _n_(439166, "rawDays", lambda: rawDays))):
        _l_(439179)

        if _n_(439169, "p", lambda: p) == _n_(439170, "rawProcedures", lambda: rawProcedures)[_n_(439171, "i", lambda: i)]:
            _l_(439178)

            counter +=  1
            _l_(439172)
            _n_(439173, "originalBookTimes", lambda: originalBookTimes)[_n_(439174, "p", lambda: p)] += _n_(439175, "rawExpectedTimes", lambda: rawExpectedTimes)[_n_(439176, "i", lambda: i)]
            _l_(439177)
    _n_(439180, "originalBookTimes", lambda: originalBookTimes)[_n_(439181, "p", lambda: p)] = _c_(439186, _n_(439182, "int", lambda: int), _n_(439183, "originalBookTimes", lambda: originalBookTimes)[_n_(439184, "p", lambda: p)]/_n_(439185, "counter", lambda: counter))
    _l_(439187)

expectedTotalTime = {} # a map from a day to the sum of booking times for that day
_l_(439189) # a map from a day to the sum of booking times for that day
for day in _n_(439190, "days", lambda: days):
    _l_(439201)

    _n_(439191, "expectedTotalTime", lambda: expectedTotalTime)[_n_(439192, "day", lambda: day)] = 0
    _l_(439193)
    for time in _n_(439194, "expectedTimes", lambda: expectedTimes)[_n_(439195, "day", lambda: day)]:
        _l_(439200)

        _n_(439196, "expectedTotalTime", lambda: expectedTotalTime)[_n_(439197, "day", lambda: day)] += _n_(439198, "time", lambda: time)
        _l_(439199)

actualTotalTime = {} # a map from a day to the sum of actual procedure times for that day
_l_(439202) # a map from a day to the sum of actual procedure times for that day
for day in _n_(439203, "days", lambda: days):
    _l_(439214)

    _n_(439204, "actualTotalTime", lambda: actualTotalTime)[_n_(439205, "day", lambda: day)] = 0
    _l_(439206)
    for time in _n_(439207, "actualTimes", lambda: actualTimes)[_n_(439208, "day", lambda: day)]:
        _l_(439213)

        _n_(439209, "actualTotalTime", lambda: actualTotalTime)[_n_(439210, "day", lambda: day)] += _n_(439211, "time", lambda: time)
        _l_(439212)

currentOvertimeCount = 0 # counts how many days the room went overtime
_l_(439215) # counts how many days the room went overtime
currentUndertimeCount = 0 # counts how many days the room went undertime
_l_(439216) # counts how many days the room went undertime
for day in _n_(439217, "days", lambda: days):
    _l_(439228)

    if _n_(439218, "expectedTotalTime", lambda: expectedTotalTime)[_n_(439219, "day", lambda: day)] + 0 < _n_(439220, "actualTotalTime", lambda: actualTotalTime)[_n_(439221, "day", lambda: day)]:
        _l_(439227)

currentOvertimeCount += 1    elif _n_(439222, "actualTotalTime", lambda: actualTotalTime)[_n_(439223, "day", lambda: day)] + 15 < _n_(439224, "expectedTotalTime", lambda: expectedTotalTime)[_n_(439225, "day", lambda: day)]:
        _l_(439226)

currentUndertimeCount +=  1
minProcedureTime = {_n_(439229, "p", lambda: p): 1440 for p in _n_(439230, "procedureTypes", lambda: procedureTypes)} # a map from a procedure to its minimum case time
_l_(439231) # a map from a procedure to its minimum case time
maxProcedureTime = {_n_(439232, "p", lambda: p): 0 for p in _n_(439233, "procedureTypes", lambda: procedureTypes)} # a map from a procedure to its maximum case time
_l_(439234) # a map from a procedure to its maximum case time

for i in _c_(439239, _n_(439235, "range", lambda: range), _c_(439238, _n_(439236, "len", lambda: len), _n_(439237, "rawDays", lambda: rawDays))):
    _l_(439263)

    if _n_(439240, "rawActualTimes", lambda: rawActualTimes)[_n_(439241, "i", lambda: i)] < _n_(439242, "minProcedureTime", lambda: minProcedureTime)[_n_(439243, "rawProcedures", lambda: rawProcedures)[_n_(439244, "i", lambda: i)]]:
        _l_(439250)

_n_(439245, "minProcedureTime", lambda: minProcedureTime)[_n_(439246, "rawProcedures", lambda: rawProcedures)[_n_(439247, "i", lambda: i)]] = _n_(439248, "rawActualTimes", lambda: rawActualTimes)[_n_(439249, "i", lambda: i)]    if _n_(439251, "rawActualTimes", lambda: rawActualTimes)[_n_(439252, "i", lambda: i)] > _n_(439253, "maxProcedureTime", lambda: maxProcedureTime)[_n_(439254, "rawProcedures", lambda: rawProcedures)[_n_(439255, "i", lambda: i)]]:
        _l_(439262)

        _n_(439256, "maxProcedureTime", lambda: maxProcedureTime)[_n_(439257, "rawProcedures", lambda: rawProcedures)[_n_(439258, "i", lambda: i)]] = _n_(439259, "rawActualTimes", lambda: rawActualTimes)[_n_(439260, "i", lambda: i)]
        _l_(439261)
count = _c_(439266, _n_(439264, "len", lambda: len), _n_(439265, "days", lambda: days)) # number of days
_l_(439267) # number of days
 
#

# Model
_c_(439271, _n_(439268, "print", lambda: print), "Starting model optimisation", file=_a_(439270, _n_(439269, "sys", lambda: sys), "stderr"))
_l_(439272)

# Decision variables
model = _c_(439275, _a_(439274, _n_(439273, "cp_model", lambda: cp_model), "CpModel")) # Create the model
_l_(439276) # Create the model

procedureSchedulingTimes = {} # Create a decision variable for the scheduling time of each procedure type
_l_(439277) # Create a decision variable for the scheduling time of each procedure type
for p in _n_(439278, "procedureTypes", lambda: procedureTypes):
    _l_(439296)

    _n_(439279, "procedureSchedulingTimes", lambda: procedureSchedulingTimes)[_n_(439280, "p", lambda: p)] = _c_(439294, _a_(439282, _n_(439281, "model", lambda: model), "NewIntVar"), _c_(439286, _n_(439283, "int", lambda: int), _n_(439284, "minProcedureTime", lambda: minProcedureTime)[_n_(439285, "p", lambda: p)]),
     _c_(439290, _n_(439287, "int", lambda: int), _n_(439288, "maxProcedureTime", lambda: maxProcedureTime)[_n_(439289, "p", lambda: p)]),
                                "procedureSchedulingTime" + _c_(439293, _n_(439291, "str", lambda: str), _n_(439292, "p", lambda: p)))
    _l_(439295)

totalScheduledTime = {} # The total time scheduled for each day
_l_(439297) # The total time scheduled for each day
overtimeTriggers={} # Set to 1 if overtime for each day
_l_(439298) # Set to 1 if overtime for each day
undertimeTriggers = {} # Set to 1 if undertime for each day
_l_(439299) # Set to 1 if undertime for each day
for day in _n_(439300, "days", lambda: days):
    _l_(439328)

    _n_(439301, "totalScheduledTime", lambda: totalScheduledTime)[_n_(439302, "day", lambda: day)] = _c_(439308, _a_(439304, _n_(439303, "model", lambda: model), "NewIntVar"), 0, 1000, "day"+ _c_(439307, _n_(439305, "str", lambda: str), _n_(439306, "day", lambda: day)))
    _l_(439309)
    _n_(439310, "overtimeTriggers", lambda: overtimeTriggers)[_n_(439311, "day", lambda: day)] = _c_(439317, _a_(439313, _n_(439312, "model", lambda: model), "NewIntVar"), 0, 1, "overtimeTrigger" + _c_(439316, _n_(439314, "str", lambda: str), _n_(439315, "day", lambda: day)))
    _l_(439318)
    _n_(439319, "undertimeTriggers", lambda: undertimeTriggers)[_n_(439320, "day", lambda: day)] = _c_(439326, _a_(439322, _n_(439321, "model", lambda: model), "NewIntVar"), 0, 1, "undertimeTrigger" + _c_(439325, _n_(439323, "str", lambda: str), _n_(439324, "day", lambda: day)))
    _l_(439327)

overtimeCount = _c_(439331, _a_(439330, _n_(439329, "model", lambda: model), "NewIntVar"), 0, 1000, "overtimeCount") # Number of days that went overtime
_l_(439332) # Number of days that went overtime
undertimeCount = _c_(439335, _a_(439334, _n_(439333, "model", lambda: model), "NewIntVar"), 0, 1000, "undertimeCount") # Number of days that went undertime
_l_(439336) # Number of days that went undertime
overtimeCost = _c_(439339, _a_(439338, _n_(439337, "model", lambda: model), "NewIntVar"), -1000, 1000, "overtimeCost") # Overtime cost
_l_(439340) # Overtime cost
undertimeCost = _c_(439343, _a_(439342, _n_(439341, "model", lambda: model), "NewIntVar"), -1000, 1000, "undertimeCost") # Undertime cost
_l_(439344) # Undertime cost
absOvertimeCost = _c_(439347, _a_(439346, _n_(439345, "model", lambda: model), "NewIntVar"), 0, 100, "absOvertimeCost") # !overtime costl
_l_(439348) # !overtime costl
absUndertimeCost = _c_(439351, _a_(439350, _n_(439349, "model", lambda: model), "NewIntVar"), 0, 100, "absUndertimeCost") # lundertime costl
_l_(439352) # lundertime costl
finalCost = _c_(439355, _a_(439354, _n_(439353, "model", lambda: model), "NewIntVar"), 0, 100, "finalCost") # final cost is sum of overtime and undertime costs
_l_(439356) # final cost is sum of overtime and undertime costs

#-------------------
# Constraints
for day in _n_(439357, "days", lambda: days):
    _l_(439418)

    # set totalScheduledTime to the sum of scheduled time in a day
    _c_(439368, _a_(439359, _n_(439358, "model", lambda: model), "Add"), _n_(439360, "totalScheduledTime", lambda: totalScheduledTime)[_n_(439361, "day", lambda: day)] == _c_(439367, _n_(439362, "sum", lambda: sum), (_n_(439363, "procedureSchedulingTimes", lambda: procedureSchedulingTimes)[_n_(439364, "i", lambda: i)] for i in _n_(439365, "proceduresPerDay", lambda: proceduresPerDay)[_n_(439366, "day", lambda: day)])))
    _l_(439369)

    # set overtime trigger to 1 if overtime
    _c_(439380, _a_(439371, _n_(439370, "model", lambda: model), "Add"), 1000 * _n_(439372, "overtimeTriggers", lambda: overtimeTriggers)[_n_(439373, "day", lambda: day)] >= _c_(439377, _n_(439374, "int", lambda: int), _n_(439375, "actualTotalTime", lambda: actualTotalTime)[_n_(439376, "day", lambda: day)]) - _n_(439378, "totalScheduledTime", lambda: totalScheduledTime)[_n_(439379, "day", lambda: day)] - 0 - 1)
    _l_(439381)
 
    # set overime trigger to O if not overtime
    _c_(439392, _a_(439383, _n_(439382, "model", lambda: model), "Add"), 1500 * (1 - _n_(439384, "overtimeTriggers", lambda: overtimeTriggers)[_n_(439385, "day", lambda: day)]) >= _n_(439386, "totalScheduledTime", lambda: totalScheduledTime)[_n_(439387, "day", lambda: day)] - _c_(439391, _n_(439388, "int", lambda: int), _n_(439389, "actualTotalTime", lambda: actualTotalTime)[_n_(439390, "day", lambda: day)]) + 0)
    _l_(439393)

    # set undertime trigger to 1 if undertime
    _c_(439404, _a_(439395, _n_(439394, "model", lambda: model), "Add"), 1000 * _n_(439396, "undertimeTriggers", lambda: undertimeTriggers)[_n_(439397, "day", lambda: day)] >= _n_(439398, "totalScheduledTime", lambda: totalScheduledTime)[_n_(439399, "day", lambda: day)] - 15 - _c_(439403, _n_(439400, "int", lambda: int), _n_(439401, "actualTotalTime", lambda: actualTotalTime)[_n_(439402, "day", lambda: day)]) - 1)
    _l_(439405)
    # set undertime trigger to O if not undertime
    _c_(439416, _a_(439407, _n_(439406, "model", lambda: model), "Add"), 1000 * (1 - _n_(439408, "undertimeTriggers", lambda: undertimeTriggers)[_n_(439409, "day", lambda: day)]) >= _c_(439413, _n_(439410, "int", lambda: int), _n_(439411, "actualTotalTime", lambda: actualTotalTime)[_n_(439412, "day", lambda: day)]) - _n_(439414, "totalScheduledTime", lambda: totalScheduledTime)[_n_(439415, "day", lambda: day)] + 15)
    _l_(439417)

_c_(439427, _a_(439420, _n_(439419, "model", lambda: model), "Add"), _n_(439421, "overtimeCount", lambda: overtimeCount) == _c_(439426, _n_(439422, "sum", lambda: sum), (_n_(439423, "overtimeTriggers", lambda: overtimeTriggers)[_n_(439424, "day", lambda: day)] for day in _n_(439425, "days", lambda: days)))) # count how many days went overtime
_l_(439428) # count how many days went overtime
_c_(439437, _a_(439430, _n_(439429, "model", lambda: model), "Add"), _n_(439431, "undertimeCount", lambda: undertimeCount) == _c_(439436, _n_(439432, "sum", lambda: sum), (_n_(439433, "undertimeTriggers", lambda: undertimeTriggers)[_n_(439434, "day", lambda: day)] for day in _n_(439435, "days", lambda: days)))) # count how many days went undertime
_l_(439438) # count how many days went undertime

_c_(439447, _a_(439440, _n_(439439, "model", lambda: model), "Add"), (_n_(439441, "overtimeCost", lambda: overtimeCost) == _n_(439442, "overtimeCount", lambda: overtimeCount) - _c_(439446, _n_(439443, "int", lambda: int), _n_(439444, "count", lambda: count) * _n_(439445, "targetOvertimeFrequency", lambda: targetOvertimeFrequency)))) #calculate overtime cost
_l_(439448) #calculate overtime cost
_c_(439457, _a_(439450, _n_(439449, "model", lambda: model), "Add"), (_n_(439451, "undertimeCost", lambda: undertimeCost) == _n_(439452, "undertimeCount", lambda: undertimeCount) - _c_(439456, _n_(439453, "int", lambda: int), _n_(439454, "count", lambda: count) * _n_(439455, "targetUndertimeFrequency", lambda: targetUndertimeFrequency)))) #calculate undertime cost
_l_(439458) #calculate undertime cost

# calculate absolute value of overtime cost
_c_(439466, _a_(439460, _n_(439459, "model", lambda: model), "AddAbsEquality"), _n_(439461, "absOvertimeCost", lambda: absOvertimeCost), _c_(439464, _n_(439462, "int", lambda: int), _n_(439463, "overtimeCostWeight", lambda: overtimeCostWeight)) * _n_(439465, "overtimeCost", lambda: overtimeCost))
_l_(439467)
# calculate absolute value of undertime cost
_c_(439475, _a_(439469, _n_(439468, "model", lambda: model), "AddAbsEquality"), _n_(439470, "absUndertimeCost", lambda: absUndertimeCost), _c_(439473, _n_(439471, "int", lambda: int), _n_(439472, "undertimeCostWeight", lambda: undertimeCostWeight)) * _n_(439474, "undertimeCost", lambda: undertimeCost))
_l_(439476)
_c_(439482, _a_(439478, _n_(439477, "model", lambda: model), "Add"), (_n_(439479, "finalCost", lambda: finalCost) == _n_(439480, "overtimeCost", lambda: overtimeCost) + _n_(439481, "undertimeCost", lambda: undertimeCost))) # calculate final cost
_l_(439483) # calculate final cost

_c_(439487, _a_(439485, _n_(439484, "model", lambda: model), "Minimize"), _n_(439486, "finalCost", lambda: finalCost)) # Objective is to minimize final cost
_l_(439488) # Objective is to minimize final cost

solver= _c_(439491, _a_(439490, _n_(439489, "cp_model", lambda: cp_model), "CpSolver"))
_l_(439492)
_c_(439496, _n_(439493, "print", lambda: print), "Starting to solve", file=_a_(439495, _n_(439494, "sys", lambda: sys), "stderr"))
_l_(439497)
status = _c_(439501, _a_(439499, _n_(439498, "solver", lambda: solver), "Solve"), _n_(439500, "model", lambda: model))
_l_(439502)

#

# Print output to console and excel sheet
if _n_(439503, "status", lambda: status) == _a_(439505, _n_(439504, "cp_model", lambda: cp_model), "OPTIMAL") or _n_(439506, "status", lambda: status) == _a_(439508, _n_(439507, "cp_model", lambda: cp_model), "FEASIBLE"):
    _l_(439519)

    _c_(439510, _n_(439509, "print", lambda: print), "Success!")
    _l_(439511)
    rows= ["Number of days","Number of cases","Original overtime frequency","Original undertime frequency","Model overtime frequency",
            "Model undertime frequency","Model cases achieved", "Original Overtime Minutes Used","Model Overtime Minutes Used",
            "Original Overtime Cost","Model Overtime Cost", "Original OR minutes used", "Model OR minutes used", "","Procedure Type"] + _n_(439512, "procedureTypes", lambda: procedureTypes)
    _l_(439513)

    dashboard= _c_(439517, _a_(439515, _n_(439514, "pd", lambda: pd), "DataFrame"), index=_n_(439516, "rows", lambda: rows),columns=["A", "B", "C",])
    _l_(439518)

for r in _n_(439520, "rows", lambda: rows):
    _l_(439526)

    _a_(439522, _n_(439521, "dashboard", lambda: dashboard), "at")[_n_(439523, "r", lambda: r),"A"]= _n_(439524, "r", lambda: r)
    _l_(439525)

#-------------------
# Output basic stats
_a_(439528, _n_(439527, "dashboard", lambda: dashboard), "at")["", ""] = ""
_l_(439529)
_a_(439531, _n_(439530, "dashboard", lambda: dashboard), "at")["Number of days", "B"] = _n_(439532, "count", lambda: count)
_l_(439533)
_c_(439536, _n_(439534, "print", lambda: print), "number of days: ", _n_(439535, "count", lambda: count))
_l_(439537)
_a_(439539, _n_(439538, "dashboard", lambda: dashboard), "at")["Number of cases", "B"] = _c_(439542, _n_(439540, "len", lambda: len), _n_(439541, "rawExpectedTimes", lambda: rawExpectedTimes))
_l_(439543)

_c_(439548, _n_(439544, "print", lambda: print), "number of cases: ", _c_(439547, _n_(439545, "len", lambda: len), _n_(439546, "rawExpectedTimes", lambda: rawExpectedTimes)))
_l_(439549)
_a_(439551, _n_(439550, "dashboard", lambda: dashboard), "at")["Original overtime frequency", "B"] = _c_(439555, _n_(439552, "round", lambda: round), _n_(439553, "currentOvertimeCount", lambda: currentOvertimeCount) / _n_(439554, "count", lambda: count), 2)
_l_(439556)
_c_(439560, _n_(439557, "print", lambda: print), "current overtime frequency: %.Of%%" % (100 * _n_(439558, "currentOvertimeCount", lambda: currentOvertimeCount) / _n_(439559, "count", lambda: count)))
_l_(439561)
_a_(439563, _n_(439562, "dashboard", lambda: dashboard), "at")["Original undertime frequency", "B"] = _c_(439567, _n_(439564, "round", lambda: round), _n_(439565, "currentUndertimeCount", lambda: currentUndertimeCount) / _n_(439566, "count", lambda: count),2)
_l_(439568)
_c_(439572, _n_(439569, "print", lambda: print), "current undertime frequency: %.Of%%" % (100 * _n_(439570, "currentUndertimeCount", lambda: currentUndertimeCount)/ _n_(439571, "count", lambda: count)))
_l_(439573)
_a_(439575, _n_(439574, "dashboard", lambda: dashboard), "at")["Model overtime frequency", "B"] = _c_(439582, _n_(439576, "round", lambda: round), _c_(439580, _a_(439578, _n_(439577, "solver", lambda: solver), "Value"), _n_(439579, "overtimeCount", lambda: overtimeCount)) /_n_(439581, "count", lambda: count), 2)
_l_(439583)
_c_(439590, _n_(439584, "print", lambda: print), "model overtime frequency: %.Of%%" % (100 * _c_(439588, _a_(439586, _n_(439585, "solver", lambda: solver), "Value"), _n_(439587, "overtimeCount", lambda: overtimeCount)) / _n_(439589, "count", lambda: count)))
_l_(439591)
_a_(439593, _n_(439592, "dashboard", lambda: dashboard), "at")["Model undertime frequency", "B"] = _c_(439600, _n_(439594, "round", lambda: round), _c_(439598, _a_(439596, _n_(439595, "solver", lambda: solver), "Value"), _n_(439597, "undertimeCount", lambda: undertimeCount)) /_n_(439599, "count", lambda: count), 2)
_l_(439601)
_c_(439608, _n_(439602, "print", lambda: print), "model undertime frequency: %.Of%%" % (100 * _c_(439606, _a_(439604, _n_(439603, "solver", lambda: solver), "Value"), _n_(439605, "undertimeCount", lambda: undertimeCount)) / _n_(439607, "count", lambda: count)))
_l_(439609)

#-------------------
# Output overtime minutes and overtime cost
originalOverMinutes = 0
_l_(439610)
modelOverMinutes = 0
_l_(439611)

originalCost = 0
_l_(439612)
modelCost = 0
_l_(439613)

for day in _n_(439614, "days", lambda: days):
    _l_(439666)

    if _c_(439619, _a_(439616, _n_(439615, "solver", lambda: solver), "Value"), _n_(439617, "totalScheduledTime", lambda: totalScheduledTime)[_n_(439618, "day", lambda: day)]) < _n_(439620, "actualTotalTime", lambda: actualTotalTime)[_n_(439621, "day", lambda: day)]:
        _l_(439644)

        modelOverMinutes += _n_(439622, "actualTotalTime", lambda: actualTotalTime)[_n_(439623, "day", lambda: day)] - _c_(439628, _a_(439625, _n_(439624, "solver", lambda: solver), "Value"), _n_(439626, "totalScheduledTime", lambda: totalScheduledTime)[_n_(439627, "day", lambda: day)])
        _l_(439629)
        modelCost += _c_(439640, _a_(439631, _n_(439630, "math", lambda: math), "ceil"), (_n_(439632, "actualTotalTime", lambda: actualTotalTime)[_n_(439633, "day", lambda: day)] - _c_(439638, _a_(439635, _n_(439634, "solver", lambda: solver), "Value"), _n_(439636, "totalScheduledTime", lambda: totalScheduledTime)[_n_(439637, "day", lambda: day)])) / _n_(439639, "overtimeBlocklength", lambda: overtimeBlocklength)) * _n_(439641, "noOfNursesPerBlock", lambda: noOfNursesPerBlock) * _n_(439642, "overtimeSalary", lambda: overtimeSalary)
        _l_(439643)
    if _n_(439645, "expectedTotalTime", lambda: expectedTotalTime)[_n_(439646, "day", lambda: day)] < _n_(439647, "actualTotalTime", lambda: actualTotalTime)[_n_(439648, "day", lambda: day)]:
        _l_(439665)

        originalOverMinutes += _n_(439649, "actualTotalTime", lambda: actualTotalTime)[_n_(439650, "day", lambda: day)] - _n_(439651, "expectedTotalTime", lambda: expectedTotalTime)[_n_(439652, "day", lambda: day)]
        _l_(439653)
        originalCost += _c_(439661, _a_(439655, _n_(439654, "math", lambda: math), "ceil"), (_n_(439656, "actualTotalTime", lambda: actualTotalTime)[_n_(439657, "day", lambda: day)] - _n_(439658, "expectedTotalTime", lambda: expectedTotalTime)[_n_(439659, "day", lambda: day)]) / _n_(439660, "overtimeBlocklength", lambda: overtimeBlocklength)) * _n_(439662, "noOfNursesPerBlock", lambda: noOfNursesPerBlock) * _n_(439663, "overtimeSalary", lambda: overtimeSalary)
        _l_(439664)


_c_(439669, _n_(439667, "print", lambda: print), "Original overtime minutes used: ", _n_(439668, "originalOverMinutes", lambda: originalOverMinutes))
_l_(439670)
_a_(439672, _n_(439671, "dashboard", lambda: dashboard), "at")["Original Overtime Minutes Used", "B"] = _n_(439673, "originalOverMinutes", lambda: originalOverMinutes)
_l_(439674)
_c_(439677, _n_(439675, "print", lambda: print), "Model overtime minutes used: ", _n_(439676, "modelOverMinutes", lambda: modelOverMinutes))
_l_(439678)
_a_(439680, _n_(439679, "dashboard", lambda: dashboard), "at")["Model Overtime Minutes Used", "B"] = _n_(439681, "modelOverMinutes", lambda: modelOverMinutes)
_l_(439682)

_c_(439685, _n_(439683, "print", lambda: print), "Original Overtime cost: ", _n_(439684, "originalCost", lambda: originalCost))
_l_(439686)
_a_(439688, _n_(439687, "dashboard", lambda: dashboard), "at")["Original Overtime Cost", "B"] = _n_(439689, "originalCost", lambda: originalCost)
_l_(439690)
_c_(439693, _n_(439691, "print", lambda: print), "Model overtime cost: ", _n_(439692, "modelCost", lambda: modelCost))
_l_(439694)
_a_(439696, _n_(439695, "dashboard", lambda: dashboard), "at")["Model Overtime Cost", "B"] = _n_(439697, "modelCost", lambda: modelCost)
_l_(439698)

_c_(439700, _n_(439699, "print", lambda: print), "\n")
_l_(439701)

#-------------------
# Output original and machine learning scheduling times for each procedure
_a_(439703, _n_(439702, "dashboard", lambda: dashboard), "at")["Procedure Type", "B"] = "Original Time"
_l_(439704)
_a_(439706, _n_(439705, "dashboard", lambda: dashboard), "at")["Procedure Type", "C"] = "Machine Learning Time"
_l_(439707)
for p in _n_(439708, "procedureTypes", lambda: procedureTypes):
    _l_(439733)

    _c_(439716, _n_(439709, "print", lambda: print), _n_(439710, "p", lambda: p) + ": " + "%/d" % _c_(439715, _a_(439712, _n_(439711, "solver", lambda: solver), "Value"), _n_(439713, "procedureSchedulingTimes", lambda: procedureSchedulingTimes)[_n_(439714, "p", lambda: p)]))
    _l_(439717)
    _a_(439719, _n_(439718, "dashboard", lambda: dashboard), "at")[_n_(439720, "p", lambda: p), "B"] = _n_(439721, "originalBookTimes", lambda: originalBookTimes)[_n_(439722, "p", lambda: p)]
    _l_(439723)
    _a_(439725, _n_(439724, "dashboard", lambda: dashboard), "at")[_n_(439726, "p", lambda: p), "C"] = _c_(439731, _a_(439728, _n_(439727, "solver", lambda: solver), "Value"), _n_(439729, "procedureSchedulingTimes", lambda: procedureSchedulingTimes)[_n_(439730, "p", lambda: p)])
    _l_(439732)

#-------------------
# Output cases completed with model and OR minutes used by original and machine learning methods
totalNoCases = 0
_l_(439734)
originalCases = 0
_l_(439735)
modelCases = 0
_l_(439736)
originalMinutes = 0
_l_(439737)
modelMinutes = 0
_l_(439738)
totalMinutes = 0
_l_(439739)

_c_(439741, _n_(439740, "print", lambda: print), "\n")
_l_(439742)
for day in _n_(439743, "days", lambda: days):
    _l_(439861)

    noOfCases = _c_(439747, _n_(439744, "len", lambda: len), _n_(439745, "actualTimes", lambda: actualTimes)[_n_(439746, "day", lambda: day)])
    _l_(439748)
    totalNoCases += _n_(439749, "noOfCases", lambda: noOfCases)
    _l_(439750)

    originalMinutes += _n_(439751, "actualTotalTime", lambda: actualTotalTime)[_n_(439752, "day", lambda: day)]
    _l_(439753)
    modelMinutes += _c_(439758, _a_(439755, _n_(439754, "solver", lambda: solver), "Value"), _n_(439756, "totalScheduledTime", lambda: totalScheduledTime)[_n_(439757, "day", lambda: day)])
    _l_(439759)

    ORTime = 450 - (_n_(439760, "noOfCases", lambda: noOfCases) - 1) * 15
    _l_(439761)
    totalMinutes += _n_(439762, "ORTime", lambda: ORTime)
    _l_(439763)

    originalTime = (_n_(439764, "ORTime", lambda: ORTime) - _n_(439765, "actualTotalTime", lambda: actualTotalTime)[_n_(439766, "day", lambda: day)])
    _l_(439767)
    modelTime = (_n_(439768, "ORTime", lambda: ORTime) - _c_(439773, _a_(439770, _n_(439769, "solver", lambda: solver), "Value"), _n_(439771, "totalScheduledTime", lambda: totalScheduledTime)[_n_(439772, "day", lambda: day)]))
    _l_(439774)
    originalCases += _n_(439775, "noOfCases", lambda: noOfCases)
    _l_(439776)
    if _n_(439777, "originalTime", lambda: originalTime) < 0:
        _l_(439816)

        for i in _c_(439785, _n_(439778, "reversed", lambda: reversed), _c_(439784, _n_(439779, "range", lambda: range), _c_(439783, _n_(439780, "len", lambda: len), _n_(439781, "actualTimes", lambda: actualTimes)[_n_(439782, "day", lambda: day)]))):
            _l_(439794)

            originalTime += _n_(439786, "actualTimes", lambda: actualTimes)[_n_(439787, "day", lambda: day)][_n_(439788, "i", lambda: i)]
            _l_(439789)
            originalCases -= 1
            _l_(439790)
            if _n_(439791, "originalTime", lambda: originalTime) > 0:
                _l_(439793)

                break
                _l_(439792)
        modelCases += _n_(439795, "noOfCases", lambda: noOfCases)
        _l_(439796)
        if _n_(439797, "modelTime", lambda: modelTime) < 0:
            _l_(439815)

            for i in _c_(439805, _n_(439798, "reversed", lambda: reversed), _c_(439804, _n_(439799, "range", lambda: range), _c_(439803, _n_(439800, "len", lambda: len), _n_(439801, "actualTimes", lambda: actualTimes)[_n_(439802, "day", lambda: day)]))):
                _l_(439814)

                modelTime += _n_(439806, "actualTimes", lambda: actualTimes)[_n_(439807, "day", lambda: day)][_n_(439808, "i", lambda: i)]
                _l_(439809)
                modelCases -= 1
                _l_(439810)
                if _n_(439811, "modelTime", lambda: modelTime) > 0:
                    _l_(439813)

                    break
                    _l_(439812)

    _c_(439820, _n_(439817, "print", lambda: print), "Cases achieved with machine learning model: %.Of%%" % (100 * _n_(439818, "modelCases", lambda: modelCases)/ _n_(439819, "totalNoCases", lambda: totalNoCases)))
    _l_(439821)
    _a_(439823, _n_(439822, "dashboard", lambda: dashboard), "at")["Model cases achieved", "B"] = _c_(439827, _n_(439824, "round", lambda: round), _n_(439825, "modelCases", lambda: modelCases) / _n_(439826, "totalNoCases", lambda: totalNoCases), 2)
    _l_(439828)
    _c_(439832, _n_(439829, "print", lambda: print), "OR minutes used with original model: %.Of%%" % (100 * _n_(439830, "originalMinutes", lambda: originalMinutes)/_n_(439831, "totalMinutes", lambda: totalMinutes)))
    _l_(439833)
    _a_(439835, _n_(439834, "dashboard", lambda: dashboard), "at")["Original OR minutes used", "B"] = _c_(439839, _n_(439836, "round", lambda: round), _n_(439837, "originalMinutes", lambda: originalMinutes) / _n_(439838, "totalMinutes", lambda: totalMinutes), 2)
    _l_(439840)
    _c_(439844, _n_(439841, "print", lambda: print), "OR minutes used with machine learning model: %.Of%%" % (100 * _n_(439842, "modelMinutes", lambda: modelMinutes) /
_n_(439843, "totalMinutes", lambda: totalMinutes)))
    _l_(439845)
    _a_(439847, _n_(439846, "dashboard", lambda: dashboard), "at")["Model OR minutes used", "B"] = _c_(439851, _n_(439848, "round", lambda: round), _n_(439849, "modelMinutes", lambda: modelMinutes) / _n_(439850, "totalMinutes", lambda: totalMinutes), 2)
    _l_(439852)

    _c_(439856, _a_(439854, _n_(439853, "dashboard", lambda: dashboard), "to_excel"), r'' + _n_(439855, "excelOutputFile", lambda: excelOutputFile), index=False)
    _l_(439857)

else:

    _c_(439859, _n_(439858, "print", lambda: print), "No feasible solution found.")
    _l_(439860)