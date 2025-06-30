def normalize_data(values):
    total = sum(values)
    return [round(v / total, 2) for v in values]

data = [1, 0, 3, 0]
print(normalize_data(data))