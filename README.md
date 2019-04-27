# AWSLambda
Lambda function on AWS cloud which will be triggered when new data is arrived. This lambda function will calculate the Air Quality Index using the concentration of gases sent by the Raspberry Pi kit. It will form new Object will send it to MongoDB. 

Here lambda_function.py is lambda function which will be triggered. And calculationfunction.py has logic to calculate the AQI from the concentration of the gas.
