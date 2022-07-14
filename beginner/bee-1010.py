# https://www.beecrowd.com.br/judge/pt/problems/view/1010
item1 = tuple(input().strip().split())
item2 = tuple(input().strip().split())

amount_pay = float( (float(item1[2]) * int(item1[1])) + (float(item2[2]) * int(item2[1])) )
print(f'VALOR A PAGAR: R$ {amount_pay:.2f}')