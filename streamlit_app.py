import streamlit as st
import requests
from datetime import date


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Loan Default Prediction",
    page_icon="💰",
    layout="wide"
)


# =========================================================
# API CONFIGURATION
# =========================================================

API_URL = "https://loan-default-api-t0dv.onrender.com/predict"


# =========================================================
# SESSION STATE
# =========================================================

if "step" not in st.session_state:
    st.session_state.step = 1

if "completed_steps" not in st.session_state:
    st.session_state.completed_steps = set()

if "applicant" not in st.session_state:
    st.session_state.applicant = None

if "employment" not in st.session_state:
    st.session_state.employment = None

if "personal" not in st.session_state:
    st.session_state.personal = None

if "loan" not in st.session_state:
    st.session_state.loan = None

if "prediction_result" not in st.session_state:
    st.session_state.prediction_result = None




# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown(
    """
    <style>

    /* =====================================================
       MAIN PAGE
       ===================================================== */

    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1400px;
    }


    /* =====================================================
       STEP TRACKER
       ===================================================== */

    .step-container {
        display: flex;
        width: 100%;
        gap: 14px;
        margin: 30px 0 18px 0;
        align-items: stretch;
    }


    /* =====================================================
       STEP BOX
       ===================================================== */

    .step-box {
        flex: 1;
        height: 92px;
        padding: 10px 8px;
        border-radius: 12px;
        text-align: center;
        box-sizing: border-box;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        transition: all 0.2s ease;
    }


    /* =====================================================
       COMPLETED
       ===================================================== */

    .step-box.completed {
        border: 2px solid #22c55e;
        background: rgba(34, 197, 94, 0.08);
    }


    /* =====================================================
       CURRENT
       ===================================================== */

    .step-box.current {
        border: 2px solid #3b82f6;
        background: rgba(59, 130, 246, 0.10);
        box-shadow: 0 0 0 2px rgba(59, 130, 246, 0.08);
    }


    /* =====================================================
       UPCOMING
       ===================================================== */

    .step-box.upcoming {
        border: 1px solid #4b5563;
        background: rgba(255, 255, 255, 0.025);
    }


    /* =====================================================
       STEP CIRCLE
       ===================================================== */

    .step-circle {
        width: 34px;
        height: 34px;
        min-width: 34px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 14px;
        font-weight: 700;
        margin-bottom: 5px;
    }


    /* Completed circle */

    .step-circle.completed {
        background: #22c55e;
        color: white;
    }


    /* Current circle */

    .step-circle.current {
        background: #3b82f6;
        color: white;
    }


    /* Upcoming circle */

    .step-circle.upcoming {
        background: #374151;
        color: #d1d5db;
    }


    /* =====================================================
       STEP TITLE
       ===================================================== */

    .step-title {
        font-size: 12px;
        font-weight: 700;
        line-height: 1.15;
    }


    .step-title.completed {
        color: #4ade80;
    }


    .step-title.current {
        color: #60a5fa;
    }


    .step-title.upcoming {
        color: #9ca3af;
    }


    /* =====================================================
       STEP STATUS
       ===================================================== */

    .step-status {
        margin-top: 3px;
        font-size: 10px;
    }


    .step-status.completed {
        color: #4ade80;
    }


    .step-status.current {
        color: #60a5fa;
    }


    .step-status.upcoming {
        color: #6b7280;
    }


    /* =====================================================
       SECTION CARD
       ===================================================== */

    .info-card {
        padding: 20px;
        border-radius: 14px;
        border: 1px solid #374151;
        background: rgba(255, 255, 255, 0.025);
        margin-bottom: 18px;
    }


    /* =====================================================
       REVIEW ITEM
       ===================================================== */


    .review-item {
    padding: 18px;
    border-radius: 12px;
    border: 1px solid #374151;
    background: rgba(255, 255, 255, 0.025);
    margin-bottom: 10px;
    }

    .review-label {
        font-size: 12px;
        color: #9ca3af;
        margin-bottom: 3px;
    }

    .review-value {
        font-size: 16px;
        font-weight: 600;
        color: #f3f4f6;
        margin-bottom: 15px;
    }


    /* =====================================================
       RESULT CARD
       ===================================================== */

    .result-card {
        padding: 25px;
        border-radius: 16px;
        border: 1px solid #374151;
        background: rgba(255, 255, 255, 0.03);
        margin-top: 20px;
    }


    /* =====================================================
       RESPONSIVE
       ===================================================== */

    @media (max-width: 900px) {

        .step-container {
            flex-direction: column;
        }

        .step-box {
            min-height: 95px;
        }
    }

    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# PAGE HEADER
# =========================================================

st.title("💰 Loan Default Prediction")

st.write(
    "Complete the loan application below to assess the "
    "applicant's default risk."
)


# =========================================================
# STEP DEFINITIONS
# =========================================================

steps = [
    "Applicant",
    "Education & Employment",
    "Personal",
    "Loan Details",
    "Review & Prediction"
]

current_step = st.session_state.step
completed_steps = st.session_state.completed_steps


# =========================================================
# STEP TRACKER
# =========================================================

step_html = '<div class="step-container">'

for i, step_name in enumerate(steps, start=1):

    # ---------------------------------------------
    # COMPLETED
    # ---------------------------------------------

    if i in completed_steps:

        box_class = "completed"
        circle_class = "completed"
        title_class = "completed"
        status_class = "completed"

        circle_content = "✓"
        status = "Completed"

    # ---------------------------------------------
    # CURRENT
    # ---------------------------------------------

    elif i == current_step:

        box_class = "current"
        circle_class = "current"
        title_class = "current"
        status_class = "current"

        circle_content = str(i)
        status = "Current"

    # ---------------------------------------------
    # UPCOMING
    # ---------------------------------------------

    else:

        box_class = "upcoming"
        circle_class = "upcoming"
        title_class = "upcoming"
        status_class = "upcoming"

        circle_content = str(i)
        status = "Upcoming"

    step_html += f"""
<div class="step-box {box_class}">
    <div class="step-circle {circle_class}">{circle_content}</div>
    <div class="step-title {title_class}">{step_name}</div>
    <div class="step-status {status_class}">{status}</div>
</div>
"""

step_html += "</div>"


# IMPORTANT:
# Use st.html() instead of st.markdown()
# so Streamlit renders the HTML directly.

st.html(step_html)


st.caption(
    f"Step {current_step} of {len(steps)} — "
    f"{steps[current_step - 1]}"
)

st.divider()

# =========================================================
# STEP 1 — APPLICANT DETAILS
# =========================================================

if current_step == 1:

    st.header("👤 Applicant Details")

    st.write(
        "Please provide the applicant's basic financial "
        "and credit information."
    )

    # Load previously saved Step 1 data
    saved_applicant = st.session_state.applicant or {}

    col1, col2 = st.columns(2)

    with col1:

        age = st.number_input(
            "Age",
            min_value=18,
            max_value=100,
            value=saved_applicant.get("Age"),
            step=1,
            placeholder="Enter age"
        )

        age_error = st.empty()

        income = st.number_input(
            "Annual Income",
            min_value=0,
            value=saved_applicant.get("Income"),
            step=1000,
            placeholder="Enter annual income"
        )

        income_error = st.empty()

        credit_score = st.number_input(
            "Credit Score",
            min_value=300,
            max_value=850,
            value=saved_applicant.get("CreditScore"),
            step=1,
            placeholder="Enter credit score"
        )

        credit_score_error = st.empty()

    with col2:

        months_employed = st.number_input(
            "Months Employed",
            min_value=0,
            value=saved_applicant.get("MonthsEmployed"),
            step=1,
            placeholder="Enter months employed"
        )

        months_employed_error = st.empty()

        num_credit_lines = st.number_input(
            "Number of Credit Lines",
            min_value=0,
            value=saved_applicant.get("NumCreditLines"),
            step=1,
            placeholder="Enter number of credit lines"
        )

        num_credit_lines_error = st.empty()

    st.divider()

    # =====================================================
    # CONTINUE BUTTON
    # =====================================================

    if st.button(
        "Continue →",
        use_container_width=True,
        type="primary"
    ):

        # Clear previous error messages
        age_error.empty()
        income_error.empty()
        credit_score_error.empty()
        months_employed_error.empty()
        num_credit_lines_error.empty()

        # Track whether validation failed
        validation_failed = False

        
        # VALIDATE AGE

        if age is None:

            age_error.error(
                "This field is required."
            )

            validation_failed = True

        
        # VALIDATE INCOME
        

        if income is None:

            income_error.error(
                "This field is required."
            )

            validation_failed = True

        
        # VALIDATE CREDIT SCORE

        if credit_score is None:

            credit_score_error.error(
                "This field is required."
            )

            validation_failed = True

        
        # VALIDATE MONTHS EMPLOYED

        if months_employed is None:

            months_employed_error.error(
                "This field is required."
            )

            validation_failed = True

        
        # VALIDATE CREDIT LINES

        if num_credit_lines is None:

            num_credit_lines_error.error(
                "This field is required."
            )

            validation_failed = True

        # =================================================
        # MOVE TO STEP 2 ONLY IF VALID
        # =================================================

        if not validation_failed:

            st.session_state.applicant = {
                "Age": age,
                "Income": income,
                "CreditScore": credit_score,
                "MonthsEmployed": months_employed,
                "NumCreditLines": num_credit_lines
            }

            st.session_state.completed_steps.add(1)
            st.session_state.step = 2

            st.rerun()


# =========================================================
# STEP 2 — EDUCATION & EMPLOYMENT
# =========================================================

elif current_step == 2:

    st.header("🎓 Education & Employment")

    st.write(
        "Provide the applicant's education and employment details."
    )

    # Load previously saved Step 2 data
    saved_employment = st.session_state.employment or {}

    col1, col2 = st.columns(2)

    with col1:

        education_options = [
            "Select education",
            "Bachelor's",
            "High School",
            "Master's",
            "PhD"
        ]

        # Load previously saved education
        saved_education = saved_employment.get("Education")

        if saved_education in education_options:
            education_index = education_options.index(
                saved_education
            )
        else:
            education_index = 0

        education = st.selectbox(
            "Education",
            education_options,
            index=education_index
        )

        education_error = st.empty()

    with col2:

        employment_options = [
            "Select employment type",
            "Full-time",
            "Part-time",
            "Self-employed",
            "Unemployed"
        ]

        # Load previously saved employment type
        saved_employment_type = saved_employment.get(
            "EmploymentType"
        )

        if saved_employment_type in employment_options:
            employment_type_index = employment_options.index(
                saved_employment_type
            )
        else:
            employment_type_index = 0

        employment_type = st.selectbox(
            "Employment Type",
            employment_options,
            index=employment_type_index
        )

        employment_type_error = st.empty()

    st.divider()

    # =====================================================
    # ACTION BUTTONS
    # =====================================================

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "← Back",
            use_container_width=True
        ):
             

            # Save current Step 2 values before going back
            st.session_state.employment = {
                "Education": education,
                "EmploymentType": employment_type
                }

            st.session_state.step = 1
            st.rerun()

    with col2:

        if st.button(
            "Continue →",
            use_container_width=True,
            type="primary"
        ):

            # Clear previous errors
            education_error.empty()
            employment_type_error.empty()

            # Track validation status
            validation_failed = False

            # =================================================
            # VALIDATE EDUCATION
            # =================================================

            if education == "Select education":

                education_error.error(
                    "This field is required."
                )

                validation_failed = True

            # =================================================
            # VALIDATE EMPLOYMENT TYPE
            # =================================================

            if employment_type == "Select employment type":

                employment_type_error.error(
                    "This field is required."
                )

                validation_failed = True

            # =================================================
            # MOVE TO STEP 3 ONLY IF VALID
            # =================================================

            if not validation_failed:

                st.session_state.employment = {
                    "Education": education,
                    "EmploymentType": employment_type
                }

                st.session_state.completed_steps.add(2)
                st.session_state.step = 3

                st.rerun()

# =========================================================
# STEP 3 — PERSONAL DETAILS
# =========================================================

elif current_step == 3:

    st.header("🧑 Personal Details")

    st.write(
        "Provide information about the applicant's "
        "personal financial situation."
    )

    # Load previously saved Step 3 data
    saved_personal = st.session_state.personal or {}

    col1, col2 = st.columns(2)

    with col1:

        marital_status = st.selectbox(
            "Marital Status",
            [
                "Select",
                "Divorced",
                "Married",
                "Single"
            ],
            index=(
                [
                    "Select",
                    "Divorced",
                    "Married",
                    "Single"
                ].index(
                    saved_personal.get("MaritalStatus", "Select")
                )
            )
        )

        marital_status_error = st.empty()

        has_mortgage = st.selectbox(
            "Has Mortgage?",
            [
                "Select",
                "No",
                "Yes"
            ],
            index=(
                [
                    "Select",
                    "No",
                    "Yes"
                ].index(
                    saved_personal.get("HasMortgage", "Select")
                )
            )
        )

        has_mortgage_error = st.empty()

    with col2:

        has_dependents = st.selectbox(
            "Has Dependents?",
            [
                "Select",
                "No",
                "Yes"
            ],
            index=(
                [
                    "Select",
                    "No",
                    "Yes"
                ].index(
                    saved_personal.get("HasDependents", "Select")
                )
            )
        )

        has_dependents_error = st.empty()

        has_cosigner = st.selectbox(
            "Has Co-Signer?",
            [
                "Select",
                "No",
                "Yes"
            ],
            index=(
                [
                    "Select",
                    "No",
                    "Yes"
                ].index(
                    saved_personal.get("HasCoSigner", "Select")
                )
            )
        )

        has_cosigner_error = st.empty()

    st.divider()

    # =====================================================
    # ACTION BUTTONS
    # =====================================================

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "← Back",
            use_container_width=True
        ):

            # Save current Step 3 values before going back
            st.session_state.personal = {
                "MaritalStatus": marital_status,
                "HasMortgage": has_mortgage,
                "HasDependents": has_dependents,
                "HasCoSigner": has_cosigner
            }

            st.session_state.step = 2
            st.rerun()

    with col2:

        if st.button(
            "Continue →",
            use_container_width=True,
            type="primary"
        ):

            # Clear previous errors
            marital_status_error.empty()
            has_mortgage_error.empty()
            has_dependents_error.empty()
            has_cosigner_error.empty()

            # Track validation status
            validation_failed = False

            # =================================================
            # VALIDATE MARITAL STATUS
            # =================================================

            if marital_status == "Select":

                marital_status_error.error(
                    "This field is required."
                )

                validation_failed = True

            # =================================================
            # VALIDATE MORTGAGE
            # =================================================

            if has_mortgage == "Select":

                has_mortgage_error.error(
                    "This field is required."
                )

                validation_failed = True

            # =================================================
            # VALIDATE DEPENDENTS
            # =================================================

            if has_dependents == "Select":

                has_dependents_error.error(
                    "This field is required."
                )

                validation_failed = True

            # =================================================
            # VALIDATE CO-SIGNER
            # =================================================

            if has_cosigner == "Select":

                has_cosigner_error.error(
                    "This field is required."
                )

                validation_failed = True

            # =================================================
            # MOVE TO STEP 4 ONLY IF VALID
            # =================================================

            if not validation_failed:

                st.session_state.personal = {
                    "MaritalStatus": marital_status,
                    "HasMortgage": has_mortgage,
                    "HasDependents": has_dependents,
                    "HasCoSigner": has_cosigner
                }

                st.session_state.completed_steps.add(3)
                st.session_state.step = 4

                st.rerun()

# =========================================================
# STEP 4 — LOAN DETAILS
# =========================================================

elif current_step == 4:

    st.header("🏦 Loan Details")

    st.write(
        "Provide information about the requested loan."
    )

    # Load previously saved Step 4 data
    saved_loan = st.session_state.loan or {}

    col1, col2 = st.columns(2)

    with col1:

        loan_amount = st.number_input(
            "Loan Amount",
            min_value=0,
            value=saved_loan.get("LoanAmount"),
            step=1000,
            placeholder="Enter loan amount"
        )

        loan_amount_error = st.empty()

        interest_rate = st.number_input(
            "Interest Rate (%)",
            min_value=0.0,
            max_value=100.0,
            value=saved_loan.get("InterestRate"),
            step=0.1,
            placeholder="Enter interest rate"
        )

        interest_rate_error = st.empty()

        loan_term = st.number_input(
            "Loan Term (months)",
            min_value=1,
            value=saved_loan.get("LoanTerm"),
            step=1,
            placeholder="Enter loan term"
        )

        loan_term_error = st.empty()

    with col2:

        dti_ratio = st.number_input(
            "DTI Ratio",
            min_value=0.0,
            max_value=10.0,
            value=saved_loan.get("DTIRatio"),
            step=0.01,
            placeholder="Enter DTI ratio"
        )

        dti_ratio_error = st.empty()

        loan_purpose_options = [
            "Select loan purpose",
            "Auto",
            "Business",
            "Education",
            "Home",
            "Other"
        ]

        saved_loan_purpose = saved_loan.get(
            "LoanPurpose",
            "Select loan purpose"
        )

        loan_purpose = st.selectbox(
            "Loan Purpose",
            loan_purpose_options,
            index=loan_purpose_options.index(
                saved_loan_purpose
            )
        )

        loan_purpose_error = st.empty()

        # Restore previously saved date
        saved_loan_date = saved_loan.get("LoanDate")

        if saved_loan_date:
            saved_date = date.fromisoformat(saved_loan_date)
        else:
            saved_date = None

        loan_date = st.date_input(
            "Loan Date",
            value=saved_date
        )

        loan_date_error = st.empty()

    st.divider()

    # =====================================================
    # ACTION BUTTONS
    # =====================================================

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "← Back",
            use_container_width=True
        ):

            # Save current Step 4 values before going back
            st.session_state.loan = {
                "LoanAmount": loan_amount,
                "InterestRate": interest_rate,
                "LoanTerm": loan_term,
                "DTIRatio": dti_ratio,
                "LoanPurpose": loan_purpose,
                "LoanDate": (
                    loan_date.isoformat()
                    if loan_date is not None
                    else None
                )
            }

            st.session_state.step = 3
            st.rerun()

    with col2:

        if st.button(
            "Review Application →",
            use_container_width=True,
            type="primary"
        ):

            # Clear previous errors
            loan_amount_error.empty()
            interest_rate_error.empty()
            loan_term_error.empty()
            dti_ratio_error.empty()
            loan_purpose_error.empty()
            loan_date_error.empty()

            # Track validation status
            validation_failed = False

            # =================================================
            # VALIDATE LOAN AMOUNT
            # =================================================

            if loan_amount is None:

                loan_amount_error.error(
                    "This field is required."
                )

                validation_failed = True

            # =================================================
            # VALIDATE INTEREST RATE
            # =================================================

            if interest_rate is None:

                interest_rate_error.error(
                    "This field is required."
                )

                validation_failed = True

            # =================================================
            # VALIDATE LOAN TERM
            # =================================================

            if loan_term is None:

                loan_term_error.error(
                    "This field is required."
                )

                validation_failed = True

            # =================================================
            # VALIDATE DTI RATIO
            # =================================================

            if dti_ratio is None:

                dti_ratio_error.error(
                    "This field is required."
                )

                validation_failed = True

            # =================================================
            # VALIDATE LOAN PURPOSE
            # =================================================

            if loan_purpose == "Select loan purpose":

                loan_purpose_error.error(
                    "This field is required."
                )

                validation_failed = True

            # =================================================
            # VALIDATE LOAN DATE
            # =================================================

            if loan_date is None:

                loan_date_error.error(
                    "This field is required."
                )

                validation_failed = True

            # =================================================
            # MOVE TO STEP 5 ONLY IF VALID
            # =================================================

            if not validation_failed:

                st.session_state.loan = {
                    "LoanAmount": loan_amount,
                    "InterestRate": interest_rate,
                    "LoanTerm": loan_term,
                    "DTIRatio": dti_ratio,
                    "LoanPurpose": loan_purpose,
                    "LoanDate": loan_date.isoformat()
                }

                st.session_state.completed_steps.add(4)
                st.session_state.step = 5

                st.rerun()

# =========================================================
# STEP 5 — REVIEW APPLICATION
# =========================================================


elif current_step == 5:

    st.header("📋 Review Application")

    st.write(
        "Please review all information before submitting "
        "the application for prediction."
    )

    applicant = st.session_state.applicant
    employment = st.session_state.employment
    personal = st.session_state.personal
    loan = st.session_state.loan

    payload = {
        **applicant,
        **employment,
        **personal,
        **loan
    }


    # =====================================================
    # APPLICANT INFORMATION
    # =====================================================

    col1, col2 = st.columns([10, 1])

    with col1:
        st.subheader("👤 Applicant Information")

    with col2:
        if st.button(
            "✏️ Edit",
            use_container_width=True
        ):
            st.session_state.step = 1
            st.rerun()

    col1, col2, col3 = st.columns(3)

    with col1:

        st.write("**Age**")
        st.write(payload["Age"])

        st.write("**Annual Income**")
        st.write(f"₹{payload['Income']:,}")

    with col2:

        st.write("**Credit Score**")
        st.write(payload["CreditScore"])

        st.write("**Months Employed**")
        st.write(payload["MonthsEmployed"])

    with col3:

        st.write("**Credit Lines**")
        st.write(payload["NumCreditLines"])


    st.divider()


    # =====================================================
    # EDUCATION & EMPLOYMENT
    # =====================================================

    col1, col2 = st.columns([10, 1])

    with col1:
        st.subheader("🎓 Education & Employment")

    with col2:
        if st.button(
            "✏️ Edit",
            use_container_width=True,
            key="edit_education"
        ):
            st.session_state.step = 2
            st.rerun()

    col1, col2 = st.columns(2)

    with col1:

        st.write("**Education**")
        st.write(payload["Education"])

    with col2:

        st.write("**Employment Type**")
        st.write(payload["EmploymentType"])


    st.divider()


    # =====================================================
    # PERSONAL DETAILS
    # =====================================================

    col1, col2 = st.columns([10, 1])

    with col1:
        st.subheader("🧑 Personal Details")

    with col2:
        if st.button(
            "✏️ Edit",
            use_container_width=True,
            key="edit_personal"
        ):
            st.session_state.step = 3
            st.rerun()

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.write("**Marital Status**")
        st.write(payload["MaritalStatus"])

    with col2:

        st.write("**Mortgage**")
        st.write(payload["HasMortgage"])

    with col3:

        st.write("**Dependents**")
        st.write(payload["HasDependents"])

    with col4:

        st.write("**Co-Signer**")
        st.write(payload["HasCoSigner"])


    st.divider()


    # =====================================================
    # LOAN DETAILS
    # =====================================================

    col1, col2 = st.columns([10, 1])

    with col1:
        st.subheader("🏦 Loan Details")

    with col2:
        if st.button(
            "✏️ Edit",
            use_container_width=True,
            key="edit_loan"
        ):
            st.session_state.step = 4
            st.rerun()

    col1, col2, col3 = st.columns(3)
    
    with col1:

        st.write("**Loan Amount**")
        st.write(f"₹{payload['LoanAmount']:,}")

        st.write("**Interest Rate**")
        st.write(f"{payload['InterestRate']}%")

    with col2:

        st.write("**Loan Term**")
        st.write(f"{payload['LoanTerm']} months")

        st.write("**DTI Ratio**")
        st.write(payload["DTIRatio"])

    with col3:

        st.write("**Loan Purpose**")
        st.write(payload["LoanPurpose"])

        st.write("**Loan Date**")
        st.write(payload["LoanDate"])


    st.divider()


    # =====================================================
    # ACTION BUTTONS
    # =====================================================

    
    submit_application = st.button(
        "🔍 Submit & Predict",
        use_container_width=True,
        type="primary"
    )


    # =====================================================
    # SEND DATA TO FASTAPI
    # =====================================================

    if submit_application:

        try:

            with st.spinner(
                "Analyzing loan application..."
            ):

                response = requests.post(
                    API_URL,
                    json=payload,
                    timeout=10
                )


            # =================================================
            # SUCCESS
            # =================================================

            if response.status_code == 200:

                result = response.json()

                # Save prediction result
                st.session_state.prediction_result = result

                # Mark Step 5 as completed
                st.session_state.completed_steps.add(5)


            # =================================================
            # VALIDATION ERROR
            # =================================================

            elif response.status_code == 422:

                error_data = response.json()

                st.error(
                    "❌ Invalid application data."
                )

                st.json(error_data)


            # =================================================
            # SERVER ERROR
            # =================================================

            else:

                st.error(
                    f"❌ API Error: {response.status_code}"
                )

                st.text(response.text)


        # =====================================================
        # CONNECTION ERROR
        # =====================================================

        except requests.exceptions.ConnectionError:

            st.error(
                "❌ Could not connect to the FastAPI server. "
                "Make sure FastAPI is running on port 8000."
            )


        # =====================================================
        # TIMEOUT ERROR
        # =====================================================

        except requests.exceptions.Timeout:

            st.error(
                "❌ The API request timed out."
            )


        # =====================================================
        # OTHER ERROR
        # =====================================================

        except Exception as e:

            st.error(
                f"❌ Unexpected error: {str(e)}"
            )


    # =========================================================
    # DISPLAY SAVED PREDICTION RESULT
    # =========================================================

    if st.session_state.prediction_result is not None:

        result = st.session_state.prediction_result


        # =====================================================
        # EXTRACT RESULT
        # =====================================================

        probability = float(
            result["default_probability"]
        )

        prediction = result["prediction"]

        decision = result["result"]

        threshold = float(
            result["decision_threshold"]
        )


        # =====================================================
        # PREDICTION RESULT
        # =====================================================

        st.divider()

        st.header("📊 Prediction Result")

        st.write(
            "The loan application has been analyzed by the "
            "default prediction model."
        )


        # =====================================================
        # RESULT SUMMARY CARD
        # =====================================================

        if prediction == 1:

            risk_title = "⚠️ HIGH DEFAULT RISK"

            risk_message = (
                "The applicant has been classified as having "
                "a higher risk of default."
            )

        else:

            risk_title = "✅ LOW DEFAULT RISK"

            risk_message = (
                "The applicant has been classified as having "
                "a lower risk of default."
            )


        st.html(
            f"""
            <div class="result-card">

                <div style="
                    text-align: center;
                    font-size: 24px;
                    font-weight: 700;
                    margin-bottom: 10px;
                ">
                    {risk_title}
                </div>

                <div style="
                    text-align: center;
                    color: #9ca3af;
                    font-size: 14px;
                    margin-bottom: 25px;
                ">
                    {risk_message}
                </div>

            </div>
            """
        )


        # =====================================================
        # RESULT METRICS
        # =====================================================

        col1, col2 = st.columns(2)

        with col1:

            st.html(
                f"""
                <div class="review-item">

                    <div class="review-label">
                        Default Probability
                    </div>

                    <div class="review-value"
                         style="font-size: 28px;">
                        {probability:.2f}%
                    </div>

                </div>
                """
            )


        with col2:

            st.html(
                f"""
                <div class="review-item">

                    <div class="review-label">
                        Decision Threshold
                    </div>

                    <div class="review-value"
                         style="font-size: 28px;">
                        {threshold:.1f}%
                    </div>

                </div>
                """
            )


        # =====================================================
        # DEFAULT RISK
        # =====================================================

        st.subheader("Default Risk")

        st.write(
            f"Estimated probability of default: "
            f"**{probability:.2f}%**"
        )


        progress_value = min(
            max(probability / 100, 0.0),
            1.0
        )

        st.progress(progress_value)


        # =====================================================
        # THRESHOLD COMPARISON
        # =====================================================

        if probability >= threshold:

            risk_text = "above"

        else:

            risk_text = "below"


        st.info(
            f"The model estimates a **{probability:.2f}%** "
            f"probability of default. This is **{risk_text}** "
            f"the decision threshold of **{threshold:.1f}%**."
        )


        # =====================================================
        # DECISION
        # =====================================================

        if prediction == 1:

            st.error(
                f"⚠️ {decision}"
            )

        else:

            st.success(
                f"✅ {decision}"
            )


        # =====================================================
        # PREDICTION DETAILS
        # =====================================================

        with st.expander(
            "🔎 View Prediction Details"
        ):

            st.write(
                "**Prediction:**",
                prediction
            )

            st.write(
                "**Result:**",
                decision
            )

            st.write(
                "**Default Probability:**",
                f"{probability:.2f}%"
            )

            st.write(
                "**Decision Threshold:**",
                f"{threshold:.1f}%"
            )