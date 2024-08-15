class DateInfoInterface:
    """
    Manages the input and output for date availability requests.
    """

    def __init__(self):
        # Initialize with empty date info
        self.__date_info = ""

    def fetch_date_info(self, date):
        # Fetch date information (Placeholder for actual date info retrieval logic)
        if date:
            self.__date_info = f"Availability checked for {date}"
            print(self.__date_info)
        else:
            raise ValueError("Date must not be null.")

    def get_date_info(self):
        # Return the fetched date information
        if self.__date_info:
            return self.__date_info
        else:
            raise ValueError("Date information has not been fetched yet.")
