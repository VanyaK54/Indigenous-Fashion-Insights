# src/image_classifier.py

"""
CNN classifier for Indigenous fashion pattern recognition
Supports training with MobileNetV2 and Grad-CAM for interpretability
"""

import os
import tensorflow as tf
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.preprocessing import image
import numpy as np

# Constants
IMG_SIZE = (224, 224)
BATCH_SIZE = 16
NUM_CLASSES = 5  # e.g., Metis_Sash, Navajo_Weave, Haida_Formline, Cree_Beadwork, Inuit_Tapestry

# 🔄 Image augmentation and loader
train_dir = "data/raw/images/train"
val_dir = "data/raw/images/val"

train_datagen = ImageDataGenerator(
    rescale=1./255, rotation_range=20, zoom_range=0.2,
    width_shift_range=0.2, height_shift_range=0.2, horizontal_flip=True
)

val_datagen = ImageDataGenerator(rescale=1./255)

train_gen = train_datagen.flow_from_directory(
    train_dir, target_size=IMG_SIZE, batch_size=BATCH_SIZE, class_mode='categorical'
)

val_gen = val_datagen.flow_from_directory(
    val_dir, target_size=IMG_SIZE, batch_size=BATCH_SIZE, class_mode='categorical'
)

# 🧠 Build model
base_model = MobileNetV2(include_top=False, input_shape=IMG_SIZE + (3,), weights='imagenet')
x = base_model.output
x = GlobalAveragePooling2D()(x)
x = Dense(128, activation='relu')(x)
predictions = Dense(NUM_CLASSES, activation='softmax')(x)

model = Model(inputs=base_model.input, outputs=predictions)

# 🔒 Freeze base model layers
for layer in base_model.layers:
    layer.trainable = False

# ⚙️ Compile
model.compile(optimizer=Adam(learning_rate=1e-4),
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# 🎯 Train
model.fit(train_gen, validation_data=val_gen, epochs=5)

# 💾 Save model
model.save("models/indigenous_pattern_cnn.h5")
print("✅ Saved model to models/indigenous_pattern_cnn.h5")
