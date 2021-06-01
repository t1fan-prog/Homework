def add(a, b):
    return a + b


# Запринтися в файле, в котором будет вызывн данный модуль
print("Import is successful")

if __name__ == '__main__':
    """Запринтится только в данном файле"""
    print(add(241, 352))
