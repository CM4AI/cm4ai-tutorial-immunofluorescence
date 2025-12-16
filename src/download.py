from pyDataverse.api import NativeApi, DataAccessApi
import zipfile
import os

cm4ai_doi = "doi:10.18130/V3/K7TGEM"
base_url = 'https://dataverse.lib.virginia.edu/'
output_dir = "data/raw"

os.makedirs(output_dir, exist_ok=True)

api = NativeApi(base_url)
data_api = DataAccessApi(base_url)

print("Downloading data set (this may take a while)...")
cm4ai_beta_dataset = api.get_dataset(cm4ai_doi)

files_list = cm4ai_beta_dataset.json()['data']['latestVersion']['files']
if_label = "Images"

for file in files_list:
    if "directoryLabel" in file and file["directoryLabel"] == if_label:
        file_id = file["dataFile"]["id"]
        filename = file["dataFile"]["filename"]
        output_path = os.path.join(output_dir, filename)
        
        if not os.path.exists(output_path):
            print(f" - Downloading {filename}")
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

duplicates = [
    "paclitaxel/red/B2AI_3_untreated_C2_R3_z01_red.jpg",
    "paclitaxel/blue/B2AI_3_untreated_C2_R3_z01_blue.jpg",
    "paclitaxel/green/B2AI_3_untreated_C2_R3_z01_green.jpg",
    "paclitaxel/yellow/B2AI_3_untreated_C2_R3_z01_yellow.jpg"
]

print("Patching data release for duplicates...")
for file in duplicates:
    file_path = os.path.join(output_dir, file)
    if os.path.exists(file_path):
        os.remove(file_path)

print(f"Complete! IF data extracted to: {output_dir}")
