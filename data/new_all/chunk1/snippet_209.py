# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/44004609/attributeerror-nonetype-object-has-no-attribute-decode
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
names, plot_dicts = [], []
_l_(405496)
for repo_dict in _n_(405497, "repo_dicts", lambda: repo_dicts):
    _l_(405512)

    _c_(405501, _a_(405499, _n_(405498, "names", lambda: names), "append"), _n_(405500, "repo_dict", lambda: repo_dict)['name'])
    _l_(405502)
    plot_dict = {
        'value': _n_(405503, "repo_dict", lambda: repo_dict)['stargazers_count'],
        'label': _n_(405504, "repo_dict", lambda: repo_dict)['description'],
        'xlink': _n_(405505, "repo_dict", lambda: repo_dict)['owner']['html_url'],
        }
    _l_(405506)
    _c_(405510, _a_(405508, _n_(405507, "plot_dicts", lambda: plot_dicts), "append"), _n_(405509, "plot_dict", lambda: plot_dict))
    _l_(405511)

my_style = _c_(405515, _n_(405513, "LS", lambda: LS), '#333366', base_style=_n_(405514, "LCS", lambda: LCS))
_l_(405516)
chart = _c_(405520, _a_(405518, _n_(405517, "pygal", lambda: pygal), "Bar"), style=_n_(405519, "my_style", lambda: my_style), x_label_rotation=45, show_legend=False)
_l_(405521)
_n_(405522, "chart", lambda: chart).title = 'Most-Stared Python Project On Github'
_l_(405523)
_n_(405524, "chart", lambda: chart).x_labels = _n_(405525, "names", lambda: names)
_l_(405526)
_c_(405530, _a_(405528, _n_(405527, "chart", lambda: chart), "add"), '', _n_(405529, "plot_dicts", lambda: plot_dicts))
_l_(405531)

_c_(405534, _a_(405533, _n_(405532, "chart", lambda: chart), "render_to_file"), 'new_repos.svg')
_l_(405535)