# 🚢 Titanic Survival Prediction — Machine Learning Project

## 📌 Project Overview

This project applies a complete machine learning workflow to predict passenger survival on the Titanic using the **Titanic dataset from Kaggle**.

The objective is to analyze passenger data, identify key factors affecting survival, and build predictive models capable of estimating survival outcomes.

This project demonstrates a **full data science pipeline**, including data preprocessing, exploratory data analysis, model training, evaluation, and optimization.

---

# 📊 Dataset

Dataset used: Titanic Passenger Dataset

The dataset contains information about Titanic passengers including:

* Passenger class
* Age
* Sex
* Fare
* Number of siblings/spouses aboard
* Number of parents/children aboard
* Port of embarkation
* Survival status

Target variable:

* **Survived** (0 = Did Not Survive, 1 = Survived)

---

# ⚙️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Jupyter Notebook

---

# 🔎 Machine Learning Workflow

## 1. Data Cleaning

* Handled missing values in **Age** and **Embarked**
* Removed the **Cabin** feature due to excessive missing data
* Converted categorical variables into numerical format
* Removed unnecessary columns such as Name, Ticket, and PassengerId

---

## 2. Exploratory Data Analysis (EDA)

Visualizations were created to understand relationships between features and survival.

Key analyses included:

* Survival distribution
* Gender vs survival
* Passenger class vs survival
* Age distribution

Example visualizations:

* Survival count plot
* Age distribution histogram
* Correlation heatmap

---

## 3. Feature Engineering

* Encoded categorical variables
* Selected relevant features for model training
* Prepared dataset for machine learning algorithms

---

# 🤖 Model Development

Two machine learning models were implemented:

### Logistic Regression

Used as a baseline classification model.

Steps:

* Train the model
* Generate predictions
* Evaluate accuracy

---

### Random Forest Classifier

An ensemble learning method used to improve prediction performance.

Steps:

* Train Random Forest model
* Generate predictions
* Evaluate using classification metrics

---

# 📈 Model Evaluation

Models were evaluated using:

* Accuracy
* Precision
* Recall
* F1 Score
* Confusion Matrix

The Random Forest model produced higher predictive performance compared to Logistic Regression.

---

# 🔍 Feature Importance Analysis

Feature importance was extracted from the Random Forest model to determine which variables most influenced survival predictions.

Key influential features included:

* Sex
* Passenger Class
* Age
* Fare

Feature importance was visualized using bar charts.

---

# ⚡ Model Optimization

Hyperparameter tuning was performed using **GridSearchCV** to identify the best model configuration.

Parameters tuned included:

* Number of trees (n_estimators)
* Maximum tree depth
* Minimum samples split

This improved the final model performance.

---

# 📊 Final Model Performance

The optimized Random Forest model achieved strong predictive performance on the test dataset.

Evaluation metrics confirmed improved accuracy compared to the baseline model.

---

# 📂 Project Structure

Titanic-ML-Project
│
├── data
│   └── train.csv
│
├── notebooks
│   └── titanic_analysis.ipynb
│
├── images
│   └── plots
│
├── models
│   └── trained_model.pkl
│
└── README.md

---

# 🚀 Key Skills Demonstrated

* Data Cleaning
* Exploratory Data Analysis
* Feature Engineering
* Machine Learning Model Training
* Model Evaluation
* Feature Importance Analysis
* Hyperparameter Tuning

---

# 📌 Future Improvements

* Implement additional models (XGBoost, Gradient Boosting)
* Apply cross-validation techniques
* Deploy the model as a web application
* Create an interactive dashboard

---

# 📚 Author: Naveen Kunam

Data Science / Machine Learning Project
