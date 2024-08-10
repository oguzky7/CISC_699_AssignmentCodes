class User:
    """
    Represents a user of the system.
    """

    def __init__(self, user_id, email):
        # Initialize user with id and email
        self.__user_id = user_id
        self.email = email

    def get_user_id(self):
        # Return the user's ID
        return self.__user_id

    def get_email(self):
        # Return the user's email
        return self.email
