# Loan_Default_Prediction_System
End-to-end loan default prediction system using Machine Learning, Random Forest, FastAPI, and Streamlit.


An end-to-end Machine Learning application that analyzes historical loan data and predicts whether a new loan applicant is likely to default.

The project covers the complete workflow from data analysis and feature engineering to model training, evaluation, API development, and an interactive Streamlit application.

## Project Objective

The objective is to identify applicants with a higher risk of loan default using financial, credit, employment, personal, and loan-related information.

The system provides:

- Default probability
- Default / No Default classification
- Decision-threshold-based prediction
- Interactive loan application form

## Dataset

- 255,347 loan records
- Target: `Default`
- `0` → No Default
- `1` → Default
- No Default: approximately 88.4%
- Default: approximately 11.6%

Important features include:

`Age`, `Income`, `LoanAmount`, `CreditScore`, `MonthsEmployed`, `NumCreditLines`, `InterestRate`, `LoanTerm`, `DTIRatio`, `Education`, `EmploymentType`, `MaritalStatus`, `HasMortgage`, `HasDependents`, `LoanPurpose`, `HasCoSigner`, and `LoanDate`.

The target variable is imbalanced, so evaluation focuses on metrics beyond accuracy.

## Project Workflow

```text
Raw Dataset
     ↓
Data Audit
     ↓
Exploratory Data Analysis
     ↓
Feature Engineering
     ↓
Preprocessing
     ↓
Model Training
     ↓
Model Evaluation
     ↓
Model Serialization
     ↓
FastAPI Backend
     ↓
Streamlit Frontend
     ↓
Loan Default Prediction
```
# Data Analysis & Feature Engineering

The project includes:

Data quality and structure analysis
Missing-value and duplicate checks
Numerical and categorical analysis
Target distribution analysis
Distribution and relationship analysis
Outlier analysis
Loan date feature extraction
Preprocessing

Numerical features are standardized using StandardScaler.

Categorical features are encoded using OneHotEncoder with:

handle_unknown="ignore"

18 original features → 33 processed features

The preprocessing pipeline is fitted only on the training data and then applied to the test data.

# Model Development

Two classification models were explored:
1.Logistic Regression
2.Random Forest

The final application uses Random Forest Classifier.

Random Forest Configuration
n_estimators = 200
max_depth = 12
class_weight = "balanced"
random_state = 42
n_jobs = -1

The class_weight="balanced" setting helps handle the imbalanced target variable.

Train/Test Data
Training records: 204,277
Testing records:   51,070

# Model Evaluation

The models were evaluated using:
Accuracy
Precision
Recall
F1 Score
ROC-AUC
Classification Report

Accuracy alone is not sufficient because the dataset contains significantly more non-default cases than default cases.
Detailed evaluation is available in: 05_Model_Evaluation.ipynb

# Decision Threshold

The Random Forest generates a probability of default.
The probability is compared with a saved decision threshold:

1.Probability ≥ Threshold → Default
2.Probability < Threshold → No Default

This allows the final classification to be based on the selected risk threshold rather than relying only on the model's default classification.

# Saved Machine Learning Components
preprocessor.pkl
random_forest_model.pkl
decision_threshold.pkl

These files allow the trained system to be reused without retraining the model.

# FastAPI Backend

The backend is implemented using FastAPI in app.py.
POST /predict

The API:

Receives loan application data
Validates input using Pydantic
Converts the input into a DataFrame
Processes LoanDate
Creates LoanYear and LoanMonth
Applies the saved preprocessing pipeline
Generates default probability
Applies the decision threshold
Returns the prediction result

The response includes:

prediction
result
default_probability
decision_threshold

Interactive API documentation is available at: http://127.0.0.1:8000/docs

# Streamlit Application

The frontend is implemented using streamlit_app.py.
The application provides a multi-step loan application workflow:

Applicant Details
      ↓
Education & Employment
      ↓
Personal Details
      ↓
Loan Details
      ↓
Application Review
      ↓
Prediction

# Features include:

Multi-step form
Input validation
Persistent form information
Section-level Edit buttons
Application review
Default probability visualization
Decision threshold comparison
Final Default / No Default decision
Prediction details

The Streamlit frontend communicates with the FastAPI backend to obtain predictions.

# Project Structure
Loan_Default_Prediction_System/
│
├── 01_Data_Audit.ipynb
├── 02_EDA.ipynb
├── 03_Feature_Engineering.ipynb
├── 04_Model_Training.ipynb
├── 05_Model_Evaluation.ipynb
│
├── app.py
├── streamlit_app.py
│
├── preprocessor.pkl
├── random_forest_model.pkl
├── decision_threshold.pkl
│
├── Loan_default.csv
├── requirements.txt
├── README.md
└── .gitignore

# Technologies Used

Python
Pandas
NumPy
Matplotlib
Seaborn
Scikit-learn
Joblib
FastAPI
Pydantic
Uvicorn
Streamlit
Jupyter Notebook
Git & GitHub

# Outcome

The project delivers a complete end-to-end loan default prediction system that connects:
Machine Learning + Model Serialization + FastAPI + Streamlit

to provide an interactive application capable of estimating loan default risk and producing a final risk classification.

