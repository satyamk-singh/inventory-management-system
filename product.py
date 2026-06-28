inventory = []


def find_product(product_id):
    for product in inventory:
        if product["id"] == product_id:
            return product
    return None


def add_product():
    product_id = input("Enter Product ID: ")

    if find_product(product_id):
        print("Product ID already exists.")
        return

    name = input("Enter Product Name: ")
    category = input("Enter Category: ")
    price = float(input("Enter Price: "))
    quantity = int(input("Enter Quantity: "))

    product = {
        "id": product_id,
        "name": name,
        "category": category,
        "price": price,
        "quantity": quantity,
    }

    inventory.append(product)
    print("Product added successfully.")


def view_products():
    if not inventory:
        print("No products available.")
        return

    print("\nProduct List")
    print("-" * 70)
    print(f"{'ID':<10} {'Name':<20} {'Category':<15} {'Price':<10} {'Qty':<10}")
    print("-" * 70)

    for product in inventory:
        print(
            f"{product['id']:<10} {product['name']:<20} "
            f"{product['category']:<15} {product['price']:<10.2f} "
            f"{product['quantity']:<10}"
        )


def search_product():
    product_id = input("Enter Product ID to search: ")
    product = find_product(product_id)

    if product:
        print("\nProduct Found")
        print(f"ID       : {product['id']}")
        print(f"Name     : {product['name']}")
        print(f"Category : {product['category']}")
        print(f"Price    : Rs. {product['price']:.2f}")
        print(f"Quantity : {product['quantity']}")
    else:
        print("Product not found.")


def update_product():
    product_id = input("Enter Product ID to update: ")
    product = find_product(product_id)

    if not product:
        print("Product not found.")
        return

    print("Leave blank if you do not want to update a field.")
    name = input("Enter new name: ")
    category = input("Enter new category: ")
    price = input("Enter new price: ")
    quantity = input("Enter new quantity: ")

    if name:
        product["name"] = name
    if category:
        product["category"] = category
    if price:
        product["price"] = float(price)
    if quantity:
        product["quantity"] = int(quantity)

    print("Product updated successfully.")


def delete_product():
    product_id = input("Enter Product ID to delete: ")
    product = find_product(product_id)

    if product:
        inventory.remove(product)
        print("Product deleted successfully.")
    else:
        print("Product not found.")
