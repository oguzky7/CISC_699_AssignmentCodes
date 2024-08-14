class DateInfoInterface:
    """
    Manages the input and output for date availability requests.
    """

    def __init__(self, resource_url):
        # Initialize with the resource URL
        self.resource_url = resource_url
        self.available_dates = []

    def get_available_dates(self):
        # Return the fetched dates
        if not self.available_dates:
            self.fetch_available_dates()
        return self.available_dates
