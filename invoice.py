import os
from datetime import datetime


INVOICE_FOLDER = "invoices"


def create_invoice(product, quantity, base_amount, gst, total_amount):
    os.makedirs(INVOICE_FOLDER, exist_ok=True)

    invoice_id = "INV" + datetime.now().strftime("%Y%m%d%H%M%S")
    invoice_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file_name = f"{invoice_id}.txt"
    file_path = os.path.join(INVOICE_FOLDER, file_name)

    invoice_text = f"""
==============================
        SALES INVOICE
==============================
Invoice ID   : {invoice_id}
Date         : {invoice_date}

Product ID   : {product['id']}
Product Name : {product['name']}
Category     : {product['category']}
Unit Price   : Rs. {product['price']:.2f}
Quantity     : {quantity}

------------------------------
Base Amount  : Rs. {base_amount:.2f}
GST 18%      : Rs. {gst:.2f}
Total Amount : Rs. {total_amount:.2f}
------------------------------

Thank you for shopping!
==============================
"""

    with open(file_path, "w") as file:
        file.write(invoice_text)

    return file_path, invoice_text
