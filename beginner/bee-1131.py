# https://www.beecrowd.com.br/judge/pt/problems/view/1131
new_case, gremio, inter, draws, games = 1, 0, 0, 0, 0

while(True):
    if(new_case == 1):
        gols = list(map(int, input().strip().split()))
        
        if(gols[0] > gols[1]): inter += 1
        elif(gols[0] < gols[1]): gremio += 1
        else: draws += 1
        new_case = 0
        games += 1
        
    elif(new_case == 2): break
    else:
        print('Novo grenal (1-sim 2-nao)')
        new_case = int(input())

print(f'{games} grenais')
print(f'Inter:{inter}')
print(f'Gremio:{gremio}')
print(f'Empates:{draws}')
if(inter > gremio): print('Inter venceu mais')
elif(gremio > inter): print('Gremio venceu mais')