import pandas as pd
df = pd.DataFrame({'City': ['New York', 'Parague', 'New Delhi', 'Venice', 'new Orleans'], 'Event': ['Music', 'Poetry', 'Theatre', 'Comedy', 'Tech_Summit'], 'Cost': [10000, 5000, 15000, 2000, 12000]})
index_ = [pd.Period('02-2018'), pd.Period('04-2018'), pd.Period('06-2018'), pd.Period('10-2018'), pd.Period('12-2018')]
print(df)