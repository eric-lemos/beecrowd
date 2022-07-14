# https://www.beecrowd.com.br/judge/pt/problems/view/1017
avg_speed = int(input())
time_travel = int(input())
distance = int(avg_speed * time_travel)
gasoline = distance / 12
print(f'{gasoline:0.3f}')