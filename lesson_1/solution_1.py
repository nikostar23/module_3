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

    def __getitem__(self, index):
        if isinstance(index, int):
            if index < 0 or index >= len(self.books):
                raise IndexError("Index out of range")
            return self.books[index]
        elif isinstance(index, slice):
            return self.books[index.start:index.stop:index.step]
        elif isinstance(index, str):
            index = next((i for i, book in enumerate(self.books) if book.title == index), None)
            if index is None:
                raise KeyError("Book not found")
            return self.books[index]
        else:
            raise TypeError("Index must be an integer, a slice, or a string")
    
    def __contains__(self, title):
        return any(book.title == title for book in self.books)

# Пример использования
library = Library()

library.add_book("Война и мир", "Лев Толстой").add_book("Преступление и наказание", "Федор Достоевский")
library.add_book("Детство", "Лев Толстой").add_book("Братья Карамазовы", "Федор Достоевский")
print(library.books)

library.remove_book("Преступление и наказание")
print(library.books)

print(library['Война и мир'])

print("Преступление и наказание" in library)

print("Война и мир" in library)

print(library[0])

print(library[1:])