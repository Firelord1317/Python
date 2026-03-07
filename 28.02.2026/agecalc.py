import tkinter as tk
from datetime import date

def calculate_age():
    try:
        name = name_entry.get()
        day = int(day_entry.get())
        month = int(month_entry.get())
        year = int(year_entry.get())

        today = date.today()
        age = today.year - year - ((today.month, today.day) < (month, day))

        result_label.config(
            text=f"Hello {name}, you are {age} years old!"
        )
    except ValueError:
        result_label.config(text="Please enter valid numbers for date, month, and year.")

# Create main window
root = tk.Tk()
root.geometry("400x400")
root.title("Age Calculator App")

# Labels and entries
tk.Label(root, text="Name:", fg="blue").grid(row=0, column=0, padx=10, pady=5, sticky="w")
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Day:", fg="green").grid(row=1, column=0, padx=10, pady=5, sticky="w")
day_entry = tk.Entry(root)
day_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Month:", fg="purple").grid(row=2, column=0, padx=10, pady=5, sticky="w")
month_entry = tk.Entry(root)
month_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Year:", fg="red").grid(row=3, column=0, padx=10, pady=5, sticky="w")
year_entry = tk.Entry(root)
year_entry.grid(row=3, column=1, padx=10, pady=5)

# Button
tk.Button(root, text="Calculate Age", command=calculate_age, bg="lightblue").grid(row=4, column=0, columnspan=2, pady=10)

# Result label
result_label = tk.Label(root, text="", fg="darkorange")
result_label.grid(row=5, column=0, columnspan=2, pady=10)

root.mainloop()
