from tkinter import Tk, Label, Entry, Frame, PhotoImage, Canvas, Button
import tkinter as tk

root = tk.Tk()
root.title('Storm-Z mainpage')
root.geometry("1080x520+45+20")
root.resizable(True, True)

def open_login_window():
    root.destroy()  
    import login
    login.main()
   
    # ADD CODE FOR ADMIN LOGIN HERE
# def open_admin_window():
#     root.destroy()  
#     import admin
#     admin.main()
    
image_path = "Storm-Z_logo-removebg-preview.png"
image = PhotoImage(file=image_path)

canvas = Canvas(root, width=1000, height=600, highlightthickness=0)
canvas.create_image(370, 5, anchor="n", image=image)
canvas.pack(side="left")

admin_login = tk.Button(root, text="Login as ADMIN ->", font=("Arial", 20, "bold"), bg="#00A9FF", fg="white", bd=4,
                                # add command here admin login")
                                )
admin_login.place(relx=0.62,rely=0.29)

user_login = tk.Button(root, text="Login as USER ->", font=("Arial", 20, "bold"), bg="#00A9FF", fg="white", bd=4,
                                command=open_login_window)
user_login.place(relx=0.62,rely=0.49)

root.mainloop()