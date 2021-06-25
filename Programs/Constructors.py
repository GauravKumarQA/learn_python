class Constructors:
    """This file will explain what are the constructors and we can use them efficiently"""

    def __init__(self):
        print(
            "You don't call me, i visit you whenever you create a new object of my class, You can use constructor for initializing the class members")
        self.first_variable = "I am first variable"

    def method_of_class(self):
        print(self.first_variable)


# Creating object and calling method of a class
object_of_class = Constructors()
object_of_class.method_of_class()


class ParameterisedConstructor:

    def __init__(self, variable1, variable2):
        self.variable1 = variable1
        self.variable2 = variable1

    def method_of_class(self):
        print(self.variable1, self.variable2)


# Creation of object and call method of the class
object_of_class = ParameterisedConstructor("variable1_value", "variable2_value")
object_of_class.method_of_class()
