from tkinter import *

# 1️⃣ Create main window
root = Tk()
root.title("Simple Calculator")
root.geometry("300x400")
root.config(bg="black")

# 2️⃣ Create the input box (where numbers appear)
entry = Entry(root, width=20, font=("Arial", 20), borderwidth=5, relief="flat", justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# 3️⃣ Function to handle button clicks
def button_click(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, current + str(number))

# 4️⃣ Function to clear the input
def button_clear():
    entry.delete(0, END)

# 5️⃣ Function to calculate result
def button_equal():
    try:
        result = eval(entry.get())
        entry.delete(0, END)
        entry.insert(0, result)
    except:
        entry.delete(0, END)
        entry.insert(0, "Error")

# 6️⃣ Define all buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

# 7️⃣ Create buttons dynamically
for (text, row, col) in buttons:
    if text == '=':
        Button(root, text=text, width=5, height=2, command=button_equal, bg="orange", fg="white").grid(row=row, column=col, padx=5, pady=5)
    else:
        Button(root, text=text, width=5, height=2, command=lambda t=text: button_click(t), bg="grey", fg="white").grid(row=row, column=col, padx=5, pady=5)

# 8️⃣ Add a clear button
Button(root, text="C", width=23, height=2, command=button_clear, bg="red", fg="white").grid(row=5, column=0, columnspan=4, padx=5, pady=5)

# 9️⃣ Keep window running
root.mainloop()
