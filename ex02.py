def map_args_to_dict(**kwargs):
    arg_dict = {}
    for key, value in kwargs.items():
        # Проверяем, можно ли использовать значение в качестве ключа
        try:
            hash(value)
            key_name = value
        except TypeError:
            key_name = str(value)
        arg_dict[key_name] = key
    return arg_dict
result = map_args_to_dict(a=1, b='hello', c=[1, 2, 3])
print(result)