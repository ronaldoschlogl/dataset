from PIL import Image
import os

def resize_and_crop(image, target_width, target_height):
    img_width, img_height = image.size
    
    # Calcular a proporção para redimensionar a imagem sem distorção
    aspect_ratio = min(target_width/img_width, target_height/img_height)
    new_width = int(img_width * aspect_ratio)
    new_height = int(img_height * aspect_ratio)
    
    # Redimensionar a imagem
    image = image.resize((new_width, new_height))
    
    # Cortar a imagem centralizando-a
    left = (new_width - target_width) / 2
    top = (new_height - target_height) / 2
    right = (new_width + target_width) / 2
    bottom = (new_height + target_height) / 2
    
    image = image.crop((left, top, right, bottom))
    
    return image

def process_images(image_paths, output_folder, target_width, target_height):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        
    for img_path in image_paths:
        with Image.open(img_path) as img:
            # Redimensionar e cortar a imagem
            processed_img = resize_and_crop(img, target_width, target_height)
            
            # Salvar a imagem processada
            img_name = os.path.basename(img_path)
            processed_img.save(os.path.join(output_folder, img_name))
            print(f'Imagem {img_name} processada e salva em {output_folder}')

# Lista de caminhos para as imagens a serem processadas
image_paths = ['9-10-V2-W.png', '9-10-V1-W.png', '9-10-V2-B.png', '9-10-V1-B.png']


# Diretório de saída para as imagens processadas
output_folder = 'caminho'

# Dimensões alvo (Largura e Altura)
target_width = 500
target_height = 500

# Processar as imagens
process_images(image_paths, output_folder, target_width, target_height)