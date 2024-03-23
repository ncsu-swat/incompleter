#Source: https://stackoverflow.com/questions/53327338/numpy-busday-count-for-days-difference-gives-typeerror-dtypem8us-to-dtyp
import pandas as pd
import numpy as np
import datetime
from datetime import date
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import xlrd
import workdays
import defusedxml
from xlrd import open_workbook
defusedxml.defuse_stdlib()


def secure_open_workbook(**kwargs):
    try:
        return open_workbook(**kwargs)
    except EntitiesForbidden:
        raise ValueError('Please use a xlsx file without XEE')


#loading Raw Data
releases = pd.read_excel(r'C:\Desktop\Releases.xlsx',
                     sheet_name = 'Releases',
                     header = 0
                     )
releases.loc[releases['REASSIGN_DATE'].isnull(),'REASSIGN_DATE']=releases['SETUP_DATE']
releases['REASSIGN_DATE']=pd.to_datetime(releases['REASSIGN_DATE'])
releases['RELEASED_DATE']=pd.to_datetime(releases['RELEASED_DATE'])
releases['RELEASED_DAYS']=releases.apply(lambda x: 
np.busday_count(x.REASSIGN_DATE,x.RELEASED_DATE),axis =1)

releases_2=releases.drop(['SETUPDATE','RELEASEDDATE','REASSIGNDATE'],axis=1)