# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/68685315/dynamic-serializer-django-rest-attributeerror-serializer-object-has-no-attr
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class UsersSerializer(_a_(436027, _n_(436026, "serializers", lambda: serializers), "ModelSerializer")):
    _l_(436070)

    class Meta:
        _l_(436031)

        model = User
        _l_(436028)
        fields = '__all__'
        _l_(436029)
        extra_kwargs = {'password': {'write_only': True}}
        _l_(436030)


    user_permissions = _c_(436033, _a_(436032, serializers, "SerializerMethodField"), 'get_user_permissions')
    _l_(436034)
    groups = _c_(436036, _a_(436035, serializers, "SerializerMethodField"), 'get_groups')
    _l_(436037)


    def get_user_permissions(self, user):
        _l_(436059)

        _c_(436048, _a_(436039, _n_(436038, "LOGGER", lambda: LOGGER), "info"), _c_(436047, _n_(436040, "list", lambda: list), _c_(436046, _a_(436045, _c_(436044, _a_(436043, _a_(436042, _n_(436041, "user", lambda: user), "user_permissions"), "all")), "values_list"), 'id', flat=True)))
        _l_(436049)
        aux = _c_(436057, _n_(436050, "list", lambda: list), _c_(436056, _a_(436055, _c_(436054, _a_(436053, _a_(436052, _n_(436051, "user", lambda: user), "user_permissions"), "all")), "values_list"), 'id', flat=True))
        _l_(436058)
        return aux


    def get_groups(self, user):
        _l_(436069)

        aux = _c_(436067, _n_(436060, "list", lambda: list), _c_(436066, _a_(436065, _c_(436064, _a_(436063, _a_(436062, _n_(436061, "user", lambda: user), "groups"), "all")), "values_list"), 'id', flat=True))
        _l_(436068)
        return aux


class UsersSerializerGeneralInfo(_a_(436072, _n_(436071, "serializers", lambda: serializers), "ModelSerializer")):
    _l_(436076)

    class Meta:
        _l_(436075)

        model = User
        _l_(436073)
        fields = ['id', 'email', 'username']
        _l_(436074)


class AccessSerializer(_a_(436078, _n_(436077, "serializers", lambda: serializers), "ModelSerializer")):
    _l_(436082)

    class Meta:
        _l_(436081)

        model = Access
        _l_(436079)
        fields = '__all__'
        _l_(436080)


class SNHUserSerializer(_a_(436084, _n_(436083, "serializers", lambda: serializers), "ModelSerializer")):
    _l_(436272)

    class Meta:
        _l_(436087)

        model = SNHUser
        _l_(436085)
        fields = '__all__'
        _l_(436086)


    def __init__(self, *args, **kwargs):
        _l_(436144)

        _c_(436093, _a_(436089, _n_(436088, "super", lambda: super)(), "__init__"), _n_(436090, "self", lambda: self), *_n_(436091, "args", lambda: args), **_n_(436092, "kwargs", lambda: kwargs))
        _l_(436094)
        # If raw, not getting any additional fields
        if not _c_(436098, _a_(436097, _a_(436096, _n_(436095, "self", lambda: self), "context"), "get"), "get_raw", False):
            _l_(436143)

            # Retrieving access if given in context
            if _c_(436102, _a_(436101, _a_(436100, _n_(436099, "self", lambda: self), "context"), "get"), "get_accesses", False):
                _l_(436109)

                _a_(436104, _n_(436103, "self", lambda: self), "fields")['accesses'] = _c_(436107, _a_(436106, _n_(436105, "serializers", lambda: serializers), "SerializerMethodField"))
                _l_(436108)
            # Retrieving all user information if given in context
            if not _c_(436113, _a_(436112, _a_(436111, _n_(436110, "self", lambda: self), "context"), "get"), "get_all_user_informations", False):
                _l_(436124)

                _a_(436115, _n_(436114, "self", lambda: self), "fields")['user'] = _c_(436117, _n_(436116, "UsersSerializer", lambda: UsersSerializer))
                _l_(436118)
            else:
                _a_(436120, _n_(436119, "self", lambda: self), "fields")['user'] = _c_(436122, _n_(436121, "UsersSerializerGeneralInfo", lambda: UsersSerializerGeneralInfo))
                _l_(436123)
            # Additional fields if not raw
            _a_(436126, _n_(436125, "self", lambda: self), "fields")['implants'] = _c_(436129, _a_(436128, _n_(436127, "serializers", lambda: serializers), "SerializerMethodField"))
            _l_(436130)
            _a_(436132, _n_(436131, "self", lambda: self), "fields")['users_clinical_trials'] = _c_(436135, _a_(436134, _n_(436133, "serializers", lambda: serializers), "SerializerMethodField"))
            _l_(436136)
            _a_(436138, _n_(436137, "self", lambda: self), "fields")['implant_patients'] = _c_(436141, _a_(436140, _n_(436139, "serializers", lambda: serializers), "SerializerMethodField"))
            _l_(436142)


    ## Save function
    def save(self, *args, **kwargs):
        _l_(436155)

        _c_(436147, _a_(436146, _n_(436145, "self", lambda: self), "full_clean"))
        _l_(436148)
        aux = _c_(436153, _a_(436150, _n_(436149, "super", lambda: super)(), "save"), *_n_(436151, "args", lambda: args), **_n_(436152, "kwargs", lambda: kwargs))
        _l_(436154)
        return aux


    ## Validation method method used to validate field
    def clean(self):
        _l_(436162)

        _c_(436160, _n_(436156, "validate_password", lambda: validate_password), _a_(436159, _a_(436158, _n_(436157, "self", lambda: self), "user"), "password"))
        _l_(436161)


    def create(self, validated_data):
        _l_(436180)

        # Create first the django user
        user_data = _c_(436165, _a_(436164, _n_(436163, "validated_data", lambda: validated_data), "pop"), 'user')
        _l_(436166)
        user = _c_(436171, _a_(436169, _a_(436168, _n_(436167, "User", lambda: User), "objects"), "create_user"), **_n_(436170, "user_data", lambda: user_data))
        _l_(436172)
        aux = _c_(436178, _a_(436175, _a_(436174, _n_(436173, "SNHUser", lambda: SNHUser), "objects"), "create"), user=_n_(436176, "user", lambda: user), **_n_(436177, "validated_data", lambda: validated_data))
        _l_(436179)
        # Create the layer of profile for the user
        return aux


    def to_representation(self, obj):
        _l_(436188)

        aux = _c_(436186, _a_(436184, _n_(436181, "super", lambda: super)(_n_(436182, "SNHUserSerializer", lambda: SNHUserSerializer), _n_(436183, "self", lambda: self)), "to_representation"), _n_(436185, "obj", lambda: obj))
        _l_(436187)
        return aux


    def get_accesses(self, obj):
        _l_(436209)

        # If context parameter is given, adding accesses
        if _c_(436192, _a_(436191, _a_(436190, _n_(436189, "self", lambda: self), "context"), "get"), "get_accesses", False):
            _l_(436208)

            accesses = _c_(436198, _a_(436195, _a_(436194, _n_(436193, "Access", lambda: Access), "objects"), "filter"), snh_user=_a_(436197, _n_(436196, "obj", lambda: obj), "id"))
            _l_(436199)
            ser = _c_(436202, _n_(436200, "AccessSerializer", lambda: AccessSerializer), _n_(436201, "accesses", lambda: accesses), many=True)
            _l_(436203)
            aux = _a_(436205, _n_(436204, "ser", lambda: ser), "data")
            _l_(436206)
            return aux
        else:
            aux = None
            _l_(436207)
            return aux


    def get_implants(self, obj):
        _l_(436233)

        # If patient, returning implants linked else None
        if _a_(436211, _n_(436210, "obj", lambda: obj), "role") == "Patient":
            _l_(436231)

            try:
                from apps.provisioning.serializers import ImplantSerializer
                _l_(436213)

            except ImportError:
                pass
            try:
                from apps.medicalmanagement.module.implant_patient import get_implants_by_patient
                _l_(436215)

            except ImportError:
                pass
            implants_o = _c_(436218, _n_(436216, "get_implants_by_patient", lambda: get_implants_by_patient), _n_(436217, "obj", lambda: obj))
            _l_(436219)
            if _n_(436220, "implants_o", lambda: implants_o) != []:
                _l_(436230)

                ser = _c_(436223, _n_(436221, "ImplantSerializer", lambda: ImplantSerializer), _n_(436222, "implants_o", lambda: implants_o), many=True)
                _l_(436224)
                aux = _a_(436226, _n_(436225, "ser", lambda: ser), "data")
                _l_(436227)
                return aux
            else:
                aux = _n_(436228, "implants_o", lambda: implants_o)
                _l_(436229)
                return aux
        aux = None
        _l_(436232)
        return aux


    def get_users_clinical_trials(self, obj):
        _l_(436250)

        try:
            from apps.medicalmanagement.models import UserClinicalTrial
            _l_(436235)

        except ImportError:
            pass
        try:
            from apps.medicalmanagement.serializers import UserClinicalTrialSerializer
            _l_(436237)

        except ImportError:
            pass
        try:
            from apps.medicalmanagement.module.user_clinical_trial import get_users_clinical_trials
            _l_(436239)

        except ImportError:
            pass
        users_clinical_trials_o: _n_(436240, "UserClinicalTrial", lambda: UserClinicalTrial) = _c_(436243, _n_(436241, "get_users_clinical_trials", lambda: get_users_clinical_trials), snh_user=_n_(436242, "obj", lambda: obj)
        )
        _l_(436244)
        aux = _a_(436248, _c_(436247, _n_(436245, "UserClinicalTrialSerializer", lambda: UserClinicalTrialSerializer), _n_(436246, "users_clinical_trials_o", lambda: users_clinical_trials_o), many=True), "data")
        _l_(436249)
        return aux


    def get_implant_patients(self, obj):
        _l_(436271)

        # If patient, returning implants patients links else None
        if _a_(436252, _n_(436251, "obj", lambda: obj), "role") == "Patient":
            _l_(436270)

            try:
                from apps.medicalmanagement.models import ImplantPatient
                _l_(436254)

            except ImportError:
                pass
            try:
                from apps.medicalmanagement.serializers import ImplantPatientSerializer
                _l_(436256)

            except ImportError:
                pass
            try:
                from apps.medicalmanagement.module.implant_patient import get_implant_patients
                _l_(436258)

            except ImportError:
                pass
            implant_patient_o: _n_(436259, "ImplantPatient", lambda: ImplantPatient) = _c_(436262, _n_(436260, "get_implant_patients", lambda: get_implant_patients), patient=_n_(436261, "obj", lambda: obj))
            _l_(436263)
            aux = _a_(436267, _c_(436266, _n_(436264, "ImplantPatientSerializer", lambda: ImplantPatientSerializer), _n_(436265, "implant_patient_o", lambda: implant_patient_o), many=True), "data")
            _l_(436268)
            return aux
        else:
            aux = None
            _l_(436269)
            return aux