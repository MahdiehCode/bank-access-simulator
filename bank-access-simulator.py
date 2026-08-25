# Bank Access Simulator
# A simple Python program that simulates
# a bank card password and account access system.

correct_password = "123"
max_attempts = 3
attempts = 0
card_locked = False

while True:

    print("\n" + "=" * 45)
    print("          BANK ACCESS SIMULATOR")
    print("=" * 45)

    if card_locked:
        print("Your card is locked.")
        print("Please contact your bank for assistance.")
        break

    print("1. Login")
    print("2. Exit")

    choice = input("Choose an option: ")

    if choice == "1":

        attempts = 0
        logged_in = False

        while attempts < max_attempts:

            password = input("\nEnter your password: ")

            if password == correct_password:
                print("\nPassword is correct.")
                print("Access granted.")
                logged_in = True
                break

            attempts += 1
            remaining = max_attempts - attempts

            print("Incorrect password.")

            if remaining > 0:
                print(f"You have {remaining} attempt(s) remaining.")
            else:
                print("Your card has been blocked.")
                card_locked = True

        if logged_in:

            while True:

                print("\n" + "-" * 35)
                print("          ACCOUNT MENU")
                print("-" * 35)
                print("1. Change password")
                print("2. Logout")

                account_choice = input("Choose an option: ")

                if account_choice == "1":

                    old_password = input("Enter your current password: ")

                    if old_password == correct_password:

                        new_password = input("Enter your new password: ")
                        confirm_password = input("Confirm your new password: ")

                        if new_password == confirm_password:

                            if len(new_password) >= 3:
                                correct_password = new_password
                                print("Password changed successfully.")
                            else:
                                print(
                                    "Password must contain at least 3 characters."
                                )

                        else:
                            print("Passwords do not match.")

                    else:
                        print("Incorrect current password.")

                elif account_choice == "2":

                    print("You have been logged out.")
                    break

                else:
                    print("Invalid option.")

    elif choice == "2":

        print("\nThank you for using Bank Access Simulator.")
        break

    else:
        print("Invalid option. Please choose 1 or 2.")