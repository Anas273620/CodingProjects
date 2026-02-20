import tkinter as tk
# Create the main window
root = tk.Tk()
root.title("My First Tkinter GUI")
# Add a label to the window
label = tk.Label(root, text="Hello, Tkinter!")
label.pack()
# Start the Tkinter event loop
root.mainloop()