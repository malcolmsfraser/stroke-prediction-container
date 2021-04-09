import json
import mlib
import predict



def lambda_handler(event, context):
    
    print(f"RAW LAMBDA EVENT BODY: {event}")
    if "body" in event:
        event = json.loads(event["body"])
        print("API Gateway Request event")
        return event
    else:
        print("Function Request")

    # If the payload is correct, predict it
    inputs = ['age','hypertension','heart_disease','avg_glucose_level', 'bmi',
    'gender_Female', 'gender_Male', 'gender_Other',
    'ever_married_No','ever_married_Yes',
    'work_type_Govt_job','work_type_Never_worked','work_type_Private','work_type_Self-employed','work_type_children',
    'Residence_type_Rural','Residence_type_Urban',
    'smoking_status_Unknown','smoking_status_formerly smoked','smoking_status_never smoked','smoking_status_smokes']
    
    if all([x in event for x in inputs]):
        payload = event["payload"]
        print(payload)
        prediction = mlib.predict(payload)
        print(f"Prediction: {prediction}")
        return {
            "statusCode" : 200,
            "body" : json.dumps(prediction),
        }
    else: 
        payload = {"Message": "Incorrect or Empty Payload"}
        return {
            "statusCode" : 200,
            "body" : json.dumps(payload),
            "event" : event
        }