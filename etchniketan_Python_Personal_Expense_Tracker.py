# ==============================================================================
# ETECHNIKETAN FINAL MEGA PROJECT: PERSONAL EXPENSE TRACKER (CLI)
# Provided by: https://www.etechniketan.com/
# Developed by: ARIP DHAR
# ==============================================================================

import csv
import os
import time
import sys
from datetime import datetime

class Expense:
    """
    Object-Oriented Model blueprint representing an individual transaction.
    """
    def __init__(self, expense_id, title, amount, category, date_str):
        self.expense_id = int(expense_id)
        self.title = str(title)
        self.amount = float(amount)
        self.category = str(category)
        self.date_str = str(date_str)

    def to_list(self):
        """Serializes object fields into a list for clean CSV writing."""
        return [self.expense_id, self.title, self.amount, self.category, self.date_str]


class ExpenseTracker:
    """
    Manager class serving as the application brain controlling in-memory CRUD operations,
    robust input validation pipelines, and data persistence routines.
    """
    FILE_NAME = "expenses.csv"

    def __init__(self):
        self.expenses = {}  # In-memory database mapping expense_id -> Expense object
        self.next_id = 101   # Baseline structural auto-generated ID setup
        self.load_from_disk()

    def load_from_disk(self):
        """Loads entries from a standard persistent CSV file container at boot."""
        if not os.path.exists(self.FILE_NAME):
            return
        try:
            with open(self.FILE_NAME, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.reader(file)
                max_id = 100
                for row in reader:
                    if not row:
                        continue
                    exp_id, title, amount, category, date_str = row
                    exp_id = int(exp_id)
                    self.expenses[exp_id] = Expense(exp_id, title, amount, category, date_str)
                    if exp_id > max_id:
                        max_id = exp_id
                self.next_id = max_id + 1
        except Exception as e:
            print(f"--> [SYSTEM ERROR] Could not initialize file container storage: {e}")

    def save_to_disk(self):
        """Writes operational updates cleanly back to the persistent disk storage."""
        try:
            with open(self.FILE_NAME, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                for expense in self.expenses.values():
                    writer.writerow(expense.to_list())
            print("--> [SYSTEM]: Data safely serialized to disk storage containers.")
        except Exception as e:
            print(f"--> [SYSTEM ERROR] Failed data persistence write: {e}")

    def add_expense(self, title, amount, category, date_input):
        """Implements unique transaction generation with auto-date and auto-time fallbacks."""
        if not title.strip():
            title = "Untitled Expense"

        # Check if the user left the date blank
        if not date_input.strip():
            # Query the system clock for both current date and exact time
            now = datetime.now()
            date_str = now.strftime("%d-%m-%Y")
            time_str = now.strftime("%H:%M:%S")
            print(f"--> [SYSTEM]: Blank detected. Auto-assigned current timestamp date: {date_str} at time: {time_str}")
        else:
            date_str = date_input.strip()

        generated_id = self.next_id
        new_expense = Expense(generated_id, title, amount, category, date_str)
        self.expenses[generated_id] = new_expense
        self.next_id += 1
        print(f"Success: New record securely appended! [Generated ID: {generated_id}]")

    def view_all_expenses(self):
        """Renders structural ledger tracking cleanly formatted in tabular format."""
        if not self.expenses:
            print("\n--> [NOTIFICATION]: The tracking ledger is currently empty.")
            return

        print("\n" + "="*82)
        print(f"{'ID':<6} | {'EXPENSE TITLE':<25} | {'AMOUNT (₹)':<12} | {'CATEGORY':<15} | {'DATE':<12}")
        print("="*82)
        for exp in self.expenses.values():
            print(f"{exp.expense_id:<6} | {exp.title:<25} | {exp.amount:<12.2f} | {exp.category:<15} | {exp.date_str:<12}")
        print("="*82 + "\n")

    def search_expense(self, expense_id):
        """Retrieves targeted data rows instantly using the unique key."""
        if expense_id in self.expenses:
            exp = self.expenses[expense_id]
            print("\n" + "-"*40)
            print(f"🔍 EXPENSE RECORD FOUND [ID: {exp.expense_id}]")
            print(f" Title:    {exp.title}")
            print(f" Amount:   ₹{exp.amount:.2f}")
            print(f" Category: {exp.category}")
            print(f" Date:     {exp.date_str}")
            print("-"*40 + "\n")
        else:
            print(f"--> [ERROR]: Record ID {expense_id} does not exist in the ledger.")

    def update_expense(self, expense_id):
        """Modifies operational entries dynamically inside active cache memories."""
        if expense_id not in self.expenses:
            print(f"--> [ERROR]: Record ID {expense_id} does not exist.")
            return

        exp = self.expenses[expense_id]
        print(f"\nUpdating Record [{expense_id}] - Press Enter to skip fields you want to keep.")
        
        new_title = input(f"Enter new Title [{exp.title}]: ").strip()
        if new_title:
            exp.title = new_title

        while True:
            new_amount_input = input(f"Enter new Amount [₹{exp.amount:.2f}]: ").strip()
            if not new_amount_input:
                break
            try:
                amt = float(new_amount_input)
                if amt < 0:
                    print("--> [ERROR]: Monetary values cannot be negative numbers.")
                    continue
                exp.amount = amt
                break
            except ValueError:
                print("--> [ERROR]: Invalid monetary value. Please enter a valid numerical decimal amount.")

        new_cat = input(f"Enter new Category [{exp.category}]: ").strip()
        if new_cat:
            exp.category = new_cat

        while True:
            new_date_input = input(f"Enter new Date [{exp.date_str}]: ").strip()
            if not new_date_input:
                break
            try:
                datetime.strptime(new_date_input, "%d-%m-%Y")
                exp.date_str = new_date_input
                break
            except ValueError:
                print("--> [ERROR]: Invalid date configuration pattern. Must match DD-MM-YYYY format.")

        print(f"Success: Record [ID: {expense_id}] has been dynamically updated in active memory!")

    def delete_expense(self, expense_id):
        """Safely removes target entries from the internal computational collections."""
        if expense_id in self.expenses:
            deleted_item = self.expenses.pop(expense_id)
            print(f"Success: Record '{deleted_item.title}' [ID: {expense_id}] removed from tracking ledger.")
        else:
            print(f"--> [ERROR]: Record ID {expense_id} does not exist.")

    def generate_telemetry_dashboard(self):
        """Generates real-time budget metrics summaries."""
        if not self.expenses:
            print("\n===============")
            print("FINANCIAL TELEMETRY DASHBOARD")
            print("COMPREHENSIVE STATUS SUMMARY")
            print("Grand Combined Total Expenditures ₹0.00")
            print("Total Active Unique Tracked Items: 0 Records")
            print("=============== \n")
            return

        grand_total = 0.0
        unique_records = len(self.expenses)
        category_breakdown = {}

        for exp in self.expenses.values():
            grand_total += exp.amount
            cat_normalized = exp.category.strip().capitalize()
            category_breakdown[cat_normalized] = category_breakdown.get(cat_normalized, 0.0) + exp.amount

        print("\n===============")
        print("FINANCIAL TELEMETRY DASHBOARD")
        print("COMPREHENSIVE STATUS SUMMARY")
        print(f"Grand Combined Total Expenditures ₹{grand_total:,.2f}")
        print(f"Total Active Unique Tracked Items: {unique_records} Records")
        print("\nDYNAMIC CATEGORY-WISE BREAKDOWN")
        for category, subtotal in category_breakdown.items():
            print(f" {category:<13} : ₹{subtotal:,.2f}")
        print("===============\n")


def display_menu():
    print("=== PERSONAL EXPENSE TRACKER ===")
    print("1. Add New Expense")
    print("2. View All Expenses")
    print("3. Search Expense")
    print("4. Update Expense")
    print("5. Delete Expense")
    print("6. View Summary Metrics")
    print("7. Exit & Save Data")


# ==============================================================================
# MAIN APPLICATION CONTROLLER ENTRY POINT 
# ==============================================================================
def main():
  
    print(r"""
     ____  _____ ____  ____  ____  _      ____  _        ________  _ ____  _____ _      ____  _____   _____ ____  ____  ____  _  __ _____ ____    ___ ____  _      _ ___ 
    /  __\/  __//  __\/ ___\/  _ \/ \  /|/  _ \/ \      /  __/\  \///  __\/  __// \  /|/ ___\/  __/  /__ __Y  __\/  _ \/   _\/ |/ //  __//  __\  / _//   _\/ \   / \\_ \
    |  \/||  \  |  \/||    \| / \|| |\ ||| / \|| |      |  \   \  / |  \/||  \  | |\ |||    \|  \      / \ |  \/|| / \||  /  |   / |  \  |  \/|  |/  |  /  | |   | |  \|
    |  __/|  /_ |    /\___ || \_/|| | \||| |-||| |_/\   |  /_  /  \ |  __/|  /_ | | \||\___ ||  /_     | | |    /| |-|||  \__|   \ |  /_ |    /  |\_ |  \__| |_/\| | _/|
    \_/   \____\\_/\_\\____/\____/\_/  \|\_/ \|\____/   \____\/__/\\\_/   \____\\_/  \|\____/\____\    \_/ \_/\_\\_/ \|\____/\_|\_\\____\\_/\_\  \__\\____/\____/\_//__/
                                                                                                                                                                     
""")
    
    print("========================================== Developed by ARIP DHAR ==========================================")
    print("> Project Provided by      : https://www.etechniketan.com/")
    print("> Purpose                  : Automated Budget Telemetry, Secure CSV Ledger Persistence, Dynamic In-Memory CRUD Analytics")
    print("> Portfolio/GitHub         : github.com/arip-dhar")
    print("> For any queries          : aripdhar800@gmail.com")
    print("============================================================================================================")
    print()

    # Emulating System Startup Diagnostics Sequence
    diagnostics = [
        "[+] Initializing advanced financial analytics mapping engines...",
        "[-] Loading target data matrix components from memory containers...",
        "[!] Info: System data stream tracking relies safely on native Python engines.",
        "[*] Active Core File  : expenses.csv",
        "[-] Running integrity scans on existing dataset collections...",
        "[-] Syncing structural currency balances and indexing algorithms..."
    ]

    for step in diagnostics:
        print(step)
        time.sleep(0.25)

    print("\n[-] Commencing local database compilation sequences...")
    
    # Dynamic Diagnostic Progress Loading Bar Simulation
    for percent in range(0, 101, 10):
        bar_length = percent // 5
        bar = "█" * bar_length + "░" * (20 - bar_length)
        sys.stdout.write(f"\r[-] Analysis Execution Progress: [{bar}] {percent}.0% Complete")
        sys.stdout.flush()
        time.sleep(0.12)
        
    print("\n\n--> Boot Sequence Complete. Launching Application Controller Suite...\n")
    time.sleep(0.5)

    # Initialize the Tracker instance safely now that classes are loaded above
    tracker = ExpenseTracker()

    while True:
        display_menu()
        choice = input("Choose option (1-7): ").strip()

        if choice == '1':
            print("\n--- 1. Add New Expense ---")
            title = input("Enter Expense Title: ")
            
            while True:
                amount_raw = input("Enter Expense Amount: ")
                try:
                    amount = float(amount_raw)
                    if amount < 0:
                        print("--> [ERROR]: Expense amount cannot be a negative value.")
                        continue
                    break
                except ValueError:
                    print("--> [ERROR]: Invalid monetary value. Please enter a valid numerical decimal amount.")
            
            category = input("Enter Expense Category: ").strip()
            if not category:
                category = "General"

            while True:
                date_input = input("Enter Expense Date (DD-MM-YYYY) or leave blank for today: ")
                if not date_input.strip():
                    break
                try:
                    datetime.strptime(date_input.strip(), "%d-%m-%Y")
                    break
                except ValueError:
                    print("--> [ERROR]: Invalid date configuration pattern. Must match DD-MM-YYYY format.")

            tracker.add_expense(title, amount, category, date_input)
            print()

        elif choice == '2':
            tracker.view_all_expenses()

        elif choice == '3':
            print("\n--- 3. Search Expense ---")
            try:
                search_id = int(input("Enter Unique Expense ID to look up: "))
                tracker.search_expense(search_id)
            except ValueError:
                print("--> [ERROR]: System identifiers must be standard raw integers.")
            print()

        elif choice == '4':
            print("\n--- 4. Update Expense ---")
            try:
                update_id = int(input("Enter Expense ID to modify: "))
                tracker.update_expense(update_id)
            except ValueError:
                print("--> [ERROR]: System identifiers must be standard raw integers.")
            print()

        elif choice == '5':
            print("\n--- 5. Delete Expense ---")
            try:
                delete_id = int(input("Enter Expense ID to remove: "))
                tracker.delete_expense(delete_id)
            except ValueError:
                print("--> [ERROR]: System identifiers must be standard raw integers.")
            print()

        elif choice == '6':
            tracker.generate_telemetry_dashboard()

        elif choice == '7':
            print("\nTerminating system pipelines safely...")
            tracker.save_to_disk()
            print("Goodbye! Execution closed successfully.Thankyou for visiting, Please visit again...")
            break
        else:
            print("\n--> [ERROR]: Out-of-bounds menu selection. Choose options strictly from 1 to 7.\n")

if __name__ == "__main__":
    main()