from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

USER = 'postgres'
PASSWORD = '123456'
HOST = 'localhost'
PORT = '5432'
DATABASE = 'dbase'


def get_connection_string():
    return f'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}'


def create_db():
    engine = create_engine(get_connection_string())
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)


if __name__ == '__main__':
    create_db()
