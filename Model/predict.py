import pandas as pd
import pickle

# loading machine learning model
with open("Model/model.pkl", 'rb') as f:
    model = pickle.load(f)

# ML FLOW
Model_version = '1.0.1'

# dataframe for input
class_labels = model.classes_.tolist()
def predict_output(user_input: dict):
    input_df = pd.DataFrame([user_input])
    predicted_class = model.predict(input_df)[0] 
    # get possibilities of all class
    probablities = model.predict_proba(input_df)[0]
    confidence = max(probablities)
    
    # class probs
    class_probs = dict(zip(class_labels, map(lambda p: round(p,4), probablities)))

    return{
        "predicted_category": predicted_class,
        "confidence": round(confidence, 4),
        "class_probablities": class_probs
    }