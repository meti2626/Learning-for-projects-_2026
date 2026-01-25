#def greet_user(usename): # parameter accepts the argument from the function call
  #print(f"hello!{usename.title()}")

#greet_user('jesse')  # jeese is an argument - passed from function call to function
#greet_user('sarah')  



# def get_formatted_name(first_name,last_name,middle_name=""):
#   full_name = f"{first_name} {middle_name} {last_name}"
#   return full_name.title()


# musician = get_formatted_name('jimi' , 'hendrix')
# print(musician)


#Returning a dictionary



# def build_person(first_name, last_name , age = None):
#   person = {'first':first_name , 'last':last_name ,'age':age}
 
#   if age:
#     person['age'] = age
#   return person  

# musician = build_person('jimi' , 'hendrix' , 27)
# print(musician)






#--------Using a Function with a while Loop------------#

def get_formatted_name(first_name, last_name):

 full_name = f"{first_name} {last_name}"
 return full_name.title()



  # This is an infinite loop

while True:
   print("\nPlease tell me your name:")
   f_name = input("First nam: ")
   l_name = input("Last name : ")

   formatted_name = get_formatted_name(f_name , l_name)
   print(f"\nHello, {formatted_name}")