"""
Defines the blueprint for the interviewer
"""
from flask import Blueprint
from flask_restful import Api

from resources import interviewerResource, interviewerResourceWithArg, interviewerResourceLogin,interviewerResourceLogout,interviewerResourceUploadFile

interviewer_BLUEPRINT = Blueprint("interviewer", __name__)

# Api(interviewer_BLUEPRINT).add_resource(
#     interviewerResource, "/"
# )

Api(interviewer_BLUEPRINT).add_resource(
    interviewerResource, "/v1/interviewer"
)

Api(interviewer_BLUEPRINT).add_resource(
    interviewerResourceUploadFile, "/v1/upload"
)

Api(interviewer_BLUEPRINT).add_resource(
    interviewerResourceLogin, "/v1/interviewer/login"
)

Api(interviewer_BLUEPRINT).add_resource(
    interviewerResourceLogout, "/v1/interviewer/logout"
)

Api(interviewer_BLUEPRINT).add_resource(
    interviewerResourceWithArg, "/v1/interviewer/<string:last_name>/<string:first_name>"
)

