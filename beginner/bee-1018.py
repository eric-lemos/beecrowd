# https://www.beecrowd.com.br/judge/pt/problems/view/1018

number = int(input())
banknotes = [0] * 7
print(number)

while(number != 0):
    if(number >= 100):
        banknotes[0] += 1
        number -= 100
        
    elif(number < 100 and number >= 50):
        banknotes[1] += 1
        number -= 50

    elif(number < 50 and number >= 20):
        banknotes[2] += 1
        number -= 20

    elif(number < 20 and number >= 10):
        banknotes[3] += 1
        number -= 10

    elif(number < 10 and number >= 5):
        banknotes[4] += 1
        number -= 5

    elif(number < 5 and number >= 2):
        banknotes[5] += 1
        number -= 2

    elif(number < 2 and number >= 1):
        banknotes[6] += 1
        number -= 1

print(f'{banknotes[0]} nota(s) de R$ 100,00')
print(f'{banknotes[1]} nota(s) de R$ 50,00')
print(f'{banknotes[2]} nota(s) de R$ 20,00')
print(f'{banknotes[3]} nota(s) de R$ 10,00')
print(f'{banknotes[4]} nota(s) de R$ 5,00')
print(f'{banknotes[5]} nota(s) de R$ 2,00')
print(f'{banknotes[6]} nota(s) de R$ 1,00')