# Import libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Load dataset
data = pd.read_csv("IMDb Movies India.csv", encoding="latin-1")

# Show first rows
print(data.head())

# Select useful columns
data = data[['Year','Genre','Director','Actor 1','Actor 2','Actor 3','Rating']]

# Clean Year column
data['Year'] = data['Year'].str.replace('(', '')
data['Year'] = data['Year'].str.replace(')', '')
data['Year'] = pd.to_numeric(data['Year'], errors='coerce')

# Remove rows with missing rating
data = data.dropna(subset=['Rating'])

# Fill missing values
data['Genre'] = data['Genre'].fillna("Unknown")
data['Director'] = data['Director'].fillna("Unknown")
data['Actor 1'] = data['Actor 1'].fillna("Unknown")
data['Actor 2'] = data['Actor 2'].fillna("Unknown")
data['Actor 3'] = data['Actor 3'].fillna("Unknown")

# Convert text to numbers
data['Genre'] = data['Genre'].astype('category').cat.codes
data['Director'] = data['Director'].astype('category').cat.codes
data['Actor 1'] = data['Actor 1'].astype('category').cat.codes
data['Actor 2'] = data['Actor 2'].astype('category').cat.codes
data['Actor 3'] = data['Actor 3'].astype('category').cat.codes

# Features and target
X = data[['Year','Genre','Director','Actor 1','Actor 2','Actor 3']]
y = data['Rating']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Create model
model = LinearRegression()

# Train model
model.fit(X_train, y_train)

# Predict ratings
prediction = model.predict(X_test)

# Evaluate model
accuracy = r2_score(y_test, prediction)

print("Model Accuracy:", accuracy)
