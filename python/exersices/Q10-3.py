
Guest = input("enter your name:")

filename = 'python/exersices/guestname.txt'

with open(filename , 'w') as file_object:
  file_object.write(Guest)