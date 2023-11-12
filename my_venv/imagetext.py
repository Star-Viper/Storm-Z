import tkinter as tk
from tkinter import Label, PhotoImage
from PIL import Image, ImageTk

def set_opacity(widget, alpha):
    img = original_aboutus_image.copy()
    img.putalpha(int(255 * alpha))
    new_photo = ImageTk.PhotoImage(img)
    widget.configure(image=new_photo)
    widget.image = new_photo  # Keep a reference to avoid garbage collection

def show_username_label(event):
    username_label.place_configure(relx=0.25, rely=0.6, anchor="center") 
    set_opacity(aboutus_image_label, 0.3)

def hide_username_label(event):
    username_label.place_forget()
    set_opacity(aboutus_image_label, 1.0)

root = tk.Tk()

aboutus_path = "StormZ_aboutus.jpg"
original_aboutus_image = Image.open(aboutus_path).resize((500, 400))
aboutus_photo = ImageTk.PhotoImage(original_aboutus_image)

aboutus_image_label = tk.Label(root, image=aboutus_photo)
aboutus_image_label.place(relx=0.25, height=400, width=500, rely=0.6, anchor="center")

username_label = Label(root, text="Your Global Shield for Immunity and Wellness", fg="black",
                       font=("Times 20 italic bold", 20, "bold", "italic"))
username_label.place_forget()

aboutus_image_label.bind("<Enter>", show_username_label)
aboutus_image_label.bind("<Leave>", hide_username_label)

root.mainloop()
