n = float(input())
breaks = [[0, 25], [25,50], [50,75], [75,100]]

for item in breaks:
    if(n < 0 or n > 100):
        print('Fora de intervalo')
        break
        
    if(n > item[0] and n <= item[1]):
   
        if(breaks.index(item) == 0):
            print('Intervalo [0,25]')
            break
        
        if(breaks.index(item) == 1):
            print('Intervalo (25,50]')
            break
        
        if(breaks.index(item) == 2):
            print('Intervalo (50,75]')
            break
        
        if(breaks.index(item) == 3):
            print('Intervalo (75,100]')
            break