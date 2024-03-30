from . models import (Base, Student, Group)
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///my_db.sql", echo=True)
Session = sessionmaker(engine,)


def init_db(engine=engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
