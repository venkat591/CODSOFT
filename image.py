import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.applications import InceptionV3
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Embedding, LSTM, Dense
from tensorflow.keras.utils import to_categorical
from PIL import Image
import numpy as np

# Load the pre-trained InceptionV3 model to extract image features
image_model = InceptionV3(include_top=False, weights='imagenet')

# Remove the classification layers
new_input = image_model.input
hidden_layer = image_model.layers[-1].output
image_features_extract_model = Model(inputs=new_input, outputs=hidden_layer)

# Preprocess the image and extract features
def preprocess_image(image_path):
    img = Image.open(image_path)
    img = img.resize((299, 299))
    img = keras.applications.inception_v3.preprocess_input(np.array(img))
    img = np.expand_dims(img, axis=0)
    return img

# Load your dataset and preprocess it
# This should include image file paths and corresponding captions

# Tokenize captions
tokenizer = Tokenizer()
tokenizer.fit_on_texts(your_captions)
total_words = len(tokenizer.word_index) + 1

# Create sequences of tokens
input_sequences = []
for caption in your_captions:
    sequence = tokenizer.texts_to_sequences([caption])[0]
    for i in range(1, len(sequence)):
        n_gram_sequence = sequence[:i+1]
        input_sequences.append(n_gram_sequence)

# Pad sequences
max_sequence_length = max([len(seq) for seq in input_sequences])
input_sequences = pad_sequences(input_sequences, maxlen=max_sequence_length, padding='pre')

# Create inputs and targets
X, y = input_sequences[:, :-1], input_sequences[:, -1]
y = to_categorical(y, num_classes=total_words)

# Define and compile the RNN model
model = keras.Sequential()
model.add(Embedding(total_words, 256, input_length=max_sequence_length - 1))
model.add(LSTM(256))
model.add(Dense(total_words, activation='softmax'))

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train the model on your dataset
model.fit(X, y, epochs=50, verbose=1)

# Function to generate captions for images
def generate_caption(image_path):
    img = preprocess_image(image_path)
    features = image_features_extract_model.predict(img)

    caption = []
    for _ in range(max_sequence_length):
        sequence = tokenizer.texts_to_sequences([caption])[0]
        sequence = pad_sequences([sequence], maxlen=max_sequence_length-1, padding='pre')
        predicted_word_index = np.argmax(model.predict(sequence, verbose=0), axis=-1)
        predicted_word = [word for word, index in tokenizer.word_index.items() if index == predicted_word_index]
        caption.extend(predicted_word)
        if predicted_word == '<end>':
            break

    return ' '.join(caption)

# Use the generate_caption function to get a caption for an image
image_path = 'your_image.jpg'
caption = generate_caption(image_path)
print('Generated Caption:', caption)
