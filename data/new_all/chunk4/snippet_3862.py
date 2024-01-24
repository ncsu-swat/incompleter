# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/66434981/styleframe-row-index-attributeerror-int-object-has-no-attribute-value
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
org_report = _c_(582337, _a_(582333, _a_(582332, _n_(582331, "styleframe", lambda: styleframe), "StyleFrame"), "read_excel"), f'{_a_(582335, _n_(582334, "organisation", lambda: organisation), "type")}{_n_(582336, "TEMPLATE_SUFFIX", lambda: TEMPLATE_SUFFIX)}')
_l_(582338)
report_data = _c_(582341, _n_(582339, 'transform_aws_service_costs_to_excel_rows', lambda: transform_aws_service_costs_to_excel_rows), _n_(582340, 'organisation_costs', lambda: organisation_costs))
_l_(582342)
report_data = _c_(582346, _a_(582344, _n_(582343, 'pandas', lambda: pandas), 'DataFrame'), _n_(582345, 'report_data', lambda: report_data))
_l_(582347)

# Used to make sure the data concatenates properly.
_n_(582348, 'report_data', lambda: report_data).columns = _a_(582350, _n_(582349, 'org_report', lambda: org_report), 'columns')
_l_(582351)


_n_(582352, 'org_report', lambda: org_report).data_df = _c_(582363, _a_(582362, _c_(582361, _n_(582353, 'concat', lambda: concat), [_a_(582356, _a_(582355, _n_(582354, 'org_report', lambda: org_report), 'data_df'), 'iloc')[:4], _n_(582357, 'report_data', lambda: report_data),
                             _a_(582360, _a_(582359, _n_(582358, 'org_report', lambda: org_report), 'data_df'), 'iloc')[5:]], axis=0), 'reset_index'), drop=True)
_l_(582364)

_c_(582372, _a_(582371, _c_(582370, _a_(582366, _n_(582365, 'org_report', lambda: org_report), 'to_excel'), _c_(582369, _n_(582367, 'create_report_name', lambda: create_report_name), _n_(582368, 'organisation', lambda: organisation))), 'save')) # Error occurs here.
_l_(582373) # Error occurs here.