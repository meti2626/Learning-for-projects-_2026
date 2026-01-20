

##ordered 
bicycles =  ['trek' , 'cannondale' , 'redline' , 'specialized']

message = f"my first bicycle was {bicycles[-3].title()}"

#print(bicycles[0].title())

#print(message)


#### modify elements in the list 
motorcycle = ['honda', 'yamaha' , 'suzuki']
#print(motorcycle)

motorcycle[0] = 'bugati'
#print(motorcycle)


## add element to the list

motorcycle.append('rolce royce')
#print(motorcycle)

motorcycle =[]

motorcycle.append('honda')
motorcycle.append('ducati')
motorcycle.append('suzuki')



#insert element at anywhere you want 

motorcycle.insert(1,"bugati")




#del statement 

# pop_motorcyle = motorcycle.pop(0)
# print(pop_motorcyle)
# print(motorcycle)

# print (motorcycle[0])



#remove a value you dont know the position but know the value 


motorcycle.remove('bugati')
print(motorcycle)




