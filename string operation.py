                #string
# creating
str="hello how are you"
print(str)

#extracting sub string
substr=str[4:8:1]
print(substr)

#reverse string
reverse=str[::-1]
print(reverse)

#accessing particular character
access=str[4]
print(access)

#finding number of character
length=len(str)
print(length)

#displaying character one by one
for x in range(len(str)):
    print(str[x])

#converting string into uppercase
upper=str.upper()
print(upper)

#converting string into lowercase
lower=str.lower()
print(lower)

#converting string into title case
title=str.title()
print(title)

#inverting casee of string
invert=str.swapcase()
print(invert)

#spilitting the string into a list based on parameter
strlist=str.split("l")
print(strlist)

#return true if string is in upper case
checkup=str.isupper()
print(checkup)

#return true if string is in lower case
checklo=str.islower()
print(checklo)

#return true if string is in title case
checktit=str.istitle()
print(checktit)
    
