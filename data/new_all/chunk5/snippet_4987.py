# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/31779456/django-error-typeerror-expected-string-or-buffer
# Django imports
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.template import RequestContext
    _l_(680976)

except ImportError:
    pass
try:
    from django.shortcuts import render_to_response, render
    _l_(680978)

except ImportError:
    pass
try:
    from django.core.files.storage import get_storage_class
    _l_(680980)

except ImportError:
    pass
try:
    from django.core.files.base import ContentFile
    _l_(680982)

except ImportError:
    pass
try:
    from django.views.decorators.csrf import csrf_exempt
    _l_(680984)

except ImportError:
    pass
try:
    from django.db import models
    _l_(680986)

except ImportError:
    pass

# Create a 'shortcut' function to wrap request in RequestContext()
def render_response(req, *args, **kwargs):
    _l_(680997)

    """Shortcut to wrap request in RequestContext"""
    _n_(680987, "kwargs", lambda: kwargs)['context_instance'] = _c_(680990, _n_(680988, "RequestContext", lambda: RequestContext), _n_(680989, "req", lambda: req))
    _l_(680991)
    aux = _c_(680995, _n_(680992, "render_to_response", lambda: render_to_response), *_n_(680993, "args", lambda: args), **_n_(680994, "kwargs", lambda: kwargs))
    _l_(680996)
    return aux
try:
    import os, sys, urllib, hashlib
    _l_(680999)

except ImportError:
    pass
try:
    import markdown
    _l_(681001)

except ImportError:
    pass
try:
    from markdown.inlinepatterns import ImagePattern, IMAGE_LINK_RE
    _l_(681003)

except ImportError:
    pass
try:
    from P1config.settings import STATICBLOG_COMPILE_DIRECTORY, \
                                STATICBLOG_POST_DIRECTORY, \
                                STATICBLOG_STORAGE
    _l_(681005)

except ImportError:
    pass

###################################################################################

class S3ImagePattern(_n_(681006, "ImagePattern", lambda: ImagePattern)):
    _l_(681116)

    """ Wrapper class to handle image matches in markdown document """

    def handleMatch(self, match):
        _l_(681115)

        node = _c_(681011, _a_(681008, _n_(681007, "ImagePattern", lambda: ImagePattern), "handleMatch"), _n_(681009, "self", lambda: self), _n_(681010, "match", lambda: match))
        _l_(681012)
        # check 'src' to ensure it is local
        src = _c_(681016, _a_(681015, _a_(681014, _n_(681013, "node", lambda: node), "attrib"), "get"), 'src')
        _l_(681017)
        storage_class = _c_(681020, _n_(681018, "get_storage_class", lambda: get_storage_class), _n_(681019, "STATICBLOG_STORAGE", lambda: STATICBLOG_STORAGE))
        _l_(681021)
        storage = _c_(681023, _n_(681022, "storage_class", lambda: storage_class))
        _l_(681024)

        # otherwise we need to do some downloading!
        if 'http://' in _n_(681025, "src", lambda: src) or 'https://' in _n_(681026, "src", lambda: src):
            _l_(681064)

            img_data = _c_(681033, _a_(681032, _c_(681031, _a_(681029, _a_(681028, _n_(681027, "urllib", lambda: urllib), "request"), "urlopen"), _n_(681030, "src", lambda: src)), "read"))
            _l_(681034)
            md5 = _c_(681037, _a_(681036, _n_(681035, "hashlib", lambda: hashlib), "md5"))
            _l_(681038)
            _c_(681042, _a_(681040, _n_(681039, "md5", lambda: md5), "update"), _n_(681041, "img_data", lambda: img_data))
            _l_(681043)
            name = _c_(681046, _a_(681045, _n_(681044, "md5", lambda: md5), "hexdigest")) + '/' + _c_(681051, _a_(681049, _a_(681048, _n_(681047, "os", lambda: os), "path"), "basename"), _n_(681050, "src", lambda: src))
            _l_(681052)
        else:
            with _c_(681056, _n_(681053, "open", lambda: open), _n_(681054, "STATICBLOG_POST_DIRECTORY", lambda: STATICBLOG_POST_DIRECTORY) + _n_(681055, "src", lambda: src)) as fhandle:
                _l_(681061)

                img_data = _c_(681059, _a_(681058, _n_(681057, "fhandle", lambda: fhandle), "read"))
                _l_(681060)
            name = _n_(681062, "src", lambda: src)
            _l_(681063)

        _c_(681069, _n_(681065, "print", lambda: print), 'Uploading ' + _n_(681066, "src", lambda: src), file=_a_(681068, _n_(681067, "sys", lambda: sys), "stderr"))
        _l_(681070)
        try:
            _l_(681112)

            _c_(681077, _a_(681072, _n_(681071, "storage", lambda: storage), "save"), _n_(681073, "name", lambda: name), _c_(681076, _n_(681074, "ContentFile", lambda: ContentFile), _n_(681075, "img_data", lambda: img_data)))
            _l_(681078)
            _a_(681080, _n_(681079, "node", lambda: node), "attrib")['src'] = _c_(681084, _a_(681082, _n_(681081, "storage", lambda: storage), "url"), _n_(681083, "name", lambda: name))
            _l_(681085)
            _c_(681094, _n_(681086, "print", lambda: print), 'Uploaded ' + _n_(681087, "src", lambda: src) + ' to ' + _c_(681091, _a_(681089, _n_(681088, "storage", lambda: storage), "url"), _n_(681090, "name", lambda: name)), file=_a_(681093, _n_(681092, "sys", lambda: sys), "stderr"))
            _l_(681095)
        except _n_(681096, "Exception", lambda: Exception) as e:
            _l_(681111)

            _c_(681103, _n_(681097, "print", lambda: print), _c_(681100, _n_(681098, "str", lambda: str), _n_(681099, "e", lambda: e)), file=_a_(681102, _n_(681101, "sys", lambda: sys), "stderr"))
            _l_(681104)
            _c_(681109, _n_(681105, "print", lambda: print), '\033[01;31mUpload of %s failed\033[0m' % _n_(681106, "src", lambda: src), file=_a_(681108, _n_(681107, "sys", lambda: sys), "stderr"))
            _l_(681110)
        aux = _n_(681113, "node", lambda: node)
        _l_(681114)
        return aux


def render_post(request, post_name):
    _l_(681214)

    """ Render a blog post based on a .post template
    The used template is rendered as html in the folder defined
    by STATICBLOG_COMPILE_DIRECTORY
    """
    content = ""
    _l_(681117)
    mdown = _c_(681120, _a_(681119, _n_(681118, "markdown", lambda: markdown), "Markdown"), extensions = ['meta',])
    _l_(681121)
    _a_(681123, _n_(681122, "mdown", lambda: mdown), "inlinePatterns")['image_link'] = _c_(681127, _n_(681124, "S3ImagePattern", lambda: S3ImagePattern), _n_(681125, "IMAGE_LINK_RE", lambda: IMAGE_LINK_RE), _n_(681126, "mdown", lambda: mdown))
    _l_(681128)
    try:
        _l_(681174)

        post_file_dir = _c_(681134, _a_(681131, _a_(681130, _n_(681129, "os", lambda: os), "path"), "join"), _n_(681132, "STATICBLOG_POST_DIRECTORY", lambda: STATICBLOG_POST_DIRECTORY), _n_(681133, "post_name", lambda: post_name) + '.md')    
        _l_(681135)    
        with _c_(681138, _n_(681136, "open", lambda: open), _n_(681137, "post_file_dir", lambda: post_file_dir), 'r') as pfDIR:
            _l_(681148)

            content = _c_(681141, _a_(681140, _n_(681139, "pfDIR", lambda: pfDIR), "read"))         # opening and reading the ENTIRE '.md' document
            _l_(681142)         # opening and reading the ENTIRE '.md' document
            html = _c_(681146, _a_(681144, _n_(681143, "mdown", lambda: mdown), "convert"), _n_(681145, "content", lambda: content))  # converting file from '.md' to ".html"
            _l_(681147)  # converting file from '.md' to ".html"

    except _n_(681149, "IOError", lambda: IOError) as e:
        _l_(681173)

        _c_(681154, _n_(681150, "print", lambda: print), _c_(681153, _n_(681151, "str", lambda: str), _n_(681152, "e", lambda: e)))
        _l_(681155)
        with _c_(681162, _n_(681156, "open", lambda: open), _c_(681161, _a_(681159, _a_(681158, _n_(681157, "os", lambda: os), "path"), "join"), _n_(681160, "STATICBLOG_POST_DIRECTORY", lambda: STATICBLOG_POST_DIRECTORY), 'preview2.md')) as f:
            _l_(681172)

            content = _c_(681165, _a_(681164, _n_(681163, "f", lambda: f), "read"))
            _l_(681166)
            html = _c_(681170, _a_(681168, _n_(681167, "mdown", lambda: mdown), "convert"), _n_(681169, "content", lambda: content))
            _l_(681171)

    post = { 'content' : _n_(681175, "html", lambda: html), }
    _l_(681176)

    try:
        _l_(681199)

        _n_(681177, "post", lambda: post)['date'] = _a_(681179, _n_(681178, "mdown", lambda: mdown), "Meta")['date'][0]
        _l_(681180)
        _n_(681181, "post", lambda: post)['title'] = _a_(681183, _n_(681182, "mdown", lambda: mdown), "Meta")['title'][0]
        _l_(681184)
        _n_(681185, "post", lambda: post)['author'] = _a_(681187, _n_(681186, "mdown", lambda: mdown), "Meta")['author'][0]
        _l_(681188)
        _n_(681189, "post", lambda: post)['summary'] = _a_(681191, _n_(681190, "mdown", lambda: mdown), "Meta")['summary'][0]
        _l_(681192)
        _n_(681193, "post", lambda: post)['tags'] = _a_(681195, _n_(681194, "mdown", lambda: mdown), "Meta")['tags'][0]
        _l_(681196)
    except:
        _l_(681198)

        pass
        _l_(681197)

    meta = {}
    _l_(681200)
    if 'title' in _n_(681201, "post", lambda: post):
        _l_(681205)

        _n_(681202, "meta", lambda: meta)['title'] = _n_(681203, "post", lambda: post)['title']
        _l_(681204)

    # Context Object containing the post, meta contexes
    context = {'post' : _n_(681206, "post", lambda: post), 'meta' : _n_(681207, "meta", lambda: meta)}
    _l_(681208)
    aux = _c_(681212, _n_(681209, "render_response", lambda: render_response), _n_(681210, "request", lambda: request),
        'post2.html',
        _n_(681211, "context", lambda: context)
    )
    _l_(681213)

    return aux


def archive(request):
    _l_(681303)

    mdown = _c_(681217, _a_(681216, _n_(681215, "markdown", lambda: markdown), "Markdown"), extensions = ['meta',])
    _l_(681218)
    # Create an empty post list for now
    posts = []
    _l_(681219)
    try:
        import string
        _l_(681221)

    except ImportError:
        pass
    # Look at every 'item' in the STATICBLOG_COMPILE_DIRECTORY
    for item in _c_(681225, _a_(681223, _n_(681222, "os", lambda: os), "listdir"), _n_(681224, "STATICBLOG_COMPILE_DIRECTORY", lambda: STATICBLOG_COMPILE_DIRECTORY)):
        _l_(681285)

        # if the 'item' in this directory ends with '.post' (like '.md' in a markdown file, or '.py' in a python file)
        # More specifically, if there is a '.post' file located in this directory...
        if _c_(681228, _a_(681227, _n_(681226, "item", lambda: item), "endswith"), '.md'):
            _l_(681230)

            # ...continue on and...
            continue
            _l_(681229)
        # ...attempt to use that 'item'
        try:
            _l_(681284)

            # ...by opening it, 
            with _c_(681238, _n_(681231, "open", lambda: open), _c_(681237, _a_(681234, _a_(681233, _n_(681232, "os", lambda: os), "path"), "join"), _n_(681235, "STATICBLOG_POST_DIRECTORY", lambda: STATICBLOG_POST_DIRECTORY), _n_(681236, "item", lambda: item) + '.md')) as fhandle:
                _l_(681281)

                # ...reading the markdown file,
                content = _c_(681241, _a_(681240, _n_(681239, "fhandle", lambda: fhandle), "read")) # (opening and reading the ENTIRE '.md' document)
                _l_(681242) # (opening and reading the ENTIRE '.md' document)
                # ...and converting it to HTML.
                _c_(681246, _a_(681244, _n_(681243, "mdown", lambda: mdown), "convert"), _n_(681245, "content", lambda: content))   # (converting file from '.md' to ".html")
                _l_(681247)   # (converting file from '.md' to ".html")

                post = { 'name' : _n_(681248, "item", lambda: item), }
                _l_(681249)
                if 'title' in _a_(681251, _n_(681250, "mdown", lambda: mdown), "Meta") and _c_(681255, _n_(681252, "len", lambda: len), _a_(681254, _n_(681253, "mdown", lambda: mdown), "Meta")['title'][0]) > 0:
                    _l_(681268)

                    # Add the markdown document's 'title' to post[]
                    # This stores the post's title from the "Meta" section of the '.md' document
                    _n_(681256, "post", lambda: post)['title'] = _a_(681258, _n_(681257, "mdown", lambda: mdown), "Meta")['title'][0]
                    _l_(681259)
                # but if that doesnt work...
                else:
                    # Add to the post list the item's Meta 'title', which simply takes \n
                    #   the title of the .md document and removes the '-' from it, so that \n 
                    #   we can make it the post's title.
                    _n_(681260, "post", lambda: post)['title'] = _c_(681266, _a_(681262, _n_(681261, "string", lambda: string), "capwords"), _c_(681265, _a_(681264, _n_(681263, "item", lambda: item), "replace"), '-', ' '))
                    _l_(681267)
                # ...and if there exists a 'date' in the item's meta attribute...
                if 'date' in _a_(681270, _n_(681269, "mdown", lambda: mdown), "Meta"):
                    _l_(681275)

                    # pass the 'date' info found in the Meta attribute to a 'date' \n
                    #   variable created in the post list
                    _n_(681271, "post", lambda: post)['date'] = _a_(681273, _n_(681272, "mdown", lambda: mdown), "Meta")['date'][0]
                    _l_(681274)

                _c_(681279, _a_(681277, _n_(681276, "posts", lambda: posts), "append"), _n_(681278, "post", lambda: post))
                _l_(681280)
        except:
            _l_(681283)

            pass
            _l_(681282)
    try:
        from operator import itemgetter
        _l_(681287)

    except ImportError:
        pass
    posts = _c_(681292, _n_(681288, "sorted", lambda: sorted), _n_(681289, "posts", lambda: posts), key=_c_(681291, _n_(681290, "itemgetter", lambda: itemgetter), 'date'))
    _l_(681293)
    _c_(681296, _a_(681295, _n_(681294, "posts", lambda: posts), "reverse"))
    _l_(681297)
    aux = _c_(681301, _n_(681298, "render_response", lambda: render_response), _n_(681299, "request", lambda: request),
        'archive.html',
        {'posts' : _n_(681300, "posts", lambda: posts)}
    )   
    _l_(681302)   

    return aux   


@_n_(681304, "csrf_exempt", lambda: csrf_exempt)
def handle_hook(request):
    _l_(681316)

    try:
        from django.http import HttpResponse
        _l_(681306)

    except ImportError:
        pass
    try:
        from django.core.management import call_command
        _l_(681308)

    except ImportError:
        pass
    result = _c_(681310, _n_(681309, "call_command", lambda: call_command), 'update_blog', verbosity = 0)
    _l_(681311)
    aux = _c_(681314, _n_(681312, "HttpResponse", lambda: HttpResponse), _n_(681313, "result", lambda: result))
    _l_(681315)
    return aux