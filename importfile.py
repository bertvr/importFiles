# from "file" import "class"
from Employee import Employee
from Employee import Boss


print ("Hello, Python!")





#print dictionarys
dict = {'Name': 'Zara', 'Age': 20, 'Class': 'First'}
for emp in dict:
    print(emp + " => " +  str(dict[emp]))


#range for for-loops
for i in range(1,12,1):
    print ( "range: " + str(i))


#def object lists
employees = []
employees.append(Employee("Maikel",5000))
employees.append(Employee("Wouter",5000))
employees.append(Employee("stijn", 1000))
employees.append( Boss("Bert", 1000))

print(employees)

employees[0].displayEmployee()
employees[1].displayEmployee()
employees[2].displayEmployee()
employees[1].displayEmployeeHiddenAtribute()
employees[1].displayCount()


print ("Employee.__doc__:", Employee.__doc__)
print ("Employee.__name__:", Employee.__name__)
print ("Employee.__module__:", Employee.__module__)
print ("Employee.__bases__:", Employee.__bases__)
print ("Employee.__dict__:", Employee.__dict__ )


