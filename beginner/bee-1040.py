# https://www.beecrowd.com.br/judge/pt/problems/view/1040
a, b, c, d = list(map(float, input().strip().split()))
avg = ((a*2) + (b*3) + (c*4) + (d*1)) / (2+3+4+1)
print(f'Media: {avg:.1f}')

if(avg >= 5 and avg <= 6.9):
    print('Aluno em exame.')
    exam_grade = float(input())
    print(f'Nota do exame: {exam_grade:.1f}')
    new_avg = (avg + exam_grade) / 2
    
    if(new_avg >= 5):
        print('Aluno aprovado.')
    else: print('Aluno reprovado.')
    print(f'Media final: {new_avg:.1f}')
    
elif(avg >= 7): print('Aluno aprovado.')
else: print('Aluno reprovado.')