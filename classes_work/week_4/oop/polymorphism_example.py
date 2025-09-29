# Base Class
class Person:
    def __init__(self, name, id_number):
        self.name = name
        self.id_number = id_number

    def register(self):
        """
        A common interface for registration.
        This method will be overridden by child classes.
        """
        raise NotImplementedError("Subclass must implement abstract method")

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"ID Number: {self.id_number}")
        print("-" * 20)

# Derived Class for Student
class Student(Person):
    def __init__(self, name, id_number, major):
        super().__init__(name, id_number)
        self.major = major

    def register(self):
        """Student-specific registration logic."""
        print(f"Student {self.name} is registering for courses in the {self.major} department.")

# Derived Class for Teacher
class Teacher(Person):
    def __init__(self, name, id_number, department):
        super().__init__(name, id_number)
        self.department = department

    def register(self):
        """Teacher-specific registration logic."""
        print(f"Teacher {self.name} is registering with the {self.department} department.")

# Polymorphic function to process registration for any Person object
def process_registration(person_object):
    """Takes any object with a .register() method and calls it."""
    person_object.display_info()
    person_object.register()

# Create objects
student1 = Student("Alice", "S1001", "Computer Science")
teacher1 = Teacher("Mr. Smith", "T2002", "Mathematics")
student2 = Student("Bob", "S1003", "Physics")

# Use the polymorphic function
print("Processing student registration:")
process_registration(student1)

print("\nProcessing teacher registration:")
process_registration(teacher1)

print("\nProcessing another student registration:")
process_registration(student2)
