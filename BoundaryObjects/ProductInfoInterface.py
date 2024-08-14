class ProductInfoInterface:
    """
    Manages the input and output for product information requests.
    """

    def __init__(self, product_url):
        # Initialize with the product URL
        self.product_url = product_url
        self.product_details = {}

    def fetch_product_details(self):
        # Pretend to fetch product details from the URL (placeholder)
        # In a real scenario, you'd scrape the page and extract details
        self.product_details = {
            'name': 'Sample Product',
            'price': '123.45',
            'availability': 'In Stock'
        }

    def get_product_details(self):
        # Return the fetched product details
        if not self.product_details:
            self.fetch_product_details()
        return self.product_details
