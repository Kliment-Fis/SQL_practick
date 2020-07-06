from prettytable import PrettyTable as PT 
import sqlite3
import time

# Подключение/Connect  
conn = sqlite3.connect('database')
cursor = conn.cursor()

# Создаём таблицу если её нет/Create Teable, if her none

cursor.execute('''CREATE TABLE IF NOT EXISTS humans (
				UserID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
				first_name varchar(30),
				last_name varchar(30),
				birthday date,
				age varchar(7)
				);''')

# Здесь главный код/Place for main code
# функции/functions

def people_add():
	first_name = input('Введите имя человека для добавления в таблицу: ')
	last_name  = input('Введите фамилию человека для добавления в таблицу: ')
	birthday   = input('Введите день рождения человека для добавления в таблицу: ')
	age        = input('Введите возраст человека для добавления в таблицу: ')

	cursor.execute('''INSERT INTO humans VALUES (Null,?, ?, ?, ?);''', (first_name, last_name, birthday, age))
	conn.commit()

def print_db():
	cursor.execute('''SELECT * FROM humans ;''')
	result = cursor.fetchall()
	print()
	table = PT()
	table.field_names = ['ID','First_name','Last_name','Birthday','Age']

	if len(result) == 0:
		print('\n', 'Сдесь пока никого нет, но скоро сдесь будут люди', '\n')
		print(table)
	else:
		for man in result:
			table.add_row(man)
		print(table.get_string(sortby="Age", reversesort=True, align='c'))

def delet_people():
	UserID = input('Введите ID пользователя данные которого хотите удалить: ')
	cursor.execute('''DELETE FROM humans WHERE UserID= ? ;''', (UserID))
	conn.commit()

def update_people():
	UserID = input('Введите ID пользователя данные которого хотите изменить: ')
	cursor.execute('''SELECT * FROM humans WHERE UserID=?;''',(UserID))
	result = cursor.fetchall()
	print(result)
	first_name = result[0][1]
	last_name  = result[0][2]
	birthday   = result[0][3]
	age        = result[0][4]

	update_can()
	update = input('Обновить нужно: ')
	if update.lower() == 'имя':
		first_name = input('Введите новое имя: ')
	elif update.lower() == 'фамилию':
		last_name = input('Введите новою фамилию: ')
	elif update.lower() == 'дату рождения':
		birthday = input('Введите новою дату рождения: ')
	elif update.lower() == 'возраст':
		age = input('Введите новый возраст: ')
	# else:
	# 	print('Ошибка ввода.')
	# 	update_can()
	cursor.execute('''UPDATE humans SET first_name=?, last_name=?, birthday=?, age=? WHERE UserID=?;''', (first_name, last_name, birthday, age, UserID))
	conn.commit()

def print_can():
	print('-Команды:')
	print('-Выйти')
	print('-Показать всех')
	print('-Удалить человека')
	print('-Добавить человека')
	print('-обновить данные о человеке')

def update_can():
	print('Обновить можно:')
	print('-Имя')
	print('-Фамилию')
	print('-Возраст')
	print('-Дату рождения')


# бесконечный цикл/loop 

while True:
	print()
	time.sleep(3)

	print_can()

	i = input('Введите команду: ')
	if i.lower() == 'выйти':
		break
	elif i.lower() == 'показать всех':
		print_db()
	elif i.lower() == 'добавить человека':
		people_add()
	elif i.lower() == 'удалить человека':
		delet_people()
	elif i.lower() == 'обновить данные о человеке': 
		update_people()
	else:
		print('-Команда введена не правильно, вот список команд.')
		print_can()
		continue

# Закрытие соединения/Close connect
conn.close()