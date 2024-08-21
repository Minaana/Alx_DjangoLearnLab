# Create Operation

## Command:
```python
from bookshelf.models import Book

# Create a new Book instance
new_book = Book(title="1984", author="George Orwell", publication_year=1949)
new_book.save()

# Confirm creation
print("Created Book:", new_book)