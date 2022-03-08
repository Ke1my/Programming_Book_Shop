from dataclasses import dataclass, field
from email.policy import default
from serde import serde
from serde.toml import from_toml


@serde
@dataclass
class Book:
    name: str
    authors: list[str]
    price: int
    rating: float
    description: str

    # Detailed info
    code: int
    publisher: str
    year: int
    pages: int
    isbn: str


class Store:
    inner: dict[int, Book]

    def __init__(self):
        self.inner = dict()

        for i in from_toml(Books, open('books.toml').read()).books:
            self.inner[i.code] = i

    def get_book(self, id: int):
        self.inner.get(id, id)


@serde
class Books:
    books: list[Book]
