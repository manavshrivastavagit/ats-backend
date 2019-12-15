"""
Define the REST verbs relative to the interviewer
"""

from flasgger import swag_from
from flask.json import jsonify
from flask_restful import Resource, request
from flask_restful.reqparse import Argument

from repositories import interviewerRepository
from util import parse_params

# logger
# from server import server
import json
from flask import make_response
from util.bcrypt import Bcrypt
from util.jwt import JWT
import time
import werkzeug
import os
from werkzeug import secure_filename


class interviewerResource(Resource):
    """ Verbs relative to the interviewer """

    @staticmethod
    @parse_params(
        Argument("id", location="args", required=True, help="Require id of the interviewer.")
    )
    @swag_from("../swagger/interviewer/DELETE.yml")
    def delete(id):
        """ delete an interviewer based on the sent information """
        # checking session token
        headers = request.headers
        if request.headers.get('Authorization') is None:
            res = jsonify({"data": [], "status": "error", "message": "Require session token"})
            return make_response(res, 401)
        if JWT.is_valid(headers.get('Authorization')) is False:
            res = jsonify({"data": [], "status": "error", "message": "Invalid session token"})
            return make_response(res, 401)
        # checking session token ends
        repository = interviewerRepository()
        interviewer = repository.delete(id=id)
        if interviewer.get('status') == "error":
            res = jsonify(interviewer)
            return make_response(res, 404)
        else:
            return jsonify(interviewer)

    @staticmethod
    @parse_params(
        Argument("page_number", location="args", help="Require page_number."),
        Argument("per_page_data", location="args", help="Require per_page_data.")
    )
    @swag_from("../swagger/interviewer/GET.yml")
    def get(page_number, per_page_data):
        """ Return an interviewer key information based on his name """
        args = request.args

        # checking session token
        headers = request.headers
        if request.headers.get('Authorization') is None:
            res = jsonify({"data": [], "status": "error", "message": "Require session token"})
            return make_response(res, 401)
        if JWT.is_valid(headers.get('Authorization')) is False:
            res = jsonify({"data": [], "status": "error", "message": "Invalid session token"})
            return make_response(res, 401)
        # checking session token ends

        try:
            id = args['id']
            if id == "all":
                interviewer = interviewerRepository.getAllIds(page_number, per_page_data)
                return jsonify(interviewer)
            else:
                interviewer = interviewerRepository.getById(id=id)
            res = jsonify({"data": interviewer.json, "status": "success"})
        except:
            res = jsonify(interviewer)
        return make_response(res, 200)

    @staticmethod
    @parse_params(
        Argument("first_name", location="json", required=True, help="The first_name of the interviewer."),
        Argument("last_name", location="json", required=True, help="The last_name of the interviewer."),
        Argument("email", location="json", required=True, help="The email of the interviewer."),
        Argument("password", location="json", required=True, help="The password of the interviewer."),
        Argument("phone_no", location="json", required=True, help="The phone_no of the interviewer."),
        Argument("alt_email", location="json", help="The alt_email of the interviewer."),
        Argument("alt_phone_no", location="json", help="The alt_phone_no of the interviewer."),
        Argument("department", location="json", help="The department of the interviewer."),
        Argument("designation", location="json", help="The designation of the interviewer."),
        Argument("profile_picture_url", location="json",
                 help="The profile_picture_url of the interviewer."),
        Argument("country", location="json", help="The country of the interviewer."),
        Argument("state", location="json", help="The state of the interviewer."),
        Argument("city", location="json", help="The city of the interviewer."),
        Argument("address", location="json", help="The address of the interviewer."),
        Argument("created_date", location="json", help="The created_date of the interviewer."),
        Argument("last_updated_date", location="json", help="The last_updated_date of the interviewer.")
    )
    @swag_from("../swagger/interviewer/POST.yml")
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
        """ Create an interviewer based on the sent information """
        # checking session token
        headers = request.headers
        if request.headers.get('Authorization') is None:
            res = jsonify({"data": [], "status": "error", "message": "Require session token"})
            return make_response(res, 401)
        if JWT.is_valid(headers.get('Authorization')) is False:
            res = jsonify({"data": [], "status": "error", "message": "Invalid session token"})
            return make_response(res, 401)
        # checking session token ends
        # hash password
        password_hashed = Bcrypt.get_hashed_password(password)
        interviewer = interviewerRepository.create(
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
        # server.logger.info(jsonify(interviewer.json))
        res = jsonify({"data": interviewer.json, "status": "success"})
        return make_response(res, 200)

    @staticmethod
    @parse_params(
        Argument("id", location="json", required=True, help="Require id of the interviewer."),
        Argument("first_name", location="json", help="The first_name of the interviewer."),
        Argument("last_name", location="json", help="The last_name of the interviewer."),
        Argument("email", location="json", help="The email of the interviewer."),
        Argument("password", location="json", help="The password of the interviewer."),
        Argument("phone_no", location="json", help="The phone_no of the interviewer."),
        Argument("alt_email", location="json", help="The alt_email of the interviewer."),
        Argument("alt_phone_no", location="json", help="The alt_phone_no of the interviewer."),
        Argument("department", location="json", help="The department of the interviewer."),
        Argument("designation", location="json", help="The designation of the interviewer."),
        Argument("profile_picture_url", location="json",
                 help="The profile_picture_url of the interviewer."),
        Argument("country", location="json", help="The country of the interviewer."),
        Argument("state", location="json", help="The state of the interviewer."),
        Argument("city", location="json", help="The city of the interviewer."),
        Argument("address", location="json", help="The address of the interviewer."),
        Argument("created_date", location="json", help="The created_date of the interviewer."),
        Argument("last_updated_date", location="json", help="The last_updated_date of the interviewer.")
    )
    @swag_from("../swagger/interviewer/PUT.yml")
    def put(id, last_name, first_name,
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
        """ Update an interviewer based on the sent information """
        # checking session token
        headers = request.headers
        if request.headers.get('Authorization') is None:
            res = jsonify({"data": [], "status": "error", "message": "Require session token"})
            return make_response(res, 401)
        if JWT.is_valid(headers.get('Authorization')) is False:
            res = jsonify({"data": [], "status": "error", "message": "Invalid session token"})
            return make_response(res, 401)
        # checking session token ends
         # hash password
        if password is not None:
            password = Bcrypt.get_hashed_password(password)
        repository = interviewerRepository()
        interviewer = repository.update(
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
            res = jsonify({"data": interviewer.json, "status": "success"})
        except:
            res = jsonify({"interviewer": interviewer})
        return make_response(res, 200)


class interviewerResourceWithArg(Resource):
    """ Verbs relative to the interviewer """
    @staticmethod
    @swag_from("../swagger/interviewer/GET.yml")
    def get(last_name, first_name):
        """ Return an interviewer key information based on his name """
        interviewer = interviewerRepository.get(last_name=last_name, first_name=first_name)
        #  server.logger.info(json.dumps(interviewer))
        # server.logger.info(interviewer)
        try:
            res = jsonify({"data": interviewer.json, "status": "success"})
        except:
            res = jsonify({"interviewer": interviewer})
        return make_response(res, 200)


class interviewerResourceLogin(Resource):
    """ Verbs relative to the interviewer login """
    # login
    @staticmethod
    @parse_params(
        Argument("email", location="json", required=True, help="Require  email of the interviewer."),
        Argument("password", location="json", required=True, help="Require password of the interviewer."),
    )
    @swag_from("../swagger/interviewer/POST.yml")
    def post(
            email,
            password):
        """ create session token """
        # server.logger.info("login")

        interviewer = interviewerRepository.getByEmail(
            email=email
        )
        # server.logger.info(interviewer)
        if interviewer is not None:
            # hash password
            password_hashed = Bcrypt.get_hashed_password(password)
            valid_password = Bcrypt.check_password(password, interviewer.password)
            # server.logger.info(valid_password)
            if valid_password:
                payload = {"email": interviewer.email, "createdAt": int(time.time() * 1000)}
                session_token = JWT.encode(payload)
                session_token = str(session_token)[1:].replace("'", "")
                # server.logger.info(session_token)
                res = jsonify({"data": {"session_token": str(session_token)}, "status": "success"})
                return make_response(res, 200)
            else:
                res = jsonify({"data": [], "status": "error", "message": "incorrect password"})
                return make_response(res, 401)
        else:
            res = jsonify({"data": [], "status": "error", "message": "incorrect email"})
            return make_response(res, 401)


class interviewerResourceLogout(Resource):
    """ Verbs relative to the interviewer logout """
    # logout
    @staticmethod
    @swag_from("../swagger/interviewer/POST.yml")
    def post():
        """ Destroy session token """
        # server.logger.info("logout")
        headers = request.headers
        if request.headers.get('Authorization'):
            # server.logger.info(headers.get('Authorization') )
            # server.logger.info(JWT.decode(headers.get('Authorization').split()[1]) )
            try:
                encoded_token = JWT.decode(headers.get('Authorization').split()[1])
                res = jsonify(
                    {"data": {"logout": "true", "valid_session_token": "true"}, "status": "success"})
                return make_response(res, 200)
            except:
                res = jsonify({"data": [], "status": "error", "message": "Invalid session token"})
                return make_response(res, 401)
        else:
            res = jsonify({"data": [], "status": "error",
                           "message": "No Authorization session token"})
            return make_response(res, 401)


def create_new_folder(local_dir):
    newpath = local_dir
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    return newpath


class interviewerResourceUploadFile(Resource):
    """ Verbs relative to the upload """
    # upload file
    @staticmethod
    @swag_from("../swagger/interviewer/POST.yml")
    def post():
        """ upload image """
        # checking session token
        headers = request.headers
        if request.headers.get('Authorization') is None:
            res = jsonify({"data": [], "status": "error", "message": "Require session token"})
            return make_response(res, 401)
        if JWT.is_valid(headers.get('Authorization')) is False:
            res = jsonify({"data": [], "status": "error", "message": "Invalid session token"})
            return make_response(res, 401)
        # checking session token ends
        # checking if the file is present or not.
        if 'file' not in request.files:
            res = jsonify({"data": [], "status": "error", "message": "No file found"})
            return make_response(res, 404)
        try:    
            app_root = '..' + os.path.dirname(os.path.abspath(__file__))
            target =  os.path.join(app_root, '../../static/img')
            if not os.path.isdir(target):
                os.makedirs(target)
            img = request.files['file']
            img_name = secure_filename(img.filename)
            destination = '/'.join([target, img_name])
            img.save(destination)
            res = jsonify({"data": {"message" : "file Successfully uploaded"}, "status": "success"})
            return make_response(res, 200)
        except Exception as e:
            res = jsonify({"data": [], "status": "error", "message": e })
            return make_response(res, 404)
