# alien_0 = {'color' : 'green' , 'points ':5}
# alien_0['x_position'] = 0
# alien_0['y_position'] = 25

# print(alien_0)
# print(alien_0['points '])


# alien_0 = {}

# alien_0['color']= 'green'
# alien_0['points'] = 5


# 



# alien_0 = {'color': 'green'}
# print(f"The alien is {alien_0['color']}.")
# alien_0['color'] = 'yellow'
# print(f"The alien is now {alien_0['color']}.")



# print(alien_0)



# alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
# print(f"Original position: {alien_0['x_position']}")

# Move the alien to the right.


# if alien_0['speed'] == 'slow':
#     x_increment = 1
# elif alien_0['speed'] == 'medium':
#     x_increment = 2
# else:
#     x_increment = 3

# alien_0['x_position'] += x_increment
# print(f"New position: {alien_0['x_position']}")


# del alien_0['speed']
# print(alien_0)




#use dic to store the same things about dfferent people




# print(favorite_languages['sarah'].title())


# alien_0 = {'color': 'green', 'speed': 5}

# point_value = alien_0.get('points', 'No point value assigned.')

#print(alien_0['points'])  # This will raise a KeyError 

favorite_languages = {
'en': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}

# for name , language in favorite_languages.items():
#  print(f"{name.title()} favorite language is {language.title()}.")


# friends = ['phil' , 'sarah']
# for name in favorite_languages.keys():
#     print(name.title())

#     if name in friends:
#       print( f"{name.title()}  , I see your favorite language is {favorite_languages[name].title()}!")



# if 'erin' not in favorite_languages.keys():
#     print("Erin , please take our poll!")



# for name in sorted(favorite_languages.keys()):
#    print(name.title())


# for language in set(favorite_languages.values()):
#     print(language.title())


# A list of Dictionary

# alien_0 = {'color': 'green', 'points': 5}
# alien_1 = {'color': 'yellow', 'points': 10}
# alien_2 = {'color': 'red', 'points': 15}


# aliens = [alien_0, alien_1, alien_2]

# for alien in aliens:
#     print(alien)



aliens = []

for alien_number in range(30):
   new_alien =  {'color': 'green', 'points': 5, 'speed': 'slow'}
   second_new_alien =  {'color': 'yellow', 'points': 10, 'speed': 'medium'}
   aliens.append(new_alien)
   aliens.append(second_new_alien)
print (f"Total aliens: {aliens}")

for aliens in aliens:
    print(aliens)
for alien in aliens[0:3]:
   if alien['color'] == 'green':
       alien['color'] = 'yellow'
       alien['speed'] = 'medium'
       alien['points'] = 10
   elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15
# for alien in aliens[:5]:
#    print(alien)
# print("...")  