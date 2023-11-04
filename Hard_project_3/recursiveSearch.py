def recSearch(data, condition):
    if type(data) == {list, tuple, set}:
        for i in data:
            res = recSearch(i, condition)
            if res:
                return res
        return None
    if type(data) == dict:
        for key, item in data.items():
            res = recSearch(item, condition)
            if res:
                return res
            return res
    if condition(item):
        return data