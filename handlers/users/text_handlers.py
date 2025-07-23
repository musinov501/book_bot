from data.loader import bot, db
from telebot.types import Message
from keyboards.default import category_buttons




@bot.message_handler(func=lambda message: message.text == "📚Categorialar")
def reaction_to_categories(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Categoriya tanlang👇👇👇", reply_markup=category_buttons())


@bot.message_handler(func=lambda message: message.text == "📚 Novels")
def reaction_to_novels(message: Message):
    chat_id = message.chat.id
    books = db.get_books_by_category("Novels")

    if not books:
        bot.send_message(chat_id, "Bu bo'limda hozircha kitob yo'q")
        return

    for book in books:
        book_id, title, author, price, description, category, file_path = book
        caption = f"📖 *{title}*\n👤 {author}\n💰 {price} so'm\n📝 {description}"
        try:
            with open(file_path, 'rb') as file:
                bot.send_document(chat_id, file, caption= caption, parse_mode='Markdown')
        except FileNotFoundError:
            bot.send_message(chat_id, f"❌ Fayl topilmadi: {file_path}" )



@bot.message_handler(func=lambda message: message.text == "💻 Programming")
def reaction_to_programming(message: Message):
    chat_id = message.chat.id
    books = db.get_books_by_category("Programming")

    if not books:
        bot.send_message(chat_id, "Bu bo'limda hozircha kitob yo'q")
        return

    for book in books:
        book_id, title, author, price, description, category, file_path = book
        caption = f"📖 *{title}*\n👤 {author}\n💰 {price} so'm\n📝 {description}"
        try:
            with open(file_path, 'rb') as file:
                bot.send_document(chat_id, file, caption=caption, parse_mode='Markdown')
        except FileNotFoundError:
            bot.send_message(chat_id, f"❌ Fayl topilmadi: {file_path}")

