class Book:
    def __init__(self, title, author, isbn, copies):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.copies = copies

    def __str__(self):
        return f"{self.title}, {self.author},{self.isbn}, {self.copies}"
    
    def borrow(self):
        if self.copies<=0:
            raise ValueError("No copies available")

        self.copies -= 1
        print(f"Borrowed {self.title}, Remaining copies: {self.copies}")

    def return_book(self):
        self.copies += 1
        print(f"Returned {self.title}, copies now: {self.copies}")

class Ebook(Book):
    def __init__(self,title, author, isbn, copies,file_size):
        super().__init__(title, author, isbn, copies)
        self.file_size = file_size

    def __str__(self):
        return f"{self.file_size} MB"
    
    def borrow(self):
        print(f"ebooks are unlimited, no change in copies")

    
class Library:
    def __init__(self):
        self.__books = []

    def add_books(self,book):
        self.__books.append(book)

    def find_books_by_author(self,author):
        return [b for b in self.__books if b.author.lower() == author.lower()]
    
    def __len__(self):
        return len(self.__books)
    
    def __getitem__(self, index):
        return self.__books[index]
    
if __name__ == "__main__":
    b1 = Book("book1", "author1", "fiction", 3)
    b2 = Book("book2", "author1", "fiction", 13)

    e1 = Ebook("ebook1", "author1", "drama", 3, 5)
    e2 = Ebook("ebook2", "author2", "drama", 4, 5)

    library = Library()
    library.add_books(b1)
    library.add_books(b2)
    library.add_books(e1)
    library.add_books(e2)
    for book in library:
        print(book)

    try:
        b1.borrow()
        b1.borrow()
        b1.borrow()
    except ValueError as e:
        print(e)

    b1.return_book()
    e1.borrow()

    results = library.find_books_by_author("author1")
    for r in results:
        print(r)

    print(f"{len(library)}")
    print(f"{library[1]}")

    