## "Обработка списка фруктов"

### Задание

Дана ведомость расчета заработной платы [data/workers.txt](data/workers.txt).

Рассчитайте зарплату всех работников, зная что они получат полный оклад, если отработают норму часов. \
Если же они отработали меньше нормы, то их ЗП уменьшается пропорционально, \
а за каждый час переработки они получают удвоенную ЗП, пропорциональную норме. \
Кол-во часов, которые были отработаны, указаны в файле ["data/hours_of.txt](data/hours_of.txt)

### Формат входных данных

Дано два текстовых файла. Один с информацией о сотрудниках, второй с количеством отработанных часов.

Гарантируется, что каждый сотрудник имеет уникальную фамилию(однофамильцев нет).

### Формат выходных данных

Выведите зарплату сотрудников с учетом переработки и недоработки.

### Решение задачи

```python
# TODO: you code here...
```
import os
from pathlib import Path
from pprint import pprint

DIR = "data"

path_workers = os.path.join(DIR, 'workers.txt')
path_hours = Path(DIR, 'hours_of.txt')
path_out = Path(DIR, 'workers_real_salary.txt')

workers = []


# каждая часть должна быть написана в виде функции.
def read_workers():
    with open(path_workers, 'r', encoding="UTF-8") as f:
        f.readline()
        for line in f:
            worker_data = line.split()
            worker = {
                "name": worker_data[0],
                "surname": worker_data[1],
                "salary": worker_data[2],
                "need_hours": worker_data[4]
            }
            workers.append(worker)


def read_workers_hours():
    with open(path_hours, 'r', encoding="UTF-8") as f:
        f.readline()
        for line in f:
            worker_data = line.split()
            for worker in workers:
                if worker['name'] == worker_data[0] and worker['surname'] == worker_data[1]:
                    worker['hours'] = worker_data[2]


def calculate_real_salary():
    for worker in workers:
        hours = int(worker['hours'])
        need_hours = int(worker['need_hours'])
        salary = int(worker['salary'])
        if hours > need_hours:
            exceeding_hours = hours - need_hours
            worker['real_salary'] = round((salary + exceeding_hours * 2 * salary / need_hours), 2)
        elif need_hours > hours:
            worker['real_salary'] = round((salary - (need_hours - hours) * salary / need_hours), 2)
        else:
            worker['real_salary'] = salary


def print_real_salary():
    print("Реальная зарплата сотрудников:")
    with open(path_out, 'w', encoding="UTF-8") as f:
        for worker in workers:
            print(worker['surname'], worker['name'], worker['real_salary'])
            f.write(f"{worker['surname']} {worker['name']} {worker['real_salary']} \n")


if __name__ == '__main__':
    read_workers()
    read_workers_hours()
    calculate_real_salary()
    print_real_salary()
    # pprint(workers)
---
