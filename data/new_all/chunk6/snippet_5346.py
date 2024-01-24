# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62886434/how-to-resolve-typeerror-a-bytes-like-object-is-required-not-str-in-this
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import json
    _l_(351136)

except ImportError:
    pass
try:
    import csv
    _l_(351138)

except ImportError:
    pass
try:
    import tweepy
    _l_(351140)

except ImportError:
    pass
try:
    import re
    _l_(351142)

except ImportError:
    pass
"""
INPUTS:
    consumer_key, consumer_secret, access_token, access_token_secret: codes 
    telling twitter that we are authorized to access this data
    hashtag_phrase: the combination of hashtags to search for
OUTPUTS:
    none, simply save the tweet info to a spreadsheet
"""
def search_for_hashtags(consumer_key, consumer_secret, access_token, access_token_secret, hashtag_phrase):
    _l_(351212)

    
    #create authentication for accessing Twitter
    auth = _c_(351147, _a_(351144, _n_(351143, "tweepy", lambda: tweepy), "OAuthHandler"), _n_(351145, "consumer_key", lambda: consumer_key), _n_(351146, "consumer_secret", lambda: consumer_secret))
    _l_(351148)
    _c_(351153, _a_(351150, _n_(351149, "auth", lambda: auth), "set_access_token"), _n_(351151, "access_token", lambda: access_token), _n_(351152, "access_token_secret", lambda: access_token_secret))
    _l_(351154)

    #initialize Tweepy API
    api = _c_(351158, _a_(351156, _n_(351155, "tweepy", lambda: tweepy), "API"), _n_(351157, "auth", lambda: auth))
    _l_(351159)
    
    #get the name of the spreadsheet we will write to
    fname = _c_(351165, _a_(351160, '_', "join"), _c_(351164, _a_(351162, _n_(351161, "re", lambda: re), "findall"), r"#(\w+)", _n_(351163, "hashtag_phrase", lambda: hashtag_phrase)))
    _l_(351166)

    #open the spreadsheet we will write to
    with _c_(351169, _n_(351167, "open", lambda: open), '%s.csv' % _n_(351168, "fname", lambda: (fname)), 'wb') as file:
        _l_(351211)


        w = _c_(351173, _a_(351171, _n_(351170, "csv", lambda: csv), "writer"), _n_(351172, "file", lambda: file))
        _l_(351174)

        #write header row to spreadsheet
        _c_(351177, _a_(351176, _n_(351175, "w", lambda: w), "writerow"), ['timestamp', 'tweet_text', 'username', 'all_hashtags', 'followers_count'])
        _l_(351178)

        #for each tweet matching our hashtags, write relevant info to the spreadsheet
        for tweet in _c_(351186, _a_(351185, _c_(351184, _a_(351180, _n_(351179, "tweepy", lambda: tweepy), "Cursor"), _a_(351182, _n_(351181, "api", lambda: api), "search"), q=_n_(351183, "hashtag_phrase", lambda: hashtag_phrase)+' -filter:retweets', \
                                   lang="en", tweet_mode='extended'), "items"), 100):
            _l_(351210)

            _c_(351208, _a_(351188, _n_(351187, "w", lambda: w), "writerow"), [_a_(351190, _n_(351189, "tweet", lambda: tweet), "created_at"), _c_(351196, _a_(351195, _c_(351194, _a_(351193, _a_(351192, _n_(351191, "tweet", lambda: tweet), "full_text"), "replace"), '\n',' '), "encode"), 'utf-8'), _c_(351201, _a_(351200, _a_(351199, _a_(351198, _n_(351197, "tweet", lambda: tweet), "user"), "screen_name"), "encode"), 'utf-8'), [_n_(351202, "e", lambda: e)['text'] for e in _a_(351204, _n_(351203, "tweet", lambda: tweet), "_json")['entities']['hashtags']], _a_(351207, _a_(351206, _n_(351205, "tweet", lambda: tweet), "user"), "followers_count")])
            _l_(351209)
consumer_key = _c_(351214, _n_(351213, "input", lambda: input), 'Consumer Key ')
_l_(351215)
consumer_secret = _c_(351217, _n_(351216, "input", lambda: input), 'Consumer Secret ')
_l_(351218)
access_token = _c_(351220, _n_(351219, "input", lambda: input), 'Access Token ')
_l_(351221)
access_token_secret = _c_(351223, _n_(351222, "input", lambda: input), 'Access Token Secret ')
_l_(351224)
    
hashtag_phrase = _c_(351226, _n_(351225, "input", lambda: input), 'Hashtag Phrase ')
_l_(351227)

if _n_(351228, "__name__", lambda: __name__) == '__main__':
    _l_(351237)

    _c_(351235, _n_(351229, "search_for_hashtags", lambda: search_for_hashtags), _n_(351230, "consumer_key", lambda: consumer_key), _n_(351231, "consumer_secret", lambda: consumer_secret), _n_(351232, "access_token", lambda: access_token), _n_(351233, "access_token_secret", lambda: access_token_secret), _n_(351234, "hashtag_phrase", lambda: hashtag_phrase))
    _l_(351236)