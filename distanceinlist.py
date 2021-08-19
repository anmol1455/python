import math
x = [5, 6, 7, 9]
y = [8, 9, 9, 5]
distance = math.sqrt(sum([(a - b) ** 2 for a, b in zip(x, y)]))
print("distance from x to y: ",distance)
