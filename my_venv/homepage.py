from tkinter import Tk, Label, Entry, Frame, PhotoImage, Canvas, Button
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
from decouple import config
from mysql.connector import Error

global product_id,action_type

def create_connection():
    """Create a connection to the MySQL database."""
    try:
        connection = mysql.connector.connect(
            host=config('DB_HOST'),
            user=config('DB_USER'),
            password=config('DB_PASSWORD'),
            database=config('DB_DATABASE')
        )
        # 'root@localhost', 'Star-Viper'

        return connection
    except Error as e:
        messagebox.showerror("Error", f"Error connecting to the database: {e}")
        return None

def add_to_cart_and_track(rectangle_number):
    add_to_cart(rectangle_number)
    selected_products.append(rectangle_number)

    # Add the selected product to the database
    connection = create_connection()
    if connection:
        try:
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO selected_products (product_id) VALUES (%s)", (rectangle_number,))
            connection.commit()
        except Error as e:
            connection.rollback()
            messagebox.showerror("Error", f"Error adding product to the database: {e}")
        finally:
            connection.close()

def delete_from_cart(delete_no):
    if delete_no in selected_products:
        selected_products.remove(delete_no)
        messagebox.showinfo("Delete Product !", f"Product {delete_no} is Deleted from the list")

        # Remove the selected product from the database
        connection = create_connection()
        if connection:
            try:
                with connection.cursor() as cursor:
                    cursor.execute("DELETE FROM selected_products WHERE product_id = %s", (delete_no,))
                connection.commit()
            except Error as e:
                connection.rollback()
                messagebox.showerror("Error", f"Error deleting product from the database: {e}")
            finally:
                connection.close()
    else:
        messagebox.showinfo("Cannot find the product !", "Please first enter the product in order to delete it")

def clear_list():
    messagebox.showinfo("Clear List", "Shopping cart cleared.")

    # Clear the selected products list and remove all records from the database
    selected_products.clear()
    connection = create_connection()
    if connection:
        try:
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM selected_products")
            connection.commit()
        except Error as e:
            connection.rollback()
            messagebox.showerror("Error", f"Error clearing the database: {e}")
        finally:
            connection.close()

def show_selected_products():
    connection = create_connection()
    if connection:
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM selected_products")
                result = cursor.fetchall()
                selected_products_from_db = [row[0] for row in result]

            messagebox.showinfo("Selected Products", f"Selected products: {', '.join(map(str, selected_products_from_db))}")
        except Error as e:
            messagebox.showerror("Error", f"Error fetching selected products from the database: {e}")
        finally:
            connection.close()
# ... (your existing code)

def log_action(product_id, action_type):
    """Log the action (add or delete) in the database."""
    connection = create_connection()
    if connection:
        try:
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO selected_products (product_id, action_type) VALUES (%s, %s)",
                               (product_id, action_type))
            connection.commit()
        except Error as e:
            connection.rollback()
            messagebox.showerror("Error", f"Error logging action in the database: {e}")
        finally:
            connection.close()

def add_to_cart_and_track(rectangle_number):
    add_to_cart(rectangle_number)
    selected_products.append(rectangle_number)
    log_action(rectangle_number, 'add')

def delete_from_cart(delete_no):
    if delete_no in selected_products:
        selected_products.remove(delete_no)
        messagebox.showinfo("Delete Product !", f"Product {delete_no} is Deleted from the list")
        log_action(delete_no, 'delete')
        # Remove the selected product from the database
        connection = create_connection()
        if connection:
            try:
                with connection.cursor() as cursor:
                    cursor.execute("DELETE FROM selected_products WHERE product_id = %s AND action_type = 'add'",
                                   (delete_no,))
                connection.commit()
            except Error as e:
                connection.rollback()
                messagebox.showerror("Error", f"Error deleting product from the database: {e}")
            finally:
                connection.close()
    else:
        messagebox.showinfo("Cannot find the product !", "Please first enter the product in order to delete it")

# ... (rest of your code)

# homepg.mainloop()

def add_to_cart(rectangle_number):
    messagebox.showinfo("Add to Cart", f"Product {rectangle_number} added to cart.")


def clear_list():
    messagebox.showinfo("Clear List", "Shopping cart cleared.")

def show_selected_products(selected_products):
    messagebox.showinfo("Selected Products", f"Selected products: {', '.join(map(str, selected_products))}")

selected_products = []

def add_to_cart_and_track(rectangle_number):
    add_to_cart(rectangle_number)
    selected_products.append(rectangle_number)
    # add_to_cart_and_track(rectangle_number)
    log_action(product_id, action_type)

def delete_from_cart(delete_no):
    if delete_no in selected_products:
        selected_products.remove(delete_no)
        messagebox.showinfo("Delete Product !",f"Product {delete_no} is Deleted from the list")

    else:
        messagebox.showinfo("Cannot find the product !","Please first enter the product in order to delete it")



#def Homepg():
homepg = tk.Tk()
homepg.title('Storm-Z Products')
homepg.geometry("1450x720+45+20")
# homepg.config(bg="#ffffff")
homepg.resizable(True, True)

# canvas_homepg = tk.Canvas(homepg, width=900, height=700, bg='lightblue')
canvas_homepg = tk.Canvas(homepg, width=1700, height=900, bg='lightblue')
canvas_homepg.pack()

image_path = "Storm-Z_logo-removebg-preview.png"
image = PhotoImage(file=image_path)
canvas = Canvas(homepg, width=900, height=500, highlightthickness=0)
canvas.create_image(170, 45, anchor="n", image=image)
canvas.pack()
# Images
SZLogo = Image.open("Storm-Z_logo-removebg-preview.png").resize((340, 290))
SZChoco = Image.open("StormZ_chocolate.jpeg").resize((248, 210))
SZDfruit = Image.open("StormZ_dryfruits.jpeg").resize((260, 200))
SZSpices = Image.open("StormZ_spices.jpeg").resize((248, 200))
SZFruits = Image.open("StormZ_fruits.jpeg").resize((260, 210))

SZLogo = ImageTk.PhotoImage(SZLogo)
SZFruits = ImageTk.PhotoImage(SZFruits)
SZChoco = ImageTk.PhotoImage(SZChoco)
SZDfruit = ImageTk.PhotoImage(SZDfruit)
SZSpices = ImageTk.PhotoImage(SZSpices)

# Calculate relx and rely based on canvas dimensions
canvas_width = canvas_homepg.winfo_width()
canvas_height = canvas_homepg.winfo_height()

# relx1, rely1, relx2, rely2 = 29 / canvas_width, 40 / canvas_height, 290 / canvas_width, 200 / canvas_height
# rect1 = canvas_homepg.create_rectangle(relx1, rely1, relx2, rely2)

# relx1, rely1, relx2, rely2 = 320 / canvas_width, 40 / canvas_height, 568 / canvas_width, 200 / canvas_height
# rect2 = canvas_homepg.create_rectangle(relx1, rely1, relx2, rely2)

# relx1, rely1, relx2, rely2 = 29 / canvas_width, 385 / canvas_height, 290 / canvas_width, 585 / canvas_height
# rect3 = canvas_homepg.create_rectangle(relx1, rely1, relx2, rely2)

# relx1, rely1, relx2, rely2 = 320 / canvas_width, 385 / canvas_height, 568 / canvas_width, 585 / canvas_height
# rect4 = canvas_homepg.create_rectangle(relx1, rely1, relx2, rely2)

canvas_homepg.create_image(600, 1, anchor=tk.NW, image=SZLogo)

canvas_homepg.create_image(120, 189, anchor=tk.NW, image=SZFruits)
canvas_homepg.create_image(440, 189, anchor=tk.NW, image=SZChoco)
canvas_homepg.create_image(760, 189, anchor=tk.NW, image=SZDfruit)
canvas_homepg.create_image(1080, 189, anchor=tk.NW, image=SZSpices)

# canvas_homepg.create_image(30, 40, anchor=tk.NW, image=SZFruits)
# canvas_homepg.create_image(320, 40, anchor=tk.NW, image=SZChoco)
# canvas_homepg.create_image(30, 385, anchor=tk.NW, image=SZDfruit)
# canvas_homepg.create_image(320, 385, anchor=tk.NW, image=SZSpices)




# #Add to cart btns
stylish_button_add1 = tk.Button(canvas_homepg, text="Add to Cart", font=("Arial", 12, "bold"), bg="#1640D6", fg="white", bd=4,
                                command=lambda: add_to_cart_and_track(1))
stylish_button_add1.place(x=190, y=457)

stylish_button_add2 = tk.Button(canvas_homepg, text="Add to Cart", font=("Arial", 12, "bold"), bg="#1640D6", fg="white", bd=4,
                                command=lambda: add_to_cart_and_track(2))
stylish_button_add2.place(x=510, y=457)

stylish_button_add3 = tk.Button(canvas_homepg, text="Add to Cart", font=("Arial", 12, "bold"), bg="#1640D6", fg="white", bd=4,
                                command=lambda: add_to_cart_and_track(3))
stylish_button_add3.place(x=830, y=457)

stylish_button_add4 = tk.Button(canvas_homepg, text="Add to Cart", font=("Arial", 12, "bold"), bg="#1640D6", fg="white", bd=4,
                                command=lambda: add_to_cart_and_track(4))
stylish_button_add4.place(x=1150, y=457)


# #Delete btns
stylish_button_add4 = tk.Button(canvas_homepg, text="Delete from Cart", font=("Arial", 12, "bold"), bg="#e74c3c", fg="white", bd=4,
                                command=lambda: delete_from_cart(1))
stylish_button_add4.place(x=175, y=503)

stylish_button_add4 = tk.Button(canvas_homepg, text="Delete from Cart", font=("Arial", 12, "bold"), bg="#e74c3c", fg="white", bd=4,
                                command=lambda: delete_from_cart(2))
stylish_button_add4.place(x=495, y=503)

stylish_button_add4 = tk.Button(canvas_homepg, text="Delete from Cart", font=("Arial", 12, "bold"), bg="#e74c3c", fg="white", bd=4,
                                command=lambda: delete_from_cart(3))
stylish_button_add4.place(x=815, y=503)

stylish_button_add4 = tk.Button(canvas_homepg, text="Delete from Cart", font=("Arial", 12, "bold"), bg="#e74c3c", fg="white", bd=4,
                                command=lambda: delete_from_cart(4))
stylish_button_add4.place(x=1135, y=503)

#Names

username_label = Label(canvas_homepg, text="WELCOME TO ",bg="lightblue" ,fg="DARKBLUE", 
                       font=("Arial", 40, "bold"))
username_label.place(x=566, y=10)

username_label = Label(canvas_homepg, text="Funky Fruits Fusion",bg="lightblue" ,fg="black", 
                       font=("Times 20 italic bold", 19, "bold","italic"))
username_label.place(x=130, y=412)

username_label = Label(canvas_homepg, text="Dazzling Dryfruit Delight",bg="lightblue" ,fg="black", 
                       font=("Times 20 italic bold", 19, "bold","italic"))
username_label.place(x=420, y=412)

username_label = Label(canvas_homepg, text="Spice Spectacle Elixir",bg="lightblue" ,fg="black", 
                       font=("Times 20 italic bold", 19, "bold","italic"))
username_label.place(x=760, y=412)

username_label = Label(canvas_homepg, text="Choco-Charm Craze",bg="lightblue" ,fg="black", 
                       font=("Times 20 italic bold", 19, "bold","italic"))
username_label.place(x=1086, y=412)


#Clear Btn
stylish_button_delete1 = tk.Button(canvas_homepg, text="Clear List", font=("Arial", 12, "bold"),padx=26,pady=4, bg="RED", fg="white", bd=4,
                                command=clear_list)
stylish_button_delete1.place(relx=0.5, rely=0.93, anchor="center")


#Show Selected Btn
show_selected_button = tk.Button(canvas_homepg, text="Show Selected Products", font=("Arial", 12, "bold"),padx=29,pady=6, bg="GREEN", fg="white", bd=4,
                                command=lambda: show_selected_products(selected_products))
show_selected_button.place(relx=0.5, rely=0.85, anchor="center")

homepg.mainloop()