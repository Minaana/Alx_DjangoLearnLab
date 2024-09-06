# Create Operation

## Command:
```python
from bookshelf.models import Book

# Create a new Book instance using `Book.objects.create`
new_book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

# Confirm creation
print("Created Book:", new_book)
