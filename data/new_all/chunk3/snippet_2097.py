# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60126257/data-visualization-typeerror-unsupported-operand-types-for-int-and-non
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import json
    _l_(524369)

except ImportError:
    pass
try:
    from plotly import offline
    _l_(524371)

except ImportError:
    pass
try:
    from plotly.graph_objs import Layout
    _l_(524373)

except ImportError:
    pass

# Open file and explore structure of the file's data
filename = "/Users/johnphillip/PycharmProjects/earth_quake_analysis/data" \
           "/latest_eq_data_30_m1.json"
_l_(524374)
with _c_(524377, _n_(524375, "open", lambda: open), _n_(524376, "filename", lambda: filename)) as data_record:
    _l_(524383)

    eq_data = _c_(524381, _a_(524379, _n_(524378, "json", lambda: json), "load"), _n_(524380, "data_record", lambda: data_record))
    _l_(524382)

eq_features = _n_(524384, "eq_data", lambda: eq_data)['features']
_l_(524385)

# Automate the title of the graph by automatically fetching the title from
# the file's metadata properties.
title = _n_(524386, "eq_data", lambda: eq_data)['metadata']['title']
_l_(524387)

# Extract the magnitudes, longitude, latitudes and earthquake title for each
# earthquake event.
mags, longs, lats, event_titles = [], [], [], []
_l_(524388)
for eq_feature in _n_(524389, "eq_features", lambda: eq_features):
    _l_(524424)

    try:
        _l_(524423)

        mag = _n_(524390, "eq_feature", lambda: eq_feature)['properties']['mag']
        _l_(524391)
        lon = _n_(524392, "eq_feature", lambda: eq_feature)['geometry']['coordinates'][0]
        _l_(524393)
        lat = _n_(524394, "eq_feature", lambda: eq_feature)['geometry']['coordinates'][1]
        _l_(524395)
        event = _n_(524396, "eq_feature", lambda: eq_feature)['properties']['title']
        _l_(524397)
    except _n_(524398, "ValueError", lambda: ValueError):
        _l_(524402)

        _c_(524400, _n_(524399, "print", lambda: print), "Data not found in the record.")
        _l_(524401)
    else:
        _c_(524406, _a_(524404, _n_(524403, "mags", lambda: mags), "append"), _n_(524405, "mag", lambda: mag))
        _l_(524407)
        _c_(524411, _a_(524409, _n_(524408, "longs", lambda: longs), "append"), _n_(524410, "lon", lambda: lon))
        _l_(524412)
        _c_(524416, _a_(524414, _n_(524413, "lats", lambda: lats), "append"), _n_(524415, "lat", lambda: lat))
        _l_(524417)
        _c_(524421, _a_(524419, _n_(524418, "event_titles", lambda: event_titles), "append"), _n_(524420, "event", lambda: event))
        _l_(524422)

# Style and map the earthquakes
data = [{
    'type': 'scattergeo',
    'lon': _n_(524425, "longs", lambda: longs),
    'lat': _n_(524426, "lats", lambda: lats),
    'text': _n_(524427, "event_titles", lambda: event_titles),
    'maker': {
        'size': [5 * _n_(524428, "mag", lambda: mag) for mag in _n_(524429, "mags", lambda: mags)],
        'color': _n_(524430, "mags", lambda: mags),
        'colorscale': 'Inferno',
        'reverserscale': True,
        'colorbar': {'title': 'Magnitude'}
    }
}]
_l_(524431)

# Set the plot layout
my_layout = _c_(524434, _n_(524432, "Layout", lambda: Layout), title=_n_(524433, "title", lambda: title))
_l_(524435)
fig = {'data': _n_(524436, "data", lambda: data), 'layout': _n_(524437, "my_layout", lambda: my_layout)}
_l_(524438)

# Plot the chart.
if _n_(524439, "__name__", lambda: __name__) == '__main__':
    _l_(524445)

    _c_(524443, _a_(524441, _n_(524440, "offline", lambda: offline), "plot"), _n_(524442, "fig", lambda: fig), filename= '/earth_quake_analysis/eq_html_plots/latest_eq_1month.html')
    _l_(524444)