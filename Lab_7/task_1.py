from typing import Union


class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"
# базовый и дочерний класс ничем не отличается, значит метод str можно унаследовать

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"

    @property
    def name(self) -> str:
        return self._name

    @property
    def author(self) -> str:
        return self._author


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r} )"
# атрибут pages отсутствует в базовом классе

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, pages: int) -> None:
        if not isinstance(pages, int):
            raise TypeError
        if not pages > 0:
            raise ValueError
        self._pages = pages
# Свойство-сеттер определяется после свойства-геттера


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r} )"
# атрибут duration отсутствует в базовом классе

    @property
    def duration(self) -> Union[int, float]:
        return self._duration

    @duration.setter
    def duration(self, duration: Union[int, float]) -> None:
        if not isinstance(duration, (int, float)):
            raise TypeError
        if not duration > 0:
            raise ValueError
        self._duration = duration