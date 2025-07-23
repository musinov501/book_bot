from telebot.types import ReplyKeyboardMarkup, KeyboardButton



def main_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = KeyboardButton("📚Categorialar")
    btn2 = KeyboardButton("‼️Do'kon haqida qisqacha")
    markup.add(btn1, btn2)
    return markup


def phone_button():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    btn = KeyboardButton("📞Raqamni yuborish", request_contact=True)
    markup.add(btn)
    return markup


def category_buttons():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("📚 Novels", "💻 Programming")
    markup.add("🏠 Bosh menyu")
    return markup

