from PIL import Image
import os
import numpy as np

# lecture d'une image dans le dossier images/train

for file in os.listdir("images/train"):
    # si le fichier correspond au champignon 42, on ouvre l'image
    if file == "champignon_42.png":
        image = Image.open("images/train/" + file)
        image.show()
        # on ferme l'image
        image.close()

# lecture d'une image dans le dossier images/test
for file in os.listdir("images/test"):
    # si le fichier correspond au champignon 42, on ouvre l'image
    if file == "champignon_42.png":
        image = Image.open("images/test/" + file)
        image.show()
        # on ferme l'image
        image.close()

# on transforme l'image du champignon 42 de images/train en numpy array
image = Image.open("images/train/champignon_42.png")
image_array = np.array(image)

# on affiche les dimensions de l'image
print(image_array.shape)
# cela donne un triplet (hauteur, largeur, 3), 3 correspond aux 3 canaux (Rouge, Vert, Bleu)

# on affiche la valeur de l'image à la position (100, 100)
print(image_array[100, 100])
# cela donne un triplet (Rouge, Vert, Bleu)

# on affiche le triplet (Rouge, Vert, Bleu) situé au milieu de l'image
print(image_array[image_array.shape[0]//2, image_array.shape[1]//2])

def traiter_une_image(image_array):
    ### vous pouvez coder un traitement de l'image ici
    return

traiter_une_image(image_array)

# on ferme l'image
image.close()
