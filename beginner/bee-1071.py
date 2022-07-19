# https://www.beecrowd.com.br/judge/pt/problems/view/1071
x = int(input())
y = int(input())
i = [x, (y+1)]
i.sort()

sum = 0
for n in range(i[0], i[1]):
    if(n % 2 != 0):
        sum += n

print(sum)