from relationship_app.models import Author, Book, Library, Librarian

def sample_queries():
    # Query all books by a specific author
    author_name = "Author Name"
    author = Author.objects.get(name=author_name)
    books_by_author = Book.objects.filter(author=author)
    print(f"Books by {author_name}: {[book.title for book in books_by_author]}")

    # List all books in a library
    library_name = "Library Name"
    library = Library.objects.get(name=library_name)
    books_in_library = library.books.all()
    print(f"Books in {library_name}: {[book.title for book in books_in_library]}")

    # Retrieve the librarian for a library
    library_name = "Library Name"
    librarian = Librarian.objects.get(library__name=library_name)  # Using the library field of Librarian
    print(f"Librarian of {library_name}: {librarian.name}")

if __name__ == "__main__":
    sample_queries()
