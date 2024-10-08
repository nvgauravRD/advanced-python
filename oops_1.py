class Person:
    def __init__(self, name, age, salary):
        # public properties
        self.name = name # property 1
        self.age = age # property 2

        # private property
        self._salary = salary # property 3

    # methods of class
    # prints person details
    def printPerson(self):
        print(f"The person name is {self.name} and age {self.age}")
    
    # gets salary of the person
    def getSalary(self):
        print(f"{self.name}'s income is {self._salary}")

    @classmethod
    def createPerson(cls, name, email, salary):
        return cls(name, email, salary)
    
    @staticmethod
    def addTwoNum(num1, num2):
        return num1 + num2

# class Person contains 2 properties name and age
# name=ram, age=20, salary=10_000
# note: 10_000 is similar to 10000
ram = Person("Ram", 20, 10_000)

# methods of class can be accessed using . method
ram.printPerson() # The person name is Ram and age 20
ram.getSalary() # Ram's income is 10000

# to access class with different instanciating methods using @classmethod
Person.createPerson("Ravi",42,15_000).printPerson()
# o/p: The person name is Ravi and age 42

# to just use functions of class and dont use actual properties
# use @staticmethod
print(Person.addTwoNum(5, 6))
# o/p: 11




