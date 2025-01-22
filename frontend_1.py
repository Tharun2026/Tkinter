import tkinter as tk 
from tkinter import messagebox 

#create the main application 
root = tk.Tk()
root.title("Greeting App")
root.geometry("300x200") # setting the window size 

#Function to display the greeting 
def greet():
    name = name_entry.get()
    if name:
        messagebox.showinfo("Greeting",f"Hello,{name}!")
    else:
        messagebox.showwarning("Input Error", "please enter your name.")

# create a label 
name_label = tk.Label(root,text = "Enter your name:")
name_label.pack(pady=10) #padding around the widget

#create an entry box for user input 
name_entry = tk.Entry(root)
name_entry.pack(pady=10)

#create a button that triggers the greet function 
greet_button = tk.Button(root, text= "Greet", command = greet)
greet_button.pack(pady=10)

#start the Tkinter event loop 
root.mainloop()