"""
Chapter 3 - Have No Side Effects

Side effects are lies.

Your function promises to do one thing, but it also does other hidden things.
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
