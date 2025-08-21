from bank import Bank, Account

def main():
    a = Bank()

    while True:
        print("\nWelcome to Aderine Bank")
        print("_" * 100)
        print("1. Login")
        print("2. Signup")
        print("3. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input! Enter a number.")
            continue

        if choice == 1:
            name = input("Enter your name: ")
            if name in a.database:
                password = input("Enter your password: ")
                if a.database[name][1] == password:
                    while True:
                        print("\n" + "-" * 100)
                        print(f"Welcome {name} to Aderine Bank")
                        print("1. Check Balance")
                        print("2. Withdraw")
                        print("3. Deposit")
                        print("4. Transactions")
                        print("5. Send Money")
                        print("6. Exit")

                        try:
                            c = int(input("Select one option: "))
                        except ValueError:
                            print("Invalid input! Enter a number.")
                            continue

                        if c == 6:
                            break
                        elif c == 1:
                            print("Current Balance:", a.database[name][3])
                        elif c == 2:
                            amount = int(input("Enter the amount: "))
                            if amount <= a.database[name][3]:
                                a.database[name][3] -= amount
                                a.database[name][4].append(f"Withdrew {amount} rupees")
                                print("✅ Withdraw successful! Balance:", a.database[name][3])
                            else:
                                print("❌ Insufficient Balance!")
                        elif c == 3:
                            amount = int(input("Enter the amount: "))
                            if amount > 0:
                                a.database[name][3] += amount
                                a.database[name][4].append(f"Deposited {amount} rupees")
                                print("✅ Deposit successful! Balance:", a.database[name][3])
                            else:
                                print("❌ Invalid Amount!")
                        elif c == 5:
                            receiver = input("Enter receiver name: ")
                            if receiver in a.database:
                                amount = int(input("Enter amount to send: "))
                                if 0 < amount <= a.database[name][3]:
                                    a.database[name][3] -= amount
                                    a.database[receiver][3] += amount
                                    a.database[name][4].append(f"Sent {amount} rupees to {receiver}")
                                    a.database[receiver][4].append(f"Received {amount} rupees from {name}")
                                    print("✅ Transfer successful!")
                                else:
                                    print("❌ Invalid or Insufficient Balance!")
                            else:
                                print("❌ Receiver not found!")
                        elif c == 4:
                            print("\nTransaction History:")
                            for t in a.database[name][4]:
                                print("-", t)
                        else:
                            print("❌ Invalid option!")
                else:
                    print("❌ Invalid Password...")
            else:
                print("❌ Invalid Username...")

        elif choice == 2:
            name = input("Enter your name: ")
            password = input("Enter your password: ")
            email = input("Enter your email: ")
            Account(name, password, email, a)

        elif choice == 3:
            print("🙏 Thank you for visiting Aderine Bank. Come back soon!")
            break
        else:
            print("❌ Invalid option!")

if __name__ == "__main__":
    main()
