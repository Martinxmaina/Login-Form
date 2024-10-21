import tkinter
from tkinter import messagebox
from tkinter import ttk

window = tkinter.Tk()
window.title("Login form")
window.geometry("340x440")
window.configure(bg="#333333")


def login():
    username="martin"
    password="1234"
    if username_entry.get()== username and password:
        messagebox.showinfo(title="login success", message="You successful logged in")
    else: messagebox.showerror(title="Error", message="Invalid login")


frame = tkinter.Frame(bg="#333333")

style = ttk.Style()
style.configure("TButton", background="#ff3399", foreground="white", font=("Arial", 16))
style.map("TButton", background=[('active', '#ff3399')])

# creating windows
login_label = tkinter.Label(
    frame, text="login", bg="#333333", fg = "#ff3399", font=("Arial",30))
username_label = tkinter.Label(
    frame, text="Username", bg="#333333", fg = "white", font=("Arial",16))
username_entry = tkinter.Entry(frame)
password_entry = tkinter.Entry(frame, show="*",font=("Arial",16))
password_label = tkinter.Label(
    frame, text="password", bg="#333333", fg = "white", font=("Arial",16))
login_button = ttk.Button(frame, text="Login", style="TButton", command=login)

# placing widgets
login_label.grid(row=0, column=0, columnspan=2,sticky="news", pady =40)
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1, pady=20)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1, pady= 20)
login_button.grid(row=3, column =0, columnspan =2, pady=30)


frame.pack()

window.mainloop()