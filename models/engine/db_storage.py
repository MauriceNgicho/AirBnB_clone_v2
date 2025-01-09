#!/usr/bin/python3
"""Database storage"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User

class DBStorage:
    """Database storage engine"""
    __engine = None
    __session = None

    def __init__(self):
        """create the engine"""
        sql_user = os.environ.get('HBNB_MYSQL_USER')
        sql_passwd = os.environ.get('HBNB_MYSQL_PWD')
        sql_host = os.environ.get('HBNB_MYSQL_HOST')
        sql_db = os.environ.get('HBNB_MYSQL_DB')
        environment = os.environ.get('HBNB_ENV')
        test_db = os.environ.get('HBNB_TEST_DB')

        self.__engine = create_engine(
                'mysql+mysqldb://{}:{}@{}/{}'
                .format(sql_user,sql_passwd, sql_host, sql_db),
                pool_pre_ping=True)
        if environment == "test":
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """query on current database session"""
        result = {}
        classes = [State, City, User, Place, Amenity, Review]
        if cls:
            cls = cls if type(cls) is not str else eval(cls)
            objs = self.__session.query(cls).all()
            for obj in objs:
                key = f"{obj.__class__.__name__}.{obj.id}"
                result[key] = obj
        else:
            for class_ in classes:
                objs = self.__session.query(class_).all()
                for obj in objs:
                    key = f"{obj.__class__.__name__}.{obj.id}"
                    result[key] = obj
        return result

    def new(self, obj):
        """Add object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit the changes to the db"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete object from current database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """reload all objects from db"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        self.__session = scoped_session(session_factory)

    def close(self):
        """Close the current running session"""
        self.__session.close()
