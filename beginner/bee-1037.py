# https://www.beecrowd.com.br/judge/pt/problems/view/1037
x = float(input())
breaks = [[0, 25], [25,50], [50,75], [75,100]]

for item in breaks:
    if(x < 0 or x > 100):
        print('Fora de intervalo')
        break
   
    elif(breaks.index(item) == 0):
        if(x >= item[0] and x <= item[1]):
            print('Intervalo [0,25]')
            break
    
    elif(x > item[0] and x <= item[1]):
        if(breaks.index(item) == 1):
            print('Intervalo (25,50]')
            break
        
        if(breaks.index(item) == 2):
            print('Intervalo (50,75]')
            break
        
        if(breaks.index(item) == 3):
            print('Intervalo (75,100]')
            break