import requests
from bs4 import BeautifulSoup

class BrowserInterface:
    """
    Handles interactions between the bot and the browser for scraping web data.
    """

    def __init__(self, browser_type, url):
        # Initialize the browser interface with browser type and URL
        self.__browser_type = browser_type
        self.__url = url

    def launch_browser(self):
        # Launch the browser with the specified URL
        if self.__url:
            print(f"Launching {self.__browser_type} browser with URL: {self.__url}")
        else:
            raise ValueError("URL must not be null.")

    def close_browser(self):
        # Close the browser
        print(f"Closing {self.__browser_type} browser.")
        self.__browser_type = None
        self.__url = None

    def login(self, account):
        # Use the Account class to log in to a website
        if account.get_username() and account.get_password():
            print(f"Logging in with username: {account.get_username()}")
            # Placeholder for actual login logic using account credentials
            # This would involve interacting with the web page elements to enter the username and password
        else:
            raise ValueError("Account credentials must not be null.")

    def display_data_in_html(self, data):
        # Create an HTML page to display the data read from Excel
        html_content = "<html><head><title>Product Data</title></head><body>"
        html_content += "<h1>Product Data</h1><table border='1'>"
        html_content += "<tr><th>Timestamp</th><th>URL</th><th>Price</th><th>Product</th></tr>"
        
        for row in data:
            html_content += f"<tr><td>{row['Timestamp']}</td><td>{row['URL']}</td><td>{row['Price']}</td><td>{row['Product']}</td></tr>"
        
        html_content += "</table></body></html>"

        # Save the HTML content to a file
        with open("product_data.html", "w") as file:
            file.write(html_content)
        
        print("Data displayed in HTML page (product_data.html).")
