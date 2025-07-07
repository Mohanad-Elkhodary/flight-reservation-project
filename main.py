from tkinter import *
import sqlite3
window = Tk()
window.geometry('500x600')
window.title('Flight reservation')

conn = sqlite3.connect('Flight.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS bookings(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
from_city TEXT,
to_city TEXT,
date TEXT)
''')
conn.commit()
conn.close()
logo = PhotoImage(file=r"C:\Users\dodoe\Downloads\jpg2png\plane logo.png")
window.iconphoto(True, logo)
Label(window, text='Book your flight',font=('Ariel', 15),).pack(pady=10)
Label(window,text='passenger name').pack()
name_entry = Entry(window, width=30)
name_entry.pack()
Label(window,text='from').pack()
from_entry = Entry(window, width=30)
from_entry.pack()
Label(window,text='to').pack()
to_entry = Entry(window, width=30)
to_entry.pack()
Label(window,text='Date(YYYY/MM/DD)').pack()
date_entry = Entry(window, width=30)
date_entry.pack()
def Book_flight():
    name = name_entry.get()
    from_city= from_entry.get()
    to_city = to_entry.get()
    date = date_entry.get()
    conn = sqlite3.connect('Flight.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO bookings(name, from_city, to_city, date) VALUES (?, ?, ?, ?)",(name,from_city,to_city,date))
    conn.commit()
    conn.close()
    confirmation=(f'{name} your flight from {from_city} to {to_city} on {date} is booked')
    Label(window, text=confirmation, font='bold',fg='green').pack()
button = Button(window, text='Book flight', command=Book_flight)
button.pack(pady=10)
window.mainloop()