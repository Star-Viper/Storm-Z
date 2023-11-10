# yellow=#ffdd53
# blue=#02dffe
# darkblue=#046bdc


from tkinter import Tk, Label, Entry, Frame, PhotoImage, Canvas, Button
from PIL import ImageTk

root = Tk()
root.title('Storm-Z Login')
root.geometry("1450x720+45+20")
# root.config(bg="#ffffff")
root.resizable(True, True)
def open_signup_window():
    root.destroy()  # Close the current window if needed
    # Importing SignUp module and calling its main function
    import signup.py
    signup.main()

image_path = "Storm-Z_logo-removebg-preview.png"
image = PhotoImage(file=image_path)
button1=PhotoImage(file="Loginsubmit_button.png")

canvas = Canvas(root, width=1000, height=600, highlightthickness=0)
canvas.create_image(170, 45, anchor="nw", image=image)
canvas.pack(side="left")

username_label = Label(root, text="Unleash the Power Within,", fg="black", font=("Times 20 italic bold", 20, "bold","italic"))
username_label.place(relx=0.29, rely=0.61, anchor="center")
username_label = Label(root, text="Your Global Shield for Immunity and Wellness", fg="black", font=("Times 20 italic bold", 20, "bold","italic"))
username_label.place(relx=0.31, rely=0.69, anchor="center")

frame = Frame(root, width=400, height=400, bg='#046bdc')
frame.place(relx=0.75, rely=0.5, anchor="center")

heading = Label(root, text="User Login", fg="#046bdc", padx=90, pady=10,bg="yellow", font=("Arial", 25, "bold"))
heading.place(relx=0.75, rely=0.15, anchor="center")

username_label = Label(frame, text="Username", fg="black", font=("Microsoft Yahei UI Light", 20, "bold"))
username_label.place(relx=0.5, rely=0.16, anchor="center")
username_entry = Entry(frame, width=17, fg="black", border=2, bg="white", font=("Microsoft Yahei UI Light", 23, "bold"))
username_entry.place(relx=0.5, rely=0.32, anchor="center")

password_label = Label(frame, text="Enter Password", fg="black", font=("Microsoft Yahei UI Light", 20, "bold"))
password_label.place(relx=0.5, rely=0.51, anchor="center")
password_entry = Entry(frame, width=17, fg="black", border=2, bg="white", show="*",font=("Microsoft Yahei UI Light", 23, "bold"))
password_entry.place(relx=0.5, rely=0.66, anchor="center")

SubmitButton=Button(frame,image=button1, border=0)
SubmitButton.place(relx=0.5, rely=0.87, anchor="center")

username_label = Label(root, text="Not a user?", fg="black", font=("Times 20 italic bold", 19, "bold"))
username_label.place(relx=0.75, rely=0.83, anchor="center")
button = Button(root, text='Sign Up',command=open_signup_window,fg="blue",bg="#ffdd53",padx=50,pady=3,font=("Arial", 20, "bold"))
button.place(relx=0.75, rely=0.91, anchor="center")
# username_label = Label(root, text="Sign Up", fg="blue", font=("Times 20 italic bold", 19, "bold"))
# username_label.place(relx=0.75, rely=0.89, anchor="center")

root.mainloop()

# def open_signup_window():
#     root.destroy()  # Close the current window if needed
#     # Importing SignUp module and calling its main function
#     import SignUp
#     SignUp.main()

# root = tk.Tk()

# # Create a button that, when clicked, opens the SignUp window
# signup_button = Button(root, text="Sign Up", command=open_signup_window)
# signup_button.pack()

# # from tkinter import Tk, Label, Entry, Frame

# # root = Tk()
# # root.geometry("1200x600")
# # frame = Frame(root, width=350, height=350, bg='lightblue')
# # # Place the frame in the center of the root window
# # frame.place(relx=0.5, rely=0.5, anchor="center")
# # heading = Label(frame, text="Sign in", fg="#57a1f8", bg="white", font=("Microsoft Yahei UI Light", 23, "bold"))
# # heading.place(relx=0.5, rely=0.05, anchor="center")
# # username_label = Label(frame, text="Username", fg="black", font=("Microsoft Yahei UI Light", 20, "bold"))
# # username_label.place(relx=0.5, rely=0.25, anchor="center")
# # username_entry = Entry(frame, width=17, fg="black", border=2, bg="white", font=("Microsoft Yahei UI Light", 23, "bold"))
# # username_entry.place(relx=0.5, rely=0.4, anchor="center")
# # password_label = Label(frame, text="Enter Password", fg="black", font=("Microsoft Yahei UI Light", 20, "bold"))
# # password_label.place(relx=0.5, rely=0.6, anchor="center")
# # password_entry = Entry(frame, width=17, fg="black", border=2, bg="white", font=("Microsoft Yahei UI Light", 23, "bold"))
# # password_entry.place(relx=0.5, rely=0.75, anchor="center")
# # root.mainloop()
