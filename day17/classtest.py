'''Notes on making classes and adding attributes'''

# You can create a new class by typing:
class New_User: # The name is in camel case

    # This is the constructor. This sets certain things to a certain value
    # When its initialized as an object.
    # This creates the init function, which initializes starting attributes.
    # VS code can start you off with a an autofill template
    # The self param is always required, but you can pass in data in the same spot.

    def __init__(self, username, ID):
        # Attributes are variables that the class has.
        # These are styled below, attached to self.
        self.username = username
        self.id = ID
        # you can also initialize a variable without adding it to the params.
        self.following = 0
        self.followers = 0

        # Methods are functions that the class does.
        # The function always requires the "self" param since it needs to
        # know about itself.
        def follow(self, user):
            self.following += 1
            user.followers += 1

user1 = New_User(3, 420)
print(user1.id)
