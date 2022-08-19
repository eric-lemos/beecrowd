# https://www.beecrowd.com.br/judge/pt/problems/view/1020
x = int(input())
ano = int(x / 365)
mes = int((x % 365) / 30)
dia = int(x - (ano * 365) - (mes * 30))

print(f'{ano} ano(s)')
print(f'{mes} mes(es)')
print(f'{dia} dia(s)')