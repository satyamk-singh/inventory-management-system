from product import find_product, inventory


LOW_STOCK_LIMIT = 5


def purchase_stock():
    product_id = input("Enter Product ID: ")
    product = find_product(product_id)

    if not product:
        print("Product not found.")
        return

    quantity = int(input("Enter purchase quantity: "))
    product["quantity"] += quantity
    print("Stock updated successfully.")


def low_stock_alert():
    low_stock = [product for product in inventory if product["quantity"] <= LOW_STOCK_LIMIT]

    if not low_stock:
        print("No low stock products.")
        return

    print("\nLow Stock Products")
    print("-" * 50)
    for product in low_stock:
        print(f"{product['id']} - {product['name']} - Qty: {product['quantity']}")
