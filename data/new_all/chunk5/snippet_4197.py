# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61782444/using-praw-to-scrape-a-list-of-subreddits-typeerror-subreddit-object-is-not
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
subs= ["sub1","sub2", "sub3", "sub4"]
_l_(648518)

commentsDict = {"comment_user": [], "comment_text":[], "comment_score":[], "comment_date":[] }
_l_(648519)
postsDict = {"post_title" : [], "post_score" : [], "post_comments_num":[], "post_date":[], \
                "post_user":[], "post_text":[], "post_id":[]}
_l_(648520)

for i in _c_(648525, _n_(648521, "range", lambda: range), _c_(648524, _n_(648522, "len", lambda: len), _n_(648523, "subs", lambda: subs))):
    _l_(648642)

    for submission in _c_(648530, _a_(648527, _n_(648526, "reddit", lambda: reddit), "subreddit"), _n_(648528, "subs", lambda: subs)[_n_(648529, "i", lambda: i)]):
        _l_(648641)

        _n_(648531, "submission", lambda: submission).comment_sort = 'new'
        _l_(648532)
        comments = _c_(648536, _n_(648533, "list", lambda: list), _a_(648535, _n_(648534, "submission", lambda: submission), "comments"))
        _l_(648537)
        for comments in _a_(648539, _n_(648538, "submission", lambda: submission), "comments"):
            _l_(648640)

            _c_(648544, _a_(648541, _n_(648540, "postsDict", lambda: postsDict)["post_title"], "append"), _a_(648543, _n_(648542, "submission", lambda: submission), "title"))#title of post with comment
            _l_(648545)#title of post with comment
            _c_(648550, _a_(648547, _n_(648546, "postsDict", lambda: postsDict)["post_score"], "append"), _a_(648549, _n_(648548, "submission", lambda: submission), "score"))#upvotes-downvotes
            _l_(648551)#upvotes-downvotes
            _c_(648556, _a_(648553, _n_(648552, "postsDict", lambda: postsDict)["post_text"], "append"), _a_(648555, _n_(648554, "submission", lambda: submission), "selftext"))#get body of post
            _l_(648557)#get body of post
            _c_(648562, _a_(648559, _n_(648558, "postsDict", lambda: postsDict)["post_id"], "append"), _a_(648561, _n_(648560, "submission", lambda: submission), "id"))#unique id address for post
            _l_(648563)#unique id address for post
            _c_(648568, _a_(648565, _n_(648564, "postsDict", lambda: postsDict)["post_user"], "append"), _a_(648567, _n_(648566, "submission", lambda: submission), "author"))  #user name of poster
            _l_(648569)  #user name of poster
            _c_(648574, _a_(648571, _n_(648570, "postsDict", lambda: postsDict)["post_comments_num"], "append"), _a_(648573, _n_(648572, "submission", lambda: submission), "num_comments")) #number of comments on post
            _l_(648575) #number of comments on post
            date = _a_(648577, _n_(648576, "submission", lambda: submission), "created_utc")                                  #create variable for date
            _l_(648578)                                  #create variable for date
            timestamp = _c_(648583, _a_(648581, _a_(648580, _n_(648579, "datetime", lambda: datetime), "datetime"), "fromtimestamp"), _n_(648582, "date", lambda: date))              #create variable to translate unix date 
            _l_(648584)              #create variable to translate unix date 
            _c_(648590, _a_(648586, _n_(648585, "postsDict", lambda: postsDict)["post_date"], "append"), _c_(648589, _a_(648588, _n_(648587, "timestamp", lambda: timestamp), "strftime"), '%Y-%m-%D %H:%M:%S')) #extract date and add to dict
            _l_(648591) #extract date and add to dict
            for top_level_comment in _a_(648593, _n_(648592, "submission", lambda: submission), "comments"):
                _l_(648600)

                if _c_(648597, _n_(648594, "isinstance", lambda: isinstance), _n_(648595, "top_level_comment", lambda: top_level_comment), _n_(648596, "MoreComments", lambda: MoreComments)):
                    _l_(648599)

                    continue
                    _l_(648598)
            _c_(648604, _a_(648603, _a_(648602, _n_(648601, "submission", lambda: submission), "comments"), "replace_more"), limit=None)                   #tell Praw to click more comments and get those too
            _l_(648605)                   #tell Praw to click more comments and get those too
            _c_(648610, _a_(648607, _n_(648606, "commentsDict", lambda: commentsDict)["comment_user"], "append"), _a_(648609, _n_(648608, "comments", lambda: comments), "author"))              #get comment username
            _l_(648611)              #get comment username
            _c_(648616, _a_(648613, _n_(648612, "commentsDict", lambda: commentsDict)["comment_score"], "append"), _a_(648615, _n_(648614, "comments", lambda: comments), "score"))            #comment upvotes-downvotes
            _l_(648617)            #comment upvotes-downvotes
            date = _a_(648619, _n_(648618, "comments", lambda: comments), "created")                                         #same date as above but for comments
            _l_(648620)                                         #same date as above but for comments
            timestamp = _c_(648625, _a_(648623, _a_(648622, _n_(648621, "datetime", lambda: datetime), "datetime"), "fromtimestamp"), _n_(648624, "date", lambda: date))
            _l_(648626)
            _c_(648632, _a_(648628, _n_(648627, "commentsDict", lambda: commentsDict)["comment_date"], "append"), _c_(648631, _a_(648630, _n_(648629, "timestamp", lambda: timestamp), "strftime"), '%Y-%m-%D %H:%M:%S')) #add translated unix date to dict
            _l_(648633) #add translated unix date to dict
            _c_(648638, _a_(648635, _n_(648634, "commentsDict", lambda: commentsDict)["comment_text"], "append"), _a_(648637, _n_(648636, "comments", lambda: comments), "body"))      #get comment text 
            _l_(648639)      #get comment text 