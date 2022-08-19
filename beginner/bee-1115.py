# https://www.beecrowd.com.br/judge/pt/problems/view/1115

while(True):
    numbers = list(map(int, input().strip().split()))
    x, y = numbers
    
    if(x > 0 and y > 0): print('primeiro')
    elif(x < 0 and y > 0): print('segundo')
    elif(x < 0 and y < 0): print('terceiro')
    elif(x > 0 and y < 0): print('quarto')
    else: break