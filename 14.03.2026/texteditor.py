# Import necessary packages
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename, asksaveasfilename

# Setup Root Window
window = Tk()
window.title("Codingal's Text Editor")
window.geometry("600x500")
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

# Function to Open a file
def open_file():
    """Open a file for editing."""

    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return

    txt_edit.delete(1.0, END)

    with open(filepath, "r", encoding="utf-8") as input_file:
        text = input_file.read()
        txt_edit.insert(END, text)

    window.title(f"Codingal's Text Editor - {filepath}")

# Function to Save a file
def save_file():
    """Save the current contents of the editor to a file."""

    filepath = asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return

    with open(filepath, "w", encoding="utf-8") as output_file:
        text = txt_edit.get(1.0, END)
        output_file.write(text)

    window.title(f"Codingal's Text Editor - {filepath}")


# Function to Share the editor contents
def share_file():
    """Copy the current editor text to the clipboard for sharing."""

    text = txt_edit.get(1.0, END)
    if not text.strip():
        messagebox.showinfo("Share", "Nothing to share. Type something first.")
        return

    window.clipboard_clear()
    window.clipboard_append(text)
    messagebox.showinfo("Share", "Text copied to clipboard. Paste it into any app to share.")


# Add widgets in the application
txt_edit = Text(window)
fr_buttons = Frame(window, relief=RAISED, bd=2)
btn_open = Button(fr_buttons, text="Open", command=open_file)
btn_save = Button(fr_buttons, text="Save As ... ",
command=save_file)
btn_share = Button(fr_buttons, text="Share", command=share_file)

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)
btn_share.grid(row=2, column=0, sticky="ew", padx=5, pady=(0, 5))

fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

# Start the GUI event loop
window.mainloop()