"""
Task
Given the meal price (base cost of a meal), tip percent (the percentage of the meal price being added as tip), and tax percent (the percentage of the meal price being added as tax) for a meal, find and print the meal's total cost.

Sample Input

12.00
20
8

Sample Output

The total meal cost is 15 dollars.
"""

def get_total_cost_of_meal():
    # original meal price
    meal_cost = float(input())
    # tip percentage
    tip_percent = int(input())
    # tax percentage
    tax_percent = int(input())

    tip = float(tip_percent*0.01*meal_cost)# calculate tip
    tax = float(tax_percent*0.01*meal_cost)# caclulate tax

    # cast the result of the rounding operation to an int and save it as total_cost
    total_cost = int(round(meal_cost + tip + tax))

    return str(total_cost)

# Print result
print("The total meal cost is " + get_total_cost_of_meal() + " dollars.")
