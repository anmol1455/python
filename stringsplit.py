string = 'this is a string with spaces' 
splits = [] 
pos = -1 
last_pos = -1 
while ' ' in string[pos + 1:]: 
      pos = string.index(' ', pos + 1) 
      splits.append(string[last_pos + 1:pos]) 
      last_pos = pos 
splits.append(string[last_pos + 1:]) 
print(splits) 
