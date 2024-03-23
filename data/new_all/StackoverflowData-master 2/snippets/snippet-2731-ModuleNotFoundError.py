#Source: https://stackoverflow.com/questions/65337966/getting-attributeerror-when-using-inherited-class
import netCDF4 as netcdf
import numpy as np

class cellData:
    
    def __init__(self, cellNetCDF, gridNetCDF):
        self.cellNetCDF = cellNetCDF
        self.gridNetCDF = gridNetCDF
        
        self.X = np.array(cellNetCDF.variables['X'])
        self.Y = np.array(cellNetCDF.variables['Y'])
        self.neighbrArray = np.array(grid.variables['minLevelCellsNghbrIds'])
        
        self.arrayList = {}
        for var in cellNetCDF.variables.values():
            self.arrayList[var.name] = np.array(var[:])
            
        self.noCells = cellNetCDF.dimensions['dim0'].size
        
    def cellCoord(self, cellId, direction):
        if direction == 0:
            return self.X[cellId]    
        elif direction == 1:
            return self.Y[cellId]
    
    def neighbrId(self, cellId, direction):
            return self.neighbrArray[4 * cellId + direction]
        
    def getVariable(self, cellId, var):
        variableNum = invertedMap[var]
        return self.arrayList[variableNum][cellId]
    
    def applyMask(self, maskArray):
        return maskedCellData(self, maskArray)

class maskedCellData(cellData):
    
    def __init__(self, cellDataObject, maskArray):
        self.X[:] = cellDataObject.X[:] * maskArray[:]  
        self.Y[:] = cellDataObject.Y[:] * maskArray[:]
        
        self.arrayList = {}
        for var in cellDataObject.arrayList:
            self.arrayList[var] = cellDataObject.arrayList[var] * maskArray
            

def getMask(cellDataObject, point1, direction): 
    
    noCells = cellDataObject.noCells
    
    maskArray = np.zeros(noCells)
    
    for cellId in range(0, noCells - 1):
        nghbrId = cellDataObject.neighbrId(cellId, direction + 2)
        if(nghbrId == -1): continue
        if (cellDataObject.cellCoord(cellId, direction) - point1 < 0 ) & (cellDataObject.cellCoord(nghbrId, direction) - point1 > 0):
            maskArray[cellId] = 1
            
    return maskArray

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

invertedMap = {v: k for k, v in Map.items()}

f = netcdf.Dataset("pressureOutput/restartVariables_2.Netcdf","r")
grid = netcdf.Dataset("pressureOutput/grid.Netcdf","r")

cellData1 = cellData(f, grid)

maskArray = getMask(cellData1, 0, 0)

maskedCellData = maskedCellData(cellData1, maskArray)