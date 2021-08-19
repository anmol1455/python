string='1234567890'
iterator=iter(string)
print(iterator)
print(next(iterator)) # next gives one by one iteration


for char in iter(string):
    print(char)




#iterator in list
list=['mon','tue','wed','thus','fri','sat','sun']
iterator=iter(list)
for x in range(0,len(list)):
    next_iter=next(iterator)
    print(next_iter)
