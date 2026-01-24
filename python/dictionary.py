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


# favorite_languages = {
# 'en': 'python',
# 'sarah': 'c',
# 'edward': 'ruby',
# 'phil': 'python',
# }

# print(favorite_languages['sarah'].title())


alien_0 = {'color': 'green', 'speed': 5}

point_value = alien_0.get('points', 'No point value assigned.')

print(alien_0['points'])  # This will raise a KeyError