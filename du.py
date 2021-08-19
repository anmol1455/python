x = (1,1,-13,-13,8,5,0,4,-1,-1,-4)
seen = []
answer = []
for elem in x:
    if elem not in seen:
        seen.append(elem)
        answer.append(elem)
print(tuple(answer))
