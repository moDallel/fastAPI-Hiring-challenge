from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# from sqlalchemy.engine import URL

#
# url = URL.create(
#     drivername="postgresql",
#     username="postgres",
#     password="123456",
#     host="localhost",
#     database="usershiringchallenge",
#     port=5432
# )

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
Session = sessionmaker(bind=engine)
session = Session()
