FROM public.ecr.aws/lambda/python:3.8

COPY stroke_prediction.joblib mlib.py healthcare-dataset-stroke-data.csv app.py predict.py requirements.txt ./

RUN python3.8 -m pip install --no-cache-dir --upgrade pip &&\
    python3.8 -m pip install --no-cache-dir -r requirements.txt -t .

# Command can be overwritten by providing a different command in the template directly.
CMD ["app.lambda_handler"]