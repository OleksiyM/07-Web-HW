# for testing and debug purposes - manually creating and drop tables
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db import get_connection_string, engine
from models import Base


def create_db(engine):
    Base.metadata.create_all(engine)
    return 'Tables were created'


def drop_db(engine):
    Base.metadata.drop_all(engine)
    return 'Tables were dropped'


if __name__ == '__main__':
    print(get_connection_string())


    # print(create_db(engine))

    # print(drop_db(engine))
