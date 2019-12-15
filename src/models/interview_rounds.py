"""
Define the interview_rounds model
"""
from . import db
from .abc import BaseModel, MetaBaseModel
import datetime


class interview_rounds(db.Model, BaseModel, metaclass=MetaBaseModel):
    """ The interview_rounds model """

    __tablename__ = "interview_rounds"
    id = db.Column(db.BigInteger,  primary_key=True,  autoincrement=True)
    interview_id = db.Column(db.BigInteger, nullable=True)
    interviewer_id = db.Column(db.BigInteger, nullable=True)
    topic = db.Column(db.String(500), nullable=True)
    ratings = db.Column(db.String(500), nullable=True)
    feedback = db.Column(db.String(500), nullable=True)
    notes = db.Column(db.String(500), nullable=True)
    status = db.Column(db.String(500), nullable=True)
    round_number = db.Column(db.BigInteger, nullable=True)
    round_name = db.Column(db.String(500), nullable=True)
    created_date = db.Column(db.DateTime, default=datetime.datetime.utcnow, nullable=True)
    last_updated_date = db.Column(db.DateTime, default=datetime.datetime.utcnow, nullable=True)
    last_updated_by_hr_id = db.Column(db.BigInteger, nullable=True)
   



    def __init__(self,
    id=None,
    interview_id =None,
    interviewer_id =None,
    topic =None,
    ratings =None,
    feedback=None,
    notes =None,
    status =None,
    round_number =None,
    round_name =None,
    created_date =None,
    last_updated_date=None,
    last_updated_by_hr_id =None
     ):
        """ Create a new interview_rounds """
        self.id = id
        self.interview_id = interview_id
        self.interviewer_id = interviewer_id
        self.topic = topic
        self.ratings = ratings
        self.feedback = feedback
        self.notes = notes
        self.status = status
        self.round_number = round_number
        self.round_name = round_name
        self.created_date = created_date
        self.last_updated_date = last_updated_date
        self.last_updated_by_hr_id = last_updated_by_hr_id