from enum import unique
from sqlalchemy import Column, ForeignKey, INTEGER, TEXT, REAL, BLOB, create_engine, event
from sqlalchemy.engine import Engine
from sqlalchemy.orm import declarative_base, relationship

# TODO: Add proper __repr__ for all classes

Base = declarative_base()


class Author(Base):
    __tablename__ = "Author"

    id = Column(INTEGER, primary_key=True)
    name = Column(TEXT, nullable=False)


class Publisher(Base):
    __tablename__ = "Publisher"

    id = Column(INTEGER, primary_key=True)
    name = Column(TEXT, nullable=False)


class Book(Base):
    __tablename__ = "Book"

    id = Column(INTEGER, primary_key=True)
    name = Column(TEXT, unique=True)
    price = Column(REAL, nullable=False)
    description = Column(TEXT)
    year = Column(INTEGER, nullable=False)
    pages = Column(INTEGER, nullable=False)
    isbn = Column(TEXT, unique=True)
    publisher = Column(TEXT, nullable=False)
    photo = Column(BLOB)


class User(Base):
    __tablename__ = "User"

    id = Column(INTEGER, primary_key=True)
    email = Column(TEXT, unique=True, nullable=False)
    login = Column(TEXT, unique=True, nullable=False)
    password = Column(BLOB, nullable=False)


### Engine definitions


# Enable sqlite foreign keys
@event.listens_for(Engine, "connect")
def sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON;")
    cursor.close()


def open_db(uri: str = "sqlite:///CoolBookDatabase.db") -> Engine:
    engine = create_engine(uri, echo=True, future=True)
    Base.metadata.create_all(engine)
    return engine
