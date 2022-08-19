# https://www.beecrowd.com.br/judge/pt/problems/view/1101

while(True):
    numbers = list(map(int, input().strip().split()))
    numbers.sort()
    x,y = numbers
    sum = 0
    
    if(x <= 0 or y <= 0): break
    else:
        for i in range(x, y+1):
            print(f'{i}', end=' ')
            sum += i
        print(f'Sum={sum}\n', end='')