# https://www.beecrowd.com.br/judge/pt/problems/view/1117
new_case = 1

while(True):
    count = 0
    result = 0

    if(new_case == 1):
        while(count != 2):
            x = float(input().strip())
            
            if(x >= 0 and x <= 10): 
                result += x
                count += 1
            else: print('nota invalida')

        print(f'media = {result/2:.2f}')
        new_case = 0
        
    elif(new_case == 2): break
    else:
        print('novo calculo (1-sim 2-nao)')
        new_case = int(input())