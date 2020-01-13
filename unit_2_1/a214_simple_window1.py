#   a113_TR_simple_window1.py
import tkinter as tk
root = tk.Tk()
root.wm_geometry("400x200")
root.title('Authorization')
# # #
def login_button_press():
    print('Username:', ent_username.get(), '\n' 'Password:', ent_password.get())
    ent_password.delete(0, "end")
    ent_username.delete(0, "end")

# # #
lbl_username = tk.Label(root, text='Username:')
lbl_username.pack()

ent_username = tk.Entry(root, bd=3)
ent_username.pack(pady=5)
###
lbl_password = tk.Label(root,text="Password:",font="Courier")
lbl_password.pack()

ent_password = tk.Entry(root, bd=3)
ent_password.pack(pady=5)

###
log_button = tk.Button(root, text="Login", command=login_button_press)
log_button.pack()

# # #
root.mainloop()