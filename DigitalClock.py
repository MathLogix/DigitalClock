#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
from persiantools.jdatetime import JalaliDate
from datetime import datetime

def update_datetime():
    current_time = datetime.now().strftime("%H:%M:%S")
    current_date1 = datetime.today()
    current_date2 = JalaliDate.today()
    time_label.config(text=f"{current_time}")
    time_label.after(1000, update_datetime)
    date_label1.config(text=f"{current_date1.strftime('%Y/%m/%d')}")
    date_label2.config(text=f"{current_date2.strftime('%Y/%m/%d')}")

root = tk.Tk()
root.title("DigitalClock")
root.attributes("-topmost", True)

time_label = ttk.Label(root, font=("Helvetica", 32))
time_label.pack()
date_label1 = ttk.Label(root, font=("Helvetica", 12))
date_label1.pack()
date_label2 = ttk.Label(root, font=("Helvetica", 12))
date_label2.pack()

update_datetime()

root.mainloop()

