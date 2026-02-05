with open('name.txt') as file_object:  
   # to do work with file you have toopen it first hence - comes open() - need the file you want to open as an argument
   contents = file_object.read()

print(contents.rstrip())  

# rstrip() method removes any whitespace characters from the right side of a string


