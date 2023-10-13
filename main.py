import h5py
import pandas as pd

class HDF5DataScraper:
    def __init__(self, file_path):
        """
        Initialize the HDF5 Data Scraper.

        Args:
            file_path (str): Path to the HDF5 file containing the data.
        """
        self.file_path = file_path

    def extract_specific_data(self, dataset_path):
        """
        Extract data from the specified dataset.

        Args:
            dataset_path (str): Path to the dataset within the HDF5 file.

        Returns:
            numpy.ndarray: Extracted data.
        """
        with h5py.File(self.file_path, 'r') as file:
            dataset = file[dataset_path][()]  # Extract the data
        return dataset

    def scrape_data(self, dataset_paths, output_filename='scraped_data.csv'):
        """
        Scrape data from the specified dataset paths, create a DataFrame, and save as a CSV.

        Args:
            dataset_paths (list): List of dataset paths to scrape.
            output_filename (str): Name of the output CSV file.

        Returns:
            pandas.DataFrame: Scraped data in DataFrame format.
        """
        scraped_data = {}  # Create an empty dictionary to store scraped data

        # Extract data from the specific dataset paths
        for i, dataset_path in enumerate(dataset_paths):
            dataset_name = dataset_path.split("/")[-1]  # Extract the dataset name from the path
            scraped_data[dataset_name] = pd.Series(self.extract_specific_data(dataset_path).ravel().tolist())

        # Create a DataFrame from the scraped data
        df = pd.DataFrame(scraped_data)

        # Save the data to a CSV file with a descriptive name
        df.to_csv(output_filename, index=False)

        print(df)

        return df

# Specify the path to your HDF5 file
file_path = r'C:\Users\Pc\Downloads\earthdataSearchApi\VNP09GA.A2023282.h08v09.001.2023283085323.h5'

# Specify the dataset paths you want to retrieve
dataset_paths = [
    'HDFEOS/GRIDS/VNP_Grid_1km_2D/Data Fields/SensorAzimuth_1',
    'HDFEOS/GRIDS/VNP_Grid_1km_2D/Data Fields/SensorZenith_1',
    # Add more dataset paths as needed
]

# Create an instance of the scraper
scraper = HDF5DataScraper(file_path)

# Scrape the data, create DataFrame, and save as CSV
output_df = scraper.scrape_data(dataset_paths, output_filename='earthdata_sensor_data.csv')

if output_df is not None:
    print("Data has been scraped and saved to 'earthdata_sensor_data.csv'.")
