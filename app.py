from flask import Flask, request, jsonify
from flask.logging import create_logger
import logging

import pandas as pd
import joblib

app = Flask(__name__)
LOG = create_logger(app)
LOG.setLevel(logging.INFO)

@app.route("/")
def home():
    html = f"<h3>Stroke Prediction Home</h3>"
    return html.format(format)

# TO DO:  Log out the prediction value
@app.route("/predict", methods=['POST'])
def predict():
    """Performs an sklearn prediction
    input looks like:
            {
    'age': {
        '0': 64
        },
    'hypertension': {
        '0': 0
        },
    'heart_disease': {
        '0': 0
        },
    'avg_glucose_level': {
        '0': 62.21
        },
    'bmi': {
        '0': 28.3
        },
    'gender_Female': {
        '0': 0
        },
    'gender_Male':{
        '0': 1
        },
    'gender_Other':{
        '0': 0
        },
    'ever_married_No': {
        '0': 0
        },
    'ever_married_Yes': {
        '0': 1
        },
    'work_type_Govt_job': {
        '0': 0
        },
    'work_type_Never_worked': {
        '0': 0
        },
    'work_type_Private': {
        '0': 1
        },
    'work_type_Self-employed': {
        '0': 0
        },
    'work_type_children': {
        '0': 0
        },
    'Residence_type_Rural': {
        '0': 0
        },
    'Residence_type_Urban': {
        '0': 1
        },
    'smoking_status_Unknown': {
        '0': 1
        },
    'smoking_status_formerly smoked': {
        '0': 0
        },
    'smoking_status_never smoked': {
        '0': 0
        },
    'smoking_status_smokes': {
        '0': 0
        }
    }

        result looks like:
    { "prediction": [0.81189334, 0.18810666]}


    """


    json_payload = request.json
    LOG.info(f"JSON payload: {json_payload}")
    inference_payload = pd.DataFrame(json_payload)
    LOG.info(f"inference payload DataFrame: {inference_payload}")
    prediction = clf.predict_proba(inference_payload)[0][0]
    
    # very_high_risk = 0.9
    # high_risk = 0.8
    # moderately_high_risk = .7
    # moderate_risk = .6
    # low_risk = .5
    # very_low_risk = .3
    
    # if prediction >= very_high_risk:
    #     statement = f'You have been identified as having very high risk of stroke: Score {prediction: .4f}.'
    #     pass
    # elif prediction >= high_risk:
    #     statement = f'You have been identified as having high risk of stroke: Score {prediction: .4f}.'
    #     pass
    # elif prediction >= moderately_high_risk:
    #     statement = f'You have been identified as having moderately high risk of stroke: Score {prediction: .4f}.'
    #     pass
    # elif prediction >= moderate_risk:
    #     statement = f'You have been identified as having moderate risk of stroke: Score {prediction: .4f}.'
    #     pass
    # elif prediction >= low_risk:
    #     statement = f'You have been identified as having low risk of stroke: Score {prediction: .4f}.'
    #     pass
    # elif prediction >= very_low_risk:
    #     statement = f'You have been identified as having very low risk of stroke: Score {prediction: .4f}.'
        
    statement = f'Probability of patient stroke is {prediction: .4f}'
    
    return statement

if __name__ == "__main__":
    clf = joblib.load("stroke_prediction.joblib")
    app.run(host='0.0.0.0', port=8080, debug=True)