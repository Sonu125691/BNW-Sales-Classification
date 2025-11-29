# 🚗 BMW Car Sales Classification (2010–2024)

This project predicts whether BMW Car sales classification in 2010-2024 is **High** or **Low**. 
The model is implemented as a **Streamlit app**

## 📌 Workflow
- Split data into **x_train, x_test** first (to avoid data leakage)
- **EDA done only on x_train**
- **One-Hot Encoding** for categorical columns
- **StandardScaler** applied for all features
- Trained **5 ML models** and compared performance
- **Random Forest Classifier** selected (**Train Accuracy** = 1.0, **Test Accuracy** = 1.0)

## 🤖 Models Evaluated
- Logistic Regression  
- Decision Tree  
- Random Forest 
- XGBoost  
- Gaussian NB
