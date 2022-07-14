# https://www.beecrowd.com.br/judge/pt/problems/view/1020
n = int(input())
ano = int(n/365)
mes = int((n % 365) /30)
dia = int(n -(ano * 365) -(mes * 30))
print(f'{ano} ano(s)')
print(f'{mes} mes(es)')
print(f'{dia} dia(s)')