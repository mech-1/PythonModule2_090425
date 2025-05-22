# Дана строка.
# Определите, все ли буквы в ней уникальны.

string = "uniq strg "
string_no_space = string.replace(" ", "")

if len(set(string_no_space)) == len(string_no_space):
    print("Символы не повторяются")
else:
    print("Есть дублика символов")
