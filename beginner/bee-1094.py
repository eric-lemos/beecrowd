# https://www.beecrowd.com.br/judge/pt/problems/view/1094
n = int(input())

c_rabbits = 0
c_frogs = 0
c_rats = 0

while(n > 0):
    new_value = input().split()
    
    if(new_value[1] == 'C'):
        c_rabbits += int(new_value[0])
        
    elif(new_value[1] == 'S'):
        c_frogs += int(new_value[0])
        
    elif(new_value[1] == 'R'):
        c_rats += int(new_value[0])
    
    n -= 1

total = (c_rabbits + c_frogs + c_rats)
p_rabbits = (c_rabbits * 100) / total
p_frogs = (c_frogs * 100) / total
p_rats = (c_rats * 100) / total

print(f'Total: {total} cobaias')
print(f'Total de coelhos: {c_rabbits}')
print(f'Total de ratos: {c_rats}')
print(f'Total de sapos: {c_frogs}')
print(f'Percentual de coelhos: {p_rabbits:.2f} %')
print(f'Percentual de ratos: {p_rats:.2f} %')
print(f'Percentual de sapos: {p_frogs:.2f} %')