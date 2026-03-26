import sqlite3


def get_books_by_author(author):
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM books
        WHERE author = ?
        ORDER BY name ASC
    """, (author,))

    books = cursor.fetchall()

    conn.close()
    return books