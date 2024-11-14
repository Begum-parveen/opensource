Bill_Price = int(input())
Discount_1 = Bill_Price*0.1
Discount_2 = 100
if Discount_1 >= Discount_2:
    final_Price = Bill_Price - Discount_1
else:
    final_Price = Bill_Price - Discount_2
print(int(final_Price))
