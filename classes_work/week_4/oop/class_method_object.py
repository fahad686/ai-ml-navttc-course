class Person:
    id=10
    name='Fahad'
    age=25
    country='Pakistan'
    city='Lahore'
    def display(self): # instance method
        print(f'ID: {self.id}, Name: {self.name}, Age: {self.age}, Country: {self.country}, City: {self.city}')
        
        
    def display_name():
        print(f'Name: {Person.name}') 
    @classmethod
    def display_country(cls):
        print(f'Country: {cls.country}')
        


p1=Person()
p1.display() # instance method calling
Person.display_name() # class method calling
Person.display_country() # class method calling