
# with open('python\exersices\pythonlearning.txt') as file_object:
#     contents = file_object.read()
# print(contents)  


filename = 'python\\exersices\\pythonlearning.txt'

# with open(filename) as file_object:
#   lines = file_object.readlines()

# for line in lines:
#    print(line.replace('python' , 'C').rstrip())  

# message = "I really like your dog"
# print(message.replace('dog' , 'cat'))



with open(filename , 'w') as file_object:
    file_object.write("I love programming")