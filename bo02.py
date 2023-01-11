import sqlite3

def db_create():
	conn  = sqlite3.connect('bot.db')
	cur = conn.cursor()
	cur.execute("""CREATE TABLE IF NOT EXISTS users (
		id integer PRIMARY KEY AUTOINCREMENT,
		telegram_id varchar(30),
		username varchar (50),
		phone_number varchar(15)NULL,
		lat_x text NULL,
		lon_y text NULL )""")


def db_select(telegram_id):
	conn  = sqlite3.connect('bot.db')
	cur = conn.cursor()
	cur.execute(f"SELECT * FROM users WHERE telegram_id='{telegram_id}' ")
	data = cur.fetchone()
	return data

def db_insert(telegram_id,username):
	conn  = sqlite3.connect('bot.db')
	cur = conn.cursor()
	cur.execute(f"""INSERT INTO users (telegram_id,username) VALUES ("{telegram_id}","{username}")""")
	return conn.commit()

def db_update(telegram_id,phone_number):
	conn  = sqlite3.connect('bot.db')
	cur = conn.cursor()
	cur.execute(f"""UPDATE users SET phone_number="{phone_number}" Where telegram_id="{telegram_id}" """)
	return conn.commit()
def db_update_location(telegram_id,lat_x,lon_y):
	conn  = sqlite3.connect('bot.db')
	cur = conn.cursor()
	cur.execute(f"""UPDATE users SET lat_x="{lat_x}",lon_y="{lon_y}" Where telegram_id="{telegram_id}" """)
	return conn.commit()
