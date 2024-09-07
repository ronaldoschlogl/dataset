import os
import json
from PIL import Image
from datetime import datetime

base_dir = 'dataset'
output_file = 'dataset/metadata.json'

def extract_image_metadata(folder_path):
    metadata = []

    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png')):
            img_path = os.path.join(folder_path, filename)
            try:
                img = Image.open(img_path)
                img_metadata = {
                    "filename": filename,
                    "width": img.width,
                    "height": img.height,
                    "format": img.format,
                    "mode": img.mode,
                    "creation_time": datetime.fromtimestamp(os.path.getctime(img_path)).strftime('%Y-%m-%d %H:%M:%S'),
                    "last_modified_time": datetime.fromtimestamp(os.path.getmtime(img_path)).strftime('%Y-%m-%d %H:%M:%S'),
                    "size_kb": round(os.path.getsize(img_path) / 1024, 2),
                }
                metadata.append(img_metadata)
            except Exception as e:
                print(f"Erro ao processar {img_path}: {e}")
    return metadata


def generate_metadata_json(base_dir, output_file):
    all_metadata = []

    for root, dirs, files in os.walk(base_dir):
        print(f'Processando a pasta: {root}')
        metadata = extract_image_metadata(root)
        all_metadata.extend(metadata)

    with open(output_file, 'w') as json_file:
        json.dump(all_metadata, json_file, indent=4)

    print(f'Arquivo JSON de metadados gerado com sucesso: {output_file}')

generate_metadata_json(base_dir, output_file)