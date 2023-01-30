import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split


class calibrationController:

    def predict_max_value(self, min_sensor, min_weight, max_weight):
        calibrationData = pd.read_csv('./storage/VmsCalibrationDataset.csv')
        X = calibrationData[['Sensor Min Value',
                             'Empty Weight', 'Full Weight']]
        Y = calibrationData['Sensor Max Value']
        # Split the data into training and test sets
        x_train, x_test, y_train, y_test = train_test_split(
            X, Y, test_size=0.2, random_state=42)

        # Create the decision tree regressor object
        model = DecisionTreeRegressor(random_state=1)
        # Train the model on the training data
        model.fit(x_train, y_train)
        # Evaluate the model on the test data
        y_pred = model.predict(x_test)
        # Convert the input to floats
        min_sensor = float(min_sensor)
        min_weight = float(min_weight)
        max_weight = float(max_weight)

        # Create an array of the input values
        X_new = np.array([min_sensor, min_weight, max_weight]).reshape(1, -1)

        # Use the model to predict the target value
        predictions = model.predict(X_new)
        predication = {
            "max_sensor": str(predictions[0]),
            "min_sensor": min_sensor,
            "min_weight": min_weight,
            "max_weight": max_weight,
        }
        return predication
