# stroke-prediction-container


## In this repo:
* [`mlib.py`](https://github.com/malcolmsfraser/stroke-prediction-container/blob/master/mlib.py) (Model Handling Library) : Functions for retraining the model and prediction
* [`predict.py`](https://github.com/malcolmsfraser/stroke-prediction-container/blob/master/predict.py) (Prediction Assistance) : Formats a JSON payload for prediction
* [`payload.json`](https://github.com/malcolmsfraser/stroke-prediction-container/blob/master/payload.json) : Test payload
* [`utilscli.py`](https://github.com/malcolmsfraser/stroke-prediction-container/blob/master/utilscli.py) (ML Tools) : CLI for retraining the model and for querying ML Endpoints with preformatted or user input payload
* [`Stroke_Prediction_Model_Export.ipynb`](https://github.com/malcolmsfraser/stroke-prediction-container/blob/master/Stroke_Prediction_Model_Export.ipynb) : Model training, evaluation, and export
* [`app.py`](https://github.com/malcolmsfraser/stroke-prediction-container/blob/master/app.py) : Stroke prediction Flask application with a /predict route
* [`resize.sh`](https://github.com/malcolmsfraser/stroke-prediction-container/blob/master/resize.sh) : Bash script for resizing AWS EC2 instance
* [`requirements.txt`](https://github.com/malcolmsfraser/stroke-prediction-container/blob/master/resize.sh) : Dependencies for the flask app, ML tools, and local container
* [`healthcare-dataset-stroke-data.csv`](https://github.com/malcolmsfraser/stroke-prediction-container/blob/master/healthcare-dataset-stroke-data.csv) : training data
* [`Dockerfile`](https://github.com/malcolmsfraser/stroke-prediction-container/blob/master/Dockerfile) : for building an image locally (can also pull image with ```docker pull malcolmsfraser/stroke-predict```)
* [`Makefile`](https://github.com/malcolmsfraser/stroke-prediction-container/blob/master/Makefile) : 
* [`aws-sambda-sam/stroke-application`](https://github.com/malcolmsfraser/stroke-prediction-container/blob/master/aws-sambda-sam/stroke-application) : Deployed application in an AWS Lambda function with using AWS SAM
* [`buildspec.yml`](https://github.com/malcolmsfraser/stroke-prediction-container/blob/master/buildspec.yml) : Configuration for deplotment contiuous delivery

## Test my project:
* Optional: create and source a virtual environment
```
python3 -m venv ~/.venv
source ~/.venv/bin/activate
```
* Clone directory and install requirements
```
git clone https://github.com/malcolmsfraser/stroke-prediction-container.git
cd stroke-prediction-container
make install
```
#### Testing the deployed model
* `python utilscli.py payload-predict --host https://n13eaek1z6.execute-api.us-east-1.amazonaws.com/Prod/predict` (*default payload: [payload.json](https://github.com/malcolmsfraser/stroke-prediction-container/blob/master/payload.json))*  
or  
* `python utilscli.py predict --host https://n13eaek1z6.execute-api.us-east-1.amazonaws.com/Prod/predict`  
 *Note: If it returns "Endpoint request timed out" try again... Lambda just needs to warm up*  
#### Build and test locally
* Run the Flask application with `python app.py`  
* In a separate terminal, enter the same directory and query the local host: `python utils.py payload-predict` or `python utils.py predict` *(queries the localhost by default)*
#### Test the containerized application
* Build image locally `docker build --tag stroke-predict` or pull from dockerhub `docker pull malcolmsfraser/stroke-predict`  
* Run the container `docker run -p 8080:8080 stroke-predict` or `docker run -p 8080:8080 malcolmsfraser/stroke-predict`  
* In a separate terminal, enter the same directory and query the local host: `python utils.py payload-predict` or `python utils.py predict` 
#### Deploy the model with AWS Lambda yourself
* create and ecr registry for the docker image `make ecr`
* deploy containerized application to Lambda `make deploy`






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
