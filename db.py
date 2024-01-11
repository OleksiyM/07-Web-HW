from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base

USER = 'postgres'
PASSWORD = '123456'
HOST = 'localhost'
PORT = '5432'
DATABASE = 'postgres'


def get_connection_string():
    return f'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}'


def create_db(engine):
    Base.metadata.create_all(engine)
    return 'Tables were created'


def drop_db(engine):
    Base.metadata.drop_all(engine)
    return 'Tables were dropped'


if __name__ == '__main__':
    print(get_connection_string())
    try:
        engine = create_engine(get_connection_string())
        Session = sessionmaker(bind=engine)
        session = Session()
    except Exception as e:
        print(f'Error:  {e}')

    print(create_db(engine))

    # print(drop_db(engine))
