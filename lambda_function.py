import boto3
from decimal import Decimal
import json
import pymongo
import calculationfunction as cf

def lambda_handler(event, context):
    # TODO implement
    uri=""

    myclient = pymongo.MongoClient(uri)
    mydb = myclient.DATA
    mycol = mydb.rasp
    #dynamodb = boto3.resource('dynamodb')
    #table = dynamodb.Table('DATA')
    timestamp=event["timestamp"]
    temp=event["data"]["temperature"]
    co=event["data"]["co"]
    sox=event["data"]["sox"]
    o3=event["data"]["o3"]
    nox=event["data"]["nox"]
    pm25=event["data"]["pm25"]
    pm10=event["data"]["pm10"]
    AQI=value(co,sox,o3,nox,pm25,pm10)
    AQI_value=round(AQI)
    if AQI_value >= 0 and AQI_value <= 50:
        cat=1
    elif AQI_value >= 51 and AQI_value <= 100:
        cat=2
    elif AQI_value >= 101 and AQI_value <= 150:
        cat=3
    elif AQI_value >= 151 and AQI_value <= 200:
        cat=4
    elif AQI_value >= 201 and AQI_value <= 300:
        cat=5
    else:
        cat=6
        
    #response = table.put_item(
    Item={
        'deviceID':event["deviceID"],
        'timestamp':timestamp,
        'temp':temp,
        'co':co,
        'sox':sox,
        'o3':o3,
        'nox':nox,
        'pm25':pm25,
        'pm10':pm10,
        'aqi':AQI_value,
        'cat':cat
        }
    #)
    x = mycol.insert(Item)
    return
#value for test case is 329.
def value(co,sox,o3,nox,pm25,pm10):
    return max(cf.key("co",co),cf.key("so2",sox),cf.key("ozone",o3),cf.key("no2",nox),cf.key("pm25",pm25),cf.key("pm10",pm10))
