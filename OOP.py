"""OOP.py"""

class MainClass:
    def __init__(self, text=""):
        self.text = text

    def set_text(self, text=""):
        self.text = text

    def get_text(self):
        return self.text

    def display_text(self):
        print(f"Text: {self.text}")


class DerivedClass(MainClass):
    def __init__(self, text, number):
        super().__init__(text)
        self.number = number

    def set_number(self, number):
        self.number = number

    def get_number(self):
        return self.number

    def display_data(self):
        print(f"Text: {self.text}, Number: {self.number}")


if __name__ == "__main__":
    main_obj = MainClass("Hello, world!")
    main_obj.display_text()

    main_obj.set_text("New text")
    main_obj.display_text()

    derived_obj = DerivedClass("Hello from derived class", 42)
    derived_obj.display_data()

    derived_obj.set_number(99)
    derived_obj.display_data()
