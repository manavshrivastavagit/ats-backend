""" Defines the interviewRounds repository """

from models import interview_rounds
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound
from flask.json import jsonify
from models import db
# logger
# from server import server
import json


class interviewRoundsRepository:
    """ The repository for the interviewRounds model """

    @staticmethod
    def get(last_name, first_name):
        """ Query a interviewRounds by last and first name """
        try:
            return interviewRounds.query.filter_by(last_name=last_name, first_name=first_name).one()
        except NoResultFound:
            return {
                "status": "error",
                "data": [],
                "message": "no data found"
            }
        except MultipleResultsFound:
            # logger.error("{} has multiple records in Marcotti database for: {}".format(model.__name__, conditions))
            return {
                "status": "error",
                "data": [],
                "message": "Multiple Results Found"
            }

    @staticmethod
    def getByEmail(email):
        """ Query a interviewRounds by email """
        try:
            return interviewRounds.query.filter_by(email=email).one()
        except NoResultFound:
            return None
            return {
                "status": "error",
                "data": [],
                "message": "no data found"
            }
        except MultipleResultsFound:
            return None
            return {
                "status": "error",
                "data": [],
                "message": "Multiple Results Found"
            }

    @staticmethod
    def getById(id):
        """ Query a interviewRounds by last and first name """
        try:
            return interviewRounds.query.filter_by(id=id).one()
        except:
            # logger.error("{} has multiple records in Marcotti database for: {}".format(model.__name__, conditions))
            return {
                "status": "error",
                "data": [],
                "message": "No Results Found"
            }

    @staticmethod
    def getAllIds(page_number=1, per_page_data=10):
        """ Query a interviewRounds by last and first name """
        try:
            # server.logger.info(page_number)
            # server.logger.info(per_page_data)
            record_query = interviewRounds.query.paginate(int(page_number), int(per_page_data), error_out=False)
            record_query_dicts = []
            for i in record_query.items:
                record_query_dict = i.__dict__
                del record_query_dict['_sa_instance_state']
                record_query_dicts.append(record_query_dict)
            record_query.items = record_query_dicts
            # server.logger.info(record_query.total)
            return dict(
                status="success",
                total=record_query.total,
                per_page=record_query.per_page,
                current_page=record_query.page,
                next_num=record_query.next_num,
                prev_num=record_query.prev_num,
                data=record_query.items,
                has_next=record_query.has_next)
        except Exception as e:
            # server.logger.info('error : '+ str(e))
            # server.logger.info(e)
            return {
                "status": "error",
                "data": [],
                "message": "No Results Found"
            }

    def update(self, id, last_name, first_name,
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
        """ Update a interviewRounds """
        interviewRounds = self.getById(id=id)
        # interviewRounds.city = city if city else "bangalore"
        if last_name is not None:
            interviewRounds.last_name = last_name
        if first_name is not None:
            interviewRounds.first_name = first_name
        if email is not None:
                interviewRounds.email = email
        if password is not None:
            interviewRounds.password = password
        if alt_email is not None:
            interviewRounds.alt_email = alt_email
        if alt_phone_no is not None:
            interviewRounds.alt_phone_no = alt_phone_no
        if phone_no is not None:
            interviewRounds.phone_no = phone_no
        if department is not None:
            interviewRounds.department = department
        if designation is not None:
            interviewRounds.designation = designation
        if profile_picture_url is not None:
            interviewRounds.profile_picture_url = profile_picture_url
        if country is not None:
            interviewRounds.country = country
        if state is not None:
            interviewRounds.state = state
        if city is not None:
            interviewRounds.city = city
        if address is not None:
            interviewRounds.address = address
        return interviewRounds.save()

    @staticmethod
    def delete(id):
        """ delete a interviewRounds """
        try:
            del_id = interviewRounds.query.filter_by(id=id).one()
            db.session.delete(del_id)
            db.session.commit()
            return {
                "status": "success",
                "data": [],
                "message": "id deleted Successfully "
            }
        except:
            return {
                "status": "error",
                "data": [],
                "message": " id not found"
            }

    @staticmethod
    def create(last_name, first_name,
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
        """ Create a new interviewRounds """
        newinterviewRounds = interviewRounds(last_name=last_name, first_name=first_name,
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

        return newinterviewRounds.save()
