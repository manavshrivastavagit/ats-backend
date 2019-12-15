from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .user import User
from .hr import HR
from .interviewer import interviewer
from .candidate import candidate
from .interview import interview
from .interview_rounds import interview_rounds
