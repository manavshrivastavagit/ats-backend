"""
Defines the blueprint for the interview
"""
from flask import Blueprint
from flask_restful import Api

from resources import interviewResource, interviewResourceWithArg, interviewResourceLogin,interviewResourceLogout,interviewResourceUploadFile

interview_BLUEPRINT = Blueprint("interview", __name__)

# Api(interview_BLUEPRINT).add_resource(
#     interviewResource, "/"
# )

Api(interview_BLUEPRINT).add_resource(
    interviewResource, "/v1/interview"
)

Api(interview_BLUEPRINT).add_resource(
    interviewResourceUploadFile, "/v1/upload"
)

Api(interview_BLUEPRINT).add_resource(
    interviewResourceLogin, "/v1/interview/login"
)

Api(interview_BLUEPRINT).add_resource(
    interviewResourceLogout, "/v1/interview/logout"
)

Api(interview_BLUEPRINT).add_resource(
    interviewResourceWithArg, "/v1/interview/<string:last_name>/<string:first_name>"
)

