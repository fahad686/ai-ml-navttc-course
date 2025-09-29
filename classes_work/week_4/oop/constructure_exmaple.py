class Person:
    def __init__(self,): # constructor method  //Dunder method // double underscore method ,Magic method
        print('This is constructor method')
        



newPerson=Person() # object creation


class Vehicle:
    def __init__(self, name, model, color, year): # constructor method  //Dunder method // double underscore method ,Magic method
        self.name_=name
        self.model_=model
        self.color_=color
        self.year_=year
        print(f'Vehicle Name: {self.name_}, Model: {self.model_}, Color: {self.color_}, Year: {self.year_}')
    
    name_='tesla' # class property
car=Vehicle('Civic', '2020', 'Black', 2020) # object creation
# print(car.name)
# print(car.model)
# print(car.color)
# print(car.year)
bike=Vehicle('Honda', '2021', 'Red', 2021) # object creation
# print(bike.name)        
# print(bike.year)
# print(bike.model)
# print(bike.color)



##creating class object
wagon=Vehicle('WagonR', '2022', 'White', 2022)
mercedes=Vehicle('Mercedes', '2023', 'Green', 2028)

print(wagon.name_) #accessing object property
print(mercedes.name_)




#destructive
del wagon
print(wagon.name_) #accessing object property  after deleting object with destruct
