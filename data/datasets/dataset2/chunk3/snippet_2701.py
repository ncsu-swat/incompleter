#Source: https://stackoverflow.com/questions/60126257/data-visualization-typeerror-unsupported-operand-types-for-int-and-non
import json

from plotly import offline
from plotly.graph_objs import Layout

# Open file and explore structure of the file's data
filename = "/Users/johnphillip/PycharmProjects/earth_quake_analysis/data" \
           "/latest_eq_data_30_m1.json"
with open(filename) as data_record:
    eq_data = json.load(data_record)

eq_features = eq_data['features']

# Automate the title of the graph by automatically fetching the title from
# the file's metadata properties.
title = eq_data['metadata']['title']

# Extract the magnitudes, longitude, latitudes and earthquake title for each
# earthquake event.
mags, longs, lats, event_titles = [], [], [], []
for eq_feature in eq_features:
    try:
        mag = eq_feature['properties']['mag']
        lon = eq_feature['geometry']['coordinates'][0]
        lat = eq_feature['geometry']['coordinates'][1]
        event = eq_feature['properties']['title']
    except ValueError:
        print("Data not found in the record.")
    else:
        mags.append(mag)
        longs.append(lon)
        lats.append(lat)
        event_titles.append(event)

# Style and map the earthquakes
data = [{
    'type': 'scattergeo',
    'lon': longs,
    'lat': lats,
    'text': event_titles,
    'maker': {
        'size': [5 * mag for mag in mags],
        'color': mags,
        'colorscale': 'Inferno',
        'reverserscale': True,
        'colorbar': {'title': 'Magnitude'}
    }
}]

# Set the plot layout
my_layout = Layout(title=title)
fig = {'data': data, 'layout': my_layout}

# Plot the chart.
if __name__ == '__main__':
    offline.plot(fig, filename= '/earth_quake_analysis/eq_html_plots/latest_eq_1month.html')