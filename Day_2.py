def solve(meal_cost, tip_percent, tax_percent):
    tip=meal_cost*(tip_percent/100)
    tax=meal_cost*(tax_percent/100)
    totalcost=meal_cost+tip+tax
    if totalcost+0.5<int(totalcost+1):
        print(int(totalcost))
    else:
        print(int(totalcost+1))

if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)
