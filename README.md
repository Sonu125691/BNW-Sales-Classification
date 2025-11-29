# 🚗 BMW Car Sales Classification (2010–2024)

This project predicts whether BMW car sales between 2010–2024 will be **High** or **Low**.  
A total of **5 Machine Learning models** were trained, and the **best-performing model (Random Forest)** was selected and implemented in a **Streamlit application**.  
The model uses **10 features**: Model, Year, Region, Color, Fuel Type, Transmission, Engine Size (L), Mileage (KM), Price (USD), Sales Volume.


## 📌 Workflow
- Split data into **x_train, x_test** first (to avoid data leakage)
- **EDA done only on x_train**
- **One-Hot Encoding** for categorical columns
- **StandardScaler** applied for all features
- Trained **5 ML models** and compared performance
- **Random Forest Classifier** selected (**Train Accuracy** = 1.0, **Test Accuracy** = 1.0)


## 📌 Models Evaluated
- Logistic Regression  
- Decision Tree  
- Random Forest 
- XGBoost  
- Gaussian NB

## ▶️ Run the Project on Your Computer
To run this project locally, use the following commands in your terminal:

pip install -r requirements.txt
streamlit run app.py

These commands will install the required libraries and open the BMW Sales Classification app in your browser (running locally on your computer).
