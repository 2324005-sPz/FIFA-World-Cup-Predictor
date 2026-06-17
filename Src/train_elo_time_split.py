import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load dataset
df = pd.read_csv(
    "Data/Processed/ml_dataset_elo.csv"
)

# Features and target
X = df.drop("target", axis=1)
y = df["target"]

# Chronological split
# First 80% matches = training
# Last 20% matches = testing

split_index = int(len(df) * 0.8)

X_train = X.iloc[:split_index]
X_test = X.iloc[split_index:]

y_train = y.iloc[:split_index]
y_test = y.iloc[split_index:]

print(f"Training Matches: {len(X_train)}")
print(f"Testing Matches: {len(X_test)}")

# Model
model = RandomForestClassifier(
    n_estimators=200,
    random_state=42,
    n_jobs=-1
)

# Train
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(
    y_test,
    predictions
)

print("\n=================================")
print("TIME-BASED EVALUATION RESULTS")
print("=================================")
print(f"Accuracy: {accuracy:.4f}")

# Feature importance
importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": model.feature_importances_
})

print("\nFeature Importance:")
print(
    importance.sort_values(
        by="Importance",
        ascending=False
    )
)

# Detailed metrics
print("\nClassification Report:")
print(
    classification_report(
        y_test,
        predictions
    )
)