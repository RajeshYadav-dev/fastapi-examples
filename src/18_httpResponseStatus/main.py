'''
The same way you can specify a response model, you can also declare the HTTP status code used for the response with the parameter status_code in any of the path operations:
@app.get()
@app.post()
@app.put()
@app.delete()
etc.

1. GET (Retrieve data)
200 OK — The request was successful, and the data is returned.
404 Not Found — The requested resource doesn’t exist.

2. POST (Create data)
201 Created — The resource was successfully created.
400 Bad Request — Invalid input or request data.
409 Conflict — Duplicate data (e.g., trying to create a user that already exists).

3. PUT (Update data)
200 OK — Resource was updated successfully.
204 No Content — Update was successful, but there's no content to return.
400 Bad Request — Invalid input.
404 Not Found — Resource to update doesn’t exist.

4. DELETE (Remove data)
204 No Content — Resource was deleted successfully.
404 Not Found — Resource to delete doesn’t exist.
403 Forbidden — The user doesn’t have permission to delete the resource.
'''

from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from typing import List

router = APIRouter()



# Book schema
class Book(BaseModel):
    id: int
    title: str
    author: str
    price: float

# Sample in-memory data (for testing)
books: List[Book] = []

# GET all books
@router.get("/books", response_model=List[Book], status_code=status.HTTP_200_OK)
def get_books():
    """
    Endpoint to retrieve a list of all books.
    GET Request
    /books

    Returns:
        List[Book]: A list of all books available.
    """

    return books

# GET a book by ID
@router.get("/books/{book_id}", response_model=Book, status_code=status.HTTP_200_OK)
def get_book(book_id: int):
    """
    Endpoint to retrieve a book by its ID.
    GET Request
    /books/{book_id}
    
    Args:
        book_id (int): The ID of the book to retrieve.
        
    Returns:
        Book: The book with the specified ID if found.
        
    Raises:
        HTTPException: If the book is not found, raises a 404 Not Found error.
    """

    for book in books:
        if book.id == book_id:  # Access attributes directly
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")

# POST (Create a new book)
@router.post("/books", response_model=Book, status_code=status.HTTP_201_CREATED)
def create_book(book: Book):
    """
    Endpoint to create a new book.
    POST Request
    /books
    
    Args:
        book (Book): The book to be created.
        
    Returns:
        Book: The created book.
        
    Raises:
        HTTPException: If the book with the same ID already exists, raises a 409 Conflict error.
    """
    if any(b.id == book.id for b in books):  # Check by attribute
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Book with this ID already exists")
    books.append(book)  # Append the Book instance directly
    return book

# PUT (Update a book)
@router.put("/books/{book_id}", response_model=Book, status_code=status.HTTP_200_OK)
def update_book(book_id: int, updated_book: Book):
    """
    Endpoint to update a book by its ID.
    PUT Request
    /books/{book_id}

    Args:
        book_id (int): The ID of the book to update.
        updated_book (Book): The updated book details.

    Returns:
        Book: The updated book if found.

    Raises:
        HTTPException: If the book is not found, raises a 404 Not Found error.
    """
    for index, book in enumerate(books):
        if book.id == book_id:
            books[index] = updated_book
            return updated_book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")

# DELETE a book
@router.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int):
    """
    Endpoint to delete a book by its ID.
    DELETE Request
    /books/{book_id}

    Args:
        book_id (int): The ID of the book to delete.

    Returns:
        None

    Raises:
        HTTPException: If the book is not found, raises a 404 Not Found error.
    """
    for index, book in enumerate(books):
        if book.id == book_id:
            books.pop(index)
            return
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
