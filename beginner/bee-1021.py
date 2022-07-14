# https://www.beecrowd.com.br/judge/pt/problems/view/1021
n = float(input())
notes = [0] * 6
cents = [0] * 6

while(n != 0):
    
    if(n >= 100):
        notes[0] += 1
        n = round(n-100, 2)
    
    elif(n >= 50 and n < 100):
        notes[1] += 1
        n = round(n-50, 2)

    elif(n >= 20 and n < 50):
        notes[2] += 1
        n = round(n-20, 2)

    elif(n >= 10 and n < 20):
        notes[3] += 1
        n = round(n-10, 2)

    elif(n >= 5 and n < 10):
        notes[4] += 1
        n = round(n-5, 2)

    elif(n >= 2 and n < 5):
        notes[5] += 1
        n = round(n-2, 2)

    elif(n >= 1 and n < 2):
        cents[0] += 1
        n = round(n-1, 2)

    elif(n >= 0.50 and n < 1):
        cents[1] += 1
        n = round(n-0.50, 2)

    elif(n >= 0.25 and n < 0.50):
        cents[2] += 1
        n = round(n-0.25, 2)

    elif(n >= 0.10 and n < 0.25):
        cents[3] += 1
        n = round(n-0.10, 2)

    elif(n >= 0.05 and n < 0.10):
        cents[4] += 1
        n = round(n-0.05, 2)

    elif(n >= 0.01 and n < 0.05):
        cents[5] += 1
        n = round(n-0.01, 2)

print('NOTAS:')
print(f'{notes[0]} nota(s) de R$ 100.00')
print(f'{notes[1]} nota(s) de R$ 50.00')
print(f'{notes[2]} nota(s) de R$ 20.00')
print(f'{notes[3]} nota(s) de R$ 10.00')
print(f'{notes[4]} nota(s) de R$ 5.00')
print(f'{notes[5]} nota(s) de R$ 2.00')

print('MOEDAS:')
print(f'{cents[0]} moeda(s) de R$ 1.00')
print(f'{cents[1]} moeda(s) de R$ 0.50')
print(f'{cents[2]} moeda(s) de R$ 0.25')
print(f'{cents[3]} moeda(s) de R$ 0.10')
print(f'{cents[4]} moeda(s) de R$ 0.05')
print(f'{cents[5]} moeda(s) de R$ 0.01')