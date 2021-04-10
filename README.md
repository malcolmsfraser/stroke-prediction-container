# stroke-prediction-container


## In this repo:
* [`mlib.py`](https://github.com/malcolmsfraser/stroke-prediction-container/blob/master/mlib.py) (Model Handling Library) : Functions for retraining the model and prediction
* `predict.py` (Prediction Assistance) : Formats a JSON payload for prediction
* `payload.json` : Test payload
* `utilscli.py` (ML Tools) : Commandline tool for retaining the model and for querying ML Endpoints (both with preformatted payload or with user inputted payload)
* `Stroke_Prediction_Model_Export` : Model training, evaluation, and export
* `app.py` : Stroke prediction Flask application with a /predict route
* `resize.sh` : Bash script for resizing AWS EC2 instance
* `requirements.txt` : Dependencies for the flask app, ML tools, and local container
* `healthcare-dataset-stroke-data.csv` : training data
* `Dockerfile` : for building an image locally (can also pull image with ```docker pull malcolmsfraser/stroke-predict```)
* `Makefile` : 
* `aws-sambda-sam/stroke-application` : Deployed application in an AWS Lambda function with using AWS SAM
* `buildspec.yml` : Configuration for deplotment contiuous delivery
*  





[![alt text](https://github.com/malcolmsfraser/stroke-prediction-container/blob/master/thumbnail.jpg)](https://youtu.be/zslng8DUUkw)  

Source code for a Docker container that has a flask based web-app inside stroke prediction.

```
docker pull malcolmsfraser/stroke-predict
docker run -p 8080:8080
```

Prediction takes a json payload, and returns a risk-level and score.

The payload looks like
>{  
    "age": {"0": 64},  
    "hypertension": {"0": 0},  
    "heart_disease": {"0": 0},  
    "avg_glucose_level": {"0": 62.21},  
    "bmi": {"0": 28.3},  
    "gender_Female": {"0": 0},    
    "gender_Male":{"0": 1},  
    "gender_Other":{"0": 0},  
    "ever_married_No": {"0": 0},  
    "ever_married_Yes": {"0": 1},  
    "work_type_Govt_job": {"0": 0},  
    "work_type_Never_worked": {"0": 0},  
    "work_type_Private": {"0": 1},  
    "work_type_Self-employed": {"0": 0},  
    "work_type_children": {"0": 0},  
    "Residence_type_Rural": {"0": 0},  
    "Residence_type_Urban": {"0": 1},  
    "smoking_status_Unknown": {"0": 1},  
    "smoking_status_formerly smoked": {"0": 0},  
    "smoking_status_never smoked": {"0": 0},  
    "smoking_status_smokes": {"0": 0}  
    }
    
The output looks like
>"Probability of patient stroke is 0.9547"
