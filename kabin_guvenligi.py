import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow import keras

# Veri setini yükle
train_data = pd.read_csv("train_data.csv")
test_data = pd.read_csv("test_data.csv")

# Veri setlerini işleme
train_data = train_data.drop(columns=["PassengerId", "Name", "Ticket", "Cabin"])
train_data = pd.get_dummies(train_data, columns=["Sex", "Embarked"])

test_data = test_data.drop(columns=["PassengerId", "Name", "Ticket", "Cabin"])
test_data = pd.get_dummies(test_data, columns=["Sex", "Embarked"])

# Modeli oluşturma
model = keras.Sequential([
    keras.layers.Dense(32, activation="relu", input_shape=[10]),
    keras.layers.Dense(16, activation="relu"),
    keras.layers.Dense(1, activation="sigmoid")
])

model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])

# Modeli eğitme
model.fit(train_data.drop(columns=["Survived"]), train_data["Survived"], epochs=10)

# Modeli değerlendirme
test_loss, test_acc = model.evaluate(test_data.drop(columns=["Survived"]), test_data["Survived"])
print("Test accuracy:", test_acc)
