class ProductInfoInterface:
    """
    Manages the input and output for product information requests.
    """

    def __init__(self):
        # Initialize with empty product details
        self.__product_details = ""

    def fetch_product_info(self, product_url):
        # Fetch product details from the URL (Placeholder for actual scraping logic)
        if product_url:
            self.__product_details = f"Details fetched from {product_url}"
            print(self.__product_details)
        else:
            raise ValueError("Product URL must not be null.")

    def get_product_details(self):
        # Return the fetched product details
        if self.__product_details:
            return self.__product_details
        else:
            raise ValueError("Product details have not been fetched yet.")
