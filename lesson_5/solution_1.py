# Бот-ассистент Ромашка

class TodoBot:
    def __init__(self):
        self.todos = []

    def add_todo(self, date, title, description, tags):
        todo = {
            'date': date,
            'title': title,
            'description': description,
            'tags': tags
        }
        self.todos.append(todo)
        print("Дело успешно добавлено!")

    def list_todos(self):
        if not self.todos:
            print("У вас нет запланированных дел.")
        else:
            for idx, todo in enumerate(self.todos, 1):
                print(f"Дело {idx}:")
                print(f"Дата: {todo['date']}")
                print(f"Название: {todo['title']}")
                print(f"Описание: {todo['description']}")
                print(f"Теги: {', '.join(todo['tags'])}")
                print("--------------------")
    def remove_todo_by_index(self, index):
        if index < len(self.todos):
            del self.todos[index]
            print("Дело успешно удалено.")
        else:
            print("Неверный индекс дела.")


# Создаем бота
todo_bot = TodoBot()

# Добавляем дела
todo_bot.add_todo("2022-10-20", "День рождения друга", "Купить подарок и поздравить друга", ["день рождения"])
todo_bot.add_todo("2022-11-15", "Важное дело", "Завершить проект и отправить отчет", ["важное дело", "не забыть"])

# Выводим список дел
todo_bot.list_todos()

# Удаляем дело по индексу
todo_bot.remove_todo_by_index(0)
todo_bot.list_todos()