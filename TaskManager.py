HELP = """
help - напечатать справку по программе.
add -  добавить задачу в список (название задачи запрашиваем у пользователя).
show -  напечатать все добавленные задачи.
exit -  выход из программы."""

today = []
tomorrow = []
other = []

run = True

while run:
  command = input("Введите команду: ")
  if command == "help":
    print(HELP)

  elif  command == "show":
    print("Сегодня")
    print(today)
    print("Завтра")
    print(tomorrow)
    print("Другая дата")
    print(other)

  elif  command == "add":
    task_2 = input("Выберете дату задачи: 1 - сегодня, 2 - завтра, 3 - другая дата :")
    task = input("Введите название задачи: ")
    if task_2 == "1":
      today.append(task)
    elif task_2 == "2":
      tomorrow.append(task)
    elif task_2 == "3":
      other.append(task)
    print("Задача добавлена")

  elif  command == "exit":
    print("Спасибо за использование! До свидания!")
    break

  else:
    print("Неизвестная команда")
    break
