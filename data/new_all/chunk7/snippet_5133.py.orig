#Source: https://stackoverflow.com/questions/49515768/typeerror-can-only-concatenate-list-not-int-to-list-help-needed
path2 = (r'C:\Users\newsample.csv')
openfile2 = pd.read_csv(path2, header='infer')

# Convert Long and Lat rows to list
lon = (list(openfile2['Long']))
lat = (list(openfile2['Lat']))
latitude = []
longitude = []

for la in lat:
    la = pd.to_numeric(openfile2['Lat'])
    latitude.append(la)

for lo in lon:
    lo = pd.to_numeric(openfile2['Long'])
    latitude.append(lo)

# compute UTM zone for the rows
def get_zone(lat, lon):
    zone = int((lon + 186) / 6)
    if lat >= 56.0 and lat < 64.0 and lon >= 3.0 and lon < 12.0:
        zone = 32
    if lat >= 72.0 and lat < 84.0:
        if lon >= 0.0 and lon < 9.0:
            zone = 31
        elif lon >= 9.0 and lon < 21.0:
            zone = 33
        elif lon >= 21.0 and lon < 33.0:
            zone = 35
        elif lon >= 33.0 and lon < 42.0:
            zone = 37
    if lat > 0:
        cs = "EPSG::326" + str(zone)
    else:
        cs = "EPSG::327" + str(zone)
    return cs

# Call function
newfile = get_zone(latitude, longitude)
print(newfile)