# https://www.beecrowd.com.br/judge/pt/problems/view/1061
start_date = int(input().strip().split()[1])
start_hour = input().strip().split()
h1, m1, s1 = [int(start_hour[0]), int(start_hour[2]), int(start_hour[4])]

final_date = int(input().strip().split()[1])
final_hour = input().strip().split()
h2, m2, s2 = [int(final_hour[0]), int(final_hour[2]), int(final_hour[4])]

start_date_sec = (start_date * 86400) + (h1 * 3600) + (m1 * 60) + s1
final_date_sec = (final_date * 86400) + (h2 * 3600) + (m2 * 60) + s2

d = int((final_date_sec - start_date_sec) / 86400)
h = int(((final_date_sec - start_date_sec) % 86400) / 3600)
m = int((((final_date_sec - start_date_sec) % 86400) % 3600) / 60)
s = int((((final_date_sec - start_date_sec) % 86400) % 3600) % 60)

print(f'{d} dia(s)')
print(f'{h} hora(s)')
print(f'{m} minuto(s)')
print(f'{s} segundo(s)')