money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить

# TODO Оформить решение
money_sum = money_capital + salary
while money_sum > spend:

    month = month + 1
    spend = spend * (1 + increase)
    money_sum = money_sum + salary - spend

print(month)