# Loan_Default_Prediction_System

An end-to-end Machine Learning application that predicts the likelihood of loan default using Random Forest, FastAPI, and Streamlit.

The project covers the complete Machine Learning workflow — from data auditing and exploratory analysis to feature engineering, model training, evaluation, API development, and deployment.

## 🚀 Live Application

**Streamlit Web Application:**  
[Loan Default Prediction System — Live Demo](https://loandefaultpredictionsystem-iabvjce8otqntp2stmvfw4.streamlit.app/)

**FastAPI Backend:**  
[Loan Default Prediction API](https://loan-default-api-t0dv.onrender.com)

The Streamlit application communicates with the deployed FastAPI backend to generate loan-default predictions.

## 🎯 Project Objective
The objective of this project is to identify applicants who may have a higher risk of loan default using financial, credit, employment, personal, and loan-related information.

The system provides:

- Default probability
- Default / No Default classification
- Decision-threshold-based prediction
- Interactive loan application form
- Risk visualization
- Prediction details

## 📊 Dataset

The dataset contains **255,347 loan records**.

**Target variable:** `Default`

- `0` → No Default
- `1` → Default

### Target Distribution

- No Default: approximately **88.4%**
- Default: approximately **11.6%**

The target variable is imbalanced, so model evaluation focuses on metrics beyond accuracy.
### Important Features

1. `Age`
2. `Income`
3. `LoanAmount`
4. `CreditScore`
5. `MonthsEmployed`
6. `NumCreditLines`
7. `InterestRate`
8. `LoanTerm`
9. `DTIRatio`
10. `Education`
11. `EmploymentType`
12. `MaritalStatus`
13. `HasMortgage`
14. `HasDependents`
15. `LoanPurpose`
16. `HasCoSigner`
17. `LoanDate`

The target variable is imbalanced, so evaluation focuses on metrics beyond accuracy.

## 🔄 Project Workflow

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

## 🔍 Data Analysis & Feature Engineering

The project includes:

- Data quality and structure analysis
- Missing-value checks
- Duplicate checks
- Numerical and categorical analysis
- Target distribution analysis
- Distribution and relationship analysis
- Outlier analysis
- Loan date feature extraction
- Feature preprocessing

### Preprocessing

Numerical features are standardized using `StandardScaler`.

Categorical features are encoded using `OneHotEncoder` with:

```text
handle_unknown="ignore"
```


## 🤖 Model Development

Two classification models were explored:

1. Logistic Regression
2. Random Forest Classifier

The final application uses a **Random Forest Classifier**.

### Random Forest Configuration

```text
n_estimators = 200
max_depth = 12
class_weight = "balanced"
random_state = 42
n_jobs = -1
```

The `class_weight="balanced"` setting helps address the imbalanced target variable.

### Train/Test Split

- Training records: **204,277**
- Testing records: **51,070**

##  Model Evaluation

The models were evaluated using:

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC
- Classification Report

Accuracy alone is not sufficient because the dataset contains significantly more non-default cases than default cases.

Detailed model evaluation is available in `05_Model_Evaluation.ipynb`.

### 🎚️ Decision Threshold

The Random Forest model generates a probability of default.

The probability is compared against a saved decision threshold:

```text
Probability ≥ Threshold
        ↓
     Default

Probability < Threshold
        ↓
   No Default
```

### Saved Machine Learning Components

The trained system uses the following serialized components:

- `preprocessor.pkl`
- `random_forest_model.pkl`
- `decision_threshold.pkl`

These files allow the deployed application to generate predictions without retraining the model.

## ⚡FastAPI Backend

The backend is implemented using FastAPI in:

`app.py`

### Endpoint

`POST /predict`

### The API

- Receives loan application data
- Validates input using Pydantic
- Converts the input into a DataFrame
- Processes `LoanDate`
- Creates `LoanYear` and `LoanMonth`
- Applies the saved preprocessing pipeline
- Generates default probability
- Applies the decision threshold
- Returns the prediction result

### API Response

The response includes:

- `prediction`
- `default_probability`
- `decision_threshold`
- `result`

### API Documentation

The FastAPI application provides interactive Swagger documentation through:

`/docs`

The deployed API is hosted separately from the Streamlit frontend.


## 🖥️ Streamlit Application

The frontend is implemented using streamlit_app.py.
The application provides a multi-step loan application workflow:

```text
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
```

### Features

- Multi-step form
- Input validation
- Persistent form information
- Section-level Edit buttons
- Application review
- Default probability visualization
- Decision threshold comparison
- Final Default / No Default decision
- Prediction details

The Streamlit frontend sends the completed application to the FastAPI `/predict` endpoint and displays the returned prediction.

## 🏗️ Application Architecture

The application follows a simple end-to-end prediction architecture:

```text
                    User
                      │
                      ▼
            ┌──────────────────┐
            │    Streamlit     │
            │    Frontend      │
            └────────┬─────────┘
                     │
                     │ HTTP POST
                     ▼
            ┌──────────────────┐
            │     FastAPI      │
            │     /predict     │
            └────────┬─────────┘
                     │
                     ▼
            ┌──────────────────┐
            │   Preprocessor   │
            │      .pkl        │
            └────────┬─────────┘
                     │
                     ▼
            ┌──────────────────┐
            │  Random Forest   │
            │      Model       │
            └────────┬─────────┘
                     │
                     ▼
             Default Probability
                     │
                     ▼
             Decision Threshold
                     │
                     ▼
               Final Prediction
```

The Streamlit frontend collects the loan application information and sends it to the FastAPI `/predict` endpoint. The FastAPI backend applies the saved preprocessing pipeline and Random Forest model, generates the default probability, applies the decision threshold, and returns the final prediction.


## 📁 Project Structure
```text
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
```

## 🛠️ Technologies Used

### Programming & Data Analysis

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn

### Machine Learning

- Scikit-learn
- Joblib

### Backend

- FastAPI
- Pydantic
- Uvicorn

### Frontend

- Streamlit

### Development & Version Control

- Jupyter Notebook
- Git
- GitHub

## 🚀 Deployment

The project uses a two-part deployment architecture:

```text
Streamlit Cloud
      │
      ▼
Streamlit Frontend
      │
      │ HTTP Request
      ▼
Render
      │
      ▼
FastAPI Backend
      │
      ▼
Machine Learning Model
```

The frontend and backend are deployed independently and communicate through the FastAPI REST API.

## 🧪 Testing

The deployed system was tested through:

- FastAPI Swagger documentation
- Streamlit application
- Multiple loan application input sets
- Comparison of API and Streamlit prediction results
- Fresh-browser/Incognito testing

The same input submitted through the API and Streamlit application produces the corresponding prediction through the same FastAPI/ML prediction pipeline.

## 📌 Outcome

The project delivers a complete end-to-end Loan Default Prediction System combining:

**Machine Learning + Model Serialization + FastAPI + Streamlit + Cloud Deployment**

The final application can accept loan application information, estimate the probability of default, apply a decision threshold, and present the final risk classification through an interactive web interface.

