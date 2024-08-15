import discord

class DiscordInterface:
    """
    Manages the interactions between the bot and the user on Discord.
    """

    def __init__(self, interface_name, discord_bot):
        # Initialize with the interface name and Discord bot instance
        self.__interface_name = interface_name
        self.__discord_bot = discord_bot

    def connect(self):
        # Connect the bot to Discord
        if self.__discord_bot:
            print(f"Connecting {self.__interface_name} to Discord...")
            self.__discord_bot.run()
        else:
            raise ValueError("Discord bot instance must not be null.")

    def disconnect(self):
        # Disconnect the bot from Discord
        if self.__discord_bot:
            self.__discord_bot.close()
            print(f"Disconnecting {self.__interface_name} from Discord...")
        else:
            raise ValueError("Discord bot instance must not be null.")
