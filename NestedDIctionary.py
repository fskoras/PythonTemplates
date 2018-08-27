
def nested_get(dataDict, mapList):
    for k in mapList: dataDict = dataDict[k]
    return dataDict


def nested_set(dic, keys, value):
    for key in keys[:-1]:
        dic = dic.setdefault(key, {})
    dic[keys[-1]] = value


data_dict = {}

nested_set(data_dict, ['TEST', 'VALUE1'], 1)
nested_set(data_dict, ['TEST', 'VALUE2'], 2)
nested_set(data_dict, ['TEST', 'VALUE3', 'VALUE31'], 21)


print(data_dict)
