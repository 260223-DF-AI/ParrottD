# budget_calculator.py - Personal Finance Calculator
# Starter code for e002-exercise-python-intro
import sys
"""
Personal Finance Calculator
---------------------------
This program helps users understand their monthly budget by collecting
income and expense information and displaying a formatted summary.

Complete the TODO sections below to finish the program.
"""

print("=" * 44)
print("       PERSONAL FINANCE CALCULATOR")
print("=" * 44)
print()

# =============================================================================
# TODO: Task 1 - Collect User Information
# =============================================================================
# Get the user's name
# Example: name = input("Enter your name: ")

name = input("Enter your name: ")

if name == "":
    name = "Anonymous"

# Get monthly income (as a float)
# Remember to convert the input to a float!

income = float(input("Enter your monthly income: "))
print()

if (income <= 0):
    print("Need income to greater than 0 to calculate")
    print()
    sys.exit(0)

# Get expenses for at least 4 categories:

# - rent: Rent/Housing
# - utilities: Utilities (electric, water, internet)
# - food: Food/Groceries
# - transportation: Transportation (gas, public transit)

rent = float(input("enter your rent/housing amount: "))
utilities = float(input("enter your utilities amount: "))
food = float(input("enter your food expense: "))
transportation = float(input("enter your transportation expense: "))

def checkExpense(expense):
    if expense < 0:
        expense = 0
    return expense

rent = checkExpense(rent)
utilities = checkExpense(utilities)
food = checkExpense(food)
transportation = checkExpense(transportation)
# =============================================================================
# TODO: Task 2 - Perform Calculations
# =============================================================================
# Calculate total expenses

expenses = rent+utilities+food+transportation

# Calculate remaining balance (income - expenses)

balance = income-expenses

# Calculate savings rate as a percentage
# Formula: (balance / income) * 100

savingsRate = (balance/income)*100

# Determine financial status
# - If balance > 0: status = "in the green"
# - If balance < 0: status = "in the red"
# - If balance == 0: status = "breaking even"
status = "N/A";

if balance > 0:
    status = "in the green"
elif balance < 0:
    status = "in the red"
else:
    status = "breaking even"    

# =============================================================================
# TODO: Task 3 - Display Results
# =============================================================================
# Create a formatted budget report
# Use f-strings for formatting
# Dollar amounts should show 2 decimal places: f"${amount:.2f}"
# Percentages should show 1 decimal place: f"{rate:.1f}%"

# Example structure:
# print("=" * 44)
# print("       MONTHLY BUDGET REPORT")
# print("=" * 44)
# print(f"Name: {name}")
# ... continue building the report ...

print("=" * 44)
print("       MONTHLY BUDGET REPORT")
print("=" * 44)
print(f"Name: {name}")
print()
print(f"INCOME: ${income:.2f}" )
print()
print(f"Rent/Housing Expense: ${rent:.2f}" )
print(f"  - Rent/Housing:    {(rent/income)*100:.1f}% of income")
print(f"Utilities Expense : ${utilities:.2f}" )
print(f"  - Utilities:    {(utilities/income)*100:.1f}% of income")
print(f"Food Expense: ${food:.2f}" )
print(f"  - Food:    {(food/income)*100:.1f}% of income")
print(f"Transportation Expense: ${transportation:.2f}" )
print(f"  - Transportation:    {(transportation/income)*100:.1f}% of income")
print()
print(f"TOTAL EXPENSES: ${expenses:.2f}" )
print()
print(f"Savings Rate: %{savingsRate:.1f}")
print(f"Financial status: {status}")


# =============================================================================
# TODO: Task 4 - Add Validation (Optional Enhancement)
# =============================================================================
# Add these validations before calculations:
# - If name is empty, use "Anonymous"
# - If income is <= 0, print error and exit
# - If any expense is negative, treat as 0


# =============================================================================
# STRETCH GOAL: Category Percentages
# =============================================================================
# Add a section showing what percentage each expense is of total income
# Example: print(f"  - Rent/Housing:    {(rent/income)*100:.1f}% of income")
