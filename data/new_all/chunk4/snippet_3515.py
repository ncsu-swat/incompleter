# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/73092421/python-flask-typeerror-int-argument-must-be-a-string-a-bytes-like-object-or
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_a_(644450, _n_(644449, "views", lambda: views), "py")
_l_(644451)
try:
    from app import app
    _l_(644453)

except ImportError:
    pass
try:
    from .models import VotesModel,CandidateModel, UserModel,db
    _l_(644455)

except ImportError:
    pass
try:
    from flask import redirect, render_template, flash,url_for,request
    _l_(644457)

except ImportError:
    pass
try:
    from flask_login import login_required, current_user,logout_user
    _l_(644459)

except ImportError:
    pass
try:
    from flask_cors import cross_origin
    _l_(644461)

except ImportError:
    pass
try:
    import string
    _l_(644463)

except ImportError:
    pass
try:
    import json
    _l_(644465)

except ImportError:
    pass
try:
    import random
    _l_(644467)

except ImportError:
    pass

@_c_(644470, _a_(644469, _n_(644468, "app", lambda: app), "route"), "/")
def index():
    _l_(644474)

    aux = _c_(644472, _n_(644471, "render_template", lambda: render_template), "home.html")
    _l_(644473)
    return aux

@_c_(644477, _a_(644476, _n_(644475, "app", lambda: app), "route"), "/profile")
@_n_(644478, "login_required", lambda: login_required)
def profile():
    _l_(644510)

    prez = _c_(644484, _a_(644483, _c_(644482, _a_(644481, _a_(644480, _n_(644479, "CandidateModel", lambda: CandidateModel), "query"), "filter_by"), post="President"), "all"))
    _l_(644485)
    vice = _c_(644491, _a_(644490, _c_(644489, _a_(644488, _a_(644487, _n_(644486, "CandidateModel", lambda: CandidateModel), "query"), "filter_by"), post="Vice-President"), "all"))
    _l_(644492)
    voter = _c_(644500, _a_(644499, _c_(644498, _a_(644495, _a_(644494, _n_(644493, "VotesModel", lambda: VotesModel), "query"), "filter_by"), roll_num=_a_(644497, _n_(644496, "current_user", lambda: current_user), "roll_num")), "first"))
    _l_(644501)
    aux = _c_(644508, _n_(644502, "render_template", lambda: render_template), "profile.html",name=_a_(644504, _n_(644503, "current_user", lambda: current_user), "name"),prez=_n_(644505, "prez", lambda: prez),vice=_n_(644506, "vice", lambda: vice),voter=_n_(644507, "voter", lambda: voter))
    _l_(644509)
    return aux

@_c_(644513, _a_(644512, _n_(644511, "app", lambda: app), "route"), "/profile", methods=["POST"])
def post_vote():
    _l_(644569)

    president = _c_(644517, _a_(644516, _a_(644515, _n_(644514, "request", lambda: request), "form"), "get"), 'president')
    _l_(644518)
    vicepresident = _c_(644522, _a_(644521, _a_(644520, _n_(644519, "request", lambda: request), "form"), "get"), 'vice-president')
    _l_(644523)

    voted = _c_(644531, _a_(644530, _c_(644529, _a_(644526, _a_(644525, _n_(644524, "VotesModel", lambda: VotesModel), "query"), "filter_by"), roll_num=_a_(644528, _n_(644527, "current_user", lambda: current_user), "roll_num")), "first"))
    _l_(644532)
    if not _n_(644533, "voted", lambda: voted):
        _l_(644568)

        voter = _c_(644545, _n_(644534, "VotesModel", lambda: VotesModel), roll_num=_a_(644536, _n_(644535, "current_user", lambda: current_user), "roll_num"),voter_id=_a_(644538, _n_(644537, "current_user", lambda: current_user), "id"),post_1=_c_(644541, _n_(644539, "int", lambda: int), _n_(644540, "president", lambda: president)),post_2=_c_(644544, _n_(644542, "int", lambda: int), _n_(644543, "vicepresident", lambda: vicepresident)))
        _l_(644546)
        _c_(644551, _a_(644549, _a_(644548, _n_(644547, "db", lambda: db), "session"), "add"), _n_(644550, "voter", lambda: voter))
        _l_(644552)
        _c_(644556, _a_(644555, _a_(644554, _n_(644553, "db", lambda: db), "session"), "commit"))
        _l_(644557)
        aux = _c_(644561, _n_(644558, "redirect", lambda: redirect), _c_(644560, _n_(644559, "url_for", lambda: url_for), 'profile'))
        _l_(644562)
        return aux
    else:
        aux = _c_(644566, _n_(644563, "redirect", lambda: redirect), _c_(644565, _n_(644564, "url_for", lambda: url_for), 'profile'))
        _l_(644567)
        return aux

@_c_(644572, _a_(644571, _n_(644570, "app", lambda: app), "route"), "/candidate")
def candidate():
    _l_(644592)

    prez = _c_(644578, _a_(644577, _c_(644576, _a_(644575, _a_(644574, _n_(644573, "CandidateModel", lambda: CandidateModel), "query"), "filter_by"), post="President"), "all"))
    _l_(644579)
    vice = _c_(644585, _a_(644584, _c_(644583, _a_(644582, _a_(644581, _n_(644580, "CandidateModel", lambda: CandidateModel), "query"), "filter_by"), post="Vice-President"), "all"))
    _l_(644586)
    aux = _c_(644590, _n_(644587, "render_template", lambda: render_template), "candidate.html",prez=_n_(644588, "prez", lambda: prez),vice=_n_(644589, "vice", lambda: vice))
    _l_(644591)
    return aux

@_c_(644595, _a_(644594, _n_(644593, "app", lambda: app), "route"), "/candidate_register")
@_n_(644596, "login_required", lambda: login_required)
def candidate_register():
    _l_(644614)

    if _a_(644598, _n_(644597, "current_user", lambda: current_user), "admin") !=1:
        _l_(644613)

        _c_(644600, _n_(644599, "logout_user", lambda: logout_user))
        _l_(644601)
        _c_(644603, _n_(644602, "flash", lambda: flash), 'You do not have required authorization')
        _l_(644604)
        aux = _c_(644608, _n_(644605, "redirect", lambda: redirect), _c_(644607, _n_(644606, "url_for", lambda: url_for), 'auth.login'))
        _l_(644609)
        return aux
    else:
        aux = _c_(644611, _n_(644610, "render_template", lambda: render_template), "candidate_register.html")
        _l_(644612)
        return aux

@_c_(644617, _a_(644616, _n_(644615, "app", lambda: app), "route"), "/candidate_register", methods=["POST"])
def candidate_post():
    _l_(644775)

    roll_num = _c_(644621, _a_(644620, _a_(644619, _n_(644618, "request", lambda: request), "form"), "get"), 'roll_num')
    _l_(644622)
    first_name = _c_(644626, _a_(644625, _a_(644624, _n_(644623, "request", lambda: request), "form"), "get"), 'first_name')
    _l_(644627)
    last_name = _c_(644631, _a_(644630, _a_(644629, _n_(644628, "request", lambda: request), "form"), "get"), 'last_name')
    _l_(644632)
    batch = _c_(644636, _a_(644635, _a_(644634, _n_(644633, "request", lambda: request), "form"), "get"), 'batch')
    _l_(644637)
    course = _c_(644641, _a_(644640, _a_(644639, _n_(644638, "request", lambda: request), "form"), "get"), 'course')
    _l_(644642)
    department = _c_(644646, _a_(644645, _a_(644644, _n_(644643, "request", lambda: request), "form"), "get"), 'department')
    _l_(644647)
    post = _c_(644651, _a_(644650, _a_(644649, _n_(644648, "request", lambda: request), "form"), "get"), 'post')
    _l_(644652)
    pic_path = _c_(644656, _a_(644655, _a_(644654, _n_(644653, "request", lambda: request), "form"), "get"), 'pic_path')
    _l_(644657)
    agenda = _c_(644661, _a_(644660, _a_(644659, _n_(644658, "request", lambda: request), "form"), "get"), 'agenda')
    _l_(644662)
    
    roll_no = _c_(644669, _a_(644668, _c_(644667, _a_(644665, _a_(644664, _n_(644663, "UserModel", lambda: UserModel), "query"), "filter_by"), roll_num =_n_(644666, "roll_num", lambda: roll_num)), "first"))
    _l_(644670)
    cand = _c_(644677, _a_(644676, _c_(644675, _a_(644673, _a_(644672, _n_(644671, "CandidateModel", lambda: CandidateModel), "query"), "filter_by"), roll_num = _n_(644674, "roll_num", lambda: roll_num)), "first"))
    _l_(644678)

    error = False
    _l_(644679)

    if not 10000000 <= _c_(644682, _n_(644680, "int", lambda: int), _n_(644681, "roll_no", lambda: roll_no)) < 99999999:
        _l_(644687)

        _c_(644684, _n_(644683, "flash", lambda: flash), 'Roll Number is not valid. Should be 8 digits.','error')
        _l_(644685)
        error = True
        _l_(644686)

    if _n_(644688, "cand", lambda: cand):
        _l_(644697)

        _c_(644690, _n_(644689, "flash", lambda: flash), 'Candidate has already been registered.','error')
        _l_(644691)
        aux = _c_(644695, _n_(644692, "redirect", lambda: redirect), _c_(644694, _n_(644693, "url_for", lambda: url_for), 'candidate_register'))
        _l_(644696)
        return aux
    
    if not _c_(644704, _a_(644701, _c_(644700, _n_(644698, "set", lambda: set), _n_(644699, "first_name", lambda: first_name)), "issubset"), _a_(644703, _n_(644702, "string", lambda: string), "ascii_letters") + " "):
        _l_(644709)

        _c_(644706, _n_(644705, "flash", lambda: flash), 'Name can only contain alphabets.','error')
        _l_(644707)
        error = True
        _l_(644708)
    
    if not _c_(644716, _a_(644713, _c_(644712, _n_(644710, "set", lambda: set), _n_(644711, "last_name", lambda: last_name)), "issubset"), _a_(644715, _n_(644714, "string", lambda: string), "ascii_letters") + " "):
        _l_(644721)

        _c_(644718, _n_(644717, "flash", lambda: flash), 'Name can only contain alphabets.','error')
        _l_(644719)
        error = True
        _l_(644720)

    if not _n_(644722, "first_name", lambda: first_name) and not _n_(644723, "last_name", lambda: last_name):
        _l_(644728)

        _c_(644725, _n_(644724, "flash", lambda: flash), 'Name cannot be left blank.','error')
        _l_(644726)
        error = True
        _l_(644727)

    if not _n_(644729, "batch", lambda: batch) and not _n_(644730, "course", lambda: course) and not _n_(644731, "department", lambda: department):
        _l_(644736)

        _c_(644733, _n_(644732, "flash", lambda: flash), 'Please fill in all the details. Batch, Course and Department information is neccessary.','error')
        _l_(644734)
        error = True
        _l_(644735)
    
    if _n_(644737, "error", lambda: error):
        _l_(644774)

        aux = _c_(644741, _n_(644738, "redirect", lambda: redirect), _c_(644740, _n_(644739, "url_for", lambda: url_for), 'candidate_register'))
        _l_(644742)
        return aux
    else:
        candidate = _c_(644753, _n_(644743, "CandidateModel", lambda: CandidateModel), roll_num=_n_(644744, "roll_num", lambda: roll_num), first_name=_n_(644745, "first_name", lambda: first_name),last_name=_n_(644746, "last_name", lambda: last_name),batch=_n_(644747, "batch", lambda: batch),course=_n_(644748, "course", lambda: course),department=_n_(644749, "department", lambda: department),post=_n_(644750, "post", lambda: post),pic_path=_n_(644751, "pic_path", lambda: pic_path),agenda=_n_(644752, "agenda", lambda: agenda))
        _l_(644754)
        _c_(644759, _a_(644757, _a_(644756, _n_(644755, "db", lambda: db), "session"), "add"), _n_(644758, "candidate", lambda: candidate))
        _l_(644760)
        _c_(644764, _a_(644763, _a_(644762, _n_(644761, "db", lambda: db), "session"), "commit"))
        _l_(644765)
        _c_(644767, _n_(644766, "flash", lambda: flash), 'Candidate successfully registered.','success')
        _l_(644768)
        aux = _c_(644772, _n_(644769, "redirect", lambda: redirect), _c_(644771, _n_(644770, "url_for", lambda: url_for), 'candidate_register'))
        _l_(644773)
        return aux

@_c_(644778, _a_(644777, _n_(644776, "app", lambda: app), "route"), "/live_result")
def live_result():
    _l_(644860)

    prez = _c_(644784, _a_(644783, _c_(644782, _a_(644781, _a_(644780, _n_(644779, "CandidateModel", lambda: CandidateModel), "query"), "filter_by"), post="President"), "all"))
    _l_(644785)
    vice = _c_(644791, _a_(644790, _c_(644789, _a_(644788, _a_(644787, _n_(644786, "CandidateModel", lambda: CandidateModel), "query"), "filter_by"), post="Vice-President"), "all"))
    _l_(644792)
    labels=[]
    _l_(644793)
    data=[]
    _l_(644794)
    labels1=[]
    _l_(644795)
    data1=[]
    _l_(644796)
    for candidate in _n_(644797, "prez", lambda: prez):
        _l_(644824)

        name = _a_(644799, _n_(644798, "candidate", lambda: candidate), "first_name")+" "+_a_(644801, _n_(644800, "candidate", lambda: candidate), "last_name")
        _l_(644802)
        _c_(644806, _a_(644804, _n_(644803, "labels", lambda: labels), "append"), _n_(644805, "name", lambda: name))
        _l_(644807)
        vote=_c_(644817, _a_(644816, _c_(644815, _a_(644810, _a_(644809, _n_(644808, "VotesModel", lambda: VotesModel), "query"), "filter"), _a_(644812, _n_(644811, "VotesModel", lambda: VotesModel), "post_1")==_a_(644814, _n_(644813, "candidate", lambda: candidate), "roll_num")), "count"))
        _l_(644818)
        _c_(644822, _a_(644820, _n_(644819, "data", lambda: data), "append"), _n_(644821, "vote", lambda: vote))
        _l_(644823)
    for candidate in _n_(644825, "vice", lambda: vice):
        _l_(644852)

        name = _a_(644827, _n_(644826, "candidate", lambda: candidate), "first_name")+" "+_a_(644829, _n_(644828, "candidate", lambda: candidate), "last_name")
        _l_(644830)
        _c_(644834, _a_(644832, _n_(644831, "labels1", lambda: labels1), "append"), _n_(644833, "name", lambda: name))
        _l_(644835)
        vote=_c_(644845, _a_(644844, _c_(644843, _a_(644838, _a_(644837, _n_(644836, "VotesModel", lambda: VotesModel), "query"), "filter"), _a_(644840, _n_(644839, "VotesModel", lambda: VotesModel), "post_2")==_a_(644842, _n_(644841, "candidate", lambda: candidate), "roll_num")), "count"))
        _l_(644846)
        _c_(644850, _a_(644848, _n_(644847, "data1", lambda: data1), "append"), _n_(644849, "vote", lambda: vote))
        _l_(644851)
    aux = _c_(644858, _n_(644853, "render_template", lambda: render_template), 'graph.html',labels=_n_(644854, "labels", lambda: labels),data=_n_(644855, "data", lambda: data),labels1=_n_(644856, "labels1", lambda: labels1),data1=_n_(644857, "data1", lambda: data1))
    _l_(644859)
 
    return aux


@_c_(644863, _a_(644862, _n_(644861, "app", lambda: app), "route"), "/vote/count")
@_c_(644865, _n_(644864, "cross_origin", lambda: cross_origin))
def voteCount():
    _l_(644955)

    prez = _c_(644871, _a_(644870, _c_(644869, _a_(644868, _a_(644867, _n_(644866, "CandidateModel", lambda: CandidateModel), "query"), "filter_by"), post="President"), "all"))
    _l_(644872)
    vice = _c_(644878, _a_(644877, _c_(644876, _a_(644875, _a_(644874, _n_(644873, "CandidateModel", lambda: CandidateModel), "query"), "filter_by"), post="Vice-President"), "all"))
    _l_(644879)
    labels=[]
    _l_(644880)
    data=[]
    _l_(644881)
    labels1=[]
    _l_(644882)
    data1=[]
    _l_(644883)
    for candidate in _n_(644884, "prez", lambda: prez):
        _l_(644911)

        name = _a_(644886, _n_(644885, "candidate", lambda: candidate), "first_name")+" "+_a_(644888, _n_(644887, "candidate", lambda: candidate), "last_name")
        _l_(644889)
        _c_(644893, _a_(644891, _n_(644890, "labels", lambda: labels), "append"), _n_(644892, "name", lambda: name))
        _l_(644894)
        vote=_c_(644904, _a_(644903, _c_(644902, _a_(644897, _a_(644896, _n_(644895, "VotesModel", lambda: VotesModel), "query"), "filter"), _a_(644899, _n_(644898, "VotesModel", lambda: VotesModel), "post_1")==_a_(644901, _n_(644900, "candidate", lambda: candidate), "roll_num")), "count"))
        _l_(644905)
        _c_(644909, _a_(644907, _n_(644906, "data", lambda: data), "append"), _n_(644908, "vote", lambda: vote))
        _l_(644910)
    for candidate in _n_(644912, "vice", lambda: vice):
        _l_(644939)

        name = _a_(644914, _n_(644913, "candidate", lambda: candidate), "first_name")+" "+_a_(644916, _n_(644915, "candidate", lambda: candidate), "last_name")
        _l_(644917)
        _c_(644921, _a_(644919, _n_(644918, "labels1", lambda: labels1), "append"), _n_(644920, "name", lambda: name))
        _l_(644922)
        vote=_c_(644932, _a_(644931, _c_(644930, _a_(644925, _a_(644924, _n_(644923, "VotesModel", lambda: VotesModel), "query"), "filter"), _a_(644927, _n_(644926, "VotesModel", lambda: VotesModel), "post_2")==_a_(644929, _n_(644928, "candidate", lambda: candidate), "roll_num")), "count"))
        _l_(644933)
        _c_(644937, _a_(644935, _n_(644934, "data1", lambda: data1), "append"), _n_(644936, "vote", lambda: vote))
        _l_(644938)

    output = {"data": _n_(644940, "data", lambda: data),
            "labels": _n_(644941, "labels", lambda: labels),
            "data1": _n_(644942, "data1", lambda: data1),
            "labels1": _n_(644943, "labels1", lambda: labels1)}
    _l_(644944)
    response = _c_(644951, _a_(644946, _n_(644945, "app", lambda: app), "response_class"), response=_c_(644950, _a_(644948, _n_(644947, "json", lambda: json), "dumps"), _n_(644949, "output", lambda: output)),
        status=200,
        mimetype='application/json'
    )
    _l_(644952)
    aux = _n_(644953, "response", lambda: response)
    _l_(644954)
    return aux