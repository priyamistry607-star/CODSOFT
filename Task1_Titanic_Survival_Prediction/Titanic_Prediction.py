# Import libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load dataset
data = pd.read_csv("Titanic-Dataset.csv")

# Show first 5 rows
print(data.head())

# Select useful columns
data = data[['Survived','Pclass','Sex','Age','SibSp','Parch','Fare','Embarked']]

# Convert gender to numbers
data['Sex'] = data['Sex'].map({'male':0, 'female':1})

# Convert Embarked values to numbers
data['Embarked'] = data['Embarked'].map({'S':0, 'C':1, 'Q':2})

# Fill missing values
data['Age'] = data['Age'].fillna(data['Age'].mean())
data['Embarked'] = data['Embarked'].fillna(0)

# Split input and output
X = data[['Pclass','Sex','Age','SibSp','Parch','Fare','Embarked']]
y = data['Survived']

# Split training and testing data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Create model
model = LogisticRegression()

# Train model
model.fit(X_train, y_train)

# Predict results
prediction = model.predict(X_test)

# Check accuracy
accuracy = accuracy_score(y_test, prediction)

print("Model Accuracy:", accuracy)
