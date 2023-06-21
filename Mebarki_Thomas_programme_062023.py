import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import cv2
import numpy as np
from joblib import load
import tensorflow as tf
from PIL import Image, ImageOps
from skimage import img_as_float
from skimage.restoration import denoise_nl_means



# Fonctions de traitement d'image
def apply_autocontrast(image):
    pil_image = Image.fromarray((image * 255).astype(np.uint8))
    autocontrasted_image = ImageOps.autocontrast(pil_image)
    return np.array(autocontrasted_image) / 255.0

def apply_equalization(image):
    pil_image = Image.fromarray((image * 255).astype(np.uint8))
    equalized_image = ImageOps.equalize(pil_image)
    return np.array(equalized_image) / 255.0

def apply_nl_means_denoising(image):
    image_float = img_as_float(image)
    denoised_image = denoise_nl_means(image_float, h=0.08, fast_mode=True, patch_size=5, patch_distance=3, channel_axis=-1)
    return denoised_image

# Charger les modèles enregistrés
model_resnet_transfert = tf.keras.models.load_model('models/resnet50v2_model.h5')
svm = load('models/svm.joblib')
le = load('models/label_encoder.joblib')

def predict_dog_breed(image):
      # Redimensionner et normaliser l'image
      image = cv2.resize(image, (224, 224))
      image = image / 255.0

      # Appliquer d'autres prétraitements si nécessaire
      image = apply_autocontrast(image)
      image = apply_equalization(image)
      image = apply_nl_means_denoising(image)
      
      # Utiliser le modèle ResNet pour extraire les caractéristiques
      features = model_resnet_transfert.predict(np.expand_dims(image, axis=0))

      # Obtenir les probabilités de chaque classe
      probabilities = svm.predict_proba(features)[0]

      # Obtenir les indices des 3 classes avec les plus hautes probabilités
      top_indices = np.argsort(probabilities)[-3:][::-1]

      # Afficher les 3 races les plus probables avec leurs probabilités
      print("Les 3 races les plus probables sont:")
      for index in top_indices:
            breed = le.inverse_transform([index])[0]
            proba = probabilities[index]
            print(f"{breed} ({proba:.2f})")


# Demander à l'utilisateur d'entrer le chemin de l'image
image_path = input("Veuillez entrer le chemin vers l'image: ")

# Charger l'image
image = cv2.imread(image_path)

# Prédire la race du chien dans l'image
predict_dog_breed(image)
