"""

>_  Inheritance, inherit the functionality of other classes along with their own functionality. That's way you got the clean & reusable code also...

"""


class Scientist():
    def sign_in(self):
        return "\n\t Welcome, Signed-In Successfully...\n"

    # You don't need to use __init__ function first if, you don't want any variables...


# Here, we inherited the functionality of Scientist in a Creator...
class Creator(Scientist):
    def __init__(self, name, research_area):
        self.name = name
        self.research_area = research_area

    def intro(self):
        print(f"\tIt's {self.name},\n \tResearch Area - {self.research_area}")


user2 = Creator("Mr. Skywalker", "Spacefaring Civilisation")
print(user2.intro())
print(user2.sign_in())


# Explorer
class Explorer(Scientist):
    pass


user1 = Explorer()
print(user1.sign_in())


# Destructor
class Destructor():
    pass


"""
>_ Inheritance-2 ;

"""

# isinstance(o, t)
