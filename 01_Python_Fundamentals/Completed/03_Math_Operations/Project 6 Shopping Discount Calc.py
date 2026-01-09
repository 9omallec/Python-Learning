
original_price = 50
coupon1 = .2
coupon2 = .15
discount_amount1 = original_price * coupon1
price1 = original_price - discount_amount1
discount_amount2 = price1 * coupon2
price2 = price1 - discount_amount2
savings = discount_amount1 + discount_amount2

print("=== Discount Calculator ===")
print(f"Price: ${original_price}")
print(f"-Coupon {coupon1 * 100}% off: ${discount_amount1}")
print(f"Total: ${price1}")
print(f"-Coupon {coupon2 * 100}% off: ${discount_amount2}")
print(f"TOTAL: ${price2}")
print()
print(f"Total Savings: ${savings}")
print("=" * 24)