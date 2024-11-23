from PIL import Image
import os

def images_to_pdf(image_folder, output_pdf):
    # Lista de imagens
    images = []
    
    # Carregar todas as imagens do diretório especificado
    for filename in os.listdir(image_folder):
        if filename.endswith((".png", ".jpg", ".jpeg")):
            img_path = os.path.join(image_folder, filename)
            img = Image.open(img_path).convert('RGB')
            images.append(img)
    
    # Verifica se há imagens para processar
    if images:
        # Salva as imagens como um arquivo PDF
        images[0].save(output_pdf, save_all=True, append_images=images[1:])
        print(f"PDF criado com sucesso: {output_pdf}")
    else:
        print("Nenhuma imagem encontrada.")

# Uso:
# images_to_pdf("caminho_para_pasta_com_imagens", "nome_do_arquivo.pdf")
images_to_pdf(r"C:\Users\cezar\OneDrive\Documentos\imagensProcesso", "documentosProcesso.pdf")

