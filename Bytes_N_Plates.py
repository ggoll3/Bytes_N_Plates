

# Base class for all employees.
class Employee:
    def __init__(self, name):
        self.name = name

    # Common view methods
    def view_seating_layout(self):
        print(f"{self.name} is viewing the seating layout screen.")

    def view_seating_availability(self):
        print(f"{self.name} is viewing seating availability.")

    def view_current_orders(self):
        print(f"{self.name} is viewing current orders.")


# Standard Employee Account: Inherits basic viewing from Employee
# and can input new orders, mark orders as complete, and change seating availability.
class StandardEmployee(Employee):
    def input_new_order(self, order):
        print(f"{self.name} is inputting a new order: {order}")

    def mark_order_complete(self, order_id):
        print(f"{self.name} is marking order {order_id} as complete.")

    def change_seating_availability(self, seating_id, availability):
        print(f"{self.name} is changing seating {seating_id}'s availability to {availability}.")


# Manager Account: Inherits from StandardEmployee so it already has the basic view and
# StandardEmployee editing methods. It adds extra viewing and editing methods.
class Manager(StandardEmployee):
    # Additional view methods for managers.
    def view_sales_data(self):
        print(f"{self.name} is viewing sales data.")

    def view_sales_analytics(self):
        print(f"{self.name} is viewing sales analytics screens.")

    def view_all_accounts(self):
        print(f"{self.name} is viewing all restaurant accounts and their permission levels.")

    # Additional editing methods for orders.
    def add_order(self, order, past=False):
        if past:
            print(f"{self.name} is adding a past order: {order}")
        else:
            print(f"{self.name} is adding a current order: {order}")

    def edit_order(self, order_id, new_order):
        print(f"{self.name} is editing order {order_id} to: {new_order}")

    # Editing seating layout is allowed for managers.
    def edit_seating_layout(self, new_layout):
        print(f"{self.name} is editing the seating layout to: {new_layout}")

    # Adding and editing accounts (only StandardEmployee and Manager accounts allowed).
    def add_new_account(self, account_type, account_name):
        if account_type.lower() in ['standardemployee', 'manager']:
            print(f"{self.name} is adding a new {account_type} account for {account_name}.")
        else:
            print("Managers can only add Standard Employee or Manager accounts.")

    def edit_account(self, account):
        # For demonstration we assume that the account has attributes name and account_type.
        if account.account_type.lower() in ['standardemployee', 'manager']:
            print(f"{self.name} is editing account {account.name}.")
        else:
            print("Managers can only edit Standard Employee or Manager accounts.")

    # Adjust menu prices and item availability.
    def adjust_menu(self, item, price, availability):
        print(f"{self.name} is adjusting menu: setting {item} to price {price} and availability {availability}.")


# Restaurant Admin Account: Inherits from Manager so it has all the Manager permissions,
# but adds some extra methods and overrides account methods to allow ALL account types.
class RestaurantAdmin(Manager):
    # Unrestricted viewing of all restaurant data.
    def view_all_data(self):
        print(f"{self.name} is viewing all restaurant data without restrictions.")

    # Editing restaurant details.
    def edit_restaurant_details(self, details):
        print(f"{self.name} is editing restaurant details: {details}")

    # Create a new restaurant.
    def create_restaurant(self, restaurant_name):
        print(f"{self.name} is creating a new restaurant called {restaurant_name}.")

    # Override account management methods to allow all account types.
    def add_new_account(self, account_type, account_name):
        print(f"{self.name} is adding a new {account_type} account for {account_name}.")

    def edit_account(self, account):
        print(f"{self.name} is editing account {account.name}.")


# A simple Account class to help demonstrate editing accounts.
class Account:
    def __init__(self, name, account_type):
        self.name = name
        self.account_type = account_type


# Test the classes.
if __name__ == '__main__':
    # Create one of each account type.
    standard_emp = StandardEmployee("Alice")
    manager = Manager("Bob")
    admin = RestaurantAdmin("Carol")

    # Standard Employee actions.
    standard_emp.view_seating_layout()
    standard_emp.view_seating_availability()
    standard_emp.view_current_orders()
    standard_emp.input_new_order("Burger and Fries")
    standard_emp.mark_order_complete(101)
    standard_emp.change_seating_availability("Table 5", "Occupied")

    print("\n--- Manager Actions ---")
    # Manager actions (which include StandardEmployee ones, plus additional).
    manager.view_sales_data()
    manager.view_sales_analytics()
    manager.view_all_accounts()
    manager.add_order("Pasta Carbonara", past=False)
    manager.edit_order(102, "Updated Pasta Carbonara")
    manager.edit_seating_layout("New seating layout version")
    manager.adjust_menu("Salad", 7.99, "Available")
    # Create a dummy account for editing:
    test_account = Account("David", "StandardEmployee")
    manager.add_new_account("StandardEmployee", "David")
    manager.edit_account(test_account)

    print("\n--- Restaurant Admin Actions ---")
    # Restaurant Admin actions (includes Manager actions plus extra).
    admin.view_all_data()
    admin.edit_restaurant_details("Updated restaurant decor")
    admin.create_restaurant("The Great Diner")
    admin.add_new_account("RestaurantAdmin", "Eve")  # now can add any type.
    admin.edit_account(Account("Frank", "Manager"))
