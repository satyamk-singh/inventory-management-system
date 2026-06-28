# Inventory Management System

This is a beginner-friendly Python project with separate files for each module.

## Files

- `main.py`: Main menu
- `product.py`: Add, view, search, update, delete products
- `inventory.py`: Purchase stock and low stock alert
- `billing.py`: Sell product and generate bill with GST
- `storage.py`: Save/load product data using JSON
- `report.py`: Generate sales report using CSV
- `invoice.py`: Create invoice text files
- `gui_app.py`: GUI version using Tkinter

## How to Run Console Version

Open this folder in VS Code and run:

```bash
python main.py
```

If `python` does not work, try:

```bash
py main.py
```

## How to Run GUI Version

Run:

```bash
python gui_app.py
```

If `python` does not work, try:

```bash
py gui_app.py
```

The GUI version supports:

- Add product
- View products in table
- Update product
- Delete product
- Sell product
- Generate invoice
- Save product data

Invoices are saved inside the `invoices` folder.

## Demo Product ID

When adding a product, enter your own Product ID like:

```text
P001
```

Use the same ID for search, update, delete, purchase, or sale.
