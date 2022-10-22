salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев

# TODO Оформить решение
expenses = spend # траты до повышения цен
for i in range(1, months):
    spend = spend * (1 + increase)
    expenses = expenses + spend
need_money = expenses - salary * months
print(round(need_money))