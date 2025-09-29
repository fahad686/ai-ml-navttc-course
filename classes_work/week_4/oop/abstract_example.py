#Animal is an abstract class and Dog, Cat, Lion are concreate classes
#abstract class can not be instanced


# pass keyword in Python is a null operation; it does nothing when executed. Its primary
# purpose is to serve as a placeholder where a statement is syntactically required but no
# actual code execution is desired or necessary at that moment.


# User case // when we want to prevent missing concerete class mehtod of abstract classes use

from abc import ABC ,abstractmethod  ## abc is an python library ,
#abstract clsass
class Animal(ABC):
    @abstractmethod   ## decorator
    def sound(self):
        pass           # give for preventing error

#subclass / concreate class
class Dog(Animal):
    def sound(self):
        print('Dog barking.....')



#concreate class
class Cat(Animal):
    def sound(self):
        print('mawo mawo...')


#dog instance
dog=Dog()
dog.sound()

# cat instance

cat=Cat()
cat.sound()