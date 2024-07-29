from telebot import TeleBot
from telebot.types import Message
from dotenv import load_dotenv
from datetime import datetime
import os

# загрузка переменных окружения
load_dotenv('.env')
TG_TOKEN = os.getenv('TG_TOKEN')

# сохраняем инициализированный объект бота
bot = TeleBot(TG_TOKEN)

class Purchase:
    def __init__(self, item_name, price):
        self.item_name = item_name
        self.price = price
        self.purchase_date = datetime.now().strftime("%d-%m-%Y")

    def __str__(self):
        return f"{self.item_name} - {self.price} руб. ({self.purchase_date})"

class Client:
    def __init__(self, user_id, first_name, last_name, birth_date, card_id):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.card_id = card_id
        self.purchases = []

clients = []  # Список для хранения информации о клиентах

def add_client(user_id, first_name, last_name, birth_date, card_id):
    # Проверяем, существует ли клиент с указанным card_id
    existing_client = next((client for client in clients if str(client.card_id) == str(card_id)), None)

    if existing_client:
        bot.send_message(user_id, "Клиент с указанным card_id уже существует.")
    else:
        new_client = Client(user_id, first_name, last_name, birth_date, card_id)
        clients.append(new_client)
        bot.send_message(user_id, "Клиент успешно записан. Для просмотра списка клиентов отправьте /show_base")


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message: Message) -> None:
    """Отправляет приветственное сообщение и помощь по использованию бота."""
    welcome_text = """
    Привет! Я бот для управления задачами. Вот как со мной работать:
    - Чтобы добавить клиента, отправьте в одном сообщение /add_client Имя, Фамилия, Дата рождения (DD.MM.YYYY), ID карты
    - Для просмотра списка клиентов отправьте /show_base
    - Для просмотра более подробной информации о клиенте отправьте /client_info и номер клиента
    - Для удаления клиента из базы введите /delete_client и номер клиента
    - Для добавления покупки введите /add_purchase card_id, название_товара, цена
    - Чтобы посмотреть эту памятку снова, отправьте /help
    """

    user_id: int = message.chat.id
    bot.send_message(user_id, welcome_text)

@bot.message_handler(commands=['add_client'])
def handle_add_client(message: Message) -> None:
    """Добавляет клиента"""
    user_id: int = message.chat.id
    text: str = message.text[11:].strip()   # берем текст после /add_client

    if not text:
        bot.send_message(user_id, "Введите данные клиента. Памятка - /help")
        return
    else: 
        client_data = text.split(", ")   # для разделения текста
        add_client(user_id, *client_data)
        
@bot.message_handler(commands=['show_base'])
def show_base(message: Message) -> None:
    """Выводит всех клиентов."""
    user_id: int = message.chat.id

    message_text = "Ваши клиенты:\n"
    message_text_2 = """
    Для просмотра более подробной информации о клиенте отправьте /client_info и номер клиента
    Для удаления клиента из базы отправьте /delete_client и номер клиента
    """
    for i, client in enumerate(clients, start=1):
        message_text += f"{i}. {client.first_name} {client.last_name} {client.card_id}\n"
    
    bot.send_message(user_id, message_text + message_text_2)

@bot.message_handler(commands=['client_info'])
def client_info(message: Message) -> None:
    """Выводит подробную информацию о клиенте"""
    user_id: int = message.chat.id
    text = message.text[12:].strip()

    try:
        client_number = int(text)
        client_info = clients[client_number - 1]  # С учетом индексации с 0
        full_info = (
            f"Имя: {client_info.first_name}\n"
            f"Фамилия: {client_info.last_name}\n"
            f"Дата рождения: {client_info.birth_date}\n"
            f"ID карты: {client_info.card_id}\n"
        )

        if client_info.purchases:
            purchases_info = "\nПокупки:\n"
            for purchase in client_info.purchases:
                purchases_info += str(purchase) + "\n"
            full_info += purchases_info
        else:
            full_info += "\nПокупок нет."

        bot.send_message(user_id, full_info)
    except (ValueError, IndexError):
        bot.send_message(user_id, "Некорректный номер клиента. Пожалуйста, введите /client_info и номер клиента.")



@bot.message_handler(commands=["add_purchase"])
def handle_add_purchase(message: Message) -> None:
    """Добавляет товар"""
    user_id: int = message.chat.id
    text: str = message.text[13:].strip()

    try:
        # Разбиваем текст на части, используя запятые как разделитель
        parts = text.split(", ")

        # Извлекаем данные из частей
        card_id = int(parts[0])
        item_name = parts[1]
        price = float(parts[2])
        purchase_date = datetime.now().strftime("%d-%m-%Y")

        # Проверяем, существует ли клиент с указанным card_id
        existing_client = next((client for client in clients if str(client.card_id) == str(card_id)), None)

        if existing_client:
            # Создаем новую покупку
            new_purchase = Purchase(item_name, price)
            new_purchase.purchase_date = purchase_date

            # Добавляем покупку к соответствующему клиенту
            existing_client.purchases.append(new_purchase)

            bot.send_message(user_id, f"Покупка для клиента {existing_client.first_name} {existing_client.last_name} добавлена.")
        else:
            bot.send_message(user_id, "Клиент с указанным card_id не найден.")

    except (ValueError, IndexError, TypeError):
        bot.send_message(user_id, "Некорректный формат ввода. Используйте /add_purchase card_id, название_товара, цена.")

@bot.message_handler(commands=['delete_client'])
def delete_client(message: Message) -> None:
    """Функция удаления клиента"""
    user_id: int = message.chat.id
    text = message.text[14:].strip()

    client_index = int(text)
    if 1 <= client_index <= len(clients):
        clients.pop(client_index - 1) # удаляет выбранного клиента
        bot.send_message(user_id, "Клиент удалён. Для просмотра списка клиентов отправьте /show_base")
    else:
        bot.send_message(user_id, "Некорректный номер клиента. Пожалуйста, укажите существующий номер.")

if __name__ == "__main__":  # для запуска скрипта только напрямую
    bot.infinity_polling()  # проверяет чат на наличие новых сообщений