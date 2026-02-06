Project Goal: 
- Compare the performance of three machine learning models: Logistic Regression (LR), Support Vector Classification (SVC), and Random Forest Classifier (RFC) for predicting a categorical outcome. The dataset used focuses on customer churn prediction.

Method: 
- Built and trained three separate models (LR, SVC, RFC) to predict customer churn.
- Compared model performance using relevant metrics, highlighting accuracy, stability, and suitability for the dataset. 

Logistic Regression Results (with a balanced class weight):
- R^2 (full dataset) = 0.7147
- R^2 (Trained 80% of the dataset) = 0.7142
- R^2 (Tested 20% of the dataset) = 0.7165
- Churn prediction = 0

Support Vector Classification Results:
- R^2 (full dataset) = 0.7963
- R^2 (Trained 80% of the dataset) = 0.7945
- R^2 (Tested 20% of the dataset) = 0.8035
- Churn prediction = 0

Random Forest Classifier Results:
- R^2 (full dataset) = 0.9569
- R^2 (Trained 80% of the dataset) = 0.9957
- R^2 (Tested 20% of the dataset) = 0.8010
- Churn prediction = 1

Key Insight:
- Based on the test performance, the Support Vector Machine (SVM) achieved the highest test score AND showed no signs of overfitting, making it the most reliable model for this dataset. Although the Random Forest Classifier (RF) also achieved a high test score, it exhibited signs of overfitting, reducing its reliability.

