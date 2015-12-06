import sqlite3
from config import DATABASE_PATH

with sqlite3.connect(DATABASE_PATH) as connection:
	c = connection.cursor()
	c.execute(
		"""CREATE TABLE garage(car_id INTEGER PRIMARY KEY AUTOINCREMENT,
		make TEXT NOT NULL, model TEXT NOT NULL, color TEXT NOT NULL, 
  		year INTEGER NOT NULL)"""
	)
	c.execute(
		'INSERT INTO garage (make, model, color, year)'
		'VALUES("Volkswagen" "Golf", "Black", 2004)'
	)
	c.execute(
		'INSERT INTO garage (make, model, color, year)'
		'VALUES("Aston Martin", "V12 Vanquish", "Silver", 2008)'
	)