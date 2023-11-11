# import tkinter as tk
# from tkinter import messagebox
# from PIL import Image, ImageTk
# import mysql.connector
# from mysql.connector import Error

# def create_connection():
#     """Create a connection to the MySQL database."""
#     try:
#         connection = mysql.connector.connect(
#             host='Star-Viper',
#             user='root@localhost',
#             password="Sharingan@123",
#             database="StormZ"
#         )
#         # 'root@localhost', 'Star-Viper'

#         return connection
#     except Error as e:
#         messagebox.showerror("Error", f"Error connecting to the database: {e}")
#         return None

# def add_to_cart_and_track(rectangle_number):
#     add_to_cart(rectangle_number)
#     selected_products.append(rectangle_number)

#     # Add the selected product to the database
#     connection = create_connection()
#     if connection:
#         try:
#             with connection.cursor() as cursor:
#                 cursor.execute("INSERT INTO selected_products (product_id) VALUES (%s)", (rectangle_number,))
#             connection.commit()
#         except Error as e:
#             connection.rollback()
#             messagebox.showerror("Error", f"Error adding product to the database: {e}")
#         finally:
#             connection.close()

# def delete_from_cart(delete_no):
#     if delete_no in selected_products:
#         selected_products.remove(delete_no)
#         messagebox.showinfo("Delete Product !", f"Product {delete_no} is Deleted from the list")

#         # Remove the selected product from the database
#         connection = create_connection()
#         if connection:
#             try:
#                 with connection.cursor() as cursor:
#                     cursor.execute("DELETE FROM selected_products WHERE product_id = %s", (delete_no,))
#                 connection.commit()
#             except Error as e:
#                 connection.rollback()
#                 messagebox.showerror("Error", f"Error deleting product from the database: {e}")
#             finally:
#                 connection.close()
#     else:
#         messagebox.showinfo("Cannot find the product !", "Please first enter the product in order to delete it")

# def clear_list():
#     messagebox.showinfo("Clear List", "Shopping cart cleared.")

#     # Clear the selected products list and remove all records from the database
#     selected_products.clear()
#     connection = create_connection()
#     if connection:
#         try:
#             with connection.cursor() as cursor:
#                 cursor.execute("DELETE FROM selected_products")
#             connection.commit()
#         except Error as e:
#             connection.rollback()
#             messagebox.showerror("Error", f"Error clearing the database: {e}")
#         finally:
#             connection.close()

# def show_selected_products():
#     connection = create_connection()
#     if connection:
#         try:
#             with connection.cursor() as cursor:
#                 cursor.execute("SELECT * FROM selected_products")
#                 result = cursor.fetchall()
#                 selected_products_from_db = [row[0] for row in result]

#             messagebox.showinfo("Selected Products", f"Selected products: {', '.join(map(str, selected_products_from_db))}")
#         except Error as e:
#             messagebox.showerror("Error", f"Error fetching selected products from the database: {e}")
#         finally:
#             connection.close()

# # ... Rest of your code ...

# homepg.mainloop()
