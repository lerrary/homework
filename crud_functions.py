import sqlite3

def initiate_db():
    connection = sqlite3.connect('initiate.db')
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    )'''
                   )
    for i in range(1, 5):
        cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)", (f'Product{i}', f'описание {i}', f'{i*100}'))
    connection.commit()
    connection.close()

def get_all_products(a):
    connection = sqlite3.connect('initiate.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Products WHERE id = ?", (a,))
    items = cursor.fetchall()
    for item in items:
        title = item[1]
        description = item[2]
        price = item[3]
    return [title, description, price]
    connection.commit()
    connection.close()
