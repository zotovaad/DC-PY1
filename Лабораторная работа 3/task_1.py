src = not False and True or False and not True

# TODO расписать упрощение выражения
# result = True and True or False and False # избавляемся от отрицаний
# result = True or True # избавляемся от логического "И"
# result = True # избавляемся от логического "ИЛИ"

result = True  # TODO подставить результат выражения

print(src == result)
