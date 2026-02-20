
# try:
#   print(5/0)
# except ZeroDivisionError:
#   print("You can't divide by zero!")  


# while True:
#    first_number = input("\nFirst number: ")
#    if first_number =='q':
#      break

#    second_num =  input("Second number: ")
#    if second_num == 'q':
#       break 
#    answer = int(first_number) / int(second_num)
#    print(answer)



while True:
  first_number = input("\nFirst number: ")
  if first_number =='q':
     break

  second_num =  input("Second number: ")
  if second_num == 'q':
      break 
  

  try:
   answer  = answer = int(first_number) / int(second_num) 
  except ZeroDivisionError:
    print("You can't divide by zero!")

  else:
    print(answer)    