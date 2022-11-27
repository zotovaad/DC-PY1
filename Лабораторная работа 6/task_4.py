import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(FILE_NAME: str) -> list[dict]:
    ...  # TODO реализовать конвертер из csv в json
    with open(FILE_NAME, 'r') as f:
        headers_list = f.readline().strip('\n').split(',')  # чтение ключей для будущих словарей

        list_for_json = []
        for line in f:
            list_obj = line.rstrip('\n').split(',')      # список значений для одного словаря
            dict_ = dict(zip(headers_list, list_obj))  # преобразование двух строк в словарь
            list_for_json.append(dict_) # запись словарей в один список
    return list_for_json


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))