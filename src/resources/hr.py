"""
Define the REST verbs relative to the hr
"""

from flasgger import swag_from
from flask.json import jsonify
from flask_restful import Resource
from flask_restful.reqparse import Argument

from repositories import HRRepository
from util import parse_params


class HRResource(Resource):
    """ Verbs relative to the hr """

    @staticmethod
    @swag_from("../swagger/hr/GET.yml")
    def get(last_name, first_name):
        """ Return an hr key information based on his name """
        hr = HRRepository.get(last_name=last_name, first_name=first_name)
        return jsonify({"hr": hr.json})

    @staticmethod
    @parse_params(
        Argument("first_name", location="json", required=True, help="The first_name of the hr.")
    )
    @swag_from("../swagger/hr/POST.yml")
    def post(last_name, first_name):
        """ Create an hr based on the sent information """
        hr = HRRepository.create(
            last_name=last_name, first_name=first_name
        )
        return jsonify({"hr": hr.json})

    @staticmethod
    @parse_params(
        Argument("first_name", location="json", required=True, help="Require first_name of the hr.")
    )
    @swag_from("../swagger/hr/PUT.yml")
    def put(last_name, first_name):
        """ Update an hr based on the sent information """
        repository = HRRepository()
        hr = repository.update(last_name=last_name, first_name=first_name)
        return jsonify({"hr": hr.json})
