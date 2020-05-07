import tkinter as tk
from tkinter import ttk

window = tk.Tk()

#add name label and text
nameLabel = tk.Label(master = window, text = "Enter name")
nameLabel.pack(side = tk.TOP)



nameText = tk.Entry(master = window)
nameText.pack(side = tk.TOP)

#add address label and text
adressLabel = tk.Label(master = window, text = "Enter adress")
adressLabel.pack(side = tk.TOP)

adressText = tk.Entry(master = window)
adressText.pack(side = tk.TOP)

#city
cityLabel = tk.Label(master = window, text = "Enter city")
cityLabel.pack(side = tk.TOP)

cityText = tk.Entry(master = window)
cityText.pack(side = tk.TOP)

#state
stateLabel = tk.Label(master = window, text = "Enter state", fg = "red", bg = "green")
stateLabel.pack(side = tk.TOP) 

stateListBox = tk.Listbox(master = window, height = 3)
stateListBox.insert(tk.END, "Texas")
stateListBox.insert(tk.END, "Florida")
stateListBox.insert(tk.END, "California")
stateListBox.pack()

#zip code

zipCodeLabel = tk.Label(master = window, text = "Enter zip code")
zipCodeLabel.pack(side = tk.TOP)

zipCodeComboBox = ttk.Combobox(master = window, values = [10212, 77077, 12312])
zipCodeComboBox.pack()


window.mainloop()