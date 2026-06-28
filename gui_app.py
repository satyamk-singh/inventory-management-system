import tkinter as tk
from tkinter import messagebox, ttk

from invoice import create_invoice
from product import find_product, inventory
from storage import load_data, save_data


GST_RATE = 0.18


class InventoryGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Management System")
        self.root.geometry("900x560")
        self.root.resizable(False, False)

        load_data()
        self.create_widgets()
        self.refresh_table()

    def create_widgets(self):
        title = tk.Label(
            self.root,
            text="Inventory Management System",
            font=("Arial", 20, "bold"),
        )
        title.pack(pady=10)

        form_frame = tk.Frame(self.root)
        form_frame.pack(pady=10)

        tk.Label(form_frame, text="Product ID").grid(row=0, column=0, padx=5, pady=5)
        tk.Label(form_frame, text="Name").grid(row=0, column=1, padx=5, pady=5)
        tk.Label(form_frame, text="Category").grid(row=0, column=2, padx=5, pady=5)
        tk.Label(form_frame, text="Price").grid(row=0, column=3, padx=5, pady=5)
        tk.Label(form_frame, text="Quantity").grid(row=0, column=4, padx=5, pady=5)

        self.product_id_entry = tk.Entry(form_frame, width=14)
        self.name_entry = tk.Entry(form_frame, width=18)
        self.category_entry = tk.Entry(form_frame, width=16)
        self.price_entry = tk.Entry(form_frame, width=12)
        self.quantity_entry = tk.Entry(form_frame, width=12)

        self.product_id_entry.grid(row=1, column=0, padx=5, pady=5)
        self.name_entry.grid(row=1, column=1, padx=5, pady=5)
        self.category_entry.grid(row=1, column=2, padx=5, pady=5)
        self.price_entry.grid(row=1, column=3, padx=5, pady=5)
        self.quantity_entry.grid(row=1, column=4, padx=5, pady=5)

        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=5)

        tk.Button(button_frame, text="Add Product", width=16, command=self.add_product).grid(row=0, column=0, padx=5)
        tk.Button(button_frame, text="Update Product", width=16, command=self.update_product).grid(row=0, column=1, padx=5)
        tk.Button(button_frame, text="Delete Product", width=16, command=self.delete_product).grid(row=0, column=2, padx=5)
        tk.Button(button_frame, text="Save Data", width=16, command=self.save_products).grid(row=0, column=3, padx=5)

        sell_frame = tk.LabelFrame(self.root, text="Sell Product / Generate Invoice")
        sell_frame.pack(pady=10)

        tk.Label(sell_frame, text="Product ID").grid(row=0, column=0, padx=5, pady=8)
        tk.Label(sell_frame, text="Sale Quantity").grid(row=0, column=2, padx=5, pady=8)

        self.sell_id_entry = tk.Entry(sell_frame, width=16)
        self.sell_quantity_entry = tk.Entry(sell_frame, width=16)
        self.sell_id_entry.grid(row=0, column=1, padx=5, pady=8)
        self.sell_quantity_entry.grid(row=0, column=3, padx=5, pady=8)

        tk.Button(sell_frame, text="Generate Invoice", width=18, command=self.sell_product).grid(row=0, column=4, padx=8)

        columns = ("id", "name", "category", "price", "quantity")
        self.table = ttk.Treeview(self.root, columns=columns, show="headings", height=12)
        self.table.pack(pady=10, padx=15, fill="x")

        self.table.heading("id", text="Product ID")
        self.table.heading("name", text="Name")
        self.table.heading("category", text="Category")
        self.table.heading("price", text="Price")
        self.table.heading("quantity", text="Quantity")

        self.table.column("id", width=120)
        self.table.column("name", width=220)
        self.table.column("category", width=160)
        self.table.column("price", width=120)
        self.table.column("quantity", width=120)

        self.table.bind("<<TreeviewSelect>>", self.fill_form_from_table)

    def clear_form(self):
        self.product_id_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)
        self.category_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)
        self.quantity_entry.delete(0, tk.END)

    def refresh_table(self):
        for row in self.table.get_children():
            self.table.delete(row)

        for product in inventory:
            self.table.insert(
                "",
                tk.END,
                values=(
                    product["id"],
                    product["name"],
                    product["category"],
                    f"{product['price']:.2f}",
                    product["quantity"],
                ),
            )

    def fill_form_from_table(self, event):
        selected = self.table.focus()
        if not selected:
            return

        values = self.table.item(selected, "values")
        self.clear_form()
        self.product_id_entry.insert(0, values[0])
        self.name_entry.insert(0, values[1])
        self.category_entry.insert(0, values[2])
        self.price_entry.insert(0, values[3])
        self.quantity_entry.insert(0, values[4])

    def add_product(self):
        try:
            product_id = self.product_id_entry.get().strip()
            name = self.name_entry.get().strip()
            category = self.category_entry.get().strip()
            price = float(self.price_entry.get())
            quantity = int(self.quantity_entry.get())

            if not product_id or not name or not category:
                messagebox.showerror("Error", "Please fill all product details.")
                return

            if find_product(product_id):
                messagebox.showerror("Error", "Product ID already exists.")
                return

            inventory.append({
                "id": product_id,
                "name": name,
                "category": category,
                "price": price,
                "quantity": quantity,
            })

            save_data()
            self.refresh_table()
            self.clear_form()
            messagebox.showinfo("Success", "Product added successfully.")
        except ValueError:
            messagebox.showerror("Error", "Price and quantity must be numbers.")

    def update_product(self):
        try:
            product_id = self.product_id_entry.get().strip()
            product = find_product(product_id)

            if not product:
                messagebox.showerror("Error", "Product not found.")
                return

            product["name"] = self.name_entry.get().strip()
            product["category"] = self.category_entry.get().strip()
            product["price"] = float(self.price_entry.get())
            product["quantity"] = int(self.quantity_entry.get())

            save_data()
            self.refresh_table()
            self.clear_form()
            messagebox.showinfo("Success", "Product updated successfully.")
        except ValueError:
            messagebox.showerror("Error", "Price and quantity must be numbers.")

    def delete_product(self):
        product_id = self.product_id_entry.get().strip()
        product = find_product(product_id)

        if not product:
            messagebox.showerror("Error", "Product not found.")
            return

        inventory.remove(product)
        save_data()
        self.refresh_table()
        self.clear_form()
        messagebox.showinfo("Success", "Product deleted successfully.")

    def sell_product(self):
        try:
            product_id = self.sell_id_entry.get().strip()
            quantity = int(self.sell_quantity_entry.get())
            product = find_product(product_id)

            if not product:
                messagebox.showerror("Error", "Product not found.")
                return

            if quantity <= 0:
                messagebox.showerror("Error", "Quantity must be greater than zero.")
                return

            if quantity > product["quantity"]:
                messagebox.showerror("Error", "Insufficient stock.")
                return

            base_amount = product["price"] * quantity
            gst = base_amount * GST_RATE
            total_amount = base_amount + gst

            product["quantity"] -= quantity
            invoice_path, invoice_text = create_invoice(product, quantity, base_amount, gst, total_amount)

            save_data()
            self.refresh_table()
            self.sell_id_entry.delete(0, tk.END)
            self.sell_quantity_entry.delete(0, tk.END)

            messagebox.showinfo("Invoice Generated", f"{invoice_text}\nSaved at: {invoice_path}")
        except ValueError:
            messagebox.showerror("Error", "Sale quantity must be a number.")

    def save_products(self):
        save_data()
        messagebox.showinfo("Success", "Data saved successfully.")


if __name__ == "__main__":
    root = tk.Tk()
    app = InventoryGUI(root)
    root.mainloop()
