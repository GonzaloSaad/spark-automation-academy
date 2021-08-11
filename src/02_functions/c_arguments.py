"""
F1: Too Many Arguments

Functions should have a small number of arguments. No argument is best, followed by one, two, and three.

More than three is very questionable and should be avoided with prejudice.

Docs:
    https://moderatemisbehaviour.github.io/clean-code-smells-and-heuristics/functions/f1-too-many-arguments.html
"""

import requests


def search_books(book_title, page, limit, fields):
    """
    Fetches a list of books from the OpenLibraryAPI based on a book title
    """
    params = {"q": book_title, "page": page, "limit": limit, "fields": fields}
    result = requests.get("http://openlibrary.org/search.json", params=params)
    books = result.json()
    print(books)


def example():
    book_title = "Microservices"
    page = 1
    limit = 5
    fields_to_fetch = "has_fulltext,key,author_name,title"
    search_books(book_title, page, limit, fields_to_fetch)


if __name__ == "__main__":
    example()
