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


#extend add on list  to 2nd list
product1=['mobile','airbirds','iphone']
product2=['amrood','banana','handfree']
print(product1)
print(product2)
product1.extend(product2)

#pop
items=product1.pop(2)
print(items)

print(product1)

#collect garbeg collect , use pop for  taking garbege collection, and remove use permanent element

product1.remove('mobile')
print(product1)
