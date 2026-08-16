from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, field_validator
import joblib
import pandas as pd


app = FastAPI(
    title="Loan Default Prediction API",
    description="API for predicting loan default risk.",
    version="1.0.0"
)


# Load trained ML components
preprocessor = joblib.load("preprocessor.pkl")
random_forest = joblib.load("random_forest_model.pkl")
decision_threshold = joblib.load("decision_threshold.pkl")


# Request model
class LoanApplication(BaseModel):
    Age: int
    Income: int
    LoanAmount: int
    CreditScore: int
    MonthsEmployed: int
    NumCreditLines: int
    InterestRate: float
    LoanTerm: int
    DTIRatio: float
    Education: str
    EmploymentType: str
    MaritalStatus: str
    HasMortgage: str
    HasDependents: str
    LoanPurpose: str
    HasCoSigner: str
    LoanDate: str

    @field_validator("Education")
    @classmethod
    def validate_education(cls, value):
        allowed = ["Bachelor's", "High School", "Master's", "PhD"]

        if value not in allowed:
            raise ValueError(
                f"Education must be one of: {allowed}"
            )

        return value

    @field_validator("EmploymentType")
    @classmethod
    def validate_employment_type(cls, value):
        allowed = [
            "Full-time",
            "Part-time",
            "Self-employed",
            "Unemployed"
        ]

        if value not in allowed:
            raise ValueError(
                f"EmploymentType must be one of: {allowed}"
            )

        return value

    @field_validator("MaritalStatus")
    @classmethod
    def validate_marital_status(cls, value):
        allowed = [
            "Divorced",
            "Married",
            "Single"
        ]

        if value not in allowed:
            raise ValueError(
                f"MaritalStatus must be one of: {allowed}"
            )

        return value

    @field_validator(
        "HasMortgage",
        "HasDependents",
        "HasCoSigner"
    )
    @classmethod
    def validate_yes_no(cls, value):
        if value not in ["No", "Yes"]:
            raise ValueError(
                "Value must be either 'No' or 'Yes'"
            )

        return value

    @field_validator("LoanPurpose")
    @classmethod
    def validate_loan_purpose(cls, value):
        allowed = [
            "Auto",
            "Business",
            "Education",
            "Home",
            "Other"
        ]

        if value not in allowed:
            raise ValueError(
                f"LoanPurpose must be one of: {allowed}"
            )

        return value


# Response model
class PredictionResponse(BaseModel):
    message: str
    prediction: int
    result: str
    default_probability: float
    decision_threshold: float


# Home endpoint
@app.get("/")
def home():
    return {
        "message": "Loan Default Prediction API is running"
    }


# Prediction endpoint
@app.post(
    "/predict",
    response_model=PredictionResponse
)
def predict_loan(application: LoanApplication):

    data = application.model_dump()

    df = pd.DataFrame([data])

    # Convert LoanDate into datetime
    try:
        df["LoanDate"] = pd.to_datetime(df["LoanDate"])
    except Exception:
        raise HTTPException(
            status_code=400,
            detail="Invalid LoanDate. Please provide a valid date."
        )

    # Create date features
    df["LoanYear"] = df["LoanDate"].dt.year
    df["LoanMonth"] = df["LoanDate"].dt.month

    # Remove original date column
    df = df.drop(columns=["LoanDate"])

    # Preprocess input
    processed_data = preprocessor.transform(df)

    # Get default probability
    default_probability = random_forest.predict_proba(
        processed_data
    )[0][1]

    # Apply decision threshold
    prediction = int(
        default_probability >= decision_threshold
    )

    # Convert prediction to readable result
    result = (
        "Default"
        if prediction == 1
        else "No Default"
    )

    return {
        "message": "Prediction successful",
        "prediction": prediction,
        "result": result,
        "default_probability": round(
            default_probability * 100,
            2
        ),
        "decision_threshold": round(
            decision_threshold * 100,
            2
        )
    }