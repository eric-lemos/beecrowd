# https://www.beecrowd.com.br/judge/pt/problems/view/1038
id, amount = list(map(int, input().strip().split()))

database = {
    1: {'item': 'Cachorro Quente', 'price': 4},
    2: {'item': 'X-Salada', 'price': '4.5'},
    3: {'item': 'X-Bacon', 'price': '5'},
    4: {'item': 'Torrada simples', 'price': '2'},
    5: {'item': 'Refrigerante', 'price': '1.5'}
}

for product in database.items():
    if(product[0] == id):
        result = float(product[1]['price']) * amount
        print(f'Total: R$ {result:.2f}')
        break