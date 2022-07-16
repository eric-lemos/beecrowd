# https://www.beecrowd.com.br/judge/pt/problems/view/1019
x = int(input())
hours = int(x / (60*60))
minutes = int((x - (hours * (60*60))) / 60)
seconds = int((x - (hours * (60*60)) - (minutes * 60)))

print(f'{hours}:{minutes}:{seconds}')