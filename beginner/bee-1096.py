# https://www.beecrowd.com.br/judge/pt/problems/view/1096

i, j = 1, 7
while(i <= 9):
    threshold = j - 3
    while(j != threshold):
        print(f'I={i} J={j}')
        j -= 1
    i += 2
    j += 5