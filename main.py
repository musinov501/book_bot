from data.loader import db, bot
import handlers


if __name__ == '__main__':
    db.create_table_users()
    bot.infinity_polling()