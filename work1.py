"""work1.py"""

class Car:
    def __init__(self, name, year, brand, ed, color, price):
        self.name = name
        self.year = year
        self.brand = brand
        self.ed = ed
        self.color = color
        self.price = price
    
    def input(self, name, year, brand, ed, color, price):
        self.name = name
        self.year = year
        self.brand = brand
        self.ed = ed
        self.color = color
        self.price = price
    
    def output(self):
        print(f"Name: {self.name}",
         f"Year: {self.year}",
          f"Brand: {self.brand}",
           f"Engine displacement: {self.ed}",
            f"Color: {self.color}",
             f"Price: {self.price}",
              "",
             sep="\n")

    def get_name(self):
        return self.name

    def get_year(self):
        return self.year

    def get_brand(self):
        return self.brand

    def get_engine_displacement(self):
        return self.ed

    def get_color(self):
        return self.color

    def get_price(self):
        return self.price

    def set_name(self, name):
        self.name = name

    def set_year(self, year):
        self.year = year

    def set_brand(self, brand):
        self.brand = brand

    def set_engine_displacement(self, ed):
        self.ed = ed

    def set_color(self, color):
        self.color = color

    def set_price(self, price):
        self.price = price




if __name__ == "__main__":
    car = Car("Model S", 2020, "Tesla", 2.0, "Red", 79999)
    car.output()
    car.input("LaFerarri", 2014, "Ferarri", 4.2, "Red-Yellow", 599999)
    car.output()
    print("\n", car.get_engine_displacement())
    car.set_color("Dark-Red")
    car.output()
