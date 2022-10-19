# load env

## environment variables defined inside a .env file

````
GCP_PROJECT_ID=my-project-id
SERVICE_ACCOUNT_FILE=path/to/serviceAccountCredentials
STORAGE_BUCKET_NAME=my-super-important-data
````

## example

````
import os
from dotenv import load_dotenv

load_dotenv()

GCP_PROJECT_ID = os.getenv('GCP_PROJECT_ID')
SERVICE_ACCOUNT_FILE = os.getenv('SERVICE_ACCOUNT_FILE')
STORAGE_BUCKET_NAME = os.getenv('STORAGE_BUCKET_NAME')
````

## load from path

````
from dotenv import load_dotenv
from pathlib import Path

dotenv_path = Path('path/to/.env')
load_dotenv(dotenv_path=dotenv_path)
````
