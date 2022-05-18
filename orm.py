from argon2 import PasswordHasher
from sqlalchemy import Column, ForeignKey, INTEGER, TEXT, REAL, BLOB, create_engine, event, \
    UniqueConstraint, Table, select, func
from sqlalchemy.engine import Engine
from sqlalchemy.orm import declarative_base, relationship, selectinload, Query

# TODO: Add proper __repr__ for all classes


Base = declarative_base()
Hasher = PasswordHasher()


# Relation between Author and Book via AuthorBook table
association_author_book_table = Table("AuthorBook", Base.metadata, Column("author", ForeignKey(
    "Author.id"), primary_key=True), Column("book", ForeignKey("Book.id"), primary_key=True))

# Association between User and Book via Cart table
association_cart_table = Table("Cart", Base.metadata, Column("user", ForeignKey(
    "User.id"), primary_key=True), Column("book", ForeignKey("Book.id"), primary_key=True))


class Author(Base):
    __tablename__ = "Author"

    # Fields
    id = Column(INTEGER, primary_key=True)
    name = Column(TEXT, nullable=False)

    # Relations
    books_rel = relationship("Book", secondary=association_author_book_table,
                             back_populates="authors_rel")

    def __repr__(self):
        return f"Author(id={self.id!r}, name={self.name!r})"


class Publisher(Base):
    __tablename__ = "Publisher"

    # Fields
    id = Column(INTEGER, primary_key=True)
    name = Column(TEXT, nullable=False)

    # Relations
    books_rel = relationship("Book", back_populates="publisher_rel")


class Book(Base):
    __tablename__ = "Book"

    # Fields
    id = Column(INTEGER, primary_key=True)
    name = Column(TEXT, unique=True)
    price = Column(REAL, nullable=False)
    description = Column(TEXT)
    year = Column(INTEGER, nullable=False)
    pages = Column(INTEGER, nullable=False)
    isbn = Column(TEXT, unique=True)
    publisher = Column(INTEGER, ForeignKey("Publisher.id"), nullable=False)
    photo = Column(BLOB)
    rating = Column(REAL)
    views = Column(INTEGER)

    # Relations
    authors_rel = relationship("Author", secondary=association_author_book_table,
                               back_populates="books_rel")
    publisher_rel = relationship("Publisher", back_populates="books_rel")
    cart_users_rel = relationship(
        "User", secondary=association_cart_table, back_populates="cart_books_rel")
    reviews_rel = relationship(
        "Review", back_populates="book_rel", uselist=False)

    def __repr__(self):
        return f"Book(id={self.id!r}, name={self.name!r}, price={self.price!r})"


class User(Base):
    __tablename__ = "User"

    # Fields
    id = Column(INTEGER, primary_key=True)
    email = Column(TEXT, unique=True, nullable=False)
    name = Column(TEXT, nullable=False)
    password = Column(TEXT, nullable=False)

    # Relations
    cart_books_rel = relationship(
        "Book", secondary=association_cart_table, back_populates="cart_users_rel")
    reviews_rel = relationship("Review", back_populates="user_rel")


class Review(Base):
    __tablename__ = "Review"

    # Fields
    id = Column(INTEGER, primary_key=True)
    mark = Column(INTEGER, nullable=False)
    user = Column(INTEGER, ForeignKey("User.id"))
    book = Column(INTEGER, ForeignKey("Book.id"))
    content = Column(TEXT, nullable=False)

    # Contraint
    uix_user_book = UniqueConstraint("user", "book", name="uix_user_book")

    # Relations
    user_rel = relationship("User", back_populates="reviews_rel")
    book_rel = relationship("Book", back_populates="reviews_rel")


# Engine definitions


# Enable sqlite foreign keys
@event.listens_for(Engine, "connect")
def sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON;")
    cursor.close()


def open_db(uri: str = "sqlite:///CoolBookDatabase.db?charset=utf8") -> Engine:
    engine = create_engine(uri, echo=True, future=True)
    Base.metadata.create_all(engine)
    return engine


# Queries

def __query_latest_books(limit: int, ordering):
    return select(Book)\
        .order_by(ordering)\
        .limit(limit)\
        .execution_options(populate_existing=True)\
        .options(selectinload(Book.authors_rel))


def query_latest_books(limit: int):
    return __query_latest_books(limit, Book.id.desc())


def query_latest_books_new(limit: int):
    return __query_latest_books(limit, Book.year.desc())


def query_latest_books_rating(limit: int):
    return __query_latest_books(limit, Book.rating.desc())


def query_latest_books_views(limit: int):
    return __query_latest_books(limit, Book.views.desc())


def query_select_book(id: int):
    return select(Book)\
        .where(Book.id == id)\
        .execution_options(populate_existing=True)\
        .options(selectinload(Book.authors_rel))

def query_select_books_review(id:int):
    return select(Review)\
        .where(Review.book == id)\
        .execution_options(populate_existing=True)\
        .options(selectinload(Review.user_rel))

def query_select_user(id: int):
    return select(User).where(User.id == id)

def query_authorization(login: str, password: str):
    return select(User.id).where((User.login == login) and (User.password == Hasher.hash(password)))


def query_select_user_by_password(password: str):
    return select(User).where(User.password == password)


def query_select_user_by_email(email: str):
    return select(User).where(User.email == email)


def query_select_cart(user: int):
    return select(User)\
        .where(User.id == user)\
        .execution_options(populate_existing=True)\
        .options(selectinload(Book.cart_users_rel))
