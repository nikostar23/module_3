"""Бот-ассистент Ромашка"""

import TeleBot
import Message
import load_dotenv
from datetime import datetime
import os


# загрузка переменных окружения
load_dotenv(".env")
TG_TOKEN = os.getenv("TG_TOKEN")

# сохраняем инициализированный объект бота
bot =TeleBot(TG_TOKEN)

# хранилище данных пользователя
tasks: list[list[str]] = []

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message: Message) -> None:
    """Отправляет приветственное сообщение и помощь по использованию бота."""
    welcome_text = """
    Привет! Я бот для управления задачами. Вот как со мной работать:
    - Чтобы добавить задачу, отправьте в  одном сообщении /add_task Название. Описание.
    - Чтобы посмотреть ваши задачи, отправьте /show_tasks
    - Чтобы удалить задачу отправьте /del_task и введите номер задачи.
    - Чтобы полностью очистить список задач оправьте /clear_tasks_list
    - Чтобы посмотреть эту памятку снова, отправьте /help
    """

    user_id: int = message.chat.id
    bot.send_message(user_id, welcome_text)

@bot.message_handler(commands=['add_task'])
def add_task(message: Message) -> None:
    """Обрабатывает команду /add_task."""
    user_id: int = message.chat.id
    text: str = message.text[9:].strip()  # берём текст после '/add_task'

    if not text:
        bot.send_message(user_id, "Вы не указали задачу. Памятка - /help")
        return
    else:
        current_time = datetime.now().strftime("%d-%m-%Y %H:%M")
        task_whith_time = f"{current_time} - {text}"    # добавляем время создания задачи
        bot.send_message(user_id, "Ваша задача успешно записана. Для просмотра списка ваших задач введите /show_tasks")
        
        task_parts = task_whith_time.split('.')  # для разделения задач
        tasks.append(task_parts)  # для сохранения задач в список к остальным задачам

@bot.message_handler(commands=['del_task'])
def delete_task(message: Message) -> None:
    """Обрабатывает команду /del_task"""
    user_id: int = message.chat.id
    text: str = message.text[10:].strip()  # берём текст после '/del_task'

    if not text.isdigit():
        bot.send_message(user_id, "Пожалуйста, введите номер задачи для удаления.")
        return

    task_index = int(text)
    if 1 <= task_index <= len(tasks):
        tasks.pop(task_index - 1)  # удаляем задачу с указанным номером
        bot.send_message(user_id, "Ваша задача удалена. Для просмотра списка ваших задач введите /show_tasks")
    else:
        bot.send_message(user_id, "Некорректный номер задачи. Пожалуйста, укажите существующий номер.")

@bot.message_handler(commands=['clear_tasks_list'])
def clear_tasks_list(message: Message) -> None:
    """Обрабатывает команду /clear_tasks_list"""
    user_id: int = message.chat.id
    
    if tasks:
        confirmation_text = "Вы уверены, что хотите полность отчистить список задач? Введите 'да' или 'нет'."
        bot.send_message(user_id, confirmation_text)
        bot.register_next_step_handler(message, process_clear_confirmation) 
    else:
        bot.send_message(user_id, "Список уже пуст")

def process_clear_confirmation(message: Message) -> None:
    """Обрабатывает ответ пользователя на вопрос подтверждения очистки"""
    user_id: int = message.chat.id
    confirmation = message.text.lower()

    if confirmation == 'да':
        tasks.clear()   # отчищает список
        bot.send_message(user_id, "Список задач полностью очищен.")
    elif confirmation == 'нет':
        bot.send_message(user_id, "Отчистка списка задач отменена.")
    else:
        bot.send_message(user_id, "Пожалуйста введите 'да' или 'нет'.")

@bot.message_handler(commands=['show_tasks'])
def show_tasks(message: Message) -> None:
    """Выводит все текущие задачи пользователя."""
    user_id: int = message.chat.id

    message_text = "Ваши задачи:\n"
    message_text_2 = "Для удаления задачи введите /delete_task и номер задачи"
    for i, task in enumerate(tasks, start=1):
        message_text += f"{i}. {task[0]} - {task[1]}\n" 

    bot.send_message(user_id, message_text + message_text_2)

if __name__ == "__main__":  # для запуска скрипта только напрямую
    bot.infinity_polling()  # проверяет чат на наличие новых сообщений