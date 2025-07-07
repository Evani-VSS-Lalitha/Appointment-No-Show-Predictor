import pandas as pd
from sklearn.model_selection import train_test_split
from src.feature_engineering import preprocess
from src.model import train_model
from imblearn.over_sampling import SMOTE

# Step 1: Load dataset
df = pd.read_csv("data/no_show.csv")

# Step 2: Preprocess
df = preprocess(df)

# Step 3: Split features and label
X = df.drop("No-show", axis=1)
y = df["No-show"]

# Step 4: Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 5 (Optional): Handle class imbalance with SMOTE
smote = SMOTE(random_state=42)
X_train, y_train = smote.fit_resample(X_train, y_train)

# Step 6: Train and save model
train_model(X_train, y_train, save_path="model.pkl")

print("Model trained and saved to model.pkl")
