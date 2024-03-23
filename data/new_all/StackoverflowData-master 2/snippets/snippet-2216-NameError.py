#Source: https://stackoverflow.com/questions/57447483/pandas-dataframe-fails-with-attributeerror-nonetype-object-has-no-attribute
file_list = glob.glob("*.json")

allFilesDict = {v:k for v, k in enumerate(file_list, 1)}

data = []

for k,v in allFilesDict.items():
    if 1 <= k <= 400000:
        with open(v, 'r') as d:
            data.append(json.load(d))

df = pd.DataFrame(data)

df.to_json(r'/home/user1/merge/output_1.json', orient='records')