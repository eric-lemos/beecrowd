seller_name = input()
fixed_salary = float(input())
sales_amount_month = float(input())
total_recv = float( fixed_salary + ((sales_amount_month * 15) / 100) )

print(f'TOTAL = R$ {total_recv:.2f}')