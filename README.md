![Build Status](https://codebuild.us-east-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiYTBNa0wwUFpGNnluZ1RGejBxc1lGK0NFWkhsNFlXd0VPVlQvcnhpOVd5dkhsNDg5MmFVcHpMWWwzVWczVU9WTEhOc3R1R2Mzc1RqYmFHQkQ3YlFkbVpvPSIsIml2UGFyYW1ldGVyU3BlYyI6Ik1ENTVIQmlHNlg4RWdWNFciLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=master)
[![Install and Lint](https://github.com/malcolmsfraser/stroke-prediction-container/actions/workflows/blank.yml/badge.svg)](https://github.com/malcolmsfraser/stroke-prediction-container/actions/workflows/blank.yml)

# stroke-prediction-container
Serverless ML application hosted on AWS with Lambda + MLOps Toolkit Integration
Continuous delivery is set up with AWS CodeBuild listening to any changes to the aws-lambda-sam sub-directory and deploys any changes to AWS Lambda
Continuous integration is set up with Github Actions listening to any changes in the main directory and then lints all the code in this repo

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
Follow the steps below in an AWS Cloud9 environment or the AWS CloudShell.
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
#### A. Testing the deployed model
* `python utilscli.py payload-predict --host https://n13eaek1z6.execute-api.us-east-1.amazonaws.com/Prod/predict` (*default payload: [payload.json](https://github.com/malcolmsfraser/stroke-prediction-container/blob/master/payload.json))*  
or  
* `python utilscli.py predict --host https://n13eaek1z6.execute-api.us-east-1.amazonaws.com/Prod/predict`  
*Note: If it returns "Endpoint request timed out" try again... Lambda just needs to warm up*  
#### B. Test the application locally
* Run the Flask application with `python app.py`  
* In a separate terminal, enter the same directory and query the local host *(utilscli.py queries the localhost by default)*:
 ```
 source ~/.venv/bin/activate
 cd stroke-prediction-container
 python utilscli.py payload-predict [OR] python utils.py predict 
 ```
#### C. Build and test the containerized application locally
* Build image locally `docker build --tag stroke-predict` or pull from dockerhub `docker pull malcolmsfraser/stroke-predict`  
* Run the container `docker run -p 8080:8080 stroke-predict` or `docker run -p 8080:8080 malcolmsfraser/stroke-predict`  
* In a separate terminal, enter the same directory and query the localhost
 ```
 source ~/.venv/bin/activate
 cd stroke-prediction-container
 python utilscli.py payload-predict [OR] python utils.py predict 
 ```
#### D. Deploy the model with AWS Lambda yourself
* create and ecr registry for the docker image `make ecr`
* deploy containerized application to Lambda `make deploy`
