# https://www.beecrowd.com.br/judge/pt/problems/view/1098
i, j = 0, 1
counter = 0

while(i <= 2):
    trigger = j + 2
    while(j <= trigger):
        if(i == 0 or counter == 5):
            print(f'I={int(round(i, 0))} J={int(round(j, 0))}')
        else: print(f'I={i:.1f} J={j:.1f}')
        if(trigger == j and counter == 5):
            counter = 0
        j += 1
    
    j -= 3
    i += 0.2
    j += 0.2
    counter += 1