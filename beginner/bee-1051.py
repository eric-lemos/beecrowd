# https://www.beecrowd.com.br/judge/pt/problems/view/1051
x = float(input())

if(x >= 0 and x <= 2000):
    print('Isento')

else:
    tax = 0
    while(x != 2000):
        if(x > 2000 and x <= 3000):
            diff = (x - 2000)
            tax += (diff * 8) / 100
            x -= diff

        elif(x > 3000 and x <= 4500):
            diff = (x - 3000)
            tax += (diff * 18) / 100
            x -= diff

        elif(x > 4500):
            diff = (x - 4500)
            tax += (diff * 28) / 100
            x -= diff
            
    print(f'R$ {tax:.2f}')