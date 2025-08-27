# importing dependencies 
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from Model.predict import model, Model_version, predict_output
from Pydantic_Schema.prediction_response import PredictionResponse
from Pydantic_Schema.UserInput import UserInput

# fast api object 
app = FastAPI()

# route for home
@app.get('/')
def home():
    return {'Prediction': 'Insurance Premium Model API'}

# health checkup
@app.get('/health')
def health():
    return {
        'status':'OK',
        'Model loaded': {Model_version is not None}
        }

# route for prediction
@app.post('/predict', response_model=PredictionResponse)
def predict_premium(data: UserInput):
    user_input = {
        'bmi': data.bmi,
        'age_group': data.age_group,
        'lifestyle_risk': data.life_style,
        'city_tier': data.city_tier,
        'income_lpa': data.income_lpa,
        'occupation': data.occupation
        }
    try:
        response = predict_output(user_input)
        return JSONResponse(status_code=200, content={"predicted_category": str(response)})
    except Exception as e:
        return JSONResponse(status_code=500, content=str(e))
    