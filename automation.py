import requests
import os
from azure.storage.filedatalake import DataLakeServiceClient

#Azure configuration
STORAGE_ACCOUNT_NAME = os.getenv("STORAGE_ACCOUNT_NAME")
STORAGE_ACCOUNT_KEY = os.getenv("STORAGE_ACCOUNT_KEY")
FILE_SYSTEM_NAME = os.getenv("FILE_SYSTEM_NAME")


FILES = [
       {
        "folder_name": "netflix_cast",
        "file_name": "netflix_cast.csv",
        "github_url": "https://raw.githubusercontent.com/jimmymuthoni/Netflix-Azure-Data-Engineering-End-to-End-Project/refs/heads/main/Netflix%20data/netflix_cast.csv"
    },
    {
        "folder_name": "netflix_category",
        "file_name": "netflix_category.csv",
        "github_url": "https://raw.githubusercontent.com/jimmymuthoni/Netflix-Azure-Data-Engineering-End-to-End-Project/refs/heads/main/Netflix%20data/netflix_category.csv"
    },
    {
        "folder_name": "netflix_countries",
        "file_name": "netflix_countries.csv",
        "github_url": "https://raw.githubusercontent.com/jimmymuthoni/Netflix-Azure-Data-Engineering-End-to-End-Project/refs/heads/main/Netflix%20data/netflix_countries.csv"
    },
    {
        "folder_name": "netflix_directors",
        "file_name": "netflix_directors.csv",
        "github_url": "https://raw.githubusercontent.com/jimmymuthoni/Netflix-Azure-Data-Engineering-End-to-End-Project/refs/heads/main/Netflix%20data/netflix_directors.csv"
    }


]


def get_datalake_client():
    service_client = DataLakeServiceClient(account_url=f"https://{STORAGE_ACCOUNT_NAME}.dfs.core.windows.net",
        credential=STORAGE_ACCOUNT_KEY                                  
        )
    return service_client

def upload_file(service_client, folder_name, file_name, github_url):
    print("Uploading data from github to cloud")
    response = requests.get(github_url)
    response.raise_for_status()
    file_content = response.content

    fs_client = service_client.get_file_system_client(FILE_SYSTEM_NAME)
    dir_client = fs_client.get_directory_client(folder_name)
    dir_client.create_directory()

    file_client = dir_client.create_file(file_name)
    file_client.append_data(data=file_content, offset=0, length=len(file_content))
    file_client.flush_data(len(file_content))
    print(f"Uploaded to: {FILE_SYSTEM_NAME}/{folder_name}/{file_name}")

    #Entry point
if __name__ == "__main__":
    print("Uploading from GitHub to Azure Data Lake (bronze)...")
    client = get_datalake_client()
    for file_info in FILES:
        upload_file(
            client,
            folder_name=file_info['folder_name'],
            file_name=file_info['file_name'],
            github_url=file_info['github_url']
        )
