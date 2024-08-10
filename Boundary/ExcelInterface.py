import pandas as pd

class ExcelInterface:
    """
    Handles data extraction to Excel.
    """

    def __init__(self, file_path):
        # Initialize with the file path where the Excel file will be saved
        self.file_path = file_path
        self.data = None

    def save_data_to_excel(self, data):
        # Save the data to an Excel file
        try:
            df = pd.DataFrame(data)
            df.to_excel(self.file_path, index=False)
            print(f"Data saved to {self.file_path}")
        except Exception as e:
            print(f"Failed to save data to Excel: {e}")

    def load_data_from_excel(self):
        # Load data from an Excel file
        try:
            self.data = pd.read_excel(self.file_path)
            print(f"Data loaded from {self.file_path}")
        except Exception as e:
            print(f"Failed to load data from Excel: {e}")
            self.data = None

    def get_data(self):
        # Return the loaded data
        if self.data is None:
            self.load_data_from_excel()
        return self.data
