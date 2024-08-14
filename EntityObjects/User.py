class User:
    """
    Represents a user of the system.
    """

    def __init__(self, user_id, email):
        # Initialize user with ID and email
        self.__user_id = user_id
        self.email = email

    def get_user_id(self):
        # Return the user's ID
        return self.__user_id

    def get_email(self):
        # Return the user's email
        return self.email

    def info_user(self):
        # Print detailed information about the user
        print(f"User ID: {self.__user_id}")
        print(f"Email: {self.email}")
