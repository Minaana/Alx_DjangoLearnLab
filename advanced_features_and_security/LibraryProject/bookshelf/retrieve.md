# Retrieve Operation

## Command:
```python
from bookshelf.models import Book

# Retrieve the book instance
book = Book.objects.get(title="1984")
print("Retrieved Book:", book)