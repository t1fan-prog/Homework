from prettytable import PrettyTable


class Author:

    def __init__(self, name, country, birthday, books: list):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = books

    def __str__(self):
        list_of_books = ', '.join(self.books)
        x = PrettyTable(["Name", "Country", "Birthday", "List of books"])
        x.add_row([self.name, self.country, self.birthday, list_of_books])
        return f'{x}'


class Library:

    def __init__(self, name):
        self.name = name
        self.books = []
        self.authors = []

    def new_book(self, name: str, year: int, author: Author):
        """returns an instance of Book class and adds the book to the books list for the current library"""
        local_author = Book(name, year, author)
        self.books.append(local_author)
        self.authors.append(local_author.author)
        return Book(name, year, author)

    def group_by_author(self, author: Author):
        """returns a list of all books grouped by the specified author"""
        return [x for x in self.books if author == x.author]

    def group_by_year(self, year: int):
        """returns a list of all the books grouped by the specified year"""
        return [x for x in self.books if year == x.year]

    def __str__(self):

        x = PrettyTable(["Books", "Authors"])
        for i in self.books:
            x.add_row([i.name, i.author.name])

        y = PrettyTable(["Name", "Country", "Birthday", "List of books"])
        for i in self.authors:
            y.add_row([i.name, i.country, i.birthday, i.books])

        return f'Name: {self.name}\n\nBooks:\n{x}\n\nAuthors:\n{y}'


class Book:
    number_of_books = 0

    def __init__(self, name, year, author: Author):
        self.name = name
        self.year = year
        self.author = author
        Book.number_of_books += 1

    def __str__(self):
        some_dict = {"Name": self.name, "Year": self.year, "Author": self.author.name}
        return f'{some_dict}'


some_author = Author("Daniel Defoe", "England", "06.05.1660", ["Robinson Crusoe", "A Journal of the Plague Year",
                                                               "Moll Flanders"])
some_library = Library("My library's name")
some_library.new_book("Кошка, которая видела всё", 2019, some_author)


list_of_books_by_author = some_library.group_by_author(some_author)

list_of_books_by_year = some_library.group_by_year(2019)

""" Как получить список книг"""
for i in list_of_books_by_year:
    print(i)

print(some_author)
print(some_library)
