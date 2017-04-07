
import json
import jsonpickle
from Employee import Employee
from Employee import Boss


#def object lists
employees = []
employees.append(Employee("Maikel",5000))
employees.append(Employee("Wouter",5000))
employees.append(Employee("stijn", 1000))
employees.append( Boss("Bert", 1000))



# s = json.dumps(employees.__dict__,default=Employee)
# print(s)

serialized = jsonpickle.encode(employees)
print(serialized)


# Open a file
exportFile = open("export.txt", "w")
exportFile.write( serialized)
exportFile.close()



# f  = FileItem("/foo/bar")
# magic(f)
#
# print ("Hello, Python!")
#
# class MyEncoder(JSONEncoder):
#     def default(self, o):
#         return o.__dict__
#
# MyEncoder().encode(f)
#     '{"fname": "/foo/bar"}'