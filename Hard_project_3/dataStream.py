def data_stream(filepath, chunk_size = None):
    with open(filepath, "r") as f:
        columns = f.read()
        if not columns:
            raise RuntimeError("Invalid dataset format")
        columns = columns.split()
        if chunk_size == None:
            chunk_size = len(f)
        i = 0
        while i != chunk_size:
            row = f.read()
            if not row:
                break
            newRow = dict()
            for column, data in zip(columns, row):
                if data.isnumeric():
                    newRow[column] = float(data)
                else:
                    newRow[column] = data
            yield newRow