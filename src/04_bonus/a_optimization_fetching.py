"""
F1: Too Many Arguments

Functions should have a small number of arguments. No argument is best, followed by one, two, and three.

More than three is very questionable and should be avoided with prejudice.

Docs:
    https://moderatemisbehaviour.github.io/clean-code-smells-and-heuristics/functions/f1-too-many-arguments.html
"""

import requests


class QueryBuilder:
    def __init__(self, book_title):
        self._book_title = book_title
        self._page = None
        self._limit = None
        self._fields = None

    def add_page(self, page):
        self._page = page
        return self

    def add_limit(self, limit):
        self._limit = limit
        return self

    def add_fields(self, fields):
        self._fields = fields
        return self

    def build(self):
        return {
            "q": self._book_title,
            "page": self._page,
            "limit": self._limit,
            "fields": self._fields,
        }


def search_books(params):
    """
    Fetches a list of books from the OpenLibraryAPI based on a book title
    """
    result = requests.get("http://openlibrary.org/search.json", params=params)
    books = result.json()
    return books


def get_books(book_title):
    """
    Get a list of books based on the title
    Args:
        book_title:

    Returns:

    """
    fields_to_fetch = "has_fulltext,key,author_name,title"

    query_builder = QueryBuilder(book_title).add_fields(fields_to_fetch)

    params = query_builder.build()
    books = search_books(params)

    return books["docs"]


def example():
    book_title = "Microservices"
    name_to_find = "Sam Newman"
    for book in get_books(book_title):
        authors_name = book.get("author_name")
        if authors_name and name_to_find in authors_name:
            print(book)
            break


if __name__ == "__main__":
    example()
