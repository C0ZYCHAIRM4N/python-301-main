# A good way to think about how classes are blueprints of objects is to think of
# an empty form, for example one that you would get at a doctor's office.
# The empty form contains all the placeholders that define what information
# you need to fill to complete the form. If you fill it correctly, then you've
# successfully instantiated a form object, and your completed form now holds
# information that is specific to just you.
# Another patient's form will follow the same blueprint, but hold different info.
# You could say that every patient's filled form instance is part of the same
# empty form blueprint class that the doctor's office provided.
#
# Model such an application form as a Python class below, and instantiate
# a few objects from it.
class ApplicationForm:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

# Instantiate objects from the ApplicationForm class

form1 = ApplicationForm("John Doe", 25, "123 Main St")
form2 = ApplicationForm("Jane Smith", 30, "456 Elm St")
form3 = ApplicationForm("Bob Johnson", 40, "789 Oak St")
