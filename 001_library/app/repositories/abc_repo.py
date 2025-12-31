from abc import ABC, abstractmethod


class BookRepository(ABC):
    """abstract class for book related repository"""

    @abstractmethod
    def get_all_books():
        pass

    @abstractmethod
    def get_book_by_id(id: str):
        pass

    @abstractmethod
    def delete_book_by_id(id: str):
        pass

    @abstractmethod
    def update_book(book):
        pass

    @abstractmethod
    def get_all_books_by_author(author: str):
        pass
