# https://www.beecrowd.com.br/judge/pt/problems/view/1097
i, j = 1, 7

while(i <= 9):
    trigger = j-2
    while(j >= trigger):
        print(f'I={i} J={j}')
        j -= 1
        
    i += 2
    j += 5