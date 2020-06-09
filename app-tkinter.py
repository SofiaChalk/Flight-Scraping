import tkinter as tk
from tkinter import *
from tkinter import ttk


def get_values(fromairport, toairport, depdate, retdate, email, mobile):
    global from_airport
    # Flight details
    from_airport = fromairport.get()
    to_airport = toairport.get()
    departure_date = depdate.get()
    return_date = retdate.get()

    # Email details
    to_email = email.get()

    # SMS details
    to_sms = mobile.get()

    # One way
    # one_way = oneway_checkbox.get()


# Create window
window = Tk()
# Title of window app
window.title('Flight Scrapper')
window.configure(background='black')

# Title of app
greeting = tk.Label(text="Find the best flight tickets for your upcoming holidays!", bg='black', fg='white',
                    font='sans-serif 14 bold')
greeting.grid(row=0, column=0)

# One way widget
oneway_checkbox = Checkbutton(window, text="One Way", variable=IntVar(), bg='black', fg='white', )
oneway_checkbox.grid(row=1, column=1, sticky=W)

# Number of stops widget
label_stops = tk.Label(text="Stops", font='none 9', bg='black', fg='white')
label_stops.grid(row=1, column=3, sticky=E)
stops_combo = ttk.Combobox(window, values=["0", "1", "2"], width=3)
stops_combo.grid(row=1, column=2, sticky=E)

# Flexible or exact search
label_flex = tk.Label(text='Search Type', font='none 9', bg='black', fg='white')
label_flex.grid(row=1, column=5, sticky=E)
flex = ttk.Combobox(window, values=['exact', '1 day before', '1 day after', '+-2', '+-3'])
flex.grid(row=1, column=4, sticky=E)

# From airport widget
label_fromairport = tk.Label(text="From:", font='none 10 bold', bg='black', fg='white')
label_fromairport.grid(row=2, column=0, sticky=W)
fromairport = Entry(window, width=20)
fromairport.grid(row=2, column=1, sticky=W)

# To airport widget
label_toairport = tk.Label(text="To:", font='none 10 bold', bg='black', fg='white')
label_toairport.grid(row=3, column=0, sticky=W)
toairport = Entry(window, width=20)
toairport.grid(row=3, column=1, sticky=W)

# Departure date widget
label_depdate = tk.Label(text="Depart Date:", font='none 10 bold', bg='black', fg='white')
label_depdate.grid(row=4, column=0, sticky=W)
depdate = Entry(window, width=20)
depdate.grid(row=4, column=1, sticky=W)

# Return date widget
label_retdate = tk.Label(text="Return Date", font='none 10 bold', bg='black', fg='white')
label_retdate.grid(row=5, column=0, sticky=W)
retdate = Entry(window, width=20)
retdate.grid(row=5, column=1, sticky=W)

# Choose if you want notification via email or sms
label_greeting1 = tk.Label(text="Select the way you want to receive notifications", bg='black', fg='white',
                           font='sans-serif 14 bold')
label_greeting1.grid(row=6, column=0, sticky=W)

label_email = tk.Label(text="Email", font='none 10 bold', bg='black', fg='white')
label_email.grid(row=7, column=0, sticky=W)
email = Entry(window, width=50)
email.grid(row=7, column=1, sticky=W)

label_mobile = tk.Label(text="Mobile", font='none 10 bold', bg='black', fg='white')
label_mobile.grid(row=8, column=0, sticky=W)
mobile = Entry(window, width=50)
mobile.grid(row=8, column=1, sticky=W)

# Submit Button widget
submit_button = Button(window, text='Submit', width=6, command=get_values(fromairport=fromairport,
                                                                          toairport=toairport, depdate=depdate,
                                                                          retdate=retdate, email=email,
                                                                          mobile=mobile)).grid(row=9, column=1,
                                                                                               sticky=E)
window.mainloop()
