class UserManager:
    def __init__(self):
        self.file = "users.txt"

    def add_user(self, name):
        with open(self.file, "a") as f:
            f.write(name + "\n")
        print("User added!")

    def view_users(self):
        with open(self.file, "r") as f:
            users = f.readlines()
        print("Users:")
        for user in users:
            print(user.strip())

    def delete_user(self, name):
        with open(self.file, "r") as f:
            users = f.readlines()
        with open(self.file, "w") as f:
            for user in users:
                if user.strip() != name:
                    f.write(user)
        print("User deleted!")

manager = UserManager()

while True:
    print("\n1. Add User\n2. View Users\n3. Delete User\n4. Exit")
    choice = input("Choose: ")

    if choice == "1":
        manager.add_user(input("Enter name: "))
    elif choice == "2":
        manager.view_users()
    elif choice == "3":
        manager.delete_user(input("Enter name: "))
    elif choice == "4":
        break
