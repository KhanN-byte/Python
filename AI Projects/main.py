import cv2
import os
import pandas as pd
from deepface import DeepFace

IMAGE_DIR = "/Users/Desktop/Pictures"

data = {
    "Name": [],
    "Age": [],
    "Gender": [],
    "Race": [],
    "Emotion": []
}

for file in os.listdir(IMAGE_DIR):
    if not file.lower().endswith((".jpg", ".jpeg", ".png")):
        continue

    img_path = os.path.join(IMAGE_DIR, file)
    img = cv2.imread(img_path)

    if img is None:
        print(f"Could not read image: {file}")
        continue

    try:
        result = DeepFace.analyze(
            img_path=img,
            actions=("age", "gender", "race", "emotion"),
            enforce_detection=False
        )

        analysis = result[0]

        data["Name"].append(os.path.splitext(file)[0])
        data["Age"].append(analysis.get("age"))
        data["Gender"].append(analysis.get("dominant_gender"))
        data["Race"].append(analysis.get("dominant_race"))
        data["Emotion"].append(analysis.get("dominant_emotion"))

        print(f"Processed {file}")

    except Exception as e:
        print(f"Error processing {file}: {e}")

df = pd.DataFrame(data)
print(df)

df.to_csv("people.csv", index=False)