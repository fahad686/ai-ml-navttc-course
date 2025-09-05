# List
fruits=['apple','banana','mango','cherry','stawberry']
print(fruits)

print(fruits[-3: -1])


ages=['young','cherry',35,78,48]
print(ages)

#accessing string by index and their charc
print(ages[0][1])
print(ages[-2])

print(ages[1][2])


#upate list
fruits=['mango','appel']
print(fruits)

#replacing
fruits[1]='banana'
print(fruits)


#adding
fruits.insert(2,'stawberry')
print(fruits)
fruits.insert(2,'grapps')
print(fruits)


#append method to use adding element on end
fruits.append('samosa')
print(fruits)

#change akhty with slicing
fruits[1:3:]=['amrood','malta']
print(fruits)

fruits1=fruits
print("assigning list",fruits1)