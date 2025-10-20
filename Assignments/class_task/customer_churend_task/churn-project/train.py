import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score
import joblib
import os
import json

# ========== 1️⃣ Load Dataset ==========
df = pd.read_csv('/Users/macbook/Desktop/AI/ai-ml-navttc-course/Assignments/class_task/customer_churend_task/churn-project/data/customer_churn_dataset-testing-master.csv')

# Drop non-predictive ID columns
if 'CustomerID' in df.columns:
    df = df.drop(columns=['CustomerID'])

# ========== 2️⃣ Encode Categorical Columns ==========
label_encoders = {}
categorical_cols = ['Gender', 'Subscription Type', 'Contract Length']

for col in categorical_cols:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le

# ========== 3️⃣ Split Data ==========
X = df.drop('Churn', axis=1)
y = df['Churn']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ========== 4️⃣ Train Model ==========
model = XGBClassifier(
    n_estimators=200,
    learning_rate=0.1,
    max_depth=6,
    subsample=0.8,
    colsample_bytree=0.8,
    random_state=42,
    enable_categorical=False
)
model.fit(X_train, y_train)

# ========== 5️⃣ Evaluate Model ==========
y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print(f"✅ Model Accuracy: {acc * 100:.2f}%")

# ========== 6️⃣ Save Model, Encoders, and Feature Names ==========
os.makedirs("models", exist_ok=True)
joblib.dump(model, "models/best_model.joblib")
joblib.dump(label_encoders, "models/label_encoders.joblib")

# Save feature list
feature_list = list(X.columns)
with open("models/feature_names.json", "w") as f:
    json.dump(feature_list, f)

print("✅ Model, encoders, and feature list saved successfully!")
