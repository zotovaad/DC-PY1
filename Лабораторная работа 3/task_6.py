list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
# TODO Оформить решение
# поиск индекса максимального
maxind = 0
maxnum = list_numbers[0]
for ind in range(1,len(list_numbers)):
  if list_numbers[ind] > maxnum:
    maxnum = list_numbers[ind]
    maxind = ind
# замена значений
temp = list_numbers[maxind]
list_numbers[maxind] = list_numbers[-1]
list_numbers[-1] = temp

print(list_numbers)
