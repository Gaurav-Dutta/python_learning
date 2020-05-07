#create a form of personal info using grid geometry manager. every window has 3 geometry managers, pack manager, grid manager, placement 
#manager. use the grid geometry manager to place a label and an entry in each row

import tkinter as tk
from tkinter import ttk

master = tk.Tk()
master.geometry("500x500")

firstName = tk.Label(master, text = "First Name:")
firstName.grid(row = 0, column = 0, pady = 2, sticky = tk.W)
firstNameEntry = tk.Entry(master)
firstNameEntry.grid(row = 0, column = 1, sticky = tk.W)

lastName = tk.Label(master, text = "Last Name:")
lastName.grid(row = 1, column = 0, pady = 2, sticky = tk.W)
lastNameEntry = tk.Entry(master)
lastNameEntry.grid(row = 1, column = 1, sticky = tk.W)

state = tk.Label(master, text = "State:")
state.grid(row = 2, column = 0, pady = 2, sticky = tk.W)
stateEntry = tk.Entry(master)
stateEntry.grid(row = 2, column = 1, sticky = tk.W)

zipCodes = [79823, 23487, 78903]

zipCode = tk.Label(master, text = "Zip Code:")
zipCode.grid(row = 3, column = 0, pady = 2, sticky = tk.W)
zipCodeEntry = ttk.Combobox(master, values = zipCodes)
zipCodeEntry.grid(row = 3, column = 1, sticky = tk.W)

description = tk.Label(master, text = "Description")
description.grid(row = 4, column = 0, pady = 2, sticky = tk.NW)
descriptionText = tk.Text(master, width = 40, height = 5)
descriptionText.grid(row = 4, column = 1)

button = tk.Button(master, text = "Submit")
button.grid(row=5, column=1, pady = 2, sticky = tk.E)



master.mainloop()