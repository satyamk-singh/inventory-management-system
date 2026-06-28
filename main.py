from billing import sell_product
from inventory import low_stock_alert, purchase_stock
from product import add_product, delete_product, search_product, update_product, view_products
from report import generate_sales_report
from storage import load_data, save_data


def main_menu():
    load_data()

    while True:
        print("\n========== Inventory Management System ==========")
        print("1. Add Product")
        print("2. View Products")
        print("3. Search Product")
        print("4. Update Product")
        print("5. Delete Product")
        print("6. Purchase Stock")
        print("7. Sell Product / Generate Bill")
        print("8. Low Stock Alert")
        print("9. Generate Sales Report")
        print("10. Save Data")
        print("11. Exit")

        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                add_product()
            elif choice == "2":
                view_products()
            elif choice == "3":
                search_product()
            elif choice == "4":
                update_product()
            elif choice == "5":
                delete_product()
            elif choice == "6":
                purchase_stock()
            elif choice == "7":
                sell_product()
            elif choice == "8":
                low_stock_alert()
            elif choice == "9":
                generate_sales_report()
            elif choice == "10":
                save_data()
            elif choice == "11":
                save_data()
                print("Thank you for using Inventory Management System.")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter numbers correctly.")


main_menu()
