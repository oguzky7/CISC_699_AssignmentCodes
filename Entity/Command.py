class Command:
    """
    Represents a command given to the bot.
    """

    def __init__(self, description, command_input):
        # Initialize command with description and input
        self.description = description
        self.input = command_input

    def get_description(self):
        # Return the command's description
        return self.description

    def get_input(self):
        # Return the input for the command
        return self.input
