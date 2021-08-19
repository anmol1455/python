fruits=['apple','mango','graps','papaya','pineapple']
#getting list by position
data=fruits[4]
print("\fourth position of list is:",data)
#length of the list
length=len(fruits)
print("\nlength of the list:",length,"\n")
#display list by using loop
for x in range(len(fruits)):
    print(fruits[x])
#inserting element at last position
fruits.append("cheery")
print(fruits)

#inserting element at specified position
fruits.insert(4,"chiku")
print(fruits)

#deleting element of particular position
fruits.pop(4)
print(fruits)

#sorting elements in ascending order
fruits.sort()
print(fruits)

#sorting elements in decending order
fruits.sort(reverse=True)
print(fruits)
