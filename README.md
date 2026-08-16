# Loan_Default_Prediction_System
End-to-end loan default prediction system using Machine Learning, Random Forest, FastAPI, and Streamlit.

# Loan Default Prediction System

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


