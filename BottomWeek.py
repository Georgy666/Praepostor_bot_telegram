import sqlite3

conn = sqlite3.connect('week.db')
cursor = conn.cursor()
cursor.execute("SELECT bottom_all FROM bottom_week")
Bottom_array = cursor.fetchall()

cursor2 = conn.cursor()
cursor2.execute("SELECT mon FROM bottom_week")
Bottom_array_Mon = cursor2.fetchall()

cursor3 = conn.cursor()
cursor3.execute("SELECT tue FROM bottom_week")
Bottom_array_Tue = cursor3.fetchall()

cursor4 = conn.cursor()
cursor4.execute("SELECT wed FROM bottom_week")
Bottom_array_Wed = cursor4.fetchall()

cursor5 = conn.cursor()
cursor5.execute("SELECT thu FROM bottom_week")
Bottom_array_Thu = cursor5.fetchall()

cursor6 = conn.cursor()
cursor6.execute("SELECT fri FROM bottom_week")
Bottom_array_Fri = cursor6.fetchall()

cursor7 = conn.cursor()
cursor7.execute("SELECT sat FROM bottom_week")
Bottom_array_Sat = cursor7.fetchall()