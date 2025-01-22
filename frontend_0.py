import tkinter as tk 

# create the application window 
root = tk.Tk()  #TK means toolkit
root.title("Simple Tkinter App")
root.geometry("200x100")  # set window size 

# Function to print "Hello Tharun!" in the console 
def say_hello():
    print("Hello Tharun!")
    print("How are you")

# creating a button that triggers the say Hello Tharun 
hello_button = tk.Button(root, text = "Click Me", command = say_hello)
hello_button.pack(pady=30) #pack the button into the window 

# start the Tkinter event loop
root.mainloop()