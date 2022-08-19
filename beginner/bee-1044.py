# https://www.beecrowd.com.br/judge/pt/problems/view/1044
inputs = list(map(int, input().strip().split()))
inputs.sort()

if(inputs[1] % inputs[0] == 0): print("Sao Multiplos")
else: print("Nao sao Multiplos")