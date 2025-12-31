from fastapi import FastAPI

app = FastAPI()
BOOKS = [
    {"title": "dance india dance", "author": "did", "category": "entertainment"},
    {"title": "legends of story", "author": "abc", "category": "drama"},
    {"title": "aaaa", "author": "bbbb", "category": "cccc"},
    {"title": "qqqq", "author": "bbbb", "category": "abccc"},
    {"title": "new book", "author": "did", "category": "test"},
    {"title": "test", "author": "test", "category": "test"},
]


@app.get("/")
def read_main():
    return {"message": "Hello World"}


@app.get("/books")
async def books():
    return BOOKS


@app.get("/books/{author}")
async def get_books_by_author(author):
    books_to_return = []
    for book in BOOKS:
        if book.get("author") == author:
            books_to_return.append(book)
    return books_to_return

@app.delete("/books/delete/{title}")
async def delete_book_by_title(title):
    for book in BOOKS:
        if book.get('title')== title:
            BOOKS.remove(book)