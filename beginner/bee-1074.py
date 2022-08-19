# https://www.beecrowd.com.br/judge/pt/problems/view/1074
n = int(input())

while(n > 0):
    v = int(input())
    x = [0] * True
    
    if(v == 0): print('NULL')
    elif(v % 2 == 0 and v > 0):
        print('EVEN POSITIVE')
        
    elif(v % 2 == 0 and v < 0):
        print('EVEN NEGATIVE')
    
    elif(v % 2 != 0 and v > 0):
        print('ODD POSITIVE')
        
    elif(v % 2 != 0 and v < 0):
        print('ODD NEGATIVE')
    
    n -= 1