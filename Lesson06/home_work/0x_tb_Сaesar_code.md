## "Код Цезаря"

### Задание

Одним из первых в истории примеров шифрования считаются закодированные послания Юлия Цезаря. \
В результате он стал шифровать свои послания довольно простым методом, который впоследствии стали называть кодом Цезаря.

Идея шифрования была совершенно тривиальной и заключалась в циклическом сдвиге букв на три позиции. \
В итоге буква A превращалась в D, B -> E, C –> F и т. д. Последние три буквы алфавита переносились на начало. \
Таким образом, буква X становилась A, Y –> B, а Z –> C. Цифры и другие символы не подвергались шифрованию.

Напишите программу, реализующую код Цезаря.

### Формат входных данных

Дана произвольная строка текста.

### Формат выходных данных

Вывести строку, зашифрованную кодом Цезаря.

### Решение задачи

```python
# TODO: you code here...
```
# text = 'Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam xyZ'
text = input("Введите строку на английском языке: ")
alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
encrypted_text = ''

for char in text:
    upper_char = False
    if char.isupper():
        upper_char = True
    if char.lower() in alphabet_list:
        i = alphabet_list.index(char.lower())
        i = i + 3 if i + 3 < len(alphabet_list) else i + 3 - len(alphabet_list)
        encrypted_text += alphabet_list[i].upper() if upper_char else alphabet_list[i]
    else:
        encrypted_text += char

print(f'Строка, зашифрованная кодом Цезаря: {encrypted_text}')
---


