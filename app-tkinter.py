import tkinter as tk
from tkinter import *
from tkinter import ttk

# Create window
window = Tk()
# Title of window app
window.title('Flight Scrapper')
window.configure(background='black')

# Title of app
greeting = tk.Label(text="Find the best flight tickets for your upcoming holidays!", bg='black', fg='white', font='sans-serif 12 bold')
greeting.grid(row=0,column=0)

# One way widget
oneway_checkbox = Checkbutton(window, text="One Way", variable=IntVar(), bg='black', fg='white',)
oneway_checkbox.grid(row=1, column=1, sticky=E)

# Number of stops widget
label_fromairport = tk.Label(text="From:", font='none 10 bold', bg='black', fg='white')
label_fromairport.grid(row=2,column=0, sticky=W)
stops_combo = ttk.Combobox(window, values=["0", "1", "2"])
stops_combo.grid(row=1, column=2, sticky=E)

# From airport widget
label_fromairport = tk.Label(text="From:", font='none 10 bold', bg='black', fg='white')
label_fromairport.grid(row=2,column=0, sticky=W)
fromairport = Entry(window, width=20)
fromairport.grid(row=2,column=1, sticky=W)

# To airport widget
label_toairport = tk.Label(text="To:", font='none 10 bold', bg='black', fg='white')
label_toairport.grid(row=3,column=0, sticky=W)
toairport = Entry(window, width=20)
toairport.grid(row=3,column=1, sticky=W)

# Departure date widget
label_depdate = tk.Label(text="Depart Date:", font='none 10 bold', bg='black', fg='white')
label_depdate.grid(row=4,column=0, sticky=W)
depdate = Entry(window, width=20)
depdate.grid(row=4,column=1, sticky=W)

# Return date widget
label_retdate = tk.Label(text="Return Date", font='none 10 bold', bg='black', fg='white')
label_retdate.grid(row=5,column=0, sticky=W)
retdate = Entry(window, width=20)
retdate.grid(row=5,column=1, sticky=W)

# Submit Button widget
submit_button = Button(window, text='Submit', width=6).grid(row=6,column=1, sticky=E)
window.mainloop()
