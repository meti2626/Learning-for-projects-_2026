# message = input('Tell me something , and I will repeat: ')
# print(message)

# name = input("Please input your name: ")
# print(name)


# prompt = "If you tell us who you are, we can personalize the messages you see."
# prompt += "\nWhat is your first name? "

# name = input(prompt)
# print(f"\nHello, {name}")


# age = input("How old are you? ")

# age = int(age)

# print(age>18)





# height = input("How tall are you , in inches?")
# height = int(height)

# if height>56:
#   print("\nYou're tall enough to ride ")
# else:
#       print("\nYou're not tall enough to ride ")
 

# print(13%3)


# number = input("Enter a number, and I'll tell you if it's even or odd:")
# number = int(number)



# if number % 2 == 0:
#     print(f"\nThe number {number} is even.")

# else:
#     print(f"\nThe number {number} is odd.")


#----------------   while Loop---------#

# current_number = 1
# while current_number <= 5:
#   print(current_number)
#   current_number +=1


# prompt =  "\nTell me something, and I will repeat it back to you:"

# prompt += "\nEnter 'quit' to end the program. "

# message = ""

# while message !='quit':
#   message = input(prompt)
  
#   if message !='quit':
#      print(message)
     
  

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

# active = True 
# while active :
#   message = input(prompt)

#   if message == 'quit':
#     active =  False
#   else :
#     print(message)


# while True:
#   city= input(prompt)

#   if city == 'quit':
#     break
#   else:
#    print(f"I'd love to go to {city.title()}!")
 



# current_number = 0

# while current_number <10:
#   current_number +=1
#   if current_number % 2 ==0:
#     continue
#   print(current_number)



# x =1 
# while x <=5:
#  print(x)
#  x+=1
 

# unconfirmed_users  = ['alice', 'brian', 'candace']
# confirmed_users = []


# while unconfirmed_users:
#     current_user = unconfirmed_users.pop()

#     print(f"Verifying user: {current_user.title()}")
#     confirmed_users.append(current_user)

# print("\nThe following users have been confirmed:")
# for confirmed_user in confirmed_users:
#     print(confirmed_user.title())


# Removing all instances of specific values from a list


# pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# print(pets)

# while 'cat' in pets:
#     pets.remove('cat')

# print(pets)

#Filling a dictionary with user input

responses = {}

polling_active = True 


while polling_active: 
  name = input("\nWhat is your name? ")
  response = input("Which mountain would you like to climb someday? ")


  responses[name] = response


  repeat = input("Would you like to let another person respond? (yes/ no)")

  if repeat == 'no':
    polling_active = False


print("\n--- Poll Results ---")
print(responses)   