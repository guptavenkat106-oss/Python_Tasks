import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

# ==========================================
# STEP 1: LOAD AND CLEAN THE DATASET
# ==========================================
# Load the single CSV file from the directory
# Note: Ensure 'Churn_Modelling.csv' is in your working directory
df = pd.read_csv('Churn_Modelling.csv')

# Drop non-predictive metadata columns that don't help the model learn general rules
df.drop(['RowNumber', 'CustomerId', 'Surname'], axis=1, inplace=True)

print("--- Dataset Summary ---")
print(df.info())

# Check the distribution of the target variable to verify data imbalance
print("\n--- Target Variable Distribution (0 = Stayed, 1 = Left) ---")
print(df['Exited'].value_counts(normalize=True))

# ==========================================
# STEP 2: CATEGORICAL FEATURE ENCODING
# ==========================================
# Convert text columns (Geography, Gender) into numerical dummy variables
# drop_first=True prevents the dummy variable trap (multicollinearity)
df = pd.get_dummies(df, columns=['Geography', 'Gender'], drop_first=True)

# Separate independent features (X) and the dependent target variable (y)
X = df.drop('Exited', axis=1)
y = df['Exited']

# ==========================================
# STEP 3: TRAIN-TEST SPLIT & DATA SCALING
# ==========================================
# Split data: 80% for training and 20% for testing.
# stratify=y guarantees both parts get an equal 80/20 ratio of churned customers.
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Standardize feature scales (crucial for columns with large gaps like Age vs Balance)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# ==========================================
# STEP 4: MODEL TRAINING (HANDLING IMBALANCE)
# ==========================================
# Initialize Random Forest Classifier
# class_weight='balanced' forces the model to penalize mistakes heavier on the rare churn class
model = RandomForestClassifier(n_estimators=100, random_state=42, class_weight='balanced')
model.fit(X_train_scaled, y_train)

# ==========================================
# STEP 5: PREDICTIONS & TECHNICAL METRICS
# ==========================================
# Generate predictions on the unseen test set
predictions = model.predict(X_test_scaled)

print("\n--- Model Evaluation ---")
print("Confusion Matrix:")
print(confusion_matrix(y_test, predictions))

print("\nClassification Report:")
print(classification_report(y_test, predictions))

# ==========================================
# STEP 6: FEATURE IMPORTANCE EXTRACTION
# ==========================================
# Extract feature relative weights from the tree nodes
importances = model.feature_importances_
feature_names = X.columns
indices = np.argsort(importances)[::-1]

# Plot the features based on how heavily they drove customer turnover decisions
plt.figure(figsize=(10, 6))
sns.barplot(x=importances[indices], y=feature_names[indices], palette='viridis')
plt.title('Business Driver Analysis: What Influences Customer Churn?')
plt.xlabel('Relative Importance Score')
plt.ylabel('Features')
plt.tight_layout()
plt.show()