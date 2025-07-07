import pandas as pd
from src.feature_engineering import preprocess
from src.model import load_model
from src.intervention import suggest_intervention

# Load trained model
model = load_model()

# Load and preprocess data
df = pd.read_csv("data/no_show.csv")
df = preprocess(df)

# Drop target column
X = df.drop("No-show", axis=1)

# Predict risk scores
df['risk_score'] = model.predict_proba(X)[:, 1]
df['intervention'] = df['risk_score'].apply(suggest_intervention)

# Print all risk scores and interventions
print("\n Full Predictions:")
print(df[['risk_score', 'intervention']].head())

# Filter only high-risk patients
high_risk = df[df['risk_score'] > 0.6]
print("\n High-Risk Patients (risk_score > 0.6):")
print(high_risk[['risk_score', 'intervention']])

# Export to CSV
df[['risk_score', 'intervention']].to_csv("output_predictions.csv", index=False)
print("\nPredictions exported to output_predictions.csv")
