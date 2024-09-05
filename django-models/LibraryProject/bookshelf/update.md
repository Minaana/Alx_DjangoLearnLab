# Update Operation

## Command:
```python
from bookshelf.models import Book

# Retrieve the book instance
book = Book.objects.get(title="1984")

# Update the title
book.title = "Nineteen Eighty-Four"
book.save()

# Confirm update
updated_book = Book.objects.get(title="Nineteen Eighty-Four")
print("Updated Book:", updated_book)
