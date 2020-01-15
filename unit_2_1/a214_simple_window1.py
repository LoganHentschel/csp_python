#END GOAL: FULLY FUNCCTIONAL SECURE SIGNIN - fix bigs, verify base works: then implament signin
#   a113_TR_simple_window1.py
import tkinter as tk
import string
#
root = tk.Tk()
root.wm_geometry("400x250")
root.title('Authorization')
# # #
def login():
    print('Username:', ent_username.get(), '\n' 'Password:', ent_password.get())
    ent_password.delete(0, "end")
    ent_username.delete(0, "end")

def password_validation():
    character_amount_check()

def character_amount_check():
    if len(ent_password.get()) < 8:
        result_label.config(text='Please have at least 8 characters.')
        ent_password.delete(0, "end")
        ent_username.delete(0, "end")
    else:
        num_included_check()

def num_included_check():
    for char in ent_password.get():
        if char.isdigit():
            upcase_lowcase_check()
        else:
            result_label.config(text='Please include at least one number.')
            ent_password.delete(0, "end")
            ent_username.delete(0, "end")            

def upcase_lowcase_check():
    upper = 0
    lower = 0
    print('checking case')
    for char in ent_password.get():
            if char.isupper():
                upper += 1
            if char.islower():
                lower += 1
    if lower and upper > 1:
        print('upper lower both check out')
        symbol_check()
    else:
        result_label.config(text='Please include both a Captial and Lowercase letter.')
        ent_password.delete(0, "end")
        ent_username.delete(0, "end")

def symbol_check():
    print('symbol check')
    for char in ent_password.get():
        if char in string.punctuation:
            login()
        else:
            result_label.config(text='Please include a symbol.')
            ent_password.delete(0, "end")
            ent_username.delete(0, "end")

# # #
lbl_username = tk.Label(root, text='Username:')
lbl_username.pack(pady=5)

ent_username = tk.Entry(root, bd=3)
ent_username.pack(pady=5)
#
lbl_password = tk.Label(root,text="Password:",font="Courier")
lbl_password.pack()

ent_password = tk.Entry(root, bd=3)
ent_password.pack(pady=5)

#
log_button = tk.Button(root, text="Login", command=password_validation)
log_button.pack()
#
result_label = tk.Label(root)
result_label.pack(pady=5)
#
sign_up = tk.Button(root, text="Sign Up",)
sign_up.pack(pady=5)

# # #
root.mainloop()
