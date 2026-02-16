# with open('python\pi_digits.txt') as file_object:
#     contents = file_object.read()
# print(contents)



# import os

# here = os.path.dirname(__file__)
# file_path = os.path.join(here, 'pi_digits.txt')
# with open(file_path) as file_object:
#     contents = file_object.read()
# print(contents)


# filename = 'python\pi_digits.txt'

# with open (filename) as file_object:
#    lines = file_object.readlines()

# for line in lines :
#     print(line.rstrip())




filename = 'python\pi_digits.txt'

with open (filename) as file_object:
   lines = file_object.readlines()

pi_string = ''
for line in lines :
   pi_string +=line.strip() 

print(pi_string)
print(len(pi_string))     