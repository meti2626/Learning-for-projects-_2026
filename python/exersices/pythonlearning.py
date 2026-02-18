
# with open('python\exersices\pythonlearning.txt') as file_object:
#     contents = file_object.read()
# print(contents)  


filename = 'python\\exersices\\pythonlearning.txt'

with open(filename) as file_object:
  lines = file_object.readlines()

for line in lines:
   print(line.rstrip())  

