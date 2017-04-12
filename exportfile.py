
import json
import jsonpickle
import pyaml
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
# jsonpickle.load_backend('simplejson', 'dumps', 'loads', ValueError)
# jsonpickle.set_preferred_backend('simplejson')
# jsonpickle.set_encoder_options('simplejson', sort_keys=True, indent=4)
# jsonpickle.set_encoder_options('json', indent=3, sort_keys=True)
# jsonpickle.set_encoder_options('simplejson', indent=3, sort_keys=True)
jsonpickle.set_encoder_options('json', indent=3)
jsonpickle.set_encoder_options('simplejson', indent=3)
serialized = jsonpickle.encode(employees)
print(serialized)




# Open a file
exportFile = open("export.txt", "w")
exportFile.write( serialized)
exportFile.close()


#yamldump
# yamlData = pyaml.p(Employee("Maikel",5000))
# exportFile = open("export.yaml", "w")
# exportFile.write(yamlData)
# exportFile.close()


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