import pandas as pd
import numpy as np
import pickle
import time
import matplotlib.pyplot as plt

from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.utils import to_categorical

# ===============================
# LOAD DATA
# ===============================
df = pd.read_csv("data/cybersecurity_attacks.csv")
df.dropna(inplace=True)

# ===============================
# FEATURES
# ===============================
features = ['Protocol', 'Packet Length', 'Packet Type',
            'Traffic Type', 'Severity Level', 'Anomaly Scores']
target = 'Attack Type'

df = df[features + [target]]

# ===============================
# ENCODING (FIXED)
# ===============================
encoders = {}

for col in df.select_dtypes(include='object').columns:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    encoders[col] = le

# SAVE encoders
pickle.dump(encoders, open("models/encoders.pkl", "wb"))

# ===============================
# SPLIT
# ===============================
X = df.drop(target, axis=1)
y = df[target]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ===============================
# SCALING
# ===============================
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# ===============================
# MULTIPLE MODELS
# ===============================
models = {
    "Random Forest": RandomForestClassifier(),
    "SVM": SVC(),
    "Logistic": LogisticRegression(max_iter=1000),
    "KNN": KNeighborsClassifier()
}

results = {}

print("\n--- MODEL PERFORMANCE ---")

for name, model in models.items():
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    acc = accuracy_score(y_test, pred)
    results[name] = acc
    print(name, ":", acc)

# ===============================
# BEST MODEL
# ===============================
best_model_name = max(results, key=results.get)
best_model = models[best_model_name]

print("Best Model:", best_model_name)

# ===============================
# ANN MODEL
# ===============================
y_train_cat = to_categorical(y_train)
y_test_cat = to_categorical(y_test)

ann = Sequential([
    Dense(128, activation='relu', input_shape=(X_train.shape[1],)),
    Dropout(0.3),
    Dense(64, activation='relu'),
    Dropout(0.2),
    Dense(y_train_cat.shape[1], activation='softmax')
])

ann.compile(optimizer='adam',
            loss='categorical_crossentropy',
            metrics=['accuracy'])

ann.fit(X_train, y_train_cat, epochs=10, batch_size=64)

# ===============================
# SAVE MODELS
# ===============================
pickle.dump(best_model, open("models/best_model.pkl", "wb"))
pickle.dump(scaler, open("models/scaler.pkl", "wb"))
ann.save("models/ann_model.h5")

print("✅ Models Saved Successfully")

# ===============================
# REAL-TIME SIMULATION (FIXED)
# ===============================
print("\n--- Real-Time Simulation ---")

for _ in range(5):
    sample = X_test[np.random.randint(0, len(X_test))].reshape(1, -1)
    pred = best_model.predict(sample)
    print("Live Prediction:", pred)
    time.sleep(2)