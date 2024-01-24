# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65337966/getting-attributeerror-when-using-inherited-class
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import netCDF4 as netcdf
    _l_(545318)

except ImportError:
    pass
try:
    import numpy as np
    _l_(545320)

except ImportError:
    pass

class cellData:
    _l_(545404)

    
    def __init__(self, cellNetCDF, gridNetCDF):
        _l_(545369)

        _n_(545321, "self", lambda: self).cellNetCDF = _n_(545322, "cellNetCDF", lambda: cellNetCDF)
        _l_(545323)
        _n_(545324, "self", lambda: self).gridNetCDF = _n_(545325, "gridNetCDF", lambda: gridNetCDF)
        _l_(545326)
        
        _n_(545327, "self", lambda: self).X = _c_(545332, _a_(545329, _n_(545328, "np", lambda: np), "array"), _a_(545331, _n_(545330, "cellNetCDF", lambda: cellNetCDF), "variables")['X'])
        _l_(545333)
        _n_(545334, "self", lambda: self).Y = _c_(545339, _a_(545336, _n_(545335, "np", lambda: np), "array"), _a_(545338, _n_(545337, "cellNetCDF", lambda: cellNetCDF), "variables")['Y'])
        _l_(545340)
        _n_(545341, "self", lambda: self).neighbrArray = _c_(545346, _a_(545343, _n_(545342, "np", lambda: np), "array"), _a_(545345, _n_(545344, "grid", lambda: grid), "variables")['minLevelCellsNghbrIds'])
        _l_(545347)
        
        _n_(545348, "self", lambda: self).arrayList = {}
        _l_(545349)
        for var in _c_(545353, _a_(545352, _a_(545351, _n_(545350, "cellNetCDF", lambda: cellNetCDF), "variables"), "values")):
            _l_(545363)

            _a_(545355, _n_(545354, "self", lambda: self), "arrayList")[_a_(545357, _n_(545356, "var", lambda: var), "name")] = _c_(545361, _a_(545359, _n_(545358, "np", lambda: np), "array"), _n_(545360, "var", lambda: var)[:])
            _l_(545362)
        _n_(545364, "self", lambda: self).noCells = _a_(545367, _a_(545366, _n_(545365, "cellNetCDF", lambda: cellNetCDF), "dimensions")['dim0'], "size")
        _l_(545368)
    def cellCoord(self, cellId, direction):
        _l_(545382)

        if _n_(545370, "direction", lambda: direction) == 0:
            _l_(545381)

            aux = _a_(545372, _n_(545371, "self", lambda: self), "X")[_n_(545373, "cellId", lambda: cellId)]    
            _l_(545374)    
            return aux    
        elif _n_(545375, "direction", lambda: direction) == 1:
            _l_(545380)

            aux = _a_(545377, _n_(545376, "self", lambda: self), "Y")[_n_(545378, "cellId", lambda: cellId)]
            _l_(545379)
            return aux
    
    def neighbrId(self, cellId, direction):
        _l_(545388)

        aux = _a_(545384, _n_(545383, "self", lambda: self), "neighbrArray")[4 * _n_(545385, "cellId", lambda: cellId) + _n_(545386, "direction", lambda: direction)]
        _l_(545387)
        return aux
        
    def getVariable(self, cellId, var):
        _l_(545397)

        variableNum = _n_(545389, "invertedMap", lambda: invertedMap)[_n_(545390, "var", lambda: var)]
        _l_(545391)
        aux = _a_(545393, _n_(545392, "self", lambda: self), "arrayList")[_n_(545394, "variableNum", lambda: variableNum)][_n_(545395, "cellId", lambda: cellId)]
        _l_(545396)
        return aux
    
    def applyMask(self, maskArray):
        _l_(545403)

        aux = _c_(545401, _n_(545398, "maskedCellData", lambda: maskedCellData), _n_(545399, "self", lambda: self), _n_(545400, "maskArray", lambda: maskArray))
        _l_(545402)
        return aux

class maskedCellData(_n_(545405, "cellData", lambda: cellData)):
    _l_(545432)

    
    def __init__(self, cellDataObject, maskArray):
        _l_(545431)

        _a_(545407, _n_(545406, "self", lambda: self), "X")[:] = _a_(545409, _n_(545408, "cellDataObject", lambda: cellDataObject), "X")[:] * _n_(545410, "maskArray", lambda: maskArray)[:]  
        _l_(545411)  
        _a_(545413, _n_(545412, "self", lambda: self), "Y")[:] = _a_(545415, _n_(545414, "cellDataObject", lambda: cellDataObject), "Y")[:] * _n_(545416, "maskArray", lambda: maskArray)[:]
        _l_(545417)
        
        _n_(545418, "self", lambda: self).arrayList = {}
        _l_(545419)
        for var in _a_(545421, _n_(545420, "cellDataObject", lambda: cellDataObject), "arrayList"):
            _l_(545430)

            _a_(545423, _n_(545422, "self", lambda: self), "arrayList")[_n_(545424, "var", lambda: var)] = _a_(545426, _n_(545425, "cellDataObject", lambda: cellDataObject), "arrayList")[_n_(545427, "var", lambda: var)] * _n_(545428, "maskArray", lambda: maskArray)
            _l_(545429)

def getMask(cellDataObject, point1, direction):
    _l_(545471)

    
    noCells = _a_(545434, _n_(545433, "cellDataObject", lambda: cellDataObject), "noCells")
    _l_(545435)
    
    maskArray = _c_(545439, _a_(545437, _n_(545436, "np", lambda: np), "zeros"), _n_(545438, "noCells", lambda: noCells))
    _l_(545440)
    
    for cellId in _c_(545443, _n_(545441, "range", lambda: range), 0, _n_(545442, "noCells", lambda: noCells) - 1):
        _l_(545468)

        nghbrId = _c_(545448, _a_(545445, _n_(545444, "cellDataObject", lambda: cellDataObject), "neighbrId"), _n_(545446, "cellId", lambda: cellId), _n_(545447, "direction", lambda: direction) + 2)
        _l_(545449)
        if(_n_(545450, "nghbrId", lambda: nghbrId) == -1):
            _l_(545451)

continue        if (_c_(545456, _a_(545453, _n_(545452, "cellDataObject", lambda: cellDataObject), "cellCoord"), _n_(545454, "cellId", lambda: cellId), _n_(545455, "direction", lambda: direction)) - _n_(545457, "point1", lambda: point1) < 0 ) & (_c_(545462, _a_(545459, _n_(545458, "cellDataObject", lambda: cellDataObject), "cellCoord"), _n_(545460, "nghbrId", lambda: nghbrId), _n_(545461, "direction", lambda: direction)) - _n_(545463, "point1", lambda: point1) > 0):
            _l_(545467)

            _n_(545464, "maskArray", lambda: maskArray)[_n_(545465, "cellId", lambda: cellId)] = 1
            _l_(545466)
    aux = _n_(545469, "maskArray", lambda: maskArray)
    _l_(545470)
    return aux

Map = {'variables0' : 'u',
           'variables1' : 'v',
           'variables2' : 'rho',
           'variables3' : 'p',
           'variables4' : 'YH2',
           'variables5' : 'YH',
           'variables6' : 'YO',
           'variables7' : 'YO2',
           'variables8' : 'YOH',
           'variables9' : 'YH2O',
           'variables10' : 'YHO2',
           'variables11' : 'YH2O2',
           'variables12' : 'YN',
           'variables13' : 'YNH',
           'variables14' : 'YNH2',
           'variables15' : 'YNH3',
           'variables16' : 'YNNH',
           'variables17' : 'YNO',
           'variables18' : 'YNO2',
           'variables19' : 'YN2O',
           'variables20' : 'YHNO',
           'variables21' : 'YN2'
    }
_l_(545472)

invertedMap = {_n_(545473, "v", lambda: v): _n_(545474, "k", lambda: k) for k, v in _c_(545477, _a_(545476, _n_(545475, "Map", lambda: Map), "items"))}
_l_(545478)

f = _c_(545481, _a_(545480, _n_(545479, "netcdf", lambda: netcdf), "Dataset"), "pressureOutput/restartVariables_2.Netcdf","r")
_l_(545482)
grid = _c_(545485, _a_(545484, _n_(545483, "netcdf", lambda: netcdf), "Dataset"), "pressureOutput/grid.Netcdf","r")
_l_(545486)

cellData1 = _c_(545490, _n_(545487, "cellData", lambda: cellData), _n_(545488, "f", lambda: f), _n_(545489, "grid", lambda: grid))
_l_(545491)

maskArray = _c_(545494, _n_(545492, "getMask", lambda: getMask), _n_(545493, "cellData1", lambda: cellData1), 0, 0)
_l_(545495)

maskedCellData = _c_(545499, _n_(545496, "maskedCellData", lambda: maskedCellData), _n_(545497, "cellData1", lambda: cellData1), _n_(545498, "maskArray", lambda: maskArray))
_l_(545500)