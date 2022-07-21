# https://www.beecrowd.com.br/judge/pt/problems/view/1099
n = int(input())
test_cases = 0

while(n != test_cases):
    odd_sum = 0
    
    numbers = list(map(int, input().strip().split()))
    numbers.sort()
    
    for i in range(numbers[0], numbers[1]):
        if(i % 2 != 0):
            odd_sum += i

    test_cases += 1
    print(odd_sum)