from telebot.types import Message, ReplyKeyboardRemove
from data.loader import bot, db
from keyboards.default import main_menu, phone_button


REGISTER = {}

@bot.message_handler(commands=['start'])
def reaction_to_start(message: Message):
    chat_id = message.chat.id
    full_name = message.from_user.full_name
    from_user_id = message.from_user.id
    text = f"Assalomu alaykum {full_name}!! 📚📚Online Books botiga xush kelibsiz!!!\n\n Avval ro'yxatdan o'ting:\nTo'liq ismingizni kiriting👇👇👇"

    user = db.get_user(from_user_id)
    print("USER FROM DB:", user)

    if not user:
        db.insert_telegram_id(from_user_id)
        msg = bot.send_message(chat_id, text)

        bot.register_next_step_handler(msg, get_name)

    else:
        if user[1] is None or user[2] is None:
            msg = bot.send_message(chat_id, text)

            bot.register_next_step_handler(msg, get_name)

        else:
            bot.send_message(chat_id, "O'zingizga kerak bo'lgan ma'lumotni tanlang👇👇👇", reply_markup=main_menu())



def get_name(message: Message):
    chat_id = message.chat.id
    from_user_id = message.from_user.id


    if message.text == '/start':
        bot.send_message(chat_id, "Bekore qilindi!!")
    else:
        full_name = message.text
        REGISTER[from_user_id] = {
            'full_name': full_name
        }

        msg = bot.send_message(chat_id, "Pastdagi tugmani bosib, telefon raqamingizni yuboring👇👇👇", reply_markup=phone_button())
        bot.register_next_step_handler(msg, get_phone)


def get_phone(message: Message):
    chat_id = message.chat.id
    from_user_id = message.from_user.id


    if message.contact:
        phone_number = message.contact.phone_number
        full_name = REGISTER[from_user_id]['full_name']
        db.update_user_info(from_user_id, full_name, phone_number)
        bot.send_message(chat_id, "Tabriklaymiz siz ro'yxatdan o'tdingiz 🎉🎉🎉", reply_markup=ReplyKeyboardRemove())
        bot.send_message(chat_id, "O'zingizga kerak bo'lgan ma'lumotni tanlang👇👇👇", reply_markup=main_menu())

    else:
        if message.text == '/start':
            bot.send_message(chat_id, "Bekore qilindi!!")
        else:
            msg = bot.send_message(chat_id, "Pastdagi tugmani bosib, telefon raqamingizni yuboring👇👇👇",
                                   reply_markup=phone_button())
            bot.register_next_step_handler(msg, get_phone)


