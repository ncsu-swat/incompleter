# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58575057/update-throwing-typeerror-serializer-update-got-an-unexpected-keyword-argum
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class SMSView(_n_(379897, "APIView", lambda: APIView)):
    _l_(379997)

    """
    This class is responsible for all the method operations of an sms. It provides implementations for the GET, POST, and OPTIONS methods.
    Each method provides it's own description.
    """

    serializer_class = SMSMessagesSerializer
    _l_(379898)

    def get(self, request):
        _l_(379921)

        """
        This method is used to GET all created instance of the SMSMessages class that are saved in the db.
        """
        queryset = _c_(379904, _a_(379901, _a_(379900, _n_(379899, "SMSMessages", lambda: SMSMessages), "objects"), "filter"), sending_user=_a_(379903, _n_(379902, "request", lambda: request), "user"))
        _l_(379905)
        while _n_(379906, "queryset", lambda: queryset):
            _l_(379920)

            aux = _c_(379913, _n_(379907, "Response", lambda: Response), data={
                    _c_(379910, _a_(379909, _n_(379908, "queryset", lambda: queryset), "values"))
                    },
                status=_a_(379912, _n_(379911, "status", lambda: status), "HTTP_200_OK"),
                content_type="application/json"
            )
            _l_(379914)
            return aux
        else:
            aux = _c_(379918, _n_(379915, "Response", lambda: Response), data={
                    "no sms has been sent"
                },
                status=_a_(379917, _n_(379916, "status", lambda: status), "HTTP_404_NOT_FOUND"),
                content_type="application/json"
            )
            _l_(379919)
            return aux

    def post(self, request):
        _l_(379996)

        """
        This method is used to create an instance of the SMSMessages indirectly by using the SMSMessagesSerializer.
        If that is valid it will be passed to the sender() method from the notification.sender module. The serializer
        will be saved, aka the object will be saved to the database, and then the sender() is called. It will run three
        times before it gives up and fails. Once that returns a True value the instance will be called, aka the object
        will be saved to the database, with a delivery_status value of True.
        """
        sms_messages_serializer = _c_(379935, _n_(379922, "SMSMessagesSerializer", lambda: SMSMessagesSerializer), data={
                "sms_number_to": _c_(379926, _a_(379925, _a_(379924, _n_(379923, "request", lambda: request), "data"), "get"), "sms_number_to"),
                "sms_content": _c_(379930, _a_(379929, _a_(379928, _n_(379927, "request", lambda: request), "data"), "get"), "sms_content"),
                "sending_user": _c_(379934, _a_(379933, _a_(379932, _n_(379931, "request", lambda: request), "data"), "get"), "sending_user")
            }
        )
        _l_(379936)
        permission_classes = _a_(379938, _n_(379937, "permissions", lambda: permissions), "IsAuthenticated")
        _l_(379939)

        if _c_(379942, _a_(379941, _n_(379940, "sms_messages_serializer", lambda: sms_messages_serializer), "is_valid")):
            _l_(379952)

            data_to_send = {
                "number": _a_(379944, _n_(379943, "sms_messages_serializer", lambda: sms_messages_serializer), "validated_data")[
                    "sms_number_to"
                ],
                "msg_text": _a_(379946, _n_(379945, "sms_messages_serializer", lambda: sms_messages_serializer), "validated_data")[
                    "sms_content"
                ]
            }
            _l_(379947)
            _c_(379950, _a_(379949, _n_(379948, "sms_messages_serializer", lambda: sms_messages_serializer), "save"))
            _l_(379951)

        # TODO refactor this into it's own function
        max_retry = 0
        _l_(379953)
        resp = _c_(379955, _n_(379954, "Response", lambda: Response))
        _l_(379956)
        while _n_(379957, "max_retry", lambda: max_retry) < 3:
            _l_(379995)

            max_retry += 1
            _l_(379958)
            status_flag, status_response = _c_(379961, _n_(379959, "sender", lambda: sender), _n_(379960, "data_to_send", lambda: data_to_send))
            _l_(379962)
            if not _n_(379963, "status_flag", lambda: status_flag):
                _l_(379987)

                resp = _c_(379969, _n_(379964, "Response", lambda: Response), data={
                        "error": f"{_a_(379966, _n_(379965, 'status_response', lambda: status_response), 'text')}"
                    },
                    status=_a_(379968, _n_(379967, "status_response", lambda: status_response), "status_code"),
                    content_type="application/json"
                )
                _l_(379970)
            else:
                _c_(379973, _a_(379972, _n_(379971, "sms_messages_serializer", lambda: sms_messages_serializer), "update"), data={
                        "delivery_status": True
                    },
                    partial=True
                )
                _l_(379974)
                resp = _c_(379983, _n_(379975, "Response", lambda: Response), data={
                        "success": f"{_c_(379978, _a_(379977, _n_(379976, 'status_response', lambda: status_response), 'json'))}"
                    },
                    headers=_a_(379980, _n_(379979, "status_response", lambda: status_response), "headers"),
                    status=_a_(379982, _n_(379981, "status_response", lambda: status_response), "status_code"),
                    content_type="application/json"
                )
                _l_(379984)
                aux = _n_(379985, "resp", lambda: resp)
                _l_(379986)
                return aux
        else:
            resp = _c_(379991, _n_(379988, "Response", lambda: Response), data={
                    "error": "unable to send sms"
                },
                status=_a_(379990, _n_(379989, "status", lambda: status), "HTTP_500_INTERNAL_SERVER_ERROR"),
                content_type="application/json"
            )
            _l_(379992)
            aux = _n_(379993, "resp", lambda: resp)
            _l_(379994)
            return aux