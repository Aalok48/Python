import tkinter as tk
from tkcalendar import Calendar, DateEntry

root = tk.Tk()
root.title("Date and Time Picker")

def show_calendar():
    top = tk.Toplevel(root)
    top.title("Calendar")
    cal = Calendar(top, selectmode='day', year=2023, month=1, day=1)
    cal.pack(pady=20)

    def grab_date():
        my_date = cal.get_date()
        date_entry.delete(0, tk.END)
        date_entry.insert(0, my_date)
        top.destroy()

    tk.Button(top, text="Select", command=grab_date).pack()

date_entry = DateEntry(root, width=12, background="darkblue", foreground="white", borderwidth=2)
date_entry.pack(pady=20)

tk.Button(root, text="Choose Date", command=show_calendar).pack()

hour_entry = tk.Entry(root, width=2)
hour_entry.pack(side=tk.LEFT, padx=5)
hour_entry.insert(0, "HH")

minute_entry = tk.Entry(root, width=2)
minute_entry.pack(side=tk.LEFT, padx=5)
minute_entry.insert(0, "MM")

second_entry = tk.Entry(root, width=2)
second_entry.pack(side=tk.LEFT, padx=5)
second_entry.insert(0, "SS")

root.mainloop()