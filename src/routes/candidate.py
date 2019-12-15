"""
Defines the blueprint for the candidate
"""
from flask import Blueprint
from flask_restful import Api

from resources import candidateResource, candidateResourceWithArg, candidateResourceLogin,candidateResourceLogout,candidateResourceUploadFile

candidate_BLUEPRINT = Blueprint("candidate", __name__)

# Api(candidate_BLUEPRINT).add_resource(
#     candidateResource, "/"
# )

Api(candidate_BLUEPRINT).add_resource(
    candidateResource, "/v1/candidate"
)

Api(candidate_BLUEPRINT).add_resource(
    candidateResourceUploadFile, "/v1/upload"
)

Api(candidate_BLUEPRINT).add_resource(
    candidateResourceLogin, "/v1/candidate/login"
)

Api(candidate_BLUEPRINT).add_resource(
    candidateResourceLogout, "/v1/candidate/logout"
)

Api(candidate_BLUEPRINT).add_resource(
    candidateResourceWithArg, "/v1/candidate/<string:last_name>/<string:first_name>"
)

