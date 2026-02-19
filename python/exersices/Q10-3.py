
Guest = input("enter your name:")

filename = 'python/exersices/guestname.txt'

with open(filename , 'a') as file_object:
  file_object.write(Guest)