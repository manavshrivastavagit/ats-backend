"""
Define the REST verbs relative to the hr
"""

from flasgger import swag_from
from flask.json import jsonify
from flask_restful import Resource, request
from flask_restful.reqparse import Argument

from repositories import HRRepository
from util import parse_params

# logger
# from server import server
import json
from flask import make_response
from util.bcrypt import Bcrypt
from util.jwt import JWT
import time



class HRResource(Resource):
    """ Verbs relative to the hr """

    @staticmethod
    @parse_params(
        Argument("id", location="args", required=True, help="Require id of the hr.")
    )
    @swag_from("../swagger/hr/DELETE.yml")
    def delete(id):
        """ delete an hr based on the sent information """
        repository = HRRepository()
        hr = repository.delete(id=id)
        return jsonify(hr)


    @staticmethod
    @parse_params(
        Argument("page_number", location="args",  help="Require page_number."),
        Argument("per_page_data", location="args",  help="Require per_page_data.")
    )
    @swag_from("../swagger/hr/GET.yml")
    def get(page_number, per_page_data):
        """ Return an hr key information based on his name """
        args = request.args
        headers =  request.headers
        # if request.headers.get('Authorization'):
            # server.logger.info(headers.get('Authorization') )
            # server.logger.info(JWT.decode(headers.get('Authorization').split()[1]) )
            # server.logger.info(JWT.is_valid(headers.get('Authorization')) )
            # try:
            #     encoded_token = JWT.decode(headers.get('Authorization').split()[1])
            #     res = jsonify({"data": {"logout":"true","valid_session_token":"true"}, "status": "success"})
            #     return make_response(res, 200)
            # except:
            #     res = jsonify({"data": [], "status": "error", "message":"Invalid session token"})
            #     return make_response(res, 401)
        # server.logger.info("headers")
        # server.logger.info(page_number)
        try:
            id = args['id']
            if id == "all":
                hr = HRRepository.getAllIds(page_number, per_page_data)
                return jsonify(hr)
            else:
                 hr = HRRepository.getById(id=id)
            res = jsonify({"data": hr.json, "status": "success"}) 
        except:
            res = jsonify(hr)
        return make_response(res, 200)


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
        # hash password
        password_hashed = Bcrypt.get_hashed_password(password)
        hr = HRRepository.create(
            last_name=last_name, first_name=first_name,
            email=email,
            password=password_hashed,
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

   


    @staticmethod
    @parse_params(
        Argument("id", location="json", required=True, help="Require id of the hr."),
        Argument("first_name", location="json",  help="The first_name of the hr."),
        Argument("last_name", location="json",  help="The last_name of the hr."),
        Argument("email", location="json",  help="The email of the hr."),
        Argument("password", location="json",   help="The password of the hr."),
        Argument("phone_no", location="json",  help="The phone_no of the hr."),
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
    @swag_from("../swagger/hr/PUT.yml")
    def put(id, last_name,first_name, 
            email,
            password,
            alt_email,
            alt_phone_no,
            phone_no,
            department,
            designation,
            profile_picture_url,
            country,
            state,
            city,
            address,
            created_date,
            last_updated_date):
        """ Update an hr based on the sent information """
         # hash password
        if password is not None:
            password = Bcrypt.get_hashed_password(password)
        repository = HRRepository()
        hr = repository.update(
            id=id,
            last_name=last_name,
            first_name=first_name,
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
            last_updated_date=last_updated_date)
        try:
            res = jsonify({"data": hr.json, "status": "success"}) 
        except:
            res = jsonify({"hr": hr}) 
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

class HRResourceLogin(Resource):
    """ Verbs relative to the hr login """
    # login 
    @staticmethod
    @parse_params(
        Argument("email", location="json", required=True, help="Require  email of the hr."),
        Argument("password", location="json",  required=True, help="Require password of the hr."),
    )
    @swag_from("../swagger/hr/POST.yml")
    def post( 
        email,
        password):
        """ create session token """
        # server.logger.info("login")
       
        
        hr = HRRepository.getByEmail(
            email=email
        )
        # server.logger.info(hr)
        if hr is not None:
            # hash password
            password_hashed = Bcrypt.get_hashed_password(password)
            valid_password = Bcrypt.check_password(password,hr.password)
            # server.logger.info(valid_password)
            if valid_password:
                payload = {"email":hr.email, "createdAt":int(time.time() * 1000)}
                session_token = JWT.encode(payload)
                session_token = str(session_token)[1:].replace("'","")
                # server.logger.info(session_token)
                res = jsonify({"data": {"session_token":str(session_token)}, "status": "success"})
                return make_response(res, 200)
            else:
                res = jsonify({"data": [], "status": "error", "message":"incorrect password"})
                return make_response(res, 401)
        else:
            res = jsonify({"data": [], "status": "error", "message":"incorrect email"})
            return make_response(res, 401)

class HRResourceLogout(Resource):
    """ Verbs relative to the hr logout """
    # logout
    @staticmethod
    @swag_from("../swagger/hr/POST.yml")
    def post():
        """ Destroy session token """
        # server.logger.info("logout")
        headers =  request.headers
        if request.headers.get('Authorization'):
            # server.logger.info(headers.get('Authorization') )
            # server.logger.info(JWT.decode(headers.get('Authorization').split()[1]) )
            try:
                encoded_token = JWT.decode(headers.get('Authorization').split()[1])
                res = jsonify({"data": {"logout":"true","valid_session_token":"true"}, "status": "success"})
                return make_response(res, 200)
            except:
                res = jsonify({"data": [], "status": "error", "message":"Invalid session token"})
                return make_response(res, 401)
        else:
            res = jsonify({"data": [], "status": "error", "message":"No Authorization session token"})
            return make_response(res, 401)
