montly_income = int(input("Enter your monthly income: "))
montly_expenses = int(input("Enter your total montly expenses: "))
montly_savings = montly_income - montly_expenses
projected_savings = montly_savings * 12 + (montly_savings * 12 * 0.05)

print(f"Your montly savings are ${montly_savings}")
print(f"Project savings after one year, with interest is: ${projected_savings}")

