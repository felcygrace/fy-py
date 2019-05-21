mileage=12
amount_per_litre=65
distance_one_way=96
per_head_cost=0
divisible_by_five=False
per_head_cost=(((distance_one_way/mileage)*amount_per_litre)*2)/4
if per_head_cost%5==0:
    divisible_by_five=True
else:
    divisible_by_five=False
print(per_head_cost)
print(divisible_by_five)
