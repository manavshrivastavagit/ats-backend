"""
Defines the blueprint for the hr
"""
from flask import Blueprint
from flask_restful import Api

from resources import HRResource, HRResourceWithArg, HRResourceLogin,HRResourceLogout,HRResourceUploadFile

HR_BLUEPRINT = Blueprint("hr", __name__)

# Api(HR_BLUEPRINT).add_resource(
#     HRResource, "/"
# )

Api(HR_BLUEPRINT).add_resource(
    HRResource, "/v1/hr"
)

Api(HR_BLUEPRINT).add_resource(
    HRResourceUploadFile, "/v1/upload"
)

Api(HR_BLUEPRINT).add_resource(
    HRResourceLogin, "/v1/hr/login"
)

Api(HR_BLUEPRINT).add_resource(
    HRResourceLogout, "/v1/hr/logout"
)

Api(HR_BLUEPRINT).add_resource(
    HRResourceWithArg, "/v1/hr/<string:last_name>/<string:first_name>"
)

