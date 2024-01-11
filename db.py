from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

USER = 'postgres'
PASSWORD = '123456'
HOST = 'localhost'
PORT = '5432'
DATABASE = 'postgres'


def get_connection_string():
    return f'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}'


URI = get_connection_string()

try:
    engine = create_engine(URI, echo=True, future=True, pool_size=5, max_overflow=0, pool_pre_ping=True)
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
except Exception as e:
    print(f'Error:  {e}')
