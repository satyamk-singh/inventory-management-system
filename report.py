import csv

from billing import sales


SALES_REPORT = "sales_report.csv"


def generate_sales_report():
    if not sales:
        print("No sales data available.")
        return

    with open(SALES_REPORT, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            "Sale ID",
            "Product ID",
            "Product Name",
            "Quantity",
            "Base Amount",
            "GST",
            "Total Amount",
            "Date",
        ])

        for sale in sales:
            writer.writerow([
                sale["sale_id"],
                sale["product_id"],
                sale["product_name"],
                sale["quantity"],
                sale["base_amount"],
                sale["gst"],
                sale["total_amount"],
                sale["date"],
            ])

    print(f"Sales report generated: {SALES_REPORT}")
