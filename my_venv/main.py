from tkinter import Tk, Label, Entry, Frame, PhotoImage, Canvas, Button

root = Tk()
root.title('Storm-Z Login')
root.geometry("1200x600")
# root.config(bg="#ffffff")
root.resizable(True, True)

# yellow=#ffdd53
# blue=#02dffe
# darkblue=#046bdc


# Load the image
image_path = "Storm-Z_logo-removebg-preview.png"
image = PhotoImage(file=image_path)
button1=PhotoImage(file="submit_button.png")

# Create a Canvas for the image on the left
canvas = Canvas(root, width=1000, height=600, highlightthickness=0)
canvas.create_image(50, 45, anchor="nw", image=image)
canvas.pack(side="left")

# Create a frame for the form on the right
frame = Frame(root, width=400, height=400, bg='#046bdc')
# Place the frame in the center-right of the root window with some minimum distance
frame.place(relx=0.75, rely=0.5, anchor="center")

heading = Label(frame, text="Sign in", fg="#046bdc", bg="yellow", font=("Arial", 25, "bold"))
heading.place(relx=0.5, rely=0.05, anchor="center")

username_label = Label(frame, text="Username", fg="black", font=("Microsoft Yahei UI Light", 20, "bold"))
username_label.place(relx=0.5, rely=0.25, anchor="center")
username_entry = Entry(frame, width=17, fg="black", border=2, bg="white", font=("Microsoft Yahei UI Light", 23, "bold"))
username_entry.place(relx=0.5, rely=0.4, anchor="center")

password_label = Label(frame, text="Enter Password", fg="black", font=("Microsoft Yahei UI Light", 20, "bold"))
password_label.place(relx=0.5, rely=0.6, anchor="center")
password_entry = Entry(frame, width=17, fg="black", border=2, bg="white", font=("Microsoft Yahei UI Light", 23, "bold"))
password_entry.place(relx=0.5, rely=0.75, anchor="center")

# Use tk.Button instead of Tk.Button
button = Button(root, text='Submit', width=25, command=root.destroy, bg="#ffdd53", pady=10, bd=0, borderwidth=0,font=("Arial", 20, "bold"), highlightthickness=0)
button.place(relx=0.75, rely=0.85, anchor="center")

# SubmitButton=Button(root,image=button1,border=0)
# SubmitButton.place(relx=0.75, rely=0.85, anchor="center")

root.mainloop()


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
