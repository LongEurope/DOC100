#How to create your own class
#Constructor (also called initialising) is a part of a class 
#Every word of a class should have no spaces and be capitalised (e.g. PascalCase)

class User:
    def __init__(self, user_id, username):  #Constructor, ATTRIBUTES
        self.id = user_id
        self.username = username
        self.followers = 0 #You can also use integers and string and stuff like that instead of parameters
        self.following = 0
    def follow(self, user): #METHODS always needs a self parameter
        user.followers += 1
        self.following += 1

user_1 = User('001', 'angela')

user_2 = User('002', 'jack')

user_1.follow(user_2)

print(user_1.following)
print(user_1.followers)
print(user_2.following)
print(user_2.followers)