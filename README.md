# 💳 Credit Risk Prediction from Financial Data

A machine learning project to predict whether an individual is **High Risk** or **Low Risk** based on their financial and personal details.  
The project uses classification algorithms (Logistic Regression, XGBoost, Random Forest) with feature engineering and scaling.

---

## 🚀 Workflow

1. **Dataset** – Includes financial and personal details like income, debt, credit score, education, marital status, etc.  
2. **Preprocessing** – Handles categorical variables (one-hot encoding), scales numerical features.  
3. **Modeling** – Logistic Regression, Random Forest, and XGBoost are tested.  
4. **Evaluation** – Accuracy, Recall, F1-Score, ROC-AUC, and Confusion Matrix.  
5. **Deployment** – Interactive Streamlit app for real-time credit risk prediction.

---

## 📂 Repository Structure
```bash
Credit_Risk_Prediction/
├── data/                        # sample dataset(s)
├── notebooks/                   # training & experiments
├── models/                      # trained ML pipeline
├── app.py                       # Streamlit app
├── requirements.txt             # dependencies
└── README.md
````


🌐 Streamlit App

The app lets you enter details like Income, Debt, Credit Score, Employment Status, etc., and predicts:

✅ High Risk
✅ Low Risk

Run the app locally:

streamlit run app.py

📦 Installation

Clone the repo:

git clone https://github.com/<your-username>/Credit_Risk_Prediction.git
cd Credit_Risk_Prediction
pip install -r requirements.txt

📊 Example Output

Accuracy: 85%

F1-Score: 0.82

Confusion Matrix:

	Predicted Low	Predicted High
Actual Low	450	50
Actual High	70	430
🔮 Future Improvements

Add explainable AI (SHAP/LIME) to interpret model predictions.

Deploy on Streamlit Cloud / Heroku / AWS.

Enhance dataset with more diverse financial records.

🙌 Credits

Developed by Sikandar Ali
📌 AI & ML Engineer | Deep Learning | Computer Vision | Data Science
