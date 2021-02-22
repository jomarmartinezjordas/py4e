'''
Week 1: Object Oriented Python

Unicode Characters and Strings
ord() - tells the numeric value of a simple ASCII Characters

Object Oriented
- a program is made up of many cooperating objects
- instead of being the 'whole program' - each object is a little island within the program and cooperatively working with other objects
- a program is made up of one of more objects working together

Object
- a bit of self-contained code and data
- key aspect of the object approach is to break the problem into smaller understandable parts (divide and conquer)
- objects have boundaries that allow us to ignore un-needed detail

Class - a template
Method or Message - a defined capability of a class / function within a class
Field or Attribute - a bit of date in a class / variable within a class
Object or Instance - a particular instance of a class / particular instance of a class

dir() - lists capabilities

constructor - sets up some instance variables to have the proper initial values when the object is created / code that runs when object is created
destructor -

inhertance - 'store and reuse', 'sub-classes'
           -  enables to reuse an existing class and inherit all the capabilities of an existring class and then add our own little bit to make our new    class
           - ability to extend a class to make a new class
'''
class PartyAnimal:
   x = 0

   def party(self) :
     self.x = self.x + 1
     print("So far",self.x)

an = PartyAnimal()
an.party()
an.party()
an.party()
PartyAnimal.party(an)

class PartyAnimal:
   x = 0

   def party(self) :
     self.x = self.x + 1
     print("So far",self.x)

an = PartyAnimal()
print ("Type", type(an))
print ("Dir ", dir(an))
print ("Type", type(an.x))
print ("Type", type(an.party))


class PartyAnimal:
   x = 0

   def __init__(self):
     print('I am constructed')

   def party(self) :
     self.x = self.x + 1
     print('So far',self.x)

   def __del__(self):
     print('I am destructed', self.x)

an = PartyAnimal()
an.party()
an.party()
an = 42
print('an contains',an)

class PartyAnimal:
   x = 0
   name = ''
   def __init__(self, nam):
     self.name = nam
     print(self.name,'constructed')

   def party(self) :
     self.x = self.x + 1
     print(self.name,'party count',self.x)

s = PartyAnimal('Sally')
j = PartyAnimal('Jim')

s.party()
j.party()
s.party()
