#END GOAL: FULLY FUNCCTIONAL SECURE SIGNIN - implament signin
import tkinter as tk
import string
#import dictionary_learning 
#
root = tk.Tk()
root.wm_geometry("400x300")
root.title('Authorization')
# # # # # # # 
users = {}
# # #
def login():
    if ent_username.get() in users and ent_password.get() == users[ent_username.get()]:
        result_label.config(text="You have successfully logged in!")
    else:
        result_label.config(text="Login failed: Username or password incorrect.")
    ent_password.delete(0, 'end')
    ent_username.delete(0, 'end')

def sign_up():
    if ent_username.get() in users:
        result_label.config(text='Username already exists. Please choose another.')
        ent_password.delete(0, 'end')
        ent_username.delete(0, 'end')
    else:
        password_validation()

def final_sign_up():
    users[ent_username.get()] = ent_password.get()
    result_label.config(text='You have successfully signed up!')
    ent_password.delete(0, 'end')
    ent_username.delete(0, 'end')

def password_validation():
    result_label.config(text='')
    character_amount_check()
    upcase_lowcase_check()
    num_included_check()
    symbol_check()
    
    if character_amount_check() and upcase_lowcase_check() and num_included_check() and symbol_check() == True:
        final_sign_up()
    else:
        result_label.config(text='Please include each of the following in your password:\nAt least 8 Characters, 1 Uppercase and Lowercase letter,\n1 number, and 1 symbol.')


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
log_button = tk.Button(root, text="Login", command=login)
log_button.pack(pady=5)
#
sign_up_button = tk.Button(root, text="Sign Up", command=sign_up)
sign_up_button.pack(pady=5)
#
result_label = tk.Label(root)
result_label.pack(pady=5)
#

# # #
root.mainloop()
