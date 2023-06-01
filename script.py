import os
import re

# Remplacer par le chemin vers votre dossier 'images'
images_dir = 'images'

# Parcourir tous les sous-dossiers dans le dossier 'images'
for folder_name in os.listdir(images_dir):
    # Ignorer les fichiers, ne traiter que les dossiers
    if os.path.isdir(os.path.join(images_dir, folder_name)):
        # Utiliser les expressions régulières pour trouver la partie du nom du dossier qui nous intéresse
        match = re.search(r'n\d+-([a-zA-Z_]+)', folder_name)
        if match:
            # Le nom de la race du chien est le premier groupe capturant dans l'expression régulière
            new_folder_name = match.group(1)
            # Créer le chemin complet vers l'ancien et le nouveau dossier
            old_folder_path = os.path.join(images_dir, folder_name)
            new_folder_path = os.path.join(images_dir, new_folder_name)
            # Renommer l'ancien dossier avec le nouveau nom
            os.rename(old_folder_path, new_folder_path)