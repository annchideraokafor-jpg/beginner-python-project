from tkinter import *
from tkinter import filedialog

# 1️⃣ Create main window
root = Tk()
root.title("Simple Notes App")
root.geometry("500x400")
root.config(bg="black")

# 2️⃣ Text area where you write your notes
text_area = Text(root, wrap='word', font=("Arial", 12), bg="white", fg="black")
text_area.pack(expand=True, fill='both', padx=10, pady=10)

# 3️⃣ Define 'Save' function
def save_file():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )
    if file_path:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(text_area.get(1.0, END))

# 4️⃣ Define 'Open' function
def open_file():
    file_path = filedialog.askopenfilename(
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )
    if file_path:
        with open(file_path, 'r', encoding='utf-8') as f:
            text_area.delete(1.0, END)
            text_area.insert(END, f.read())

# 5️⃣ Create buttons
button_frame = Frame(root, bg="black")
button_frame.pack(pady=5)

open_btn = Button(button_frame, text="Open File", command=open_file, bg="grey", fg="white", padx=10)
open_btn.pack(side=LEFT, padx=10)

save_btn = Button(button_frame, text="Save File", command=save_file, bg="grey", fg="white", padx=10)
save_btn.pack(side=LEFT, padx=10)

# 6️⃣ Run the main loop
root.mainloop()
