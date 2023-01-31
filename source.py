import uvicorn
from joblib import load
from fastapi import FastAPI

app = FastAPI()


#model = load('ml_model/dtm.joblib')
#print(model)

#y = model.predict([[10,20,30,10,20,30]])
#print(y)

@app.post("/api/ml/water")
async def ml_water(item):
    #data = model.predict(item)
    return {
        "data": item,
        "success": True,
        "message": "Something went wrong"
    }