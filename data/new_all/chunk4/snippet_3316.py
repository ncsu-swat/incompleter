# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75797013/python-invoke-throwing-attributeerror-argument-object-has-no-attribute-pre
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_a_(599686, _n_(599685, "invoke", lambda: invoke), "task")
def prepare_ssm(ctx):
    _l_(599695)

    _c_(599689, _a_(599688, _n_(599687, "invoke", lambda: invoke), "run"), "echo 'Preparing the SSM secret string parameter for the Slack OAuth token'")
    _l_(599690)
    _c_(599693, _a_(599692, _n_(599691, "invoke", lambda: invoke), "run"), """
        cd prepare && \
        npm install && \
        npm run cdk deploy ParameterStack
    """)
    _l_(599694)

@_c_(599710, _a_(599697, _n_(599696, "invoke", lambda: invoke), "task"), _c_(599700, _a_(599699, _n_(599698, "invoke", lambda: invoke), "Argument"), "stage",
                    default="dev",
                    help="Stage of the serverless application",
                    ),
    _c_(599703, _a_(599702, _n_(599701, "invoke", lambda: invoke), "Argument"), "app_name",
                    default="aws-slackbot-py",
                    help="Name of the serverless application",
                    ),
    _c_(599706, _a_(599705, _n_(599704, "invoke", lambda: invoke), "Argument"), "bitbucket_pipeline_client_id",
                    default="",
                    help="Bitbucket OAuth2 client ID",
                    ),
    _c_(599709, _a_(599708, _n_(599707, "invoke", lambda: invoke), "Argument"), "bitbucket_pipeline_auth_url",
                    default="https://bitbucket.org/site/oauth2/access_token",
                    help="Bitbucket OAuth2 access token URL",
                    ),
)
def prepare_bitbucket(ctx, stage, app_name=None, bitbucket_pipeline_client_id=None, bitbucket_pipeline_auth_url=None):
    _l_(599725)

    _c_(599713, _a_(599712, _n_(599711, "invoke", lambda: invoke), "run"), "echo 'Preparing the environment for Bitbucket Pipeline role based access'")
    _l_(599714)
    _c_(599723, _a_(599716, _n_(599715, "invoke", lambda: invoke), "run"), _c_(599722, _a_(599717, """
        SERVERLESS_APP_NAME="{app_name}-{stage}" \
        BITBUCKET_PIPELINE_CLIENT_ID="{bitbucket_pipeline_client_id}" \
        BITBUCKET_PIPELINE_AUTH_URL="{bitbucket_pipeline_auth_url}" \
        cd prepare && \
        npm install && \
        npm run cdk deploy BitbucketIAMStack
    """, "format"), stage=_n_(599718, "stage", lambda: stage),
        app_name=_n_(599719, "app_name", lambda: app_name),
        bitbucket_pipeline_client_id=_n_(599720, "bitbucket_pipeline_client_id", lambda: bitbucket_pipeline_client_id),
        bitbucket_pipeline_auth_url=_n_(599721, "bitbucket_pipeline_auth_url", lambda: bitbucket_pipeline_auth_url)
    ))
    _l_(599724)