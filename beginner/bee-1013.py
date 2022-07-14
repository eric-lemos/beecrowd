values = tuple(input().strip().split())
a = int(values[0])
b = int(values[1])
c = int(values[2])

higher = int(((a + b) + abs(a-b)) / 2)
if(c > higher): higher = c
print(f'{higher} eh o maior')