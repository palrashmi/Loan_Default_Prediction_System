\# 🏦 Loan Default Analysis \& Prediction System 



A complete end-to-end machine learning application for analyzing loan data and predicting whether a loan applicant is likely to default.



The project combines \*\*Exploratory Data Analysis, Feature Engineering, Machine Learning, FastAPI, and Streamlit\*\* into a single application.



\---



\## 📌 Project Overview



Loan default prediction is an important problem in the financial domain. Incorrectly approving high-risk applicants can result in financial losses, while rejecting low-risk applicants can lead to missed opportunities.



This project analyzes historical loan data and builds a machine learning model that predicts the probability of loan default for a new applicant.



The final system provides:



\- 📊 Exploratory data analysis

\- 🔧 Feature engineering

\- 🤖 Machine learning-based prediction

\- 🚀 FastAPI backend

\- 🎨 Streamlit frontend

\- ✅ Form validation

\- 📈 Default probability

\- ⚖️ Decision-threshold-based classification



\---



\## 🎯 Problem Statement



The objective of this project is to predict whether a loan applicant is likely to default based on financial, credit, employment, and personal information.



The model predicts:



\- `0` → No Default

\- `1` → Default



In addition to the final classification, the application returns the estimated probability of default.



\---



\## 📂 Dataset



The project uses a loan default dataset containing applicant and loan-related information.



Important features include:



\- Age

\- Income

\- Loan Amount

\- Credit Score

\- Months Employed

\- Number of Credit Lines

\- Interest Rate

\- Loan Term

\- DTI Ratio

\- Education

\- Employment Type

\- Marital Status

\- Mortgage Status

\- Dependents

\- Loan Purpose

\- Co-Signer Status

\- Loan Date



The original dataset is included in the project for analysis and reproducibility.



\---



\## 🔍 Exploratory Data Analysis



The EDA stage was used to understand:



\- Dataset structure

\- Missing values

\- Data types

\- Numerical distributions

\- Categorical distributions

\- Target-class distribution

\- Relationships between features

\- Potential patterns associated with loan defaults



The target variable is imbalanced, with the majority of applications belonging to the non-default class.



\---



\## 🔧 Feature Engineering



The preprocessing pipeline includes:



\### Numerical Features



Numerical variables are standardized using:



`StandardScaler`



\### Categorical Features



Categorical variables are converted using:



`OneHotEncoder`



with:



```text

handle\_unknown="ignore"


```



## 🛠️ Tech Stack



\- \*\*Python\*\* — Programming language

\- \*\*Pandas, NumPy\*\* — Data analysis

\- \*\*Matplotlib, Seaborn\*\* — Data visualization

\- \*\*Scikit-learn\*\* — Machine learning

\- \*\*FastAPI\*\* — Prediction API

\- \*\*Streamlit\*\* — Web application

\- \*\*Joblib\*\* — Model serialization

\- \*\*Jupyter Notebook\*\* — Analysis and experimentation

\- \*\*Git \& GitHub\*\* — Version control


## 📂 Project Structure



```text

Loan\_Default\_Analysis/

├── 01\_Data\_Audit.ipynb

├── 02\_EDA.ipynb

├── 03\_Feature\_Engineering.ipynb

├── 04\_Model\_Training.ipynb

├── 05\_Model\_Evaluation.ipynb

├── app.py

├── streamlit\_app.py

├── preprocessor.pkl

├── random\_forest\_model.pkl

├── decision\_threshold.pkl

├── Loan\_default.csv

├── requirements.txt

├── README.md

└── .gitignore


