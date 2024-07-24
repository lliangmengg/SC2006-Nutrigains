from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError


Base = declarative_base()

class DatabaseCRUDOperator:
    def __init__(self):
        self.db_url = "mysql+pymysql://root:12345@localhost:3306/nutrigains"


        self.engine = create_engine(self.db_url)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)


    def create(self, obj, keep_session_open = False):
        session = self.Session()
        session.add(obj)
        session.commit()
        if not keep_session_open:
            session.close()


    def read(self, model, keep_session_open = False, **kwargs):
        session = self.Session()
        query = session.query(model)
        for attr, value in kwargs.items():
            if isinstance(value, dict):
                for op, val in value.items():
                    column = getattr(model, attr)
                    if op == 'ge':
                        query = query.filter(column >= val)
                    # Add more operators as needed
            else:
                query = query.filter(getattr(model, attr) == value)
        result = query.all()
        if not keep_session_open:
            session.close()
        return result

    def update(self, model, primary_key_dict, kwargs, keep_session_open = False):
        session = self.Session()
        # Filter by the primary keys and update with kwargs
        session.query(model).filter_by(**primary_key_dict).update(kwargs)
        session.commit()
        session.close()

    def delete(self, model, primary_key_dict):
        session = self.Session()
        obj = session.get(model, primary_key_dict)
        session.delete(obj)
        session.commit()
        session.close()