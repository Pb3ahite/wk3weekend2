def calculate_roi(down_payment, closing_costs, repair_budget, miscellaneous, income, expenses):
    total_investment = down_payment + closing_costs + repair_budget + miscellaneous
    monthly_income = income
    monthly_expenses = sum(expenses)
    monthly_net_income = monthly_income - monthly_expenses
    roi_percentage = (monthly_net_income / total_investment) * 100
    return roi_percentage

print(" ROI Calculator for Rental Property.")


down_payment = float(input("Enter the down payment amount: $"))
closing_costs = float(input("Enter the closing costs: $"))
repair_budget = float(input("Enter the repair budget: $"))
miscellaneous = float(input("Enter the miscellaneous expenses: $"))

income = float(input("Enter the monthly income: $"))


print("Enter the monthly expenses:")
expenses = [
    float(input("Tax: $")),
    float(input("Insurance: $")),
    float(input("Vacancy: $")),
    float(input("Repairs: $")),
    float(input("Capital expenditures: $")),
    float(input("Property management: $")),
    float(input("Mortgage: $")),
]

roi = calculate_roi(down_payment, closing_costs, repair_budget, miscellaneous, income, expenses)
print(f"The monthly ROI percentage for the rental property is: {roi:.2f}%")




