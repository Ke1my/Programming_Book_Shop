from sqlalchemy import Column, ForeignKey, INTEGER, TEXT, REAL, BLOB, create_engine, event, UniqueConstraint, Table
from sqlalchemy.engine import Engine
from sqlalchemy.orm import declarative_base, relationship

# TODO: Add proper __repr__ for all classes

Base = declarative_base()


association_author_book_table = Table("AuthorBook", Base.metadata,
                                      Column("author", ForeignKey(
                                          "Author.id"), primary_key=True),
                                      Column("book", ForeignKey(
                                          "Book.id"), primary_key=True),
                                      )


class Author(Base):
    __tablename__ = "Author"

    id = Column(INTEGER, primary_key=True)
    name = Column(TEXT, nullable=False)

    books_rel = relationship("Book", secondary=association_author_book_table,
                             back_populates="authors_rel")


class Publisher(Base):
    __tablename__ = "Publisher"

    id = Column(INTEGER, primary_key=True)
    name = Column(TEXT, nullable=False)

    books_rel = relationship("Book", back_populates="publisher_rel")


class Book(Base):
    __tablename__ = "Book"

    id = Column(INTEGER, primary_key=True)
    name = Column(TEXT, unique=True)
    price = Column(REAL, nullable=False)
    description = Column(TEXT)
    year = Column(INTEGER, nullable=False)
    pages = Column(INTEGER, nullable=False)
    isbn = Column(TEXT, unique=True)
    publisher = Column(INTEGER, ForeignKey("Publisher.id"), nullable=False)
    photo = Column(BLOB)

    authors_rel = relationship("Author", secondary=association_author_book_table,
                               back_populates="books_rel")
    publisher_rel = relationship("Publisher", back_populates="books_rel")
    cart_rel = relationship("Cart", back_populates="book_rel")
    reviews_rel = relationship(
        "Review", back_populates="book_rel", uselist=False)
    popularity_rel = relationship(
        "Popularity", back_populates="book_rel", uselist=False)


class User(Base):
    __tablename__ = "User"

    id = Column(INTEGER, primary_key=True)
    email = Column(TEXT, unique=True, nullable=False)
    login = Column(TEXT, unique=True, nullable=False)
    password = Column(BLOB, nullable=False)

    cart_rel = relationship("Cart", back_populates="user_rel")
    reviews_rel = relationship("Review", back_populates="user_rel")


class Cart(Base):
    __tablename__ = "Cart"

    user = Column(INTEGER, ForeignKey("User.id"), primary_key=True)
    book = Column(INTEGER, ForeignKey("Book.id"), primary_key=True)

    uix_user_book = UniqueConstraint("user", "book", name="uix_user_book")

    user_rel = relationship("User", back_populates="cart_rel")
    book_rel = relationship("Book", back_populates="cart_rel")


class Review(Base):
    __tablename__ = "Review"

    id = Column(INTEGER, primary_key=True)
    mark = Column(INTEGER, nullable=False)
    user = Column(INTEGER, ForeignKey("User.id"))
    book = Column(INTEGER, ForeignKey("Book.id"))
    content = Column(TEXT, nullable=False)

    uix_user_book = UniqueConstraint("user", "book", name="uix_user_book")

    user_rel = relationship("User", back_populates="reviews_rel")
    book_rel = relationship("Book", back_populates="reviews_rel")


class Popularity(Base):
    __tablename__ = "Popularity"

    book = Column(INTEGER, ForeignKey("Book.id"), primary_key=True)
    views = Column(INTEGER, nullable=False, default=0)

    book_rel = relationship("Book", back_populates="popularity_rel")


# Engine definitions


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
