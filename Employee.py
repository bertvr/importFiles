
class Employee:
    # 'Common base class for all employees'
    empCount = 0
    __hiddenatribute__ = 10

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)

    def displayEmployeeHiddenAtribute(self):
        print("    __hiddenatribute__  : ", self.    __hiddenatribute__ )

class Boss(Employee):
    def displayEmployee(self):
        print("Boss Name : ", self.name, ", Salary: ", self.salary)