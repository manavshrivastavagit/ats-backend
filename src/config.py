import logging
import os

DEBUG = os.getenv("ENVIRONEMENT") == "DEV"
APPLICATION_ROOT = os.getenv("APPLICATION_APPLICATION_ROOT", "/application")
HOST = os.getenv("APPLICATION_HOST")
PORT = int(os.getenv("APPLICATION_PORT", "3000"))
SQLALCHEMY_TRACK_MODIFICATIONS = False

DB_CONTAINER = os.getenv("APPLICATION_DB_CONTAINER", "db")
POSTGRES = {
    "user": os.getenv("APPLICATION_POSTGRES_USER", "uadqvrzvvhsgvl"),
    "pw": os.getenv("APPLICATION_POSTGRES_PW", "76e9e53176d897f8bb1290fec47bcdde69043710aecb602067de96961e1c7bc0"),
    "host": os.getenv("APPLICATION_POSTGRES_HOST", "ec2-107-21-126-201.compute-1.amazonaws.com"),
    "port": os.getenv("APPLICATION_POSTGRES_PORT", 5432),
    "db": os.getenv("APPLICATION_POSTGRES_DB", "d7d2gs1qbqj579"),
}
DB_URI = "postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s" % POSTGRES

logging.basicConfig(
    filename=os.getenv("SERVICE_LOG", "server.log"),
    level=logging.DEBUG,
    format="%(levelname)s: %(asctime)s \
        pid:%(process)s module:%(module)s %(message)s",
    datefmt="%d/%m/%y %H:%M:%S",
)
