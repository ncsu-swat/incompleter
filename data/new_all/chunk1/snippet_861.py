# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59905286/nonetype-error-when-trying-to-make-a-custom-beautifulsoup-dagster-type
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import requests
    _l_(389107)

except ImportError:
    pass
try:
    from bs4 import BeautifulSoup
    _l_(389109)

except ImportError:
    pass
try:
    from dagster import (
        dagster_type,
        input_hydration_config,
        Selector,
        Field,
        String,
        TypeCheck,
        EventMetadataEntry
    )
    _l_(389111)

except ImportError:
    pass

def max_depth(soup):
    _l_(389127)

    if _c_(389114, _n_(389112, "hasattr", lambda: hasattr), _n_(389113, "soup", lambda: soup), "contents") and _a_(389116, _n_(389115, "soup", lambda: soup), "contents"):
        _l_(389126)

        aux = _c_(389123, _n_(389117, "max", lambda: max), [_c_(389120, _n_(389118, "max_depth", lambda: max_depth), _n_(389119, "child", lambda: child)) for child in _a_(389122, _n_(389121, "soup", lambda: soup), "contents")]) + 1
        _l_(389124)
        return aux
    else:
        aux = 0
        _l_(389125)
        return aux

def html_soup_type_check(value):
    _l_(389171)

    if not _c_(389131, _n_(389128, "isinstance", lambda: isinstance), _n_(389129, "value", lambda: value), _n_(389130, "BeautifulSoup", lambda: BeautifulSoup)):
        _l_(389140)

        aux = _c_(389138, _n_(389132, "TypeCheck", lambda: TypeCheck), success=False,
            description=_c_(389137, _a_(389133, (
                'HtmlSoup should be a BeautifulSoup Object, got '
                '{type_}'
            ), "format"), type_=_c_(389136, _n_(389134, "type", lambda: type), _n_(389135, "value", lambda: value)))
        )
        _l_(389139)
        return aux

    if not _c_(389143, _n_(389141, "hasattr", lambda: hasattr), _n_(389142, "soup", lambda: soup), "contents"):
        _l_(389147)

        aux = _c_(389145, _n_(389144, "TypeCheck", lambda: TypeCheck), success=False,
            description=(
                'HtmlSoup has no contents, check that the URL has content'
            )
        )
        _l_(389146)
        return aux
    aux = _c_(389169, _n_(389148, "TypeCheck", lambda: TypeCheck), success=True,
        description='HtmlSoup Summary Stats',
        metadata_entries=[
            _c_(389156, _a_(389150, _n_(389149, "EventMetadataEntry", lambda: EventMetadataEntry), "text"), _c_(389155, _n_(389151, "str", lambda: str), _c_(389154, _n_(389152, "max_depth", lambda: max_depth), _n_(389153, "value", lambda: value))),
                'max_depth',
                'Max Nested Depth of the Page Soup'
            ),
            _c_(389168, _a_(389158, _n_(389157, "EventMetadataEntry", lambda: EventMetadataEntry), "text"), _c_(389167, _n_(389159, "str", lambda: str), _c_(389166, _n_(389160, "set", lambda: set), (_a_(389162, _n_(389161, "tag", lambda: tag), "name") for tag in _c_(389165, _a_(389164, _n_(389163, "value", lambda: value), "find_all"))))),
                'tag_names',
                'All available tags in the Page Soup'
            )
        ]
    )
    _l_(389170)

    return aux


@_c_(389178, _n_(389172, "input_hydration_config", lambda: input_hydration_config), _c_(389177, _n_(389173, "Selector", lambda: Selector), {
            'url': _c_(389176, _n_(389174, "Field", lambda: Field), _n_(389175, "String", lambda: String),
                is_optional=False,
                description=(
                    'URL to be ingested and converted to a Soup Object'
                )
            )
        }
    )
)
def html_soup_input_hydration_config(context, selector):
    _l_(389206)

    url = _n_(389179, "selector", lambda: selector)['url']
    _l_(389180)
    res = _c_(389184, _a_(389182, _n_(389181, "requests", lambda: requests), "get"), _n_(389183, "url", lambda: url), params={
        'Content-type': 'text/html'
    })
    _l_(389185)

    if (not _a_(389187, _n_(389186, "res", lambda: res), "status_code") == 200):
        _l_(389196)

        aux = _c_(389194, _n_(389188, "TypeCheck", lambda: TypeCheck), success=False,
            description=_c_(389193, _a_(389189, (
                '{status_code} ERROR, Check that URL: {url} is correct'
            ), "format"), status_code=_a_(389191, _n_(389190, "res", lambda: res), "status_code"), url=_n_(389192, "url", lambda: url))
        )
        _l_(389195)
        return aux
    soup = _c_(389200, _n_(389197, "BeautifulSoup", lambda: BeautifulSoup), _a_(389199, _n_(389198, "res", lambda: res), "content"), 'html.parser')
    _l_(389201)
    aux = _c_(389204, _n_(389202, "HtmlSoup", lambda: HtmlSoup), _n_(389203, "soup", lambda: soup))
    _l_(389205)
    return aux

@_c_(389210, _n_(389207, "dagster_type", lambda: dagster_type), name='HtmlSoup',
    description=(
        'The HTML extracted from a URL stored in '
        'a BeautifulSoup object.'
    ),
    type_check=_n_(389208, "html_soup_type_check", lambda: html_soup_type_check),
    input_hydration_config=_n_(389209, "html_soup_input_hydration_config", lambda: html_soup_input_hydration_config)
)
class HtmlSoup(_n_(389211, "BeautifulSoup", lambda: BeautifulSoup)):
    _l_(389213)

    pass
    _l_(389212)