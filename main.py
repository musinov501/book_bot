from data.loader import db, bot
import handlers



if not db.get_all_books():
    db.insert_books(
        "To Kill a Mockingbird",
        "Harper Lee",
        42000,
        "A novel about justice and race in America.",
        "Novels",
        "books/novels/to_kill_a_mockingbird.pdf"
    )


    db.insert_books(
        "Clean Code",
        "Robert C. Martin",
        60000,
        "Software craftsmanship handbook.",
        "Programming",
        "books/programming/clean_code.pdf"
    )

    db.insert_books(
        "Pride and Prejudice",
        "Jane Austen",
        6.99,
        "A classic novel of manners exploring the nature of love, reputation, and class in 19th-century England.",
        "books/novels/pride.pdf"
    )

    db.insert_books(
        "1984",
        "George Orwell",
        8.49,
        "A dystopian novel depicting a totalitarian regime that uses surveillance and propaganda to control its citizens.",
        "books/novels/big_brother.pdf"
    )


    db.insert_books(
        "Python Crash Course",
        "Eric Matthes",
        10.99,
        "A hands-on, project-based introduction to programming using Python. Great for beginners who want to build real-world applications.",
        "books/programming/python_crash_course.pdf"
    )

    db.insert_books(
        "Clean Code",
        "Robert C. Martin",
        12.50,
        "A widely recommended book on writing clean, maintainable, and efficient code with examples in Java, but applicable to all programmers.",
        "books/programming/write_clean.pdf"
    )





if __name__ == '__main__':
    db.create_table_books()
    db.create_table_users()

    bot.infinity_polling()