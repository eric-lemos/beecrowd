# https://www.beecrowd.com.br/judge/pt/problems/view/1114

pswd = 2002
while(True):
    attempt = int(input())
    if(pswd == attempt):
        print('Acesso Permitido')
        break
    else:
        print('Senha Invalida')