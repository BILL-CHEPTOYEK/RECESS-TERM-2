
# create a simple calculator program with a GUI interface.
# maKe the title of the calculator program window wit your name.


import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    expression = entry.get()
    result = eval(expression)
    entry.delete(0, tk.END)
    entry.insert(tk.END, result)

# Create the main window
window = tk.Tk()
window.title("Cheptoyek Bill")

# Customize colors and positions
bg_color = "#FFFF00"  # Background color
button_color = "#cccccc"  # Button color
button_active_color = "#999999"  # Button active color

window.configure(bg=bg_color)
entry = tk.Entry(window, width=30, borderwidth=5)
entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Create the number buttons
for i in range(9):
    button = tk.Button(window, text=str(i+1), padx=20, pady=10, bg=button_color, activebackground=button_active_color,
                       command=lambda num=i+1: button_click(num))
    button.grid(row=(i+2)//3, column=(i+2)%3, padx=5, pady=5)

# Create the zero button
button_zero = tk.Button(window, text="0", padx=20, pady=10, bg=button_color, activebackground=button_active_color,
                        command=lambda: button_click(0))
button_zero.grid(row=4, column=1, padx=5, pady=5)

# Create the operation buttons
button_add = tk.Button(window, text="+", padx=20, pady=10, bg=button_color, activebackground=button_active_color,
                       command=lambda: button_click("+"))
button_subtract = tk.Button(window, text="-", padx=20, pady=10, bg=button_color, activebackground=button_active_color,
                            command=lambda: button_click("-"))
button_multiply = tk.Button(window, text="*", padx=20, pady=10, bg=button_color, activebackground=button_active_color,
                            command=lambda: button_click("*"))
button_divide = tk.Button(window, text="/", padx=20, pady=10, bg=button_color, activebackground=button_active_color,
                          command=lambda: button_click("/"))
button_equal = tk.Button(window, text="=", padx=46, pady=10, bg=button_color, activebackground=button_active_color,
                         command=button_equal)
button_clear = tk.Button(window, text="Clear", padx=35, pady=10, bg=button_color, activebackground=button_active_color,
                         command=button_clear)

button_add.grid(row=2, column=3, padx=5, pady=5)
button_subtract.grid(row=3, column=3, padx=5, pady=5)
button_multiply.grid(row=4, column=3, padx=5, pady=5)
button_divide.grid(row=5, column=3, padx=5, pady=5)
button_equal.grid(row=5, column=1, columnspan=2, padx=5, pady=5)
button_clear.grid(row=6, column=1, columnspan=3, padx=5, pady=5)

# Start the main loop
window.mainloop()
