# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/44004609/attributeerror-nonetype-object-has-no-attribute-decode
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
names, plot_dicts = [], []
_l_(377372)
for repo_dict in _n_(377373, "repo_dicts", lambda: repo_dicts):
    _l_(377387)

    _c_(377377, _a_(377375, _n_(377374, "names", lambda: names), "append"), _n_(377376, "repo_dict", lambda: repo_dict)['name'])
    _l_(377378)
    plot_dict = {
        'value': _n_(377379, "repo_dict", lambda: repo_dict)['stargazers_count'],
        #'label': repo_dict['description'],
        'xlink': _n_(377380, "repo_dict", lambda: repo_dict)['owner']['html_url'],
        }
    _l_(377381)
    _c_(377385, _a_(377383, _n_(377382, "plot_dicts", lambda: plot_dicts), "append"), _n_(377384, "plot_dict", lambda: plot_dict))
    _l_(377386)