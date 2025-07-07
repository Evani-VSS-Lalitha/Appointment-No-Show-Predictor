import streamlit as st
import pandas as pd
import plotly.express as px
from src.feature_engineering import preprocess
from src.model import load_model
from src.intervention import suggest_intervention

st.set_page_config(page_title="No-Show Predictor", layout="centered")

st.title("🩺 Appointment No-Show Predictor")
st.markdown("""
Upload appointment data to identify patients likely to miss their appointments
and see recommended intervention strategies.
""")

# Download sample template
with open("data/no_show.csv", "rb") as f:
    st.download_button("📥 Download Sample Template", f, "no_show.csv", "text/csv")

uploaded_file = st.file_uploader("📁 Upload Appointment CSV File", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.subheader("📄 Uploaded Data Preview")
    st.dataframe(df.head())

    try:
        model = load_model("model.pkl")
        processed_df = preprocess(df)
        X = processed_df.drop("No-show", axis=1)

        # Predict
        processed_df['risk_score'] = model.predict_proba(X)[:, 1]
        processed_df['intervention'] = processed_df['risk_score'].apply(suggest_intervention)

        # Display predictions
        st.subheader("📊 Prediction Results")
        st.dataframe(processed_df[['risk_score', 'intervention']].round(3))

        # KPI metrics
        st.subheader("📌 Key Metrics")
        st.metric("Total Appointments", len(df))
        high_risk_df = processed_df[processed_df['risk_score'] > 0.6]
        st.metric("High Risk Patients", len(high_risk_df))
        st.metric("Average Risk Score", round(processed_df['risk_score'].mean(), 2))

        # Intervention summary chart with Plotly
        st.subheader("📉 Intervention Summary")
        intervention_counts = processed_df['intervention'].value_counts().reset_index()
        intervention_counts.columns = ['Intervention', 'Count']
        fig = px.bar(intervention_counts, x='Intervention', y='Count', color='Intervention',
                     title='Intervention Strategy Distribution', template='plotly',
                     color_discrete_sequence=px.colors.qualitative.Pastel)
        st.plotly_chart(fig)

        # Filter high-risk patients
        st.subheader("🔥 High-Risk Patients (risk > 0.6)")
        st.dataframe(high_risk_df[['risk_score', 'intervention']].round(3))

        # Simulate sending SMS
        if st.button("🚀 Simulate Sending Reminders"):
            st.success(f"SMS sent to {len(high_risk_df)} high-risk patients.")

        # Download button
        csv = processed_df[['risk_score', 'intervention']].to_csv(index=False).encode('utf-8')
        st.download_button("⬇️ Download Predictions as CSV", data=csv, file_name="predictions.csv", mime='text/csv')

    except Exception as e:
        st.error(f"❌ Error during prediction: {e}")
else:
    st.info("Please upload a valid CSV file to begin.")