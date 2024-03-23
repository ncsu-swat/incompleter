# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/16694907/download-large-file-in-python-with-requests
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import aiofiles
    _l_(61534)

except ImportError:
    pass
try:
    import aiohttp
    _l_(61536)

except ImportError:
    pass
try:
    import asyncio
    _l_(61538)

except ImportError:
    pass

async def async_http_download(src_url, dest_file, chunk_size=65536):
    _l_(61564)

    async with _c_(61542, _a_(61540, _n_(61539, "aiofiles", lambda: aiofiles), "open"), _n_(61541, "dest_file", lambda: dest_file), 'wb') as fd:
        _l_(61563)

        async with _c_(61545, _a_(61544, _n_(61543, "aiohttp", lambda: aiohttp), "ClientSession")) as session:
            _l_(61562)

            async with _c_(61549, _a_(61547, _n_(61546, "session", lambda: session), "get"), _n_(61548, "src_url", lambda: src_url)) as resp:
                _l_(61561)

                async for chunk in _c_(61554, _a_(61552, _a_(61551, _n_(61550, "resp", lambda: resp), "content"), "iter_chunked"), _n_(61553, "chunk_size", lambda: chunk_size)):
                    _l_(61560)

                    await _c_(61558, _a_(61556, _n_(61555, "fd", lambda: fd), "write"), _n_(61557, "chunk", lambda: chunk))
                    _l_(61559)

SRC_URL = "/path/to/url"
_l_(61565)
DEST_FILE = "/path/to/file/on/local/machine"
_l_(61566)

_c_(61573, _a_(61568, _n_(61567, "asyncio", lambda: asyncio), "run"), _c_(61572, _n_(61569, "async_http_download", lambda: async_http_download), _n_(61570, "SRC_URL", lambda: SRC_URL), _n_(61571, "DEST_FILE", lambda: DEST_FILE)))
_l_(61574)

