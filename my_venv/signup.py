# yellow=#ffdd53
# blue=#02dffe
# darkblue=#046bdc


from tkinter import *
from PIL import ImageTk
import tkinter as tk

root = tk.Tk()
root.title('Storm-Z Signup')
root.geometry("1450x720+45+20")
# root.config(bg="#ffffff")
root.resizable(True, True)

def open_login_window():
    root.destroy()  # Close the current window if needed
    # Importing SignUp module and calling its main function
    import login.py
    login.main()


image_path = "Storm-Z_logo-removebg-preview.png"
image = PhotoImage(file=image_path)
button1=PhotoImage(file="Signupsubmit_button.png")

canvas = Canvas(root, width=1000, height=600, highlightthickness=0)
canvas.create_image(170, 45, anchor="nw", image=image)
canvas.pack(side="left")

username_label = Label(root, text="Unleash the Power Within,", fg="black", font=("Times 20 italic bold", 20, "bold","italic"))
username_label.place(relx=0.29, rely=0.61, anchor="center")
username_label = Label(root, text="Your Global Shield for Immunity and Wellness", fg="black", font=("Times 20 italic bold", 20, "bold","italic"))
username_label.place(relx=0.31, rely=0.69, anchor="center")

frame = Frame(root, width=400, height=500, bg='#046bdc')
frame.place(relx=0.75, rely=0.5, anchor="center")

heading = Label(root, text="User Sign Up", fg="#046bdc", padx=90, pady=10,bg="yellow", font=("Arial", 25, "bold"))
heading.place(relx=0.75, rely=0.08, anchor="center")

username_label = Label(frame, text="Enter Username", fg="black", font=("Microsoft Yahei UI Light", 20, "bold"))
username_label.place(relx=0.1, rely=0.08, anchor="w")
username_entry = Entry(frame, width=17, fg="black", border=2, bg="white", font=("Microsoft Yahei UI Light", 23, "bold"))
username_entry.place(relx=0.1, rely=0.19, anchor="w")

password_label = Label(frame, text="Enter new Password", fg="black", font=("Microsoft Yahei UI Light", 20, "bold"))
password_label.place(relx=0.1, rely=0.32, anchor="w")
password_entry = Entry(frame, width=17, fg="black", border=2, bg="white", show="*",font=("Microsoft Yahei UI Light", 23, "bold"))
password_entry.place(relx=0.1, rely=0.43, anchor="w")

password_label = Label(frame, text="Re-enter your Password", fg="black", font=("Microsoft Yahei UI Light", 20, "bold"))
password_label.place(relx=0.1, rely=0.57, anchor="w")
password_entry = Entry(frame, width=17, fg="black", border=2, bg="white", show="*",font=("Microsoft Yahei UI Light", 23, "bold"))
password_entry.place(relx=0.1, rely=0.68, anchor="w")

password_label = Label(frame, text="Select your Gender", fg="black", font=("Microsoft Yahei UI Light", 20, "bold"))
password_label.place(relx=0.1, rely=0.81, anchor="w")
gender = tk.StringVar()
Radiobutton(frame, text="Male", variable=gender, value="Male", font=("Arial", 19)).place(relx=0.35, rely=0.92, anchor="e")
Radiobutton(frame, text="Female", variable=gender, value="Female" ,font=("Arial", 19)).place(relx=0.4, rely=0.92, anchor="w")


# SubmitButton=Button(frame,image=button1, border=0)
# SubmitButton.place(relx=0.5, rely=0.92, anchor="center")

button = Button(root, text='Back To Login',command=open_login_window,fg="blue",bg="#ffdd53",padx=50,pady=3,font=("Arial", 20, "bold"))
button.place(relx=0.75, rely=0.91, anchor="center")

root.mainloop()