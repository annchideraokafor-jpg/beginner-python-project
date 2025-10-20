from tkinter import *
import random

# 1️⃣ Create the main window
root = Tk()
root.title("Random Quote Generator")
root.geometry("400x250")
root.config(bg="black")

# 2️⃣ A list of motivational quotes
quotes = [
    "Believe in yourself!",
    "Keep going, you're doing great!",
    "Dream big, work hard.",
    "Code, sleep, repeat.",
    "Success is built daily.",
    "Start where you are, use what you have.",
    "Stay curious, stay humble.",
    "You are stronger than you think."
]

# 3️⃣ Create a label to display quotes
quote_label = Label(root,
                    text=random.choice(quotes),
                    wraplength=350,
                    font=("Arial", 14, "italic"),
                    fg="white",
                    bg="black",
                    justify="center")
quote_label.pack(pady=40)

# 4️⃣ Function to show a new random quote
def new_quote():
    quote_label.config(text=random.choice(quotes))

# 5️⃣ Button to generate a new quote
Button(root, text="New Quote", command=new_quote, bg="grey", fg="white", font=("Arial", 12)).pack()

# 6️⃣ Run the app
root.mainloop()
