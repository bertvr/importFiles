
import json
import jsonpickle
import pyaml
from Employee import Employee
from Employee import Boss


# Open a file
importFile = open("export.txt", "r")
serialized = importFile.read()
importFile.close()


print(serialized)

employees = jsonpickle.decode(serialized)

print(employees)
employees[0].displayEmployee()
employees[1].displayEmployee()
employees[2].displayEmployee()
employees[1].displayEmployeeHiddenAtribute()
employees[1].displayCount()


