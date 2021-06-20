import urllib.request
import json
import io
import os
import ssl
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)

input1 = "1"
input2 = "1"
input3 = "1"
input4 = "1"
input5 = "1"
input6 = "0"
input7 = "0"
input8 = "0"
input9 = "0"
input10 = "0"


@app.route('/', methods=['GET', 'POST'])
def requestModel():

    global input1
    global input2
    global input3
    global input4
    global input5
    global input6
    global input7
    global input8
    global input9
    global input10

    if(request.method == "POST"):
        request_data = request.data
        request_data = json.loads(request_data.decode('utf-8'))
        input1 = request_data['input1']
        input2 = request_data['input2']
        input3 = request_data['input3']
        input4 = request_data['input4']
        input5 = request_data['input5']
        input6 = request_data['input6']
        input7 = request_data['input7']
        input8 = request_data['input8']
        input9 = request_data['input9']
        input10 = request_data['input10']
        return "Hello World!"

    elif(request.method == "GET"):
        data = {
            "Inputs": {
                "input1":
                [
                    {
                        'Quiz 1_Q1 Score': input1,
                        'Quiz 1_Q1 Time': input6,
                        'Quiz 1_Q2 Score': input2,
                        'Quiz 1_Q2 Time': input7,
                        'Quiz 1_Q3 Score': input3,
                        'Quiz 1_Q3 Time': input8,
                        'Quiz 1_Q4 Score': input4,
                        'Quiz 1_Q4 Time': input9,
                        'Quiz 1_Q5 Score': input5,
                        'Quiz 1_Q5 Time': input10,
                    }
                ],
            },
            "GlobalParameters":  {
            }
        }


        body = str.encode(json.dumps(data))

        url = 'https://ussouthcentral.services.azureml.net/workspaces/54e6a72a76114f87bf09edafdf2bfab5/services/e6847abba161454b8fe535f0266dc64f/execute?api-version=2.0&format=swagger'
        # Replace this with the API key for the web service
        api_key = 'qF1+An9iH0AOkx/PbfQTmH9d5D4zS0Yh5YL2hQ8pLerwC5Lo4gbyHIcBFAfr1SpukxntTsR3Nw2xpNM8yR7aYg=='  
        headers = {'Content-Type': 'application/json',
                'Authorization': ('Bearer ' + api_key)}

        req = urllib.request.Request(url, body, headers)

        try:
            response = urllib.request.urlopen(req)

            result = response.read()
            
            final_result = result.replace(b"'", b"'")
            my_json = json.load(io.BytesIO(final_result))
            print(my_json)
            return my_json

        except urllib.error.HTTPError as error:
            print("The request failed with status code: " + str(error.code))

            # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
            print(error.info())
            print(json.loads(error.read().decode("utf8", 'ignore')))


if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=8000)