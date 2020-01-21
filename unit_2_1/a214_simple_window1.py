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
    print(character_amount_check())
    upcase_lowcase_check()
    print(upcase_lowcase_check())
    num_included_check()
    print( num_included_check())
    symbol_check()
    print(symbol_check())
    
    if character_amount_check() and upcase_lowcase_check() and num_included_check() and symbol_check() == True:
        print('all clear')
        login()


def character_amount_check():
    if len(ent_password.get()) >= 8:
        return True
# XXXXXXXXXXXXXXXXXX #

def upcase_lowcase_check():
    upper = 0
    lower = 0
    for char in ent_password.get():
            if char.isupper():
                upper += 1
            if char.islower():
                lower += 1
    if upper >= 1:
        if lower >= 1:
            return True

# XXXXXXXXXXXXXXXXXX #
def num_included_check():
    num_count = 0
    for char in ent_password.get():
        if char.isdigit():
            return True  

# XXXXXXXXXXXXXXXXXX #
def symbol_check():
    for char in ent_password.get():
        if char in string.punctuation:
            return True

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
