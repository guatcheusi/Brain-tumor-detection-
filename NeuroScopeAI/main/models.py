import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from django.db import models
from django.core.files.storage import default_storage

# Charger le modèle CNN entraîné
model = tf.keras.models.load_model("main\\templates\model.h5")


# Create your models here.
# Create your models here.
class Image(models.Model):
    caption=models.CharField(max_length=100, null=True)
    image=models.ImageField(upload_to="img/%y")

    def __str__(self):
        return self.caption

    def model_prediction(self):
        # Charger et prétraiter l'image
        image = load_img(self.image.path, target_size=(150, 150))  # Ajuster la taille de l'image selon les besoins
        image_array = img_to_array(image)
        image_array = image_array.reshape((1, image_array.shape[0], image_array.shape[1], image_array.shape[2]))  # Ajouter une dimension pour la prédiction par lot
        image_array = image_array.astype('float32') / 255.0  # Normaliser les valeurs des pixels

        print("Charger et prétraiter l'image reussi")

        # Effectuer la prédiction
        prediction = model.predict(image_array)
        classes = ['Glioma', 'Meningioma', 'No Tumor', 'Pituitary']
        print("Effectuer la prédiction reussi")

        # Interpréter la prédiction
        classe_predite = np.argmax(prediction[0])
        print('Classe prédite :', classes[classe_predite])
        print([classes[classe_predite], np.round(prediction, 4)])
        
        return (classes[classe_predite], np.round(prediction, 4))

