import os
from PIL import Image

base_dir = 'dataset' 
new_size = (128, 128)

def resize_images_in_folder(folder_path, new_size=(128, 128)):
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png')):
            img_path = os.path.join(folder_path, filename)
            try:
                img = Image.open(img_path)
                img_resized = img.resize(new_size)
                img_resized.save(img_path)
                print(f'Imagem {filename} redimensionada para {new_size} e salva em {img_path}')
            except Exception as e:
                print(f"Erro ao processar {img_path}: {e}")

def resize_images_in_directory(base_dir, new_size=(128, 128)):
    for root, dirs, files in os.walk(base_dir):
        for subdir in dirs:
            folder_path = os.path.join(root, subdir)
            print(f'Processando a pasta: {folder_path}')
            resize_images_in_folder(folder_path, new_size)
        
        print(f'Processando a pasta raiz: {root}')
        resize_images_in_folder(root, new_size)

resize_images_in_directory(base_dir, new_size)