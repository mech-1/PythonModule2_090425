# Данные о сотрудниках в программе хранятся в словаре
staff = [
    {
        'name': 'Алексей',
        'surname': 'Петров',
        'salary': 124300
    },
    {
        'name': 'Николай',
        'surname': 'Петров',
        'salary': 120000
    },
    {
        'name': 'Иван',
        'surname': 'Павлов',
        'salary': 34500
    },
    {
        'name': 'Василий',
        'surname': 'Кукушкин',
        'salary': 162500
    },
    {
        'name': 'Василий',
        'surname': 'Павлов',
        'salary': 47800
    },
]

sorted_staff = sorted(staff, key=lambda x: x['salary'], reverse=False)

print(f"Имя и Фамилию сотрудника с самой высокой зарплатой: {sorted_staff[-1]['name']} {sorted_staff[-1]['surname']}")

print(f"Имя и Фамилию сотрудника с самой низкой зарплатой: {sorted_staff[0]['name']} {sorted_staff[0]['surname']}")

total_salary = 0
surnames_set = set()
print("*Список всех сотрудников(Имя и Фамилию) в порядке возрастания их зарплаты")
for person in sorted_staff:
    total_salary += person['salary']
    surnames_set.add(person['surname'])
    print(person['name'], person['surname'])

avg_salary = total_salary / len(sorted_staff)
print(f"Среднеарифметическую зарплату всех сотрудников: {avg_salary}")

same_surname = len(staff) - len(surnames_set)
print(f"Количество однофамильцев в организации: {same_surname} ")
