"""
Define the REST verbs relative to the hr
"""

from flasgger import swag_from
from flask.json import jsonify
from flask_restful import Resource
from flask_restful.reqparse import Argument

from repositories import HRRepository
from util import parse_params

# logger
# from server import server
import json
from flask import make_response


class HRResource(Resource):
    """ Verbs relative to the hr """

    @staticmethod
    @parse_params(
        Argument("id", location="json", required=True, help="Require id of the hr.")
    )
    @swag_from("../swagger/hr/DELETE.yml")
    def delete(id):
        """ delete an hr based on the sent information """
        repository = HRRepository()
        hr = repository.delete(id=id)
        return jsonify(hr)

    @staticmethod
    @parse_params(
        Argument("first_name", location="json", required=True, help="The first_name of the hr."),
        Argument("last_name", location="json", required=True, help="The last_name of the hr."),
        Argument("email", location="json", required=True, help="The email of the hr."),
        Argument("password", location="json",  required=True, help="The password of the hr."),
        Argument("phone_no", location="json", required=True, help="The phone_no of the hr."),
        Argument("alt_email", location="json",  help="The alt_email of the hr."),
        Argument("alt_phone_no", location="json",  help="The alt_phone_no of the hr."),
        Argument("department", location="json",  help="The department of the hr."),
        Argument("designation", location="json",  help="The designation of the hr."),
        Argument("profile_picture_url", location="json",  help="The profile_picture_url of the hr."),
        Argument("country", location="json",  help="The country of the hr."),
        Argument("state", location="json",  help="The state of the hr."),
        Argument("city", location="json",  help="The city of the hr."),
        Argument("address", location="json",  help="The address of the hr."),
        Argument("created_date", location="json",  help="The created_date of the hr."),
        Argument("last_updated_date", location="json",  help="The last_updated_date of the hr.")
    )
    @swag_from("../swagger/hr/POST.yml")
    def post(last_name, first_name, email,
     password,
     alt_email,
     alt_phone_no,
     phone_no,
     department,
     designation,
     profile_picture_url,
     created_date,
     last_updated_date,
     country,
     state,
     city,
     address):
        """ Create an hr based on the sent information """
        hr = HRRepository.create(
            last_name=last_name, first_name=first_name,
            email=email,
            password=password,
            alt_email=alt_email,
            alt_phone_no=alt_phone_no,
            phone_no=phone_no,
            department=department,
            designation=designation,
            profile_picture_url=profile_picture_url,
            country=country,
            state=state,
            city=city,
            address=address,
            created_date=created_date,
            last_updated_date=last_updated_date
        )
        # server.logger.info(jsonify(hr.json))
        res = jsonify({"data": hr.json, "status": "success"})
        return make_response(res, 200)

class HRResourceWithArg(Resource):
    """ Verbs relative to the hr """

    @staticmethod
    @swag_from("../swagger/hr/GET.yml")
    def get(last_name, first_name):
        """ Return an hr key information based on his name """
        hr = HRRepository.get(last_name=last_name, first_name=first_name)
        #  server.logger.info(json.dumps(hr))
        # server.logger.info(hr)
        try:
            res = jsonify({"data": hr.json, "status": "success"}) 
        except:
            res = jsonify({"hr": hr}) 
        return make_response(res, 200)

   

    @staticmethod
    @parse_params(
        Argument("first_name", location="json", required=True, help="Require first_name of the hr."),
        Argument("last_name", location="json", required=True, help="Require last_name of the hr.")
    )
    @swag_from("../swagger/hr/PUT.yml")
    def put(last_name, first_name):
        """ Update an hr based on the sent information """
        repository = HRRepository()
        hr = repository.update(last_name=last_name, first_name=first_name)
        return jsonify({"hr": hr.json})

    @staticmethod
    @parse_params(
        Argument("id", location="json", required=True, help="Require id of the hr.")
    )
    @swag_from("../swagger/hr/DELETE.yml")
    def delete(id):
        """ delete an hr based on the sent information """
        repository = HRRepository()
        hr = repository.delete(id=id)
        return jsonify({"hr": hr.json})
