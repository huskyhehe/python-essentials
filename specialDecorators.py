# @staticmethod, @classmethod, and @property

class Cellphone:
    def __init__(self, brand, number):
        self.brand = brand
        self.number = number

    def get_number(self):
        return self.number

    @staticmethod
    def get_emergency_number():
        return "911"

    @classmethod
    def iphone(cls, number):
        _iphone = cls("Apple", number)
        print("An iPhone is created.")
        return _iphone


# @staticmethod
# a static method is a method that does not require the creation of an instance of a class.
# For Python, it means that the first argument of a static method is not self, but a regular positional or keyword argument.
# Also, a static method can have no arguments at all
Cellphone.get_emergency_number()  # '911', no need to create a instance of Cellphone


# @classmethod
#  the @classmethod decorator  requires the class itself as the first argument, which is written as cls.
#  A class method normally works as a factory method and returns an instance of the class with supplied arguments. Class methods are very commonly used in third-party libraries.
#  However, it doesn't always have to work as a factory class and return an instance.

iphone = Cellphone.iphone("1112223333")     # An iPhone is created.
iphone.get_number()                         # "1112223333"
iphone.get_emergency_number()               # "911"
