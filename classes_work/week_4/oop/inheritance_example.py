# Multiple inheritance
# from classes_work.week_4.oop.constructure_exmaple import Vehicle


class Animal:
    def speak(self):
        print("animal speaks....")
class Dog(Animal):
    def bark(self):
        print('dog barking')
class Sparrow(Dog):
    def fly(self):
        print('flying.....')




obj=Sparrow()
obj.fly()
obj.bark()
obj.speak()


print('----------- Multiple inheritance mean multiple parents --------')

# Multiple Inheritance

class Vehicle:
    def speed(self):
        print('Vehicle running..')
class Specious:
    def runs(self):
        print('Specious running...')

class Calculating(Vehicle,Specious):
    def accelrate(self):
        print('accelrations...')

obj=Calculating()
obj.accelrate()
obj.runs()

print('------------------Method Overloading........')

##### method overriding and overloading
#mehtod overloading
class Calculator:
    def add(self, a, b=0): ### default parameter method
        return a + b


calc = Calculator()
print(calc.add(5))  # b defaults to 0
print(calc.add(5, 3))  # b is 3


#Variable-length arguments (*args and `: kwargs`):** These allow a method
# to accept an arbitrary number of positional or keyword arguments.
class Greeter:
    def greet(self, *names):
        if not names:
            print("Hello!")
        else:
            for name in names:
                print(f"Hello, {name}!")


greeter = Greeter()
greeter.greet()
greeter.greet("Alice", "Bob")



#--------------------- Method overriding---------------------#
print('--------Method overriding -----------')

class Animal:
    def speak(self):
        print("Generic animal sound")

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        super().speak() # Call parent's speak method
        print("Meow!")

animal = Animal()
dog = Dog()
cat = Cat()

animal.speak()
dog.speak()
cat.speak()