# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/68443649/attributeerror-object-has-no-attribute-task-id-when-using-celery
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_c_(591184, _a_(591183, _n_(591182, "app", lambda: app), "task"), ignore_result=True, name='pydolphin.dolphin.tasks.tasks')
def pull_channel_impl(channel_id, level):
    _l_(591206)

    _c_(591189, _n_(591185, "print", lambda: print), _a_(591188, _a_(591187, _n_(591186, "app", lambda: app), "current_task"), "task_id"))
    _l_(591190)
    rss = _c_(591192, _n_(591191, "RssSource", lambda: RssSource))
    _l_(591193)
    source = _c_(591197, _a_(591195, _n_(591194, "rss", lambda: rss), "select_channel_by_id"), _n_(591196, "channel_id", lambda: channel_id))
    _l_(591198)
    _c_(591204, _a_(591200, _n_(591199, "RssPullImpl", lambda: RssPullImpl), "single_rss_hub"), _n_(591201, "source", lambda: source), _n_(591202, "rss", lambda: rss), _n_(591203, "level", lambda: level))
    _l_(591205)