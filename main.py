# 1. Library imports
import uvicorn
from fastapi import FastAPI, HTTPException
from client import CustomerData  # Importing the BaseModel from client.py
import joblib
import numpy as np
import logging
import warnings

warnings.filterwarnings("ignore")

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load the trained model
model = joblib.load('best_model.pkl')

# 2. Create the FastAPI app object
app = FastAPI()

# 3. Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {'message': 'Welcome to the Customer Churn Prediction'}

# 5. Expose the prediction functionality, make a prediction from the passed JSON data
@app.post('/predict')
def predict_churn(customer: CustomerData):
    try:
        # Convert input data to an array (assuming the data is already in the form expected by the model)
        data = customer.dict()
        input_data = np.array([[
            data['Tenure'],
            data['PreferredLoginDevice'],
            data['CityTier'],
            data['WarehouseToHome'],
            data['PreferredPaymentMode'],
            data['Gender'],
            data['HourSpendOnApp'],
            data['NumberOfDeviceRegistered'],
            data['PreferedOrderCat'],
            data['SatisfactionScore'],
            data['MaritalStatus'],
            data['NumberOfAddress'],
            data['Complain'],
            data['OrderAmountHikeFromlastYear'],
            data['CouponUsed'],
            data['OrderCount'],
            data['DaySinceLastOrder'],
            data['CashbackAmount']
        ]])

        # Make prediction
        prediction = model.predict(input_data)
        probability = model.predict_proba(input_data)[0][1]  # Probability of churn

        # Return the result
        return {
            "churn_prediction": bool(prediction[0]),
            "churn_probability": float(probability)
        }
    except Exception as e:
        logger.error(f"Error during prediction: {e}")
        raise HTTPException(status_code=500, detail=str(e))


# 6. Run the API with uvicorn
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
