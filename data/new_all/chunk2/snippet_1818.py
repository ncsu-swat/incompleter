# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/52681646/python-typeerror-nonetype-object-is-not-iterable-but-every-variables-defined
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
if _n_(448366, "slackinput_list", lambda: slackinput_list) and _c_(448369, _n_(448367, "len", lambda: len), _n_(448368, "slackinput_list", lambda: slackinput_list)) > 0:
  _l_(448398)

  user_answer, user_id, channel, event_type = _c_(448372, _n_(448370, "parse_slack_useranswer", lambda: parse_slack_useranswer), _n_(448371, "slackinput_list", lambda: slackinput_list))
  _l_(448373)
  #print(user_answer,user_id)#test
  if _n_(448374, "user_answer", lambda: user_answer) and _n_(448375, "user_id", lambda: user_id) and _n_(448376, "user_id", lambda: user_id) != 'U7GRT34H3' and _n_(448377, "event_type", lambda: event_type)=="message":
    _l_(448397)

    if _n_(448378, "user_answer", lambda: user_answer)=="1" or _n_(448379, "user_answer", lambda: user_answer)=="5":
      _l_(448396)

      _c_(448386, _n_(448380, "print", lambda: print), _n_(448381, "user_answer", lambda: user_answer), _n_(448382, "user_id", lambda: user_id), _n_(448383, "user_count", lambda: user_count), _n_(448384, "total_mood", lambda: total_mood), _n_(448385, "av_mood", lambda: av_mood)) #test
      _l_(448387) #test
      #if user_id not in user_list:
      av_mood, user_count, total_mood = _c_(448394, _n_(448388, "datamood", lambda: datamood), _n_(448389, "user_answer", lambda: user_answer), _n_(448390, "user_id", lambda: user_id), _n_(448391, "user_count", lambda: user_count), _n_(448392, "total_mood", lambda: total_mood), _n_(448393, "av_mood", lambda: av_mood))
      _l_(448395)