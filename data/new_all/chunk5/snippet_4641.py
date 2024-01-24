# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53848930/how-can-i-resolve-this-error-typeerror-nonetype-object-is-not-callable
#This is the model that stores the tender.
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Tender(_a_(666329, _n_(666328, "models", lambda: models), "Model")):
    _l_(666387)

    tenderCategory = _c_(666331, _a_(666330, models, "ManyToManyField"), Category, blank=False)       #this field holds the tender category, e.g. construction, engineering, human resources etc.
    _l_(666332)       #this field holds the tender category, e.g. construction, engineering, human resources etc.
    tenderProvince = _c_(666334, _a_(666333, models, "ManyToManyField"), Province, blank=False)       #this is the province the tender was advertised from.
    _l_(666335)       #this is the province the tender was advertised from.
    buyersName = _c_(666337, _a_(666336, models, "CharField"), max_length=100)   #this is the name of the Buyer e.g. Dept. of Transport, Transnet, Dept of Agriculture etc.
    _l_(666338)   #this is the name of the Buyer e.g. Dept. of Transport, Transnet, Dept of Agriculture etc.
    summary = _c_(666340, _a_(666339, models, "TextField"), blank=False)      #this is the tender title as per the Buyer.
    _l_(666341)      #this is the tender title as per the Buyer.
    refNum = _c_(666343, _a_(666342, models, "CharField"), max_length=100)    #tender ref number as per the Buyer.
    _l_(666344)    #tender ref number as per the Buyer.
    issueDate = _c_(666346, _a_(666345, models, "DateTimeField"), blank=True, null=True)     #date the tender was published
    _l_(666347)     #date the tender was published
    closingDate = _c_(666350, _a_(666348, models, "DateTimeField"), default=_a_(666349, timezone, "now"), blank=True, null=True)   #tender closing date
    _l_(666351)   #tender closing date
    siteInspectionDate = _c_(666353, _a_(666352, models, "DateTimeField"), blank=True, null=True)
    _l_(666354)
    siteInspection = _c_(666355, RichTextField, blank=True, null=True)     #site inspection date, if any
    _l_(666356)     #site inspection date, if any
    enquiries = _c_(666357, RichTextField, blank=True, null=True) #this field stores details of the contact person, for the tender.
    _l_(666358) #this field stores details of the contact person, for the tender.
    description = _c_(666359, RichTextField, blank=True, null=True)   #this is the body of the tender. the tender details are captured here.
    _l_(666360)   #this is the body of the tender. the tender details are captured here.
    assigned_keywords = _c_(666362, _a_(666361, models, "ManyToManyField"), Keywords, blank=True)
    _l_(666363)
    matched = _c_(666365, _a_(666364, models, "BooleanField"), default=False, blank=False)
    _l_(666366)
    capture_date = _c_(666369, _a_(666367, models, "DateField"), default=_a_(666368, timezone, "now"), blank=False, null=False)
    _l_(666370)
    date_assigned = _c_(666372, _a_(666371, models, "DateField"), blank=True, null=True)
    _l_(666373)
    tDocLinks = _c_(666374, RichTextField, blank=True)
    _l_(666375)

    def check_if_expired(self):
        _l_(666384)

        if _a_(666377, _n_(666376, "self", lambda: self), "closingDate") < _c_(666380, _a_(666379, _n_(666378, "timezone", lambda: timezone), "now")):
            _l_(666383)

            aux = True
            _l_(666381)
            return aux
        else:
            aux = False
            _l_(666382)
            return aux

    class Meta:
        _l_(666386)

        ordering = ['-closingDate']
        _l_(666385)