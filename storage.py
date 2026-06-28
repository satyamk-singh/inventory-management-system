import json
import os

import product


PRODUCT_FILE = "products.json"


def load_data():
    if os.path.exists(PRODUCT_FILE):
        with open(PRODUCT_FILE, "r") as file:
            product.inventory.clear()
            product.inventory.extend(json.load(file))
        print("Data loaded successfully.")
    else:
        print("No saved data found. Starting fresh.")


def save_data():
    with open(PRODUCT_FILE, "w") as file:
        json.dump(product.inventory, file, indent=4)
    print("Data saved successfully.")
