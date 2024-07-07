"""work2.py"""

class Book:
    def __init__(self, name, year, genre, author, price):
        self.name = name
        self.year = year
        self.genre = genre
        self.author = author
        self.price = price
    
    def input(self, name, year, genre, author, price):
        self.name = name
        self.year = year
        self.genre = genre
        self.author = author
        self.price = price
    
    def output(self):
        print(f"Name: {self.name}",
         f"Year: {self.year}",
          f"Genre: {self.genre}",
           f"Author: {self.author}",
            f"Price: {self.price}",
             "",
             sep="\n")

    def get_name(self):
        return self.name

    def get_year(self):
        return self.year

    def get_genre(self):
        return self.genre

    def get_author(self):
        return self.author

    def get_price(self):
        return self.price

    def set_name(self, name):
        self.name = name

    def set_year(self, year):
        self.year = year

    def set_genre(self, genre):
        self.genre = genre

    def set_author(self, author):
        self.author = author

    def set_price(self, price):
        self.price = price




if __name__ == "__main__":
    book = Book("Harry Potter and Gifts of Death I", 2007, "Fantasy", "J. K. Rouling", 5000)
    book.output()
    book.input("The Town Where Only I Am Missing", 2012, "Seinen", "Sambe Kei", 7500)
    book.output()
    print(book.get_author())
    book.set_year(2010)
    book.output()
