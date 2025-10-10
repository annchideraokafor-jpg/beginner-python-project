from tkinter import *
import time

# Create the main window
root = Tk()
root.title("Digital Clock")

# Function to update the time every second
def update_time():
    current_time = time.strftime("%H:%M:%S")  # Get time in hours:minutes:seconds
    label.config(text=current_time)           # Change the label text to current time
    label.after(1000, update_time)            # Run this function again after 1000ms (1 second)

# Create a label to display the time
label = Label(root, font=("Arial", 50), fg="white", bg="black")
label.pack(anchor="center")

# Call the function to start the clock
update_time()

# Keep the window open
root.mainloop()

