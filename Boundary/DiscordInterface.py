class DiscordInterface:
    """
    Manages the interactions between the bot and the user on Discord.
    """

    def __init__(self, message):
        # Store the message received from the user
        self.message = message
        # Store the message as the command directly
        self.command = message
        self.response = None

    def generate_response(self):
        # Generate a response based on the command
        # Mostly examples to give ideas, will be dynamic and changed soon
        if self.command.lower() == 'hello':
            self.response = 'Hey there!'
        elif self.command.lower() == 'help':
            self.response = 'These are the commands you can use: hello, help, latest price, last checked, share url...'
        elif self.command.lower() == 'latest price':
            # Placeholder for fetching the latest price from the system
            self.response = 'The latest price for the tracked product is $123.45.'
        elif self.command.lower() == 'last checked':
            # Placeholder for fetching the last checked time
            self.response = 'The last time we checked the price was at 10:30 AM, August 10, 2024.'
        elif self.command.lower().startswith('share url'):
            # Assuming the URL is shared in the format "share url <url>"
            url = self.command[len('share url'):].strip()
            # Placeholder response for URL processing
            self.response = f'Thank you for sharing the URL: {url}. We are fetching the details...'
        else:
            self.response = 'Sorry, I didn’t understand that command.'

        return self.response
