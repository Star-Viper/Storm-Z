from tkinter import Tk, Label, Entry, Frame, Canvas
import tkinter as tk
from PIL import Image, ImageTk

root = Tk()
root.title('Storm-Z Login')
root.geometry("1450x720+45+20")
root.resizable(True, True)
root.config(bg="#B0DAFF")

frame = Frame(root, width=700, height=400, bg='#046bdc')
frame.place(relx=0.70, rely=0.6, anchor="center")

heading = Label(root, text="About Us", fg="#046bdc",padx=90, pady=10,bg="#F4CE14", font=("Arial", 29, "bold"))
heading.place(relx=0.5, rely=0.1, anchor="center")

username_label = Label(frame, text="Trustworthy Brand \nCertified by top scientists globally\nGood for both physical and mental well-being\nStrengthens your immune and digestion system\nHigh-quality at an affordable price", fg="black",bg='#046bdc', font=("Microsoft Yahei UI Light", 21, "bold"))
username_label.place(relx=0.5, rely=0.35, anchor="center")

password_label = Label(frame, text="**Now available in 4 different flavours**", fg="black",bg='#046bdc',font=("Microsoft Yahei UI Light", 25, "bold"))
password_label.place(relx=0.5, rely=0.78, anchor="center")

team= Label(root, text="Our Team", fg="black", bg="#B0DAFF",font=("Times 20 italic bold", 26, "bold","italic"))
team.place(relx=0.25, rely=0.25, anchor="center")

features = Label(root, text="Our Features :", fg="black",bg="#B0DAFF", font=("Times 20 italic bold",26, "bold","italic"))
features.place(relx=0.7, rely=0.25, anchor="center")

# hover effect
def set_opacity(widget, alpha):
    img = original_aboutus_image.copy()
    img.putalpha(int(255 * alpha))
    new_photo = ImageTk.PhotoImage(img)
    widget.configure(image=new_photo)
    widget.image = new_photo  # Keep a reference to avoid garbage collection

def show_username_label(event):
    username_label.place_configure(relx=0.25, rely=0.66, anchor="center") 
    set_opacity(aboutus_image_label, 0.3)

def hide_username_label(event):
    username_label.place_forget()
    set_opacity(aboutus_image_label, 1.0)

# root = tk.Tk()

aboutus_path = "StormZ_aboutus.jpg"
original_aboutus_image = Image.open(aboutus_path).resize((500, 400))
aboutus_photo = ImageTk.PhotoImage(original_aboutus_image)

aboutus_image_label = tk.Label(root, image=aboutus_photo)
aboutus_image_label.place(relx=0.25, height=400, width=500, rely=0.6, anchor="center")

username_label = Label(root, text="Vipul Mhatre\nRiddhesh Firake\nParth Mehta\nUthkrushta Mathur", fg="black",
                       font=("Times 20 italic bold", 21, "bold", "italic"))
username_label.place_forget()

aboutus_image_label.bind("<Enter>", show_username_label)
aboutus_image_label.bind("<Leave>", hide_username_label)



root.mainloop()

#         "Welcome to Storm-Z, your trusted brand and the first choice of families worldwide. "
#         "Our product is designed to improve both physical and mental health, "
#         "strengthening your immune and digestion systems. Here's why you should choose Storm-Z:\n\n"
#         "- **Trustworthy Brand:** Chosen by families globally.\n"
#         "- **Health Benefits:** Good for both physical and mental well-being.\n"
#         "- **Immune Support:** Strengthens your immune and digestion system.\n"
#         "- **Affordable:** High-quality at an affordable price.\n"
#         "- **Global Reach:** Sold and trusted worldwide.\n"
#         "- **Scientifically Certified:** Certified by top scientists globally.\n"
#         "- **Doctor Recommended:** Recommended by medical professionals.\n"
#         "- **Variety:** Now available in 4 different flavors.\n\n"
#         "Meet Our Team:\n"
#         "- Vipul Mhatre\n"
#         "- Riddhesh Firake\n"
#         "- Parth Mehta\n"
#         "- Uthkrushta Mathur"

# username_label = Label(root, text="Unleash the Power Within,", fg="black", font=("Times 20 italic bold", 20, "bold","italic"))
# username_label.place(relx=0.29, rely=0.61, anchor="center")
# username_label = Label(root, text="Your Global Shield for Immunity and Wellness", fg="black", font=("Times 20 italic bold", 20, "bold","italic"))
# username_label.place(relx=0.31, rely=0.69, anchor="center")

# Create a Label widget for the About Us image
# canvas = Canvas(root, width=500, height=400, highlightthickness=0)
# canvas.create_image(250, 200, anchor="center", image=aboutus_photo)
# canvas.place(relx=0.25, rely=0.6, anchor="center")
