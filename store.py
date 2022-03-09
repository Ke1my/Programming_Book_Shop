from dataclasses import dataclass
from serde import serde
from serde.toml import from_toml

@serde
@dataclass
class Book:
    # Класс контейнер для информации о книге
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
    # Класс - хранилище с книгами
    inner: dict[int, Book]

    def __init__(self):
        self.inner = dict()

        # Парсинг информации о книгах
        for i in from_toml(Books, open('books.toml').read()).books:
            self.inner[i.code] = i

    def get_book(self, id: int) -> Book | None:
        return self.inner.get(int(id))

@serde
class Books:
    # Доп. класс для парсинга
    books: list[Book]
