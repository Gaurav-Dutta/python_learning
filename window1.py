#python provides a tkenter package for graphical user interface programing (gui), this shows how to basically create a window and display it
#by calling window.mainloop, the user interface is created by combining a set of user interface elements called widgets, examples of widgets
#are checkbox, radio button, panel, progress bar
#the widgets are laid out on the window by using what's called geometry manager, the ui consists of a hiearchy of widegets with the window at
#the root of the hiearchy
#learn all widgets and geometry manager stuff
import tkinter as tk 

window = tk.Tk()

label = tk.Label(master = window, text = "Hello World", width = 50, height = 20)
label.pack()
label = tk.Label(master = window, text = "Goodbye World", width = 50, height = 20)
label.pack()


window.mainloop()