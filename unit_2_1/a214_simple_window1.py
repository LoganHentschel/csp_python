#   a113_TR_simple_window1.py
import tkinter as tk
root = tk.Tk()
root.wm_geometry("400x200")
root.title('Authorization')
# # #
frame_login = tk.Frame(root)
frame_login.grid()
###
lbl_username = tk.Label(frame_login, text='Username:')
lbl_username.pack()
#
ent_username = tk.Entry(frame_login, bd=3)
ent_username.pack(pady=5)
###
lbl_password = tk.Label(frame_login,text="Password:",font="Courier")
lbl_password.pack()
#
ent_password = tk.Entry(frame_login, bd=3)
ent_password.pack(pady=5)
###

#

#

#

#

#

#

# # #
root.mainloop()