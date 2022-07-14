# https://www.beecrowd.com.br/judge/pt/problems/view/1038

products = {
    1: {'item': 'Cachorro Quente', 'price': 4},
    2: {'item': 'X-Salada', 'price': '4.5'},
    3: {'item': 'X-Bacon', 'price': '5'},
    4: {'item': 'Torrada simples', 'price': '2'},
    5: {'item': 'Refrigerante', 'price': '1.5'},
}

input_numbers = tuple(input().strip().split())
id = int(input_numbers[0])
qt = int(input_numbers[1])

for product in products.items():
    if(product[0] == id):
        total = float(product[1]['price']) * qt
        print(f'Total: R$ {total:.2f}')
        break