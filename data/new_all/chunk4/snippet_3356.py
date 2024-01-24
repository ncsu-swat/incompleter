# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75408162/for-key-in-keys-typeerror-nonetype-object-is-not-iterable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
url = _c_(609256, _n_(609255, "input", lambda: input), '\nEnter URL Here: ')
_l_(609257)
type_url = _c_(609262, _a_(609261, _c_(609260, _a_(609259, _n_(609258, "url", lambda: url), "split"), '?')[0], "split"), '/')[-1]
_l_(609263)

if _n_(609264, "type_url", lambda: type_url) == 'tv-guide':
    _l_(609275)

    id_url = _c_(609267, _a_(609266, _n_(609265, "url", lambda: url), "split"), '=')[-1]
    _l_(609268)
else:
    id_url = _c_(609273, _a_(609272, _c_(609271, _a_(609270, _n_(609269, "url", lambda: url), "split"), '&')[0], "split"), '=')[-1]
    _l_(609274)

#id_url = url.split('&')[0].split('=')[-1]
#fix_id = id_url.split('=')[-1]
resp = _c_(609285, _a_(609284, _c_(609283, _a_(609277, _n_(609276, "requests", lambda: requests), "post"), _c_(609280, _a_(609278, 'https://tvapi-sgn.solocoo.tv/v1/assets/{}/play', "format"), _n_(609279, "id_url", lambda: id_url)), headers=_n_(609281, "headers", lambda: headers), json=_n_(609282, "json_data", lambda: json_data)), "json"))
_l_(609286)
lic_url = _n_(609287, "resp", lambda: resp)['drm']['licenseUrl']
_l_(609288)
mpd_url = _n_(609289, "resp", lambda: resp)['url']
_l_(609290)

_c_(609293, _n_(609291, "print", lambda: print), f'\nMPD URL: {_n_(609292, "mpd_url", lambda: mpd_url)}')
_l_(609294)
_c_(609297, _n_(609295, 'print', lambda: print), f'\nLICENSE URL: {_n_(609296, "lic_url", lambda: lic_url)}')
_l_(609298)

def get_pssh_kid(keyId):
    _l_(609333)

    array_of_bytes = _c_(609300, _n_(609299, 'bytearray', lambda: bytearray), b'\x00\x00\x002pssh\x00\x00\x00\x00')
    _l_(609301)
    _c_(609307, _a_(609303, _n_(609302, 'array_of_bytes', lambda: array_of_bytes), 'extend'), _c_(609306, _a_(609305, _n_(609304, 'bytes', lambda: bytes), 'fromhex'), "edef8ba979d64acea3c827dcd51d21ed"))
    _l_(609308)
    _c_(609311, _a_(609310, _n_(609309, 'array_of_bytes', lambda: array_of_bytes), 'extend'), b'\x00\x00\x00\x12\x12\x10')
    _l_(609312)
    _c_(609321, _a_(609314, _n_(609313, 'array_of_bytes', lambda: array_of_bytes), 'extend'), _c_(609320, _a_(609316, _n_(609315, 'bytes', lambda: bytes), 'fromhex'), _c_(609319, _a_(609318, _n_(609317, 'keyId', lambda: keyId), 'replace'), "-", "")))
    _l_(609322)
    aux = _c_(609331, _a_(609324, _n_(609323, 'base64', lambda: base64), 'b64encode'), _c_(609330, _a_(609326, _n_(609325, 'bytes', lambda: bytes), 'fromhex'), _c_(609329, _a_(609328, _n_(609327, 'array_of_bytes', lambda: array_of_bytes), 'hex'))))
    _l_(609332)
    return aux

def get_pssh_mpd(mpd_url):
    _l_(609377)

    r = _c_(609337, _a_(609335, _n_(609334, 'requests', lambda: requests), 'get'), url=_n_(609336, 'mpd_url', lambda: mpd_url))
    _l_(609338)
    _c_(609341, _a_(609340, _n_(609339, 'r', lambda: r), 'raise_for_status'))
    _l_(609342)
    xml = _c_(609347, _a_(609344, _n_(609343, 'xmltodict', lambda: xmltodict), 'parse'), _a_(609346, _n_(609345, 'r', lambda: r), 'text'))
    _l_(609348)
    mpd = _c_(609355, _a_(609350, _n_(609349, 'json', lambda: json), 'loads'), _c_(609354, _a_(609352, _n_(609351, 'json', lambda: json), 'dumps'), _n_(609353, 'xml', lambda: xml)))
    _l_(609356)
    tracks = _n_(609357, 'mpd', lambda: mpd)['MPD']['Period']['AdaptationSet']
    _l_(609358)
    for video_tracks in _n_(609359, 'tracks', lambda: tracks):
        _l_(609374)

        if _n_(609360, 'video_tracks', lambda: video_tracks)['@mimeType'] == 'video/mp4':
            _l_(609373)

            for t in _n_(609361, 'video_tracks', lambda: video_tracks)["ContentProtection"]:
                _l_(609372)

                if _c_(609364, _a_(609363, _n_(609362, 't', lambda: t)['@schemeIdUri'], 'lower')) == "urn:mpeg:dash:mp4protection:2011":
                    _l_(609371)

                    kid = _n_(609365, 't', lambda: t)['@cenc:default_KID']
                    _l_(609366)
                    pssh = _c_(609369, _n_(609367, 'get_pssh_kid', lambda: get_pssh_kid), _n_(609368, 'kid', lambda: kid))
                    _l_(609370)
    aux = _n_(609375, 'pssh', lambda: pssh)
    _l_(609376)
    return aux

pssh = _c_(609382, _a_(609381, _c_(609380, _n_(609378, 'get_pssh_mpd', lambda: get_pssh_mpd), _n_(609379, 'mpd_url', lambda: mpd_url)), 'decode'), 'utf-8')
_l_(609383)

_c_(609386, _n_(609384, 'print', lambda: print), "\n[green]+ [INFO] PSSH: [/green]" + _n_(609385, 'pssh', lambda: pssh))
_l_(609387)

def decrypt_keys():
    _l_(609427)

    wvdecrypt = _c_(609390, _n_(609388, 'WvDecrypt', lambda: WvDecrypt), _n_(609389, 'pssh', lambda: pssh))
    _l_(609391)
    raw_challenge = _c_(609394, _a_(609393, _n_(609392, 'wvdecrypt', lambda: wvdecrypt), 'get_challenge'))
    _l_(609395)
    challenge_b64 = _c_(609400, _a_(609399, _c_(609398, _n_(609396, 'b64encode', lambda: b64encode), _n_(609397, 'raw_challenge', lambda: raw_challenge)), 'decode'))
    _l_(609401)
    widevine_license = _c_(609407, _a_(609403, _n_(609402, 'requests', lambda: requests), 'post'), url=_n_(609404, 'lic_url', lambda: lic_url), data=_n_(609405, 'raw_challenge', lambda: raw_challenge), headers=_n_(609406, 'headers', lambda: headers), timeout=10)
    _l_(609408)
    license_b64 = _c_(609412, _n_(609409, 'b64encode', lambda: b64encode), _a_(609411, _n_(609410, 'widevine_license', lambda: widevine_license), 'content'))
    _l_(609413)
    _c_(609417, _a_(609415, _n_(609414, 'wvdecrypt', lambda: wvdecrypt), 'update_license'), _n_(609416, 'license_b64', lambda: license_b64))
    _l_(609418)
    keys = _c_(609421, _a_(609420, _n_(609419, 'wvdecrypt', lambda: wvdecrypt), 'start_process'))
    _l_(609422)
    if _n_(609423, 'keys', lambda: keys):
        _l_(609426)

        aux = _n_(609424, 'keys', lambda: keys)
        _l_(609425)
        return aux

keys = _c_(609429, _n_(609428, 'decrypt_keys', lambda: decrypt_keys))
_l_(609430)

for key in _n_(609431, 'keys', lambda: keys):
    _l_(609436)

    _c_(609434, _n_(609432, 'print', lambda: print), "\n[green]+ [INFO] KEY: --key [/green]" + _n_(609433, 'key', lambda: key))
    _l_(609435)