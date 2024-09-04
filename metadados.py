import os
import json
from PIL import Image
from datetime import datetime

def get_image_metadata(image_path):
    with Image.open(image_path) as img:
        metadata = {
            "filename": os.path.basename(image_path),
            "width": img.width,
            "height": img.height,
            "format": img.format,
            "mode": img.mode,
            "creation_time": datetime.fromtimestamp(os.path.getctime(image_path)).strftime('%Y-%m-%d %H:%M:%S'),
            "last_modified_time": datetime.fromtimestamp(os.path.getmtime(image_path)).strftime('%Y-%m-%d %H:%M:%S'),
            "size_kb": round(os.path.getsize(image_path) / 1024, 2)
        }
    return metadata

def create_metadata_file(image_paths, output_file):
    metadata_list = []
    
    for img_path in image_paths:
        metadata = get_image_metadata(img_path)
        metadata_list.append(metadata)
    
    with open(output_file, 'w') as f:
        json.dump(metadata_list, f, indent=4)
    
    print(f'Metadata file {output_file} created successfully!')

# Lista de caminhos para as imagens
image_paths = ['500x500/9-10-V1-W.png', '500x500/9-10-V2-W.png', '500x500/9-10-V1-B.png', '500x500/9-10-V2-B.png']
for i in range(0,9):
    image_paths.append(f'500x500/{i}-0{i+1}-V1-W.png')
    image_paths.append(f'500x500/{i}-0{i+1}-V2-W.png')
    image_paths.append(f'500x500/{i}-0{i+1}-V1-B.png')
    image_paths.append(f'500x500/{i}-0{i+1}-V2-B.png')

# Nome do arquivo de saída para os metadados
output_file = '500x500/metadata.json'

# Criar o arquivo de metadados
create_metadata_file(image_paths, output_file)