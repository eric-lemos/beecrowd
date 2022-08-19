# https://www.beecrowd.com.br/judge/pt/problems/view/1080

index = 0
higher = 0

for i in range(1, 100+1):
    x = int(input())
    if(x > higher):
        index = i
        higher = x
        
print(higher)
print(index)