import os
import numpy as np
import matplotlib.pyplot as plt
from skimage import io, transform
from skimage.util import montage
from PIL import Image

# Caminho para o diretório que contém as pastas das classes
dataset_path = './500x500'  # Substitua pelo caminho real

# Verificar se o caminho existe
if not os.path.exists(dataset_path):
    raise ValueError(f'O caminho especificado não existe: {dataset_path}')

# Listar todas as subpastas (classes) no diretório do dataset
classes = [d for d in os.listdir(dataset_path) if os.path.isdir(os.path.join(dataset_path, d))]

print(f'Classes encontradas: {classes}')

def load_images_from_class(class_path, image_size=(128, 128), max_images=100):
    """
    Carrega e redimensiona imagens de uma classe específica.

    Args:
        class_path (str): Caminho para a pasta da classe.
        image_size (tuple): Tamanho para redimensionar as imagens (largura, altura).
        max_images (int): Número máximo de imagens a serem carregadas.

    Returns:
        list: Lista de arrays de imagens.
    """
    images = []
    count = 0
    for filename in os.listdir(class_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            img_path = os.path.join(class_path, filename)
            try:
                # Abrir a imagem e converter para RGB
                img = Image.open(img_path).convert('RGB')
                # Redimensionar a imagem
                img = img.resize(image_size)
                # Converter para array NumPy
                img = np.array(img)
                images.append(img)
                count += 1
                if count >= max_images:
                    break
            except Exception as e:
                print(f'Erro ao carregar {img_path}: {e}')
    return images

# Definindo o tamanho das imagens e o número máximo de imagens por classe para exibir
IMAGE_SIZE = (500, 500)  # Largura, Altura
MAX_IMAGES_PER_CLASS = 4  # Ajuste conforme necessário

# Dicionário para armazenar as montagens de cada classe
montages = {}

for classe in classes:
    print(f'Processando a classe: {classe}')
    class_path = os.path.join(dataset_path, classe)
    images = load_images_from_class(class_path, image_size=IMAGE_SIZE, max_images=MAX_IMAGES_PER_CLASS)
    
    if not images:
        print(f'Nenhuma imagem encontrada para a classe "{classe}".')
        continue
    
    # Converter a lista de imagens em um array NumPy
    images_array = np.array(images)
    
    # Criar a montagem
    print(f'Metadata file {images_array} created successfully!')
    montage_image = montage(images_array)
    
    # Armazenar a montagem no dicionário
    montages[classe] = montage_image
    
    print(f'Montagem para a classe "{classe}" criada com {len(images)} imagens.\n')

def display_montage(montage_image, title='Montagem', figsize=(10, 10)):
    """
    Exibe uma montagem de imagens.

    Args:
        montage_image (ndarray): Array da imagem da montagem.
        title (str): Título para a montagem.
        figsize (tuple): Tamanho da figura.
    """
    plt.figure(figsize=figsize)
    plt.imshow(montage_image)
    plt.title(title)
    plt.axis('off')
    plt.show()

for classe, montage_image in montages.items():
    display_montage(montage_image, title=f'Montagem da Classe: {classe}')
