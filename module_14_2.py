# Код из предыдущего задания
import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

# cursor.execute('''
# CREATE TABLE IF NOT EXISTS Users(
# id INTEGER PRIMARY KEY,
# username TEXT NOT NULL,
# email TEXT NOT NULL,
# age INTEGER,
# balance INTEGER NOT NULL
# )
# ''')
#
# cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")
#
# for i in range(1, 11):
#     cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)", (f'User{i}', f'example{i}@gmail.com', f'{i*10}', '1000'))
#
# for i in range(1, 11, 2):
#     cursor.execute("UPDATE Users SET balance = ? WHERE id = ?", (500, i))
#
# for i in range(1, 11, 3):
#     cursor.execute("DELETE from Users WHERE id = ?", (i,))
#
# cursor.execute("SELECT * FROM Users WHERE age != ?", (60,))
# users = cursor.fetchall()
# for user in users:
#     print (f'Имя: {user[1]} | Почта: {user[2]} | Возраст: {user[3]} | Баланс: {user[4]}')

# Удаление пользователя с id=6

cursor.execute("DELETE from Users WHERE id = ?", (6,))
connection.commit()

# Подсчёт кол-ва всех пользователей

cursor.execute("SELECT COUNT(*) FROM Users")
total_users = cursor.fetchone()[0]

# Подсчёт суммы всех балансов

cursor.execute("SELECT SUM(balance) FROM Users")
all_balances = cursor.fetchone()[0]

print(all_balances / total_users)
connection.close()
