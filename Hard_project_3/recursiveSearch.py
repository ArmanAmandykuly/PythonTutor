def recSearch(data, searched):
    if type(data) == {list, tuple, set}:
        for i in data:
            res = recSearch(i, searched)
            if res:
                return res
        return None
    if type(data) == dict:
        for key, item in data.items():
            res = recSearch(item, searched)
            if res:
                return res
            return res
    if data == searched:
        return data