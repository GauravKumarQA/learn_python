class ClassName:
    """This is the documentation string of the class"""

    def method_name(self):
        """This is method documentation string, In Methods,the first and the mandatory parameter is self.
        Self is a keyword which is the used for the instance of the current object of the class.self
        doest not require when method is not a part of any class.To access this object in the other py file
        we need to import class, create object and call method"""


# To print the documentation of the class
print(ClassName().__doc__)

#  To create an object of the class
object_of_class = ClassName()
# Call a method of a class
object_of_class.method_name()
'''You can not access the method of a class without creating an object'''


def method_outside_class():
    """You can access methods which are outside the class by calling there name directly.If you want to access the
    method in other py file, you need to import the file and call the name directly"""
    print("I am a method outside the class")


# Calling a method which is outside the class
method_outside_class()

# Deletion of object, use del keyword to delete an object
del object_of_class



