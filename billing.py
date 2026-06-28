from datetime import datetime

from product import find_product


GST_RATE = 0.18
sales = []


def sell_product():
    product_id = input("Enter Product ID: ")
    product = find_product(product_id)

    if not product:
        print("Product not found.")
        return

    quantity = int(input("Enter sale quantity: "))

    if quantity > product["quantity"]:
        print("Insufficient stock.")
        return

    base_amount = product["price"] * quantity
    gst = base_amount * GST_RATE
    total_amount = base_amount + gst
    product["quantity"] -= quantity

    sale = {
        "sale_id": "SALE" + datetime.now().strftime("%H%M%S"),
        "product_id": product["id"],
        "product_name": product["name"],
        "quantity": quantity,
        "base_amount": base_amount,
        "gst": gst,
        "total_amount": total_amount,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }

    sales.append(sale)

    print("\nBill Generated")
    print("-" * 40)
    print(f"Product      : {product['name']}")
    print(f"Quantity     : {quantity}")
    print(f"Base Amount  : Rs. {base_amount:.2f}")
    print(f"GST 18%      : Rs. {gst:.2f}")
    print(f"Total Amount : Rs. {total_amount:.2f}")
    print("-" * 40)
