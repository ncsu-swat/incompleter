# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/54263271/attributeerror-unknown-property-column-in-geopandas-plotting-of-events-in-zipco
# set a variable that will call column to visualise on the map

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
variable = 'ZIPNUM'
_l_(391913)

# set the range for the choropleth

vmin, vmax = 50, 2000
_l_(391914)

# create figure and axes for Matplotlib

fig, ax = _c_(391917, _a_(391916, _n_(391915, "plt", lambda: plt), "subplots"), 1, figsize=(15, 15))
_l_(391918)

# create map

_c_(391923, _a_(391920, _n_(391919, "merged_df", lambda: merged_df), "plot"), column=_n_(391921, "variable", lambda: variable), cmap='Reds', linewidth=0.8, ax=_n_(391922, "ax", lambda: ax), edgecolor='0.8');
_l_(391924)

_c_(391927, _a_(391926, _n_(391925, "ax", lambda: ax), "axis"), 'off')
_l_(391928)

_c_(391931, _a_(391930, _n_(391929, "ax", lambda: ax), "set_title"), 'Fire Incident Rate in Wake County', fontdict={'fontsize': '25', 'fontweight' : '3'})
_l_(391932)

# Create colorbar as a legend

sm = _c_(391941, _a_(391935, _a_(391934, _n_(391933, "plt", lambda: plt), "cm"), "ScalarMappable"), cmap='Reds', norm=_c_(391940, _a_(391937, _n_(391936, "plt", lambda: plt), "Normalize"), vmin=_n_(391938, "vmin", lambda: vmin), vmax=_n_(391939, "vmax", lambda: vmax)))
_l_(391942)

# empty array for the data range

_n_(391943, "sm", lambda: sm)._A = []
_l_(391944)

# add the colorbar to the figure

cbar = _c_(391948, _a_(391946, _n_(391945, "fig", lambda: fig), "colorbar"), _n_(391947, "sm", lambda: sm))
_l_(391949)

_c_(391952, _a_(391951, _n_(391950, "ax", lambda: ax), "annotate"), '2008-2018',
            xy=(0.001, .225), xycoords='figure fraction',
            horizontalalignment='left', verticalalignment='top',
            fontsize=35)
_l_(391953)

_c_(391956, _a_(391955, _n_(391954, "fig", lambda: fig), "savefig"), "Fire Incident Rate in Wake County 2008-2018.png", dpi=300)
_l_(391957)