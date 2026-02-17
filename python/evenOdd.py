
# num = input("Enter a number:")

# if int(num) % 2 == 0:
#   print("the number is even")
# else:
#   print("the number is odd") 



num1 = input("enter the first number:")
num2 = input ("enter the second number:")
operator = input("enter the operator(+, -, *, /):")

if operator == '+':
  print(int(num1 )+ int(num2))
elif operator == '-':
   print(int(num1 )- int(num2))
elif operator == '*':
   print(int(num1 ) * int(num2))   
elif operator == '/':
   print(int(num1 ) / int(num2))   

else:
   print("enter the right operator")   