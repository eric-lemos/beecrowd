# https://www.beecrowd.com.br/judge/pt/problems/view/1050
x = int(input())

ddd = {
    61: 'Brasilia',
    71: 'Salvador',
    11: 'Sao Paulo',
    21: 'Rio de Janeiro',
    32: 'Juiz de Fora',
    19: 'Campinas',
    27: 'Vitoria',
    31: 'Belo Horizonte'
}

for num in ddd.keys():
    if(num == x):
        print(ddd[num])
        break
    
    elif(x not in ddd):
        print('DDD nao cadastrado')
        break