# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58575057/update-throwing-typeerror-serializer-update-got-an-unexpected-keyword-argum
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class SMSMessagesSerializer(_a_(396351, _n_(396350, "serializers", lambda: serializers), "ModelSerializer")):
    _l_(396373)

    """
    A class for serializing the SMSMessages model's data. It sub-classes the
    ModelSerializer class from serializer's module.
    """

    class Meta:
        _l_(396372)

        model = SMSMessages
        _l_(396352)
        fields = '__all__'
        _l_(396353)

        def update(self, instance, validated_data):
            _l_(396371)

            """
            This method is used to update an instance of the SMSMessages's delivery_status attribute.
            It get's the value for delivery_status from the input parameter, updates the specific instance
            of the SMSMessagesSerializer, saves that instance and returns it.
            """
            instance = _c_(396356, _a_(396355, _n_(396354, "self", lambda: self), "get_object"))
            _l_(396357)
            _n_(396358, "instance", lambda: instance).delivery_status = _c_(396363, _a_(396360, _n_(396359, "validated_data", lambda: validated_data), "get"), 'delivery_status', _a_(396362, _n_(396361, "instance", lambda: instance), "delivery_status"))
            _l_(396364)
            _c_(396367, _a_(396366, _n_(396365, "instance", lambda: instance), "save"))
            _l_(396368)
            aux = _n_(396369, "instance", lambda: instance)
            _l_(396370)
            return aux