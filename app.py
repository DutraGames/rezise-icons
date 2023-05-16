from PIL import Image
import time
import os

contador = 1

max = int(input("Digite o max de imagens que ira redimensionar: "))

while (contador <= max):
    # solicitar o caminho da imagem original
    imagem_original = input("Digite o caminho da imagem original: ")

    # abrir a imagem
    imagem = Image.open(imagem_original)

    pasta = os.path.basename(imagem_original).split('.')[0]

    # cria a pasta para armazenar as imagens redimensionadas
    if not os.path.isdir('icones'):
        os.mkdir('icones')
    print('Pasta Icones criada!')

    if not os.path.isdir('icones/' + pasta):
        os.mkdir('icones/' + pasta)
    print('Pasta ' + pasta + ' criada!')

    pasta_new = os.path.join(os.path.dirname(__file__), pasta)
    print('caminho: ' + pasta_new)

    # redimensionar para 1024x1024
    imagem_red = imagem.resize((1024, 1024))
    imagem_red.save('icones/' + pasta + '/icon_1024.jpg')
    print("A imagem 1024x1024 foi criada em: " + pasta_new)

    # redimensionar para 512x512
    imagem_red = imagem.resize((512, 512))
    imagem_red.save('icones/' + pasta + '/icon_512.jpg')
    print("A imagem 512x512 foi criada em: " + pasta_new)

    # redimensionar para 256x256
    imagem_red = imagem.resize((256, 256))
    imagem_red.save('icones/' + pasta + '/icon_256.jpg')
    print("A imagem 256x256 foi criada em: " + pasta_new)

    # redimensionar para 128x128
    imagem_red = imagem.resize((128, 128))
    imagem_red.save('icones/' + pasta + '/icon_128.jpg')
    print("A imagem 128x128 foi criada em: " + pasta_new)

    # redimensionar para 114x114
    imagem_red = imagem.resize((114, 114))
    imagem_red.save('icones/' + pasta + '/icon_114.jpg')
    print("A imagem 114x114 foi criada em: " + pasta_new)

    # redimensionar para 64x64
    imagem_red = imagem.resize((64, 64))
    imagem_red.save('icones/' + pasta + '/icon_64.jpg')
    print("A imagem 64x64 foi criada em: " + pasta_new)

    # redimensionar para 32x32
    imagem_red = imagem.resize((32, 32))
    imagem_red.save('icones/' + pasta + '/icon_32.jpg')
    print("A imagem 32x32 foi criada em: " + pasta_new)

    # redimensionar para 16x16
    imagem_red = imagem.resize((16, 16))
    imagem_red.save('icones/' + pasta + '/icon_16.jpg')
    print("A imagem 16x16 foi criada em: " + pasta_new)
    contador = contador+1
    time.sleep(1)
    os.system('cls')

input("Pressione qualquer tecla para sair...")
