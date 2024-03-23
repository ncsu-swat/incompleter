#Source: https://stackoverflow.com/questions/75670256/executing-pandasgui-package-raises-a-attributeerror
import pandas as pd
from pandasgui import show
df = pd.DataFrame({'a':[1,2,3], 'b':[4,5,6], 'c':[7,8,9]})
show(df)