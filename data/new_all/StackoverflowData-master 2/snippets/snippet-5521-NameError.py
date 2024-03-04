#Source: https://stackoverflow.com/questions/63169198/typeerror-slicenone-59-none-slicenone-none-none-is-an-invalid-key
data.drop(data[:59,:],inplace= True)
print(data)