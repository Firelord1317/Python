import tkinter as tk
from tkinter import ttk
import re


class LoginApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Professional Login App")
        self.geometry("380x300")
        # make window resizable so contents can grow
        self.resizable(True, True)
        self.configure(bg="#F0F2F5")

        self._setup_style()
        # allow window contents to expand when resized
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self._build_ui()

    def _setup_style(self):
        style = ttk.Style(self)

        try:
            style.theme_use("clam")
        except:
            pass

        style.configure("TLabel",
                        font=("Segoe UI", 10),
                        background="#F0F2F5")

        style.configure("TEntry",
                        padding=6)

        style.configure("TButton",
                        font=("Segoe UI", 10, "bold"),
                        padding=6)

    def _build_ui(self):

        container = ttk.Frame(self, padding=20)
        # put container in root grid and make it stretch
        container.grid(row=0, column=0, sticky='NSEW')
        container.columnconfigure(1, weight=1)
        container.rowconfigure(4, weight=1)  # allow button row to stay centered

        # Full Name
        ttk.Label(container, text="Full Name:").grid(row=0, column=0, sticky="W", pady=5)
        self.name_var = tk.StringVar()
        ttk.Entry(container, textvariable=self.name_var).grid(row=0, column=1, sticky="EW", pady=5)

        # Email
        ttk.Label(container, text="Email ID:").grid(row=1, column=0, sticky="W", pady=5)
        self.email_var = tk.StringVar()
        ttk.Entry(container, textvariable=self.email_var).grid(row=1, column=1, sticky="EW", pady=5)

        # Password
        ttk.Label(container, text="Password:").grid(row=2, column=0, sticky="W", pady=5)
        self.pass_var = tk.StringVar()
        self.password_entry = ttk.Entry(container, textvariable=self.pass_var, show="*")
        self.password_entry.grid(row=2, column=1, sticky="EW", pady=5)

        # Show Password Checkbox
        self.show_var = tk.BooleanVar(value=False)
        ttk.Checkbutton(
            container,
            text="Show Password",
            variable=self.show_var,
            command=self._toggle_password
        ).grid(row=3, column=1, sticky="W")

        # Submit Button
        ttk.Button(
            container,
            text="Create Account",
            command=self.display
        ).grid(row=4, column=0, columnspan=2, pady=12)

        # Message Label
        self.msg_label = ttk.Label(container, text="")
        self.msg_label.grid(row=5, column=0, columnspan=2)

        # Press Enter to Submit
        self.bind("<Return>", lambda event: self.display())

    def _toggle_password(self):
        if self.show_var.get():
            self.password_entry.config(show="")
        else:
            self.password_entry.config(show="*")

    def display(self):
        name = self.name_var.get().strip()
        email = self.email_var.get().strip()
        password = self.pass_var.get().strip()

        # Validation Checks
        if not name:
            self._show_message("Please enter your name.", "red")
            return

        if not email:
            self._show_message("Please enter your email.", "red")
            return

        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            self._show_message("Enter a valid email address.", "red")
            return

        if not password:
            self._show_message("Please enter a password.", "red")
            return

        if len(password) < 6:
            self._show_message("Password must be at least 6 characters.", "red")
            return

        # Success
        self._show_message(f"Welcome {name}! Account created successfully 🎉", "green")

        # Clear fields
        self.name_var.set("")
        self.email_var.set("")
        self.pass_var.set("")

    def _show_message(self, message, color):
        self.msg_label.config(text=message, foreground=color)


if __name__ == "__main__":
    app = LoginApp()
    app.mainloop()