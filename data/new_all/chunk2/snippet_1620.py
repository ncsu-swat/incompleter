# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/69744733/attributeerror-wsgirequest-object-has-no-attribute-get-heroku
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class PostSerializer(_a_(429466, _n_(429465, "serializers", lambda: serializers), "ModelSerializer")):
    _l_(429589)

    """Post Serializer"""
    owner = _c_(429467, UserProfile, read_only=True)
    _l_(429468)
    tags = _c_(429469, TagSerializer, many=True)
    _l_(429470)
    comments = _c_(429471, CommentSerializer, many=True, read_only=True)
    _l_(429472)
    slug = _c_(429474, _a_(429473, serializers, "SlugField"), read_only=True)
    _l_(429475)

    class Meta:
        _l_(429478)

        model = Post
        _l_(429476)
        fields = ('id', 'title', 'body', 'owner', 'slug',
                  'comments', 'tags', 'description', 'image', 'bookmarks',
                  'created', 'modified', 'blog_views', 'blog_likes',
                  'read_time',)
        _l_(429477)

    def create(self, validated_data):
        _l_(429529)

        """Create a blog post in a customized way."""
        tags = _c_(429481, _a_(429480, _n_(429479, "validated_data", lambda: validated_data), "pop"), 'tags', [])
        _l_(429482)
        post = _c_(429490, _a_(429485, _a_(429484, _n_(429483, "Post", lambda: Post), "objects"), "create"), **_n_(429486, "validated_data", lambda: validated_data),
                                   owner=_a_(429489, _a_(429488, _n_(429487, "self", lambda: self), "context"), "user"))
        _l_(429491)
        for tag in _n_(429492, "tags", lambda: tags):
            _l_(429526)

            tag_qs = _c_(429499, _a_(429495, _a_(429494, _n_(429493, "Tag", lambda: Tag), "objects"), "filter"), name__iexact=_c_(429498, _a_(429497, _n_(429496, "tag", lambda: tag), "get"), 'name'))
            _l_(429500)
            if _c_(429503, _a_(429502, _n_(429501, "tag_qs", lambda: tag_qs), "exists")):
                _l_(429519)

                tag_obj = _c_(429506, _a_(429505, _n_(429504, "tag_qs", lambda: tag_qs), "first"))
                _l_(429507)
            else:
                tag_obj = _c_(429517, _a_(429510, _a_(429509, _n_(429508, "Tag", lambda: Tag), "objects"), "create"), name=_c_(429513, _a_(429512, _n_(429511, "tag", lambda: tag), "get"), 'name'),
                    owner=_a_(429516, _a_(429515, _n_(429514, "self", lambda: self), "context"), "user"), )
                _l_(429518)
            _c_(429524, _a_(429522, _a_(429521, _n_(429520, "post", lambda: post), "tags"), "add"), _n_(429523, "tag_obj", lambda: tag_obj))
            _l_(429525)
        aux = _n_(429527, "post", lambda: post)
        _l_(429528)

        return aux

    def update(self, instance, validated_data):
        _l_(429588)

        """Update blog posts."""
        tags = _c_(429532, _a_(429531, _n_(429530, "validated_data", lambda: validated_data), "pop"), 'tags', [])
        _l_(429533)
        instance = _c_(429540, _a_(429537, _n_(429534, "super", lambda: super)(_n_(429535, "PostSerializer", lambda: PostSerializer), _n_(429536, "self", lambda: self)), "update"), _n_(429538, "instance", lambda: instance), _n_(429539, "validated_data", lambda: validated_data))
        _l_(429541)

        if _c_(429544, _n_(429542, "len", lambda: len), _n_(429543, "tags", lambda: tags)):
            _l_(429585)

            for tag in _n_(429545, "tags", lambda: tags):
                _l_(429584)

                tag_qs = _c_(429552, _a_(429548, _a_(429547, _n_(429546, "Tag", lambda: Tag), "objects"), "filter"), name__iexact=_c_(429551, _a_(429550, _n_(429549, "tag", lambda: tag), "get"), 'name'))
                _l_(429553)
                if _c_(429556, _a_(429555, _n_(429554, "tag_qs", lambda: tag_qs), "exists")):
                    _l_(429572)

                    tag = _c_(429559, _a_(429558, _n_(429557, "tag_qs", lambda: tag_qs), "first"))
                    _l_(429560)
                else:
                    tag = _c_(429570, _a_(429563, _a_(429562, _n_(429561, "Tag", lambda: Tag), "objects"), "create"), name=_c_(429566, _a_(429565, _n_(429564, "tag", lambda: tag), "get"), 'name'),
                                             owner=_a_(429569, _a_(429568, _n_(429567, "self", lambda: self), "context"), "user"), )
                    _l_(429571)
                _c_(429576, _a_(429575, _a_(429574, _n_(429573, "instance", lambda: instance), "tags"), "clear"))
                _l_(429577)
                _c_(429582, _a_(429580, _a_(429579, _n_(429578, "instance", lambda: instance), "tags"), "add"), _n_(429581, "tag", lambda: tag))
                _l_(429583)
        aux = _n_(429586, "instance", lambda: instance)
        _l_(429587)

        return aux