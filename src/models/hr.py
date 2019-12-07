"""
Define the HR model
"""
from . import db
from .abc import BaseModel, MetaBaseModel
import datetime


class HR(db.Model, BaseModel, metaclass=MetaBaseModel):
    """ The HR model """

    __tablename__ = "hr"
    id = db.Column(db.BigInteger,  primary_key=True,  autoincrement=True)
    email = db.Column(db.String(100), nullable=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    password = db.Column(db.String(200), nullable=True)
    alt_email = db.Column(db.String(100), nullable=True)
    alt_phone_no = db.Column(db.String(100), nullable=True)
    phone_no = db.Column(db.String(100), nullable=True)
    department = db.Column(db.String(100), nullable=True)
    designation = db.Column(db.String(100), nullable=True)
    profile_picture_url = db.Column(db.String(100), nullable=True)
    created_date = db.Column(db.DateTime, default=datetime.datetime.utcnow, nullable=True)
    last_updated_date = db.Column(db.DateTime, default=datetime.datetime.utcnow, nullable=True)
    country = db.Column(db.String(100), nullable=True)
    state = db.Column(db.String(100), nullable=True)
    city = db.Column(db.String(100), nullable=True)
    address = db.Column(db.String(500), nullable=True)

    # age = db.Column(db.Integer, nullable=True)

    def __init__(self,
     first_name,
     last_name,
     email=None,
     password=None,
     alt_email=None,
     alt_phone_no=None,
     phone_no=None,
     department=None,
     designation=None,
     profile_picture_url=None,
     created_date=None,
     last_updated_date=None,
     country=None,
     state=None,
     city=None,
     address=None
     ):
        """ Create a new HR """
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.alt_email = alt_email
        self.alt_phone_no = alt_phone_no
        self.phone_no = phone_no
        self.department = department
        self.designation = designation
        self.profile_picture_url = profile_picture_url
        self.created_date = created_date
        self.last_updated_date = last_updated_date
        self.country = country
        self.state = state
        self.city = city
        self.address = address