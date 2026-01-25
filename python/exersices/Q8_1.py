 

# def display_message():
#   print("learning about function")

# display_message() 

# def describe_pet(animal_type, pet_name='willie'):
#       print(f"\nI have a {animal_type}.")
#       print(f"My {animal_type}'s name is {pet_name.title()}.")

# describe_pet('Dog', 'churchil')     
# describe_pet('hamster', 'harry')

# describe_pet( animal_type='cat' , owner_naame = 'cathy')


def get_formatted_name(first_name, last_name):
  full_name = f"{first_name} {last_name}"
  return full_name.title()


musician = get_formatted_name('jimi' , 'hendrix')
print(musician)