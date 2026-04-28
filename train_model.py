import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
import os

print("🛡️ Initializing Project Sentinel AI Core...")

# 1. Generate Synthetic Training Data (Hackathon workaround)
# We simulate 1000 past shipments. 
# Each shipment has a sequence of 5 days of "Risk Scores" (0 to 10).
num_samples = 1000
time_steps = 5
features = 1

print("Generating historical sequence data...")
X_train = np.random.rand(num_samples, time_steps, features) * 10

# The target (Y) is the delay in hours. 
# We build a logical correlation: Higher risk scores in the sequence = longer delay.
y_train = np.sum(X_train, axis=1) * (np.random.rand(num_samples, 1) * 0.5 + 0.5)

# 2. Build the LSTM Neural Network
print("Compiling LSTM Architecture...")
model = Sequential([
    LSTM(32, activation='relu', input_shape=(time_steps, features), return_sequences=False),
    Dropout(0.2),
    Dense(16, activation='relu'),
    Dense(1, activation='linear') # Linear output because we are predicting a continuous number (hours)
])

model.compile(optimizer='adam', loss='mse', metrics=['mae'])

# 3. Train the Model
print("Training the Predictive Engine...")
# We use a small number of epochs so it trains in seconds during your build
model.fit(X_train, y_train, epochs=10, batch_size=32, verbose=1)

# 4. Save the Model
model.save("sentinel_lstm.h5")
print("\n✅ Model successfully trained and saved as 'sentinel_lstm.h5'")
print("Ready for Streamlit integration.")