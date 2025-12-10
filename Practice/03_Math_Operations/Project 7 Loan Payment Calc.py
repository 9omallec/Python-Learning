principal = 220000
annual_interest_rate = .058
loan_term = 15
monthly_rate = annual_interest_rate / 12
total_months = loan_term * 12
monthly_payment = principal * (monthly_rate * (1 + monthly_rate) ** total_months) / ((1 + monthly_rate) ** total_months - 1)
total_paid = monthly_payment * total_months
total_interest = total_paid - principal
balance = principal

print("\n****** Loan Payment Calc. ******\n")
print(f"Principal:             {principal}")
print(f"Annual Interest Rate:  {round(annual_interest_rate * 100, 2)}")
print(f"Loan Term:             {loan_term}")
print(f"Monthly Rate:          {round(monthly_rate * 100, 2)}%")
print(f"Monthly Payment:     $ {round(monthly_payment, 2)}")
print(f"Total Payment:       $ {round(total_paid, 2)}")
print(f"Total Interest Paid: $ {round(total_interest, 2)}\n")
print("*******************************\n")
