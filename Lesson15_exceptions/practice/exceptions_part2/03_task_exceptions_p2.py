def check_string_length(text, min_length):
    # Добавьте проверку, что длина строки не меньше min_length.
    # Если строка слишком короткая, выбросьте исключение ValueError.
    if len(text) < min_length:
        raise ValueError("слишком короткая строка")
    return text


# Добавьте обработку исключения ValueError
print(check_string_length("abc", 5))
