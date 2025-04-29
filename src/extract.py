import os
import requests

# Function to download a file from a URL and save it to a local path
def download_file(url, local_path):
    """
    Downloads a file from a given URL and saves it to the specified local path.

    Args:
        url (str): The URL of the file to download.
        local_path (str): The local path where the file will be saved.

    Returns:
        None
    """
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Raise an error for bad responses

        with open(local_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)

        print(f"Downloaded {url} to {local_path}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to download {url}: {e}")

url = "https://www.kaggle.com/api/v1/datasets/download/rutuspatel/walmart-dataset-retail"
data_dir = "data"
download_file(url, os.path.join(data_dir, "Walmart_Store_sales.csv"))

# Function to extract data from a CSV file
def extract_data(file_path):
    """
    Extracts data from a CSV file.

    Args:
        file_path (str): The path to the CSV file.

    Returns:
        list: A list of dictionaries representing the rows in the CSV file.
    """
    data = []
    try:
        with open(file_path, 'r') as file:
            headers = file.readline().strip().split(',')
            for line in file:
                values = line.strip().split(',')
                row = dict(zip(headers, values))
                data.append(row)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")

    return data