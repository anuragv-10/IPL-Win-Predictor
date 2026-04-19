# IPL Win Predictor using Machine Learning

## Overview

This project is a real-time prediction system that estimates the winning probability of a team during the second innings of an IPL match. It uses machine learning models trained on historical IPL data and provides an interactive interface for users to input live match conditions and view predictions instantly.

## Objectives

* Predict winning probability during the second innings of IPL matches
* Build an interactive UI for real-time prediction
* Compare Logistic Regression and Random Forest models

## Dataset

* Source: IPL dataset (matches.csv and deliveries.csv) 
* ~650 matches and 150,000+ deliveries
* Features include:

  * Teams, city, match results
  * Ball-by-ball runs, wickets, overs

## Features Used

* Runs left
* Balls left
* Wickets remaining
* Current Run Rate (CRR)
* Required Run Rate (RRR)

## Methodology

* Data preprocessing and feature engineering
* Handling missing values and encoding categorical data
* Train-test split (80:20)
* Models used:

  * Logistic Regression (baseline)
  * Random Forest (improved performance)

## Model Performance

* Accuracy: ~80%
* Logistic Regression: Good baseline, interpretable
* Random Forest: Better at handling non-linear patterns

## Visualization

* Match progression graph:

  * X-axis: Overs
  * Y-axis: Win %, Loss %, Runs, Wickets
* Shows how win probability changes during the match

## How to Run

1. Clone the repository
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
3. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```
4. Enter match details and view predictions

## Technologies Used

* Python
* pandas, scikit-learn
* matplotlib, seaborn
* Streamlit

## Limitations

* Does not consider player-level data
* Only works for IPL and second innings
* Sudden match momentum shifts may reduce accuracy

## Future Improvements

* Include player statistics and pitch conditions
* Extend to other T20 leagues
* Use advanced models like Gradient Boosting
* Integrate live match data using APIs
* Deploy as a web/mobile application

## Conclusion

This project demonstrates how machine learning can be applied to sports analytics to provide real-time insights. It enhances decision-making and improves user engagement through an interactive prediction system.

## References

* Kaggle IPL Dataset
* scikit-learn Documentation
* Streamlit Documentation


