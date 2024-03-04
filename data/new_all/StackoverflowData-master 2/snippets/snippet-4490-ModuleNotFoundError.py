#Source: https://stackoverflow.com/questions/56673753/nameerror-name-fh-is-not-defined
from netCDF4 import Dataset 
import numpy as np  
my_example_nc_file = r'''\D:\UoR\Practice data\cru10min30_tmp.nc'
fh = (my_example_nc_file, mode='r')'''
lons = fh.variables['lon'][:]
lats = fh.variables['lat'][:]
tmax = fh.variables['Tmax'][:]
tmax_units = fh.variables['Tmax'].units