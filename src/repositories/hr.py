""" Defines the HR repository """

from models import HR
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound
from flask.json import jsonify
from models import db


class HRRepository:
    """ The repository for the HR model """

    @staticmethod
    def get(last_name, first_name):
        """ Query a HR by last and first name """
        try:
            return HR.query.filter_by(last_name=last_name, first_name=first_name).one()
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
    def getById(id):
        """ Query a HR by last and first name """
        try:
            return HR.query.filter_by(id=id).one()
        except:
            # logger.error("{} has multiple records in Marcotti database for: {}".format(model.__name__, conditions))
            return {
                "status": "error",
                "data": [],
                "message": "No Results Found"
            }

    @staticmethod
    def getAllIds():
        """ Query a HR by last and first name """
        try:
            return HR.query.paginate(1,10,error_out=False)
        except:
            # logger.error("{} has multiple records in Marcotti database for: {}".format(model.__name__, conditions))
            return {
                "status": "error",
                "data": [],
                "message": "No Results Found"
            }        

    def update(self, last_name, first_name,
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
        """ Update a HR's age """
        HR = self.get(last_name, first_name)
        # HR.age = age

        return HR.save()

    @staticmethod
    def delete(id):
        """ delete a HR """
        try:
            del_id = HR.query.filter_by(id=id).one()
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
        """ Create a new HR """
        newHR = HR(last_name=last_name, first_name=first_name,
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

        return newHR.save()
