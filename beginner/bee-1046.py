# https://www.beecrowd.com.br/judge/pt/problems/view/1046
x, y = list(map(int, input().strip().split()))

result = (24 - x) + y
if(result > 24): result -= 24
print(f'O JOGO DUROU {result} HORA(S)')