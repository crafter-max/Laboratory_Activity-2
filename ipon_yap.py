class Ipon:
    def __init__(self, name, days, initial_balance=0.0):
        self.name = name
        self.days = days
        self.balance = initial_balance
        self.target = days * 200

    def deposit(self, amount):
        if amount <= 0:
            print("You must add cash, not empty words.")
            return
        self.balance += amount
        print(f"Amount {amount} added to your '{self.name}' challenge.")
        
        if amount >= (self.target * 0.20):
            print(f"Holy dawg, {amount} is too much! You're crushing it.")

    def check(self):
        print(f"There is {self.balance} in your account.")
        print(f"Target goal: {self.target}")

def main():
    try:
        user_name = input("Enter your ipon challenge name: ")
        days_input = float(input("Input how many days (days * 200): "))
        
        my_ipon = Ipon(user_name, days_input)

        while True:
            print("\n1. Deposit | 2. Check | 3. Exit")
            choice = input("Select an option: ")

            if choice == '1':
                amount = float(input("Enter amount to deposit: "))
                my_ipon.deposit(amount)
            elif choice == '2':
                my_ipon.check()
            elif choice == '3':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please select 1, 2, or 3.")

    except ValueError:
        print("Input Error: Please enter a numeric value for days/amounts.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()