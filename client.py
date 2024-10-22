# 1. Import necessary libraries
from pydantic import BaseModel


# 2. Create the CustomerData class inheriting from BaseModel
class CustomerData(BaseModel):
    Tenure: float
    PreferredLoginDevice: object
    CityTier: int
    WarehouseToHome: float
    PreferredPaymentMode: object
    Gender: object
    HourSpendOnApp: float
    NumberOfDeviceRegistered: int
    PreferedOrderCat: object
    SatisfactionScore: int
    MaritalStatus: object
    NumberOfAddress: int
    Complain: int
    OrderAmountHikeFromlastYear: float
    CouponUsed: float
    OrderCount: float
    DaySinceLastOrder: float
    CashbackAmount: float
