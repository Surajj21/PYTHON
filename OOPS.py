class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def getSalary(self):
        print(self.salary)

rohan = Employee("Rohan", "3456")
print("Employe name is: ",rohan.name)
print("salary of",rohan.name,rohan.salary)
rohan.getSalary()


harry = Employee("Harry", "50000")
print("Employe name is: ",harry.name)
print("salary of",harry.name, harry.salary)
harry.getSalary()