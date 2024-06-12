# Public members
class MyClass:
    def __init__(self):
        self.public_var = "I am public"

    def public_method(self):
        return "This is a public method"


obj = MyClass()
print(obj.public_var)  # Output: I am public
print(obj.public_method())  # Output: This is a public method


# Protected members
class MyClass:
    def __init__(self):
        self._protected_var = "I am protected"

    def _protected_method(self):
        return "This is a protected method"


obj = MyClass()
print(obj._protected_var)  # Output: I am protected
print(obj._protected_method())  # Output: This is a protected method

# Private members

class MyClass:
    def __init__(self):
        self.__private_var = "I am private"

    def __private_method(self):
        return "This is a private method"

    def get_private_var(self):
        return self.__private_var

obj = MyClass()
# Accessing private member directly will result in an attribute error
# print(obj.__private_var)  # Raises AttributeError
# print(obj.__private_method())  # Raises AttributeError

# Accessing private member through a public method
print(obj.get_private_var())  # Output: I am private
