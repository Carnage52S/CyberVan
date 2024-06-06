import hashlib
import json
import os

class PasswordManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.passwords = {}
        self.load_passwords()

    def load_passwords(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                self.passwords = json.load(file)
        else:
            self.passwords = {}

    def save_passwords(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.passwords, file)

    def add_password(self, website, username, password):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        self.passwords[website] = {'username': username, 'password': hashed_password}
        self.save_passwords()

    def get_password(self, website):
        return self.passwords.get(website, None)

    def delete_password(self, website):
        if website in self.passwords:
            del self.passwords[website]
            self.save_passwords()

    def list_passwords(self):
        return list(self.passwords.keys())
    
    def main():
        manager = PasswordManager('passwords.json')

        while True:
            print("\nPassword Manager")
            print("1. Add Password")
            print("2. Get Password")
            print("3. Delete Password")
            print("4. List Passwords")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                website = input("Enter website: ")
                username = input("Enter username: ")
                password = input("Enter password: ")
                manager.add_password(website, username, password)
                print("Password added successfully.")

            elif choice == '2':
                website = input("Enter website: ")
                result = manager.get_password(website)
                if result:
                    print(f"Username: {result['username']}, Password: {result['password']}")
                else:
                    print("No password found for the website.")

            elif choice == '3':
                website = input("Enter website: ")
                manager.delete_password(website)
                print("Password deleted successfully.")

            elif choice == '4':
                websites = manager.list_passwords()
                for site in websites:
                    print(site)

            elif choice == '5':
                break

            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()