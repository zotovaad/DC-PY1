def delete(list_, index=None):
      # TODO реализовать функцию удаления элемента из списка по индексу
    if index == 0:
        new_list = list_[1:]
    elif index:
        new_list = list_[:index] + list_[index+1:]
    else:
        new_list = list_[:-1]
    return new_list


print(delete([0, 0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2]
print(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3]
