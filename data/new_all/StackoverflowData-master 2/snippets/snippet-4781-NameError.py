#Source: https://stackoverflow.com/questions/77232147/filenotfounderror-errno-2-no-such-file-or-directory-c-users-sardo-downl
df=pd.read_csv(r'C:\Users\sardo\Downloads\ChicagoCensusData.csv')
df.to_sql("CENSUS_DATA", con, if_exists='replace', index=False, method='mutli')