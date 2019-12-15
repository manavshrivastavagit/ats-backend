"""
Define the interview model
"""
from . import db
from .abc import BaseModel, MetaBaseModel
import datetime


class interview(db.Model, BaseModel, metaclass=MetaBaseModel):
    """ The interview model """

    __tablename__ = "interview"
    id = db.Column(db.BigInteger,  primary_key=True,  autoincrement=True)
    candidate_id = db.Column(db.BigInteger, nullable=True)
    hr_id = db.Column(db.BigInteger, nullable=True)
    interviewer_id = db.Column(db.BigInteger, nullable=True)
    interview_date = db.Column(db.DateTime, default=datetime.datetime.utcnow, nullable=True)
    department = db.Column(db.String(100), nullable=True)
    designation = db.Column(db.String(100), nullable=True)
    country = db.Column(db.String(100), nullable=True)
    state = db.Column(db.String(100), nullable=True)
    city = db.Column(db.String(100), nullable=True)
    address = db.Column(db.String(500), nullable=True)
    created_date = db.Column(db.DateTime, default=datetime.datetime.utcnow, nullable=True)
    last_updated_date = db.Column(db.DateTime, default=datetime.datetime.utcnow, nullable=True)
    last_updated_by_hr_id = db.Column(db.BigInteger, nullable=True)
   



    def __init__(self,
    id=None,
    candidate_id =None,
    hr_id=None,
    interviewer_id =None,
    interview_date=None,
    department=None,
    designation =None,
    country =None,
    state =None,
    city =None,
    address =None,
    created_date =None,
    last_updated_date =None,
    last_updated_by_hr_id=None
     ):
        """ Create a new interview """
        self.id = id
        self.candidate_id = candidate_id
        self.hr_id = hr_id
        self.interviewer_id = interviewer_id
        self.department = department
        self.designation = designation
        self.interview_date = interview_date
        self.created_date = created_date
        self.last_updated_date = last_updated_date
        self.country = country
        self.state = state
        self.city = city
        self.address = address
        self.last_updated_by_hr_id = last_updated_by_hr_id