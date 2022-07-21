# https://www.beecrowd.com.br/judge/pt/problems/view/1116

n = int(input())
test_cases = 0

while(n != test_cases):
    numbers = list(map(int, input().strip().split()))
    x, y = numbers
    
    try: print(f'{x/y:.1f}')
    except ZeroDivisionError:
        print('divisao impossivel')

    test_cases += 1