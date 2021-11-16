import json
import awsgi
from flask_cors import CORS
from flask import Flask, jsonify
from os import environ, path
import boto3


FORECAST_BUCKET = environ['FORECAST_BUCKET']
S3 = boto3.resource('s3')

BASE_ROUTE = "/bid"

app = Flask(__name__)
CORS(app)

def get_forecast_key():
    Bucket = S3.Bucket(FORECAST_BUCKET)
    prefix_objs = Bucket.objects.filter(Prefix="current/")
    forecast_key = None
    if prefix_objs:
        for obj in prefix_objs:
            key = obj.key
            if not key.endswith('.json') and not key.endswith('.JSON'):
                continue
            else:
                forecast_key = key
    else:
        raise NameError("No Current Forecast")
    return forecast_key

def retrieve_forecast_data(objKey):
    # S3 Object
    object = S3.Bucket(FORECAST_BUCKET).Object(objKey)
    response = object.get()
    # Read object's content
    content = response['Body'].read().decode("utf-8")
    return content

def calculate_bid_from_forecast(forecast, budget):
    user_budget = float(budget)
    fc_dict = json.loads(forecast)
    fc = fc_dict["Forecast"]
    c1 = fc["q1"] * 42
    c2 = fc["q2"] * 42 + c1
    c3 = fc["q3"] * 42 + c2
    c4 = fc["max"] * 42 + c3
    max = fc['max']
    if user_budget >= c4:
        suggestion =  fc["max"]
        total = c4
        time = 168
    elif user_budget >= c3:
        suggestion = fc["q3"]
        total = c3
        time = 126
    elif user_budget >= c2:
        suggestion = fc["q2"]
        total = c2
        time = 84
    elif user_budget >= c1:
        suggestion = fc["q1"]
        total = c1
        time = 42
    else:
        suggestion = -1
        total = 0
        time = 0

    return format(suggestion, ',.4f'), total, time, max

@app.route(BASE_ROUTE + '/<budget>', methods=['GET'])
def get_bid(budget):
    # Retrieve object key of current forecast
    forecastKey = get_forecast_key()

    # Retrieve contents of current forecast
    forecastData = retrieve_forecast_data(forecastKey)

    # Calculate suggested spot bid, the cost of the spot bid for the week, and the expected runtime at that spot price
    bid, cost, runTime, maxPrice = calculate_bid_from_forecast(forecastData, budget)
    
    # First day of the week of the forecast
    weekOf = path.basename(forecastKey).split('.')[0]
    # Define dictionary of values in question and dump into Json object
    Data = {"Bid": bid, "Cost": cost, "Runtime": runTime, "WeekOf": weekOf, "max": maxPrice}
    Data = json.dumps(Data, indent=4, sort_keys=True)
    
    # Log Data to Cloudwatch Logs
    print(f"Logging Data\n{Data}")
    
    return jsonify(data=Data)


def handler(event, context):
    print(f'Log Event:\n{event}')
    return awsgi.response(app, event, context)