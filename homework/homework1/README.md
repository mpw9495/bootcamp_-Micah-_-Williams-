# Predicting the Financial Impact of Insurance Claims

**Stage:** Problem Framing & Scoping (Stage 01)

## Problem Statement

Insurance companies face uncertainty in how often claims occur and how large each claim might be from a policyholder. The cost of a claim can vary considerably depending on characteristics associated with the policyholder, policy, and claim itself. This uncertainty can make it difficult for insurers to anticipate potential losses and manage their loss reserves. 

This project will investigate whether analyzing historical claims data and statistical distribution can be used to predict the financial cost of an insurance claim. The goal is to develop a quantitative model that estimates potential claim costs and helps insurers better understand their financial exposure to future claims.

## Stakeholder & User

- **Decision owner:** Insurance risk/Claims manager

- **Tool/operator:** Actuary 

## Useful Answer

- **Descriptive / Predictive / Causal:** Predictive 

- **Metric:** R² (coefficient of determination)
- 
- **Artifact:** A regression model that predicts the expected financial cost of an insurance claim based on available insurance characteristics.

## Assumptions & Constraints

- Historical insurance claim data and numerical amounts will be available and sufficiently reliable for analysis.
- Policy, policyholder and claim characteristics may contain useful information such as coverage limits, deductibles and policy terms for predicting claim costs.
- The analysis will be limited by the variables, number of observations, and time period represented in the available dataset.
- Relationships observed in historical insurance data may change over time.

## Known Unknowns / Risks

- It is not yet known which available characteristics will have the strongest relationship with insurance claim costs.
- The amount of variation in claim costs that can be explained by the model is not yet known.
- Extremely large or unusual claims may act as outliers and affect the regression model.
- Relationships observed in historical claim data due to unpredictable events (like hurricanes, earthquakes, etc) may not accurately represent future claims.

## Lifecycle Mapping

Define the insurance claim cost prediction problem → Collect and prepare historical insurance claims data → Explore relationships between claim characteristics and costs → Build a regression model → Evaluate model performance using R² → Identify key factors associated with claim costs → Determine whether the model provides useful financial predictions → Final decision-oriented report

## Repo Plan

- `data/` — raw and processed insurance datasets
- `src/` — reusable Python functions and project source code
- `notebooks/` — exploratory analysis, modeling, and evaluation notebooks
- `docs/` — stakeholder-facing documentation and project materials

The repo will be updated as the project progresses through each stage of the project lifecycle.
