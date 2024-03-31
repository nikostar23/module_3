class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __repr__(self):
        return f'Book({self.title}, {self.author})'

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        new_book = Book(title, author)
        self.books.append(new_book)
        return self

    def remove_book(self, title):
        self.books = [book for book in self.books if book.title != title]
        return self

    def __getitem__(self, title):
        for book in self.books:
            if book.title == title:
                return book
        raise KeyError(f'Book with title {title} not found')
    
    def __contains__(self, title):
        return any(book.title == title for book in self.books)

    def add_book(self, title, author):
        new_book = Book(title, author)
        self.books.append(new_book)
        return self

    def remove_book(self, title):
        self.books = [book for book in self.books if book.title != title]
        return self

# Пример использования
library = Library()
library.add_book("Война и мир", "Лев Толстой").add_book("Преступление и наказание", "Федор Достоевский")
print(library.books)

library.remove_book("Преступление и наказание")
print(library.books)

print(library['Война и мир'])

print("Преступление и наказание" in library)

print("Война и мир" in library)