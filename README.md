# 🩺 Appointment No-Show Predictor

This project predicts which patients are likely to **miss their medical appointments** and recommends **intervention strategies** such as SMS reminders or cab offers to reduce no-show rates.

---

## 📌 Problem Statement

No-shows in healthcare cause wasted time, money, and missed care opportunities.  
This system uses machine learning to:
- Predict appointment attendance
- Suggest personalized interventions

---

## 🚀 Features

- ✅ Predicts **no-show probability** using appointment and patient data
- 🧠 Built with a **Random Forest Classifier**
- 📲 Recommends interventions (e.g., SMS reminders, transportation)
- 💻 Clean **Streamlit frontend** for interaction
- 📁 CSV file upload and download support

---

## 📁 Project Structure

```

Appointment-No-Show-Predictor/
├── app.py                  # Streamlit frontend app
├── train\_model.py          # ML model training script
├── model.pkl               # Trained model file
├── requirements.txt        # Dependencies
├── output\_predictions.csv  # Output with predictions
├── data/
│   └── sample\_no\_show\_template.csv
└── src/
├── feature\_engineering.py
├── model.py
└── intervention.py

````

---

## ⚙️ How to Run the Project Locally

### 1. Clone the repository

```bash
git clone https://github.com/Evani-VSS-Lalitha/Appointment-No-Show-Predictor.git
cd Appointment-No-Show-Predictor
````

### 2. (Optional) Create a virtual environment

```bash
python -m venv venv
# Activate on Windows:
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit app

```bash
streamlit run app.py
```

---

## 📥 Sample Data

Use the provided CSV template for testing:

```
data/no_show.csv
```

Upload it using the Streamlit interface.

---

## 📤 Output

After upload:

* View individual risk scores and interventions
* Download a full prediction report
* View visual summaries and high-risk flags

---

## 🛠 Tech Stack

* Python 3.9+
* scikit-learn
* pandas
* imbalanced-learn (SMOTE)
* Streamlit
* joblib

---

## 📊 Future Enhancements

* SMS or Email reminder integration
* Admin dashboard for patient management
* Time series modeling for seasonal trends

---

## 🙋‍♀️ Author

**Evani VSS Lalitha**
📫 [GitHub](https://github.com/Evani-VSS-Lalitha)

---
