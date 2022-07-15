# https://www.beecrowd.com.br/judge/pt/problems/view/1042
numbers = list(map(int, input().strip().split()))
x, y, z = numbers
numbers.sort()

print(f'{numbers[0]}\n{numbers[1]}\n{numbers[2]}')
print(f'\n{x}\n{y}\n{z}')

# beecrowd did not accept manual solution
# for i in range(1, len(numbers)):
#     item = numbers[i]
#     j = i - 1
    
#     while(j >= 0 and numbers[j] > item):
#         numbers[j+1] = numbers[j]
#         j -= 1
    
#     numbers[j+1] = item