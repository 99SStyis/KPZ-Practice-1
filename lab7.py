import sqlite3
import hashlib

# Підключення до бази даних
conn = sqlite3.connect('users.db')

# Створення таблиці користувачів, якщо вона ще не існує
conn.execute('''CREATE TABLE IF NOT EXISTS users
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             username TEXT NOT NULL UNIQUE,
             password TEXT NOT NULL);''')

# Функція для створення нового користувача
def register():
    username = input('Введіть ім\'я користувача: ')
    password = input('Введіть пароль: ')

    # Хешування пароля перед збереженням в базу даних
    hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()

    try:
        # Додавання нового користувача до бази даних
        conn.execute("INSERT INTO users (username, password) VALUES (?, ?);", (username, hashed_password))
        conn.commit()
        print('Користувач успішно створений')
    except sqlite3.IntegrityError:
        print('Користувач з таким ім\'ям вже існує')

# Функція для входу в систему
def login():
    username = input('Введіть ім\'я користувача: ')
    password = input('Введіть пароль: ')

    # Хешування введеного пароля для перевірки збігу з паролем з бази даних
    hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()

    # Перевірка наявності користувача з введеним ім'ям та паролем в базі даних
    cursor = conn.execute("SELECT username FROM users WHERE username = ? AND password = ?", (username, hashed_password))

    result = cursor.fetchone()
    if result:
        user_id = result[0]
        print('Ви увійшли до системи')
        return user_id
    else:
        print('Неправильне ім\'я користувача або пароль')
        return None

# Функція для створення нового завдання
def create_task(user_id):
    title = input('Введіть назву завдання: ')
    description = input('Введіть опис завдання: ')

    # Додавання нового завдання до бази даних
    conn.execute("INSERT INTO tasks (user_id, title, description) VALUES (?, ?, ?);", (user_id, title, description))
    conn.commit()
    print('Завдання успішно створене')

def list_tasks(user_id):
# Виконання запиту до бази даних
    conn = sqlite3.connect('tasks.db')

    cursor = conn.execute("SELECT id, title, description FROM tasks WHERE user_id = ?;", (user_id,))
    rows = cursor.fetchall()
# Виведення результатів запиту
    if rows:
        print('Список завдань:')
        for row in rows:
            print(f'{row[0]}. {row[1]}: {row[2]}')
    else:
        print('У вас немає жодного завдання')

def delete_task(user_id):
    conn = sqlite3.connect('tasks.db')

    task_id = input('Введіть ID завдання, яке бажаєте видалити: ')
    # Виконання запиту до бази даних
    cursor = conn.execute("SELECT id FROM tasks WHERE user_id = ? AND id = ?;", (user_id, task_id))
    result = cursor.fetchone()
    if result:
        conn.execute("DELETE FROM tasks WHERE id = ?;", (task_id,))
        conn.commit()
        print(f'Завдання з ID {task_id} успішно видалено')
    else:
        print('Завдання з таким ID не знайдено або не належить вам')

conn = sqlite3.connect('task_list.db')
c = conn.cursor()

# Створення таблиці users
c.execute('''CREATE TABLE IF NOT EXISTS users
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             username TEXT NOT NULL UNIQUE,
             password TEXT NOT NULL)''')

conn.commit()
conn.close()

# Підключення до бази даних
conn = sqlite3.connect('task_list.db')
c = conn.cursor()

def exit_program():
    print('Дякую, що скористалися нашою програмою. До побачення!')
    conn.close()



# Функція для виходу з системи
def logout():
    print("Вихід з системи успішний")

def main():
    print('Ласкаво просимо до системи керування завданнями!')
    while True:
        print('\nВиберіть опцію:')
        print('1 - зареєструвати нового користувача')
        print('2 - увійти в систему')
        print('3 - вийти з програми')
        choice = input('Ваш вибір: ')

        if choice == '1':
            register()
        elif choice == '2':
            user_id = login()
            if user_id:
                while True:
                    print('\nВиберіть опцію:')
                    print('1 - переглянути список завдань')
                    print('2 - створити нове завдання')
                    print('3 - видалити завдання')
                    print('4 - вийти з облікового запису')
                    sub_choice = input('Ваш вибір: ')

                    if sub_choice == '1':
                        list_tasks(user_id)
                    elif sub_choice == '2':
                        create_task(user_id)
                    elif sub_choice == '3':
                        delete_task(user_id)
                    elif sub_choice == '4':
                        break
                    else:
                        print('Неправильний вибір')
        elif choice == '3':
            print('До побачення!')
            conn.close()
            break
        else:
            print('Неправильний вибір')