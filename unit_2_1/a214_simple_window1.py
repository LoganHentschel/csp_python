#   a113_TR_simple_window1.py
import tkinter as tk
root = tk.Tk()
root.wm_geometry("400x200")
root.title('Authorization')
# # #
def login():
    print('Username:', ent_username.get(), '\n' 'Password:', ent_password.get())
    ent_password.delete(0, "end")
    ent_username.delete(0, "end")

def password_validation():
    #character_amount_check()
    upcase_lowcase_check()

def character_amount_check():
    if len(ent_password.get()) < 8:
        print('Please have at least 8 characters.')
        ent_password.delete(0, "end")
        ent_username.delete(0, "end")
    else:
        #num_included_check()
        pass

def num_included_check():
    print('num check')
    #upcase_lowcase_check()

def upcase_lowcase_check():
    upper = 0
    lower = 0
    print('upper lower check')
    for char in ent_password.get():
        if upper  < 1:
            if char.isupper():
                upper += 1
        if lower < 1:
            if char.islower():
                lower += 1
    print(upper, lower, 'clear')
            

    #symbol_check()
  

def symbol_check():
    print('symbol check')
    #login()

# # #
lbl_username = tk.Label(root, text='Username:')
lbl_username.pack(pady=5)

ent_username = tk.Entry(root, bd=3)
ent_username.pack(pady=5)
###
lbl_password = tk.Label(root,text="Password:",font="Courier")
lbl_password.pack()

ent_password = tk.Entry(root, bd=3)
ent_password.pack(pady=5)

###
log_button = tk.Button(root, text="Login", command=password_validation)
log_button.pack()

# # #
root.mainloop()

#1 UPCASE, 1 LOWERCASE, SPECIAL CHARACTER, DIGIT 