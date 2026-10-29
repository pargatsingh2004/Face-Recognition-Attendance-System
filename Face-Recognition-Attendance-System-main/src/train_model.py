import cv2
import numpy as np
import os

recognizer = cv2.face.LBPHFaceRecognizer_create()

dataset_path = "dataset"

faces = []
labels = []

for user_folder in os.listdir(dataset_path):
    if user_folder.startswith("user_"):
        user_id = int(user_folder.split("_")[1])
        folder_path = os.path.join(dataset_path, user_folder)

        for image_name in os.listdir(folder_path):
            img_path = os.path.join(folder_path, image_name)

            img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

            if img is None:
                continue

            faces.append(img)
            labels.append(user_id)

print("Total faces:", len(faces))

if len(faces) == 0:
    print("No data found!")
    exit()

recognizer.train(faces, np.array(labels))

os.makedirs("trainer", exist_ok=True)
recognizer.save("trainer/trainer.yml")

print("Model trained successfully!")