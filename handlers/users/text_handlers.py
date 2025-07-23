from data.loader import bot, db
from telebot.types import Message
from keyboards.default import category_buttons




@bot.message_handler(func=lambda message: message.text == "📚Categorialar")
def reaction_to_categories(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Categoriya tanlang👇👇👇", reply_markup=category_buttons())

