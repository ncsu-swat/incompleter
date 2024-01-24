# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53848930/how-can-i-resolve-this-error-typeerror-nonetype-object-is-not-callable
#This is the model that stores the tender.
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Tender(_a_(670568, _n_(670567, "models", lambda: models), "Model")):
    _l_(670626)

    tenderCategory = _c_(670570, _a_(670569, models, "ManyToManyField"), Category, blank=False)       #this field holds the tender category, e.g. construction, engineering, human resources etc.
    _l_(670571)       #this field holds the tender category, e.g. construction, engineering, human resources etc.
    tenderProvince = _c_(670573, _a_(670572, models, "ManyToManyField"), Province, blank=False)       #this is the province the tender was advertised from.
    _l_(670574)       #this is the province the tender was advertised from.
    buyersName = _c_(670576, _a_(670575, models, "CharField"), max_length=100)   #this is the name of the Buyer e.g. Dept. of Transport, Transnet, Dept of Agriculture etc.
    _l_(670577)   #this is the name of the Buyer e.g. Dept. of Transport, Transnet, Dept of Agriculture etc.
    summary = _c_(670579, _a_(670578, models, "TextField"), blank=False)      #this is the tender title as per the Buyer.
    _l_(670580)      #this is the tender title as per the Buyer.
    refNum = _c_(670582, _a_(670581, models, "CharField"), max_length=100)    #tender ref number as per the Buyer.
    _l_(670583)    #tender ref number as per the Buyer.
    issueDate = _c_(670585, _a_(670584, models, "DateTimeField"), blank=True, null=True)     #date the tender was published
    _l_(670586)     #date the tender was published
    closingDate = _c_(670589, _a_(670587, models, "DateTimeField"), default=_a_(670588, timezone, "now"), blank=True, null=True)   #tender closing date
    _l_(670590)   #tender closing date
    siteInspectionDate = _c_(670592, _a_(670591, models, "DateTimeField"), blank=True, null=True)
    _l_(670593)
    siteInspection = _c_(670594, RichTextField, blank=True, null=True)     #site inspection date, if any
    _l_(670595)     #site inspection date, if any
    enquiries = _c_(670596, RichTextField, blank=True, null=True) #this field stores details of the contact person, for the tender.
    _l_(670597) #this field stores details of the contact person, for the tender.
    description = _c_(670598, RichTextField, blank=True, null=True)   #this is the body of the tender. the tender details are captured here.
    _l_(670599)   #this is the body of the tender. the tender details are captured here.
    assigned_keywords = _c_(670601, _a_(670600, models, "ManyToManyField"), Keywords, blank=True)
    _l_(670602)
    matched = _c_(670604, _a_(670603, models, "BooleanField"), default=False, blank=False)
    _l_(670605)
    capture_date = _c_(670608, _a_(670606, models, "DateField"), default=_a_(670607, timezone, "now"), blank=False, null=False)
    _l_(670609)
    date_assigned = _c_(670611, _a_(670610, models, "DateField"), blank=True, null=True)
    _l_(670612)
    tDocLinks = _c_(670613, RichTextField, blank=True)
    _l_(670614)

    def check_if_expired(self):
        _l_(670623)

        if _a_(670616, _n_(670615, "self", lambda: self), "closingDate") < _c_(670619, _a_(670618, _n_(670617, "timezone", lambda: timezone), "now")):
            _l_(670622)

            aux = True
            _l_(670620)
            return aux
        else:
            aux = False
            _l_(670621)
            return aux

    class Meta:
        _l_(670625)

        ordering = ['-closingDate']
        _l_(670624)