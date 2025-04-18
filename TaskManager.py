import random as rnd

HELP = """
help - напечатать справку по программе.
add -  добавить задачу в список.
show -  напечатать все добавленные задачи.
random - добавить случайную задачу на дату Сегодня."""

random_tasks = ["Записаться на курс в Нетологию", "Написать Гвидо письмо", "Покормить кошку", "Помыть машину"]

tasks = {
  
}

run = True

def add_todo(date, task):
  if date in tasks:
    tasks[date].append(task)
  else:
    tasks[date] = []
    tasks[date].append(task)
  print("Задача ", task, "добавлена на дату", date)

while run:
  command = input("Введите команду: ")
  if command == "help":
    print(HELP)
  elif  command == "show":
    date = input("Введите дату для отображения списка задач: ")
    if date in tasks:
      for task in tasks[date]:
        print('- ', task)
    else:
      print("Такой даты нет")
  elif  command == "add":
    date = input("Введите дату для добавления задачи: ")
    task = input("Введите название задачи: ")
    add_todo(date, task)
  elif command == "random":
    task = rnd.choice(random_tasks)
    add_todo("Сегодня", random_tasks)
  else:
    print("Неизвестная команда")
    break

print("Спасибо за использование! До свидания!")