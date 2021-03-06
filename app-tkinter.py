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
                    font=("Helvetica", 16))
greeting.grid(row=0, column=0)

# One way widget
oneway_checkbox = Checkbutton(window, text="One Way", variable=IntVar(), bg='black', fg='white', )
oneway_checkbox.grid(row=2, column=0, sticky=W, columnspan=3)

# Number of stops widget
label_stops = tk.Label(text="Stops", font=("Helvetica", 9), bg='black', fg='white')
label_stops.grid(row=2, column=0, sticky=W, columnspan=3)
stops_combo = ttk.Combobox(window, values=["0", "1", "2"], width=3)
stops_combo.grid(row=2, column=0, sticky=W, columnspan=3)

# Flexible or exact search
label_flex = tk.Label(text='Search Type', font=("Helvetica", 9), bg='black', fg='white')
label_flex.grid(row=2, column=0, sticky=W, columnspan=3)
flex = ttk.Combobox(window, values=['exact', '1 day before', '1 day after', '+-2', '+-3'], width=5)
flex.grid(row=2, column=0, sticky=W, columnspan=3)

# From airport widget
label_fromairport = tk.Label(text="From:", font=("Helvetica", 10), bg='black', fg='white')
label_fromairport.grid(row=3, column=0, sticky=W)
fromairport = Entry(window, width=20)
fromairport.grid(row=3, column=1, sticky=W)

# To airport widget
label_toairport = tk.Label(text="To:", font=("Helvetica", 10), bg='black', fg='white')
label_toairport.grid(row=4, column=0, sticky=W)
toairport = Entry(window, width=20)
toairport.grid(row=4, column=1, sticky=W)

# Departure date widget
label_depdate = tk.Label(text="Depart Date:", font=("Helvetica", 10), bg='black', fg='white')
label_depdate.grid(row=5, column=0, sticky=W)
depdate = Entry(window, width=20)
depdate.grid(row=5, column=1, sticky=W)

# Return date widget
label_retdate = tk.Label(text="Return Date", font=("Helvetica", 10), bg='black', fg='white')
label_retdate.grid(row=6, column=0, sticky=W)
retdate = Entry(window, width=20)
retdate.grid(row=6, column=1, sticky=W)

# Choose if you want notification via email or sms
label_greeting1 = tk.Label(text="Select the way you want to receive notifications", bg='black', fg='white',
                           font=("Helvetica", 12))
label_greeting1.grid(row=8, column=0, sticky=W)

label_email = tk.Label(text="Email", font=("Helvetica", 10), bg='black', fg='white')
label_email.grid(row=10, column=0, sticky=W)
email = Entry(window, width=50)
email.grid(row=10, column=1, sticky=W)

label_mobile = tk.Label(text="Mobile", font=("Helvetica", 10), bg='black', fg='white')
label_mobile.grid(row=11, column=0, sticky=W)
mobile = Entry(window, width=50)
mobile.grid(row=11, column=1, sticky=W)

# Submit Button widget
submit_button = Button(window, text='Submit', width=6, command=get_values(fromairport=fromairport,
                                                                          toairport=toairport, depdate=depdate,
                                                                          retdate=retdate, email=email,
                                                                          mobile=mobile)).grid(row=12, column=1,
                                                                                               sticky=E)
window.mainloop()
