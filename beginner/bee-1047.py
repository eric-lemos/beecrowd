# https://www.beecrowd.com.br/judge/pt/problems/view/1047
a, b, c, d = list(map(int, input().strip().split()))
diff = ((c * 60) + d) - ((a * 60) + b)
if(diff <= 0): diff += 24*60
h = int(diff / 60)
m = int(diff % 60)

print(f'O JOGO DUROU {h} HORA(S) E {m} MINUTO(S)')