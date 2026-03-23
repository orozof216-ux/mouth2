import sqlite3


# функция для создания таблицы
def create_table(connection):
    connection.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY,
            name TEXT,
            author TEXT,
            publication_year INTEGER,
            genre TEXT,
            number_of_pages INTEGER,
            number_of_copies INTEGER
        )
    """)
    print("Таблица создана")


# функция для добавления книг
def insert_books(connection):
    books = [
        ("Война и мир", "Лев Толстой", 1869, "Роман", 1225, 5),
        ("Преступление и наказание", "Фёдор Достоевский", 1866, "Роман", 671, 4),
        ("Мастер и Маргарита", "Михаил Булгаков", 1967, "Фантастика", 470, 6),
        ("Гарри Поттер", "Джоан Роулинг", 1997, "Фэнтези", 500, 10),
        ("1984", "Джордж Оруэлл", 1949, "Антиутопия", 328, 7),
        ("Шерлок Холмс", "Артур Конан Дойл", 1892, "Детектив", 307, 3),
        ("Алхимик", "Пауло Коэльо", 1988, "Роман", 208, 8),
        ("Три товарища", "Эрих Мария Ремарк", 1936, "Роман", 480, 5),
        ("Маленький принц", "Антуан де Сент-Экзюпери", 1943, "Сказка", 96, 9),
        ("Хоббит", "Джон Толкин", 1937, "Фэнтези", 310, 6)
    ]

    connection.executemany("""
        INSERT INTO books (
            name, author, publication_year,
            genre, number_of_pages, number_of_copies
        ) VALUES (?, ?, ?, ?, ?, ?)
    """, books)

    print("Книги добавлены")


if __name__ == "__main__":
    connection = sqlite3.connect("library.db")

    create_table(connection)
    insert_books(connection)

    connection.commit()
    connection.close()

    print("Работа завершена")