import sqlite3
from _config import DATABASE_PATH

with sqlite3.connect(DATABASE_PATH) as connection:
	c = connection.cursor()	
	c.execute(
		'INSERT INTO garage (make, model, color, year)'
		'VALUES("Volkswagen", "Golf", "Black", 2004)'
	)
	c.execute(
		'INSERT INTO details (odom, oil, trans, brake)'
		'VALUES(14350, "Last month", "Last week", "Last week")'
	)