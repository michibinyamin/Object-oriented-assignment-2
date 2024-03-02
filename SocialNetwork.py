from User import User


class SocialNetwork:

    __instance = None  # Class variable to store the singleton instance

    def __new__(cls, network_type):   # Singleton design pattern to make sure that there is only one instance of network
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.network_type = network_type  # Initialize network type
            cls.__instance.users = []   # Initialize users list
            print(f"The social network {network_type} was created!")
        return cls.__instance

    def sign_up(self, name, password):
        if self.__user_in_list(name):
            raise ValueError("User already exists")
        if self.__is_illegal_password(password):
            raise ValueError("Illegal password")
        new_user = User(name, password)  # Create new user
        self.users.append(new_user)  # Add user to list
        return new_user

    def __user_in_list(self, name):  # Check if user already exists
        return any(user.name == name for user in self.users)

    def __is_illegal_password(self, password):  # Check if password is legal
        return not (4 <= len(password) <= 8)

    def log_in(self, username, password):
        for user in self.users:
            if username == user.name:
                if password == user.get_password():
                    user.set_online(True)   # Set user to online
                    print(f"{username} connected")  # Print
                    return None
                else:
                    print("Wrong password")
                    return None
        print("Username not found")
        return None

    def log_out(self, username):
        for user in self.users:
            if username == user.name:
                user.set_online(False)   # Set user to offline
                print(f"{username} disconnected")   # Print
                return None
        print("Wrong username")

    def __str__(self):
        st = f"{self.network_type} social network:"
        for user in self.users:
            st = st + "\n" + user.__str__()
        return st

