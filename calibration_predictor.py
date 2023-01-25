import pandas as pd
from sklearn.tree import DecisionTreeClassifier


class calibrationController:

    def predict_max_value(self, min_sensor, min_weight, max_weight):
        calibrationData = pd.read_csv("WeightCalibrationData.csv")
        # print(calibrationData)
        X = calibrationData.drop(columns=["MaxVolt"])
        y = calibrationData["MaxVolt"]
        model = DecisionTreeClassifier()
        model.fit(X, y)
        predictions = model.predict([[min_sensor, min_weight, max_weight]])
        predication = {
            "max_sensor": str(predictions[0]),
            "min_sensor": min_sensor,
            "min_weight": min_weight,
            "max_weight": max_weight,
        }
        return predication
