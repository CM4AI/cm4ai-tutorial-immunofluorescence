from pyDataverse.api import NativeApi, DataAccessApi
import zipfile
import os

cm4ai_beta_doi = "doi:10.18130/V3/B35XWX"
base_url = 'https://dataverse.lib.virginia.edu/'
output_dir = "data/raw"

os.makedirs(output_dir, exist_ok=True)

api = NativeApi(base_url)
data_api = DataAccessApi(base_url)

print("Downloading data set (this may take a while)...")
cm4ai_beta_dataset = api.get_dataset(cm4ai_beta_doi)

files_list = cm4ai_beta_dataset.json()['data']['latestVersion']['files']
if_label = "Protein Localization Subcellular Images"

for file in files_list:
    if file["directoryLabel"] == if_label:
        file_id = file["dataFile"]["id"]
        filename = file["dataFile"]["filename"]
        output_path = os.path.join(output_dir, filename)
        
        if not os.path.exists(output_path):
            print(f" - Downloading {file}")
            response = data_api.get_datafile(file_id, is_pid=False)
            
            with open(output_path, "wb") as f:
                f.write(response.content)

print("Download complete, extracing archives...")
for filename in os.listdir(output_dir):
    if filename.endswith('.zip'):
        zip_path = os.path.join(output_dir, filename)
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(output_dir)
        os.remove(zip_path)

print(f"Complete! IF data extracted to: {output_dir}")
