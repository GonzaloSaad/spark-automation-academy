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
    print(books)
    return books


def example():
    book_title = "Microservices"
    page = 1
    limit = 5
    fields_to_fetch = "has_fulltext,key,author_name,title"

    query_builder = (
        QueryBuilder(book_title)
        .add_page(page)
        .add_limit(limit)
        .add_fields(fields_to_fetch)
    )

    params = query_builder.build()
    books = search_books(params)
    print(f"I got {len(books)} books!")


if __name__ == "__main__":
    example()
