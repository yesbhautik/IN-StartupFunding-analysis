from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import accuracy_score
from sklearn.metrics import r2_score

from sklearn.preprocessing import LabelEncoder
import pandas as pd

class MLModel:
    def __init__(self, data):
        self.data = data
        self.model = RandomForestRegressor()

    def preprocess_data(self):
        # Convert date to datetime and extract year
        self.data['date'] = pd.to_datetime(self.data['date'])
        self.data['year'] = self.data['date'].dt.year

        # Drop the original date column
        self.data = self.data.drop('date', axis=1)

        # Encode categorical columns
        le = LabelEncoder()
        categorical_cols = ['name', 'vertical', 'subvertical', 'city', 'investors', 'type']
        for col in categorical_cols:
            self.data[col] = le.fit_transform(self.data[col])

    def train_model(self):
        X_train, X_test, y_train, y_test = train_test_split(self.data.drop('amount', axis=1), self.data['amount'], test_size=0.2, random_state=42)
        self.model.fit(X_train, y_train)
        predictions = self.model.predict(X_test)
        print(f"Model R^2 Score: {r2_score(y_test, predictions)}")