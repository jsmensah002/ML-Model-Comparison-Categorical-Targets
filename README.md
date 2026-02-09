Project Goal: 
- Compare the performance of three machine learning models: Logistic Regression (LR), Support Vector Classification (SVC), and Random Forest Classifier (RFC) for predicting a categorical outcome. The dataset used focuses on customer churn prediction using Gender, CreditScore,Age, and Tenure.

Method: 
- Built and trained three separate models (LR, SVC, RFC) to predict customer churn.
- Compared model performance using relevant metrics, highlighting accuracy, stability, and suitability for the dataset. 

Logistic Regression Result:
- R^2 (full dataset) = 0.7147
- R^2 (Trained 80% of the dataset) = 0.7142
- R^2 (Tested 20% of the dataset) = 0.7165
- Churn prediction = 0

Support Vector Classification Results:
- R^2 (full dataset) = 0.7394
- R^2 (Trained 80% of the dataset) = 0.7392
- R^2 (Tested 20% of the dataset) = 0.7400
- Churn prediction = 0

Random Forest Classifier Results:
- R^2 (full dataset) = 0.9568
- R^2 (Trained 80% of the dataset) = 0.9964
- R^2 (Tested 20% of the dataset) = 0.7985
- Churn prediction = 0

Key Insight:
- Although the Random Forest Classifier achieved the highest test score, it showed clear signs of overfitting, which reduces its reliability and makes it a less suitable choice.
- The Support Vector Classification model recorded the next highest test score and demonstrated no signs of overfitting, making it the most appropriate model to use.

