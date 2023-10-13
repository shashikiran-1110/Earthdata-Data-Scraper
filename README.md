# HDF5 Data Scraper

This Python script is designed to scrape data from an HDF5 file and save it to a CSV file. It's particularly useful for extracting specific datasets from HDF5 files and converting them into a more accessible format.

## Prerequisites

Before you begin, ensure you have met the following requirements:
- Python (3.7 or higher) installed on your system.
- Required Python packages installed. You can install them using `pip install -r requirements.txt`.

## Usage

1. Specify the path to your HDF5 file by setting the `file_path` variable in the script.

2. Specify the dataset paths you want to retrieve by adding them to the `dataset_paths` list.

3. Run the script. It will extract data from the specified dataset paths, create a DataFrame, and save the data to a CSV file.

4. You can customize the output file name by changing the `output_filename` parameter in the `scrape_data` method.

## Example

In this example, the script is set to extract data from two dataset paths:
- 'HDFEOS/GRIDS/VNP_Grid_1km_2D/Data Fields/SensorAzimuth_1'
- 'HDFEOS/GRIDS/VNP_Grid_1km_2D/Data Fields/SensorZenith_1'

The data is saved to 'earthdata_sensor_data.csv'.

```python
# Specify the path to your HDF5 file
file_path = r'your_hdf5_file.h5'

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
