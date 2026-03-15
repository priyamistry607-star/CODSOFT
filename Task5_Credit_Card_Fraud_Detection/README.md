# CREDIT CARD FRAUD DETECTION 💳

## Project Overview

This project is part of the **CODSOFT Data Science Internship**.
The objective of this project is to build a machine learning model that can detect fraudulent credit card transactions.

Credit card fraud detection is an important problem in financial systems. Machine learning techniques help identify suspicious transactions and reduce financial losses.

---

## Problem Statement

The goal of this project is to classify transactions as:

* **Fraudulent Transaction (1)**
* **Genuine Transaction (0)**

The dataset contains anonymized transaction features obtained through PCA transformation.

---

## Dataset

The dataset used for this project is large (approximately 150 MB), so it is not uploaded directly to this GitHub repository.

You can download the dataset from Kaggle using the following link:

Credit Card Fraud Detection Dataset:
https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud

After downloading the dataset, place the **creditcard.csv** file inside the project folder before running the code.

The dataset contains anonymized credit card transaction data including features such as:

* Time
* V1 – V28 (PCA transformed features)
* Amount
* Class (0 = Genuine transaction, 1 = Fraudulent transaction)

This dataset is widely used in machine learning projects for detecting fraudulent transactions.

---

## Technologies Used

* Python
* Pandas
* Scikit-learn
* Google Colab / Jupyter Notebook

---

## Machine Learning Model

In this project, we used the **Random Forest Classifier** to detect fraudulent transactions.

The steps involved in this project include:

1. Importing required libraries
2. Loading the dataset
3. Data preprocessing and normalization
4. Splitting the dataset into training and testing sets
5. Training the machine learning model
6. Predicting fraudulent transactions
7. Evaluating the model using performance metrics

---

## Model Evaluation

The model performance is evaluated using:

* **Precision**
* **Recall**
* **F1-score**

These metrics help measure how accurately the model detects fraudulent transactions.


## Conclusion

This project demonstrates how machine learning can be used to detect fraudulent credit card transactions.

Using transaction data and classification algorithms, the model can help financial institutions identify suspicious activity and improve security.

---

## Author

Priya Mistry

CODSOFT Data Science Internship
