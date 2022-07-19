# https://www.beecrowd.com.br/judge/pt/problems/view/1072
n = int(input())
x = []

while(n > 0):
    new_value = int(input())
    x.append(new_value)
    n -= 1

count_in = 0
count_out = 0

for i in x:
    if(i >= 10 and i <= 20):
        count_in += 1
    else:
        count_out += 1
    
print(f'{count_in} in')
print(f'{count_out} out')