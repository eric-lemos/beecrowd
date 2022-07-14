# https://www.beecrowd.com.br/judge/pt/problems/view/1040
input_numbers = tuple(input().strip().split())
n1 = float(input_numbers[0])
n2 = float(input_numbers[1])
n3 = float(input_numbers[2])
n4 = float(input_numbers[3])

avg = ((n1*2)+(n2*3)+(n3*4)+(n4*1)) / (2+3+4+1)
print(f'Media: {avg:.1f}')

if(avg >= 5 and avg <= 6.9):
    print('Aluno em exame.')

    n5 = float(input())
    print(f'Nota do exame: {n5:.1f}')
    new_avg = (avg + n5) / 2
    
    if(new_avg >= 5):
        print('Aluno aprovado.')
        
    else:
       print('Aluno reprovado.')
    
    print(f'Media final: {new_avg:.1f}')
    
elif(avg >= 7):
    print('Aluno aprovado.')
    
else:
    print('Aluno reprovado.')