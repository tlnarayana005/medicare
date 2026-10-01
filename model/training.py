import numpy as np
import pandas as pd
import joblib as jb
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# Load and preprocess data
df = pd.read_csv('./Training.csv')
X = df.iloc[:, 0:132]
Y = df['prognosis']
le = LabelEncoder()
Y = le.fit_transform(Y)

# Train-test split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Train Random Forest model with 100 estimators
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, Y_train)

# Predict and evaluate
Y_pred = model.predict(X_test)
accuracy = accuracy_score(Y_test, Y_pred)

print(f"The accuracy of the model is {accuracy:.4f}")
print("\nClassification Report:")
print(classification_report(Y_test, Y_pred))

# Save model
jb.dump(model, 'diseasepred.pkl')
print("Model saved successfully")
