#oop

# class BigObject: #class
#   pass

# obj1 = BigObject() #instanciate
# obj2 = BigObject() #instanciate
# obj3 = BigObject() #instanciate

# print(type(None))
# print(type(True))
# print(type(5))
# print(type(5.5))
# print(type('hi'))
# print(type([]))
# print(type(()))
# print(type({}))
# print(type(obj1))


class PlayerCharacter:
  # Class Object Attribute
   def __init__(self, name , age):   
       self.name = name #attributes
       self.age = age

def shout(self):
   
 @classmethod
 def adding_things(cls, num1, num2):
    return cls('Teddy', num1 + num2)

# player1 = PlayerCharacter('tom', 10)

player3 = PlayerCharacter.adding_things(2,3)
print(player3.age)

