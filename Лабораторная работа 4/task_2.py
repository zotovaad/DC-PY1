def get_count_char(str_):
    # TODO посчитать количество каждой буквы в строке в аргументе str_
    str_ = str_.lower()
    all_letters = []
    for letter in str_:     # цикл для записи только букв в строку
        if letter.isalpha():
            all_letters += letter.strip()
    dict_letters = {}   # словарь с подсчетом количества символов
    for letter in all_letters:
        if letter in dict_letters:
            dict_letters[letter] += 1
        else:
            dict_letters[letter] = 1
    return dict_letters


def get_ratio(dict_):    # функция, которая возвращает словарь с процентным содержанием букв
    total_amount = sum(dict_.values())
    for letter, amount in dict_.items():
        ratio = round(amount / total_amount * 100, 2)
        dict_[letter] = ratio
    return dict_


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))

