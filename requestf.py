import requests

# Define the URL of your FastAPI endpoint
url = "http://127.0.0.1:8000/predict"

# Define the payload for the POST request
data = {
    "Tenure": 10.0,
    "WarehouseToHome": 15.0,
    "HourSpendOnApp": 3.0,
    "OrderAmountHikeFromlastYear": 11.0,
    "CouponUsed": 1.0,
    "OrderCount": 3.0,
    "DaySinceLastOrder": 5.0,
    "CashbackAmount": 159.93,
    "PreferredLoginDevice_Computer": False,
    "PreferredLoginDevice_MobilePhone": True,
    "PreferredLoginDevice_Phone": False,
    "CityTier_1": True,
    "CityTier_2": False,
    "CityTier_3": False,
    "PreferredPaymentMode_CC": False,
    "PreferredPaymentMode_COD": False,
    "PreferredPaymentMode_CashOnDelivery": False,
    "PreferredPaymentMode_CreditCard": True,
    "PreferredPaymentMode_DebitCard": False,
    "PreferredPaymentMode_EWallet": False,
    "PreferredPaymentMode_UPI": False,
    "Gender_Female": False,
    "Gender_Male": True,
    "PreferedOrderCat_Fashion": False,
    "PreferedOrderCat_Grocery": False,
    "PreferedOrderCat_LaptopAndAccessory": True,
    "PreferedOrderCat_Mobile": False,
    "PreferedOrderCat_MobilePhone": False,
    "PreferedOrderCat_Others": False,
    "MaritalStatus_Divorced": False,
    "MaritalStatus_Married": True,
    "MaritalStatus_Single": False
}

# Send the POST request
response = requests.post(url, json=data)

# Check the response
if response.status_code == 200:
    print("Prediction response:", response.json())
else:
    print(f"Error: {response.status_code}, {response.text}")

