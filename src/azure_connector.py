# src/azure_connector.py

"""
Upload local files (models, predictions, dashboards) to Azure Blob Storage.
Secured via environment variable loading (.env).
Requires: azure-storage-blob, python-dotenv
"""

import os
from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv

# 🔐 Load environment variables from .env file
load_dotenv()

# ⚙️ Settings
AZURE_CONNECTION_STRING = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
CONTAINER_NAME = "indigenous-fashion-data"

def upload_to_blob(local_file_path, blob_name=None):
    """
    Upload a file to Azure Blob Storage.
    Creates container if it doesn't exist.
    """
    if not AZURE_CONNECTION_STRING:
        print("⚠️ Azure connection string not set. Skipping upload.")
        return

    if not blob_name:
        blob_name = os.path.basename(local_file_path)

    try:
        # Connect to Blob Service
        blob_service_client = BlobServiceClient.from_connection_string(AZURE_CONNECTION_STRING)
        container_client = blob_service_client.get_container_client(CONTAINER_NAME)

        # Create container if not present
        if not container_client.exists():
            container_client.create_container()
            print(f"📦 Created container: {CONTAINER_NAME}")

        # Upload file
        with open(local_file_path, "rb") as data:
            container_client.upload_blob(name=blob_name, data=data, overwrite=True)

        print(f"✅ Uploaded: {local_file_path} → {CONTAINER_NAME}/{blob_name}")

    except Exception as e:
        print(f"❌ Upload failed: {e}")

# 🔁 Example usage
if __name__ == "__main__":
    # Optional: add your test files here
    test_files = [
        "models/rf_units_predictor.pkl",
        "outputs/predictions.csv"
    ]
    for file in test_files:
        if os.path.exists(file):
            upload_to_blob(file)
        else:
            print(f"⛔ File not found: {file}")
