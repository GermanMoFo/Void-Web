from flask import Flask, render_template, request, Response, jsonify
import json
import requests
from void_scribe import NameGenerator, Stories
import Void_Main
from Void_Logger import Void_Log_Info, Void_Log_Debug, Void_Log_Warning

app = Flask(__name__)

@app.route("/crossdomain.xml")
def crossdomain():
    return render_template('crossdomain.xml')

@app.route("/VoidScribeRequest", methods = ['POST'])
def VoidScribeRequest():
    data = request.get_json()

    Void_Log_Info(f"Received request on VoidScribeRequest from: {request.remote_addr}.")
    Void_Log_Debug(f"Request Data: {str(request.get_json())}")

    #Validate Primary Fields
    if "Req_Type" not in data.keys():
        Void_Log_Debug("Request did not include required Req_Type field.")
        return Response(json.dumps({"Message":"Missing Required Argument: Req_Type"}), 400, mimetype='application/json')
    if "Req_Arguments" not in data.keys():
        Void_Log_Debug("Request did not include required Req_Argument field.")
        return Response(json.dumps({"Message":"Missing Required Argument: Req_Argument"}), 400, mimetype='application/json')
    if "User_ID" not in data.keys():
        Void_Log_Debug("Request did not include required User_ID field.")
        return Response(json.dumps({"Message":"Missing Required Argument: User_ID"}), 400, mimetype='application/json')
    if "Request_Source" not in data.keys():
        Void_Log_Debug("Received a request with an unspecified source. Marking as: Web_API.")
        data["Request_Source"] = "Web_API"

    #Validate Argument Fields
    if data["Req_Type"] == "Name":
        if "Name_Type" not in data["Req_Arguments"].keys():
            Void_Log_Debug("Name request did not include required Name_Type field.")
            return Response(json.dumps({"Message":"Missing Required Argument For Name Request: Name_Type"}), 400, mimetype='application/json')
        if data["Req_Arguments"]["Name_Type"] not in list(NameGenerator.getNameTypes()):
            Void_Log_Debug("Request's Name_Type field was an unsupported value.")
            return Response(json.dumps({"Message":"Argument: Name_Type, Is An Unhandled Value"}), 400, mimetype='application/json')
        if "Amount" not in data["Req_Arguments"].keys():
            Void_Log_Debug("Request did not include Amount field, defaulting to: 1")
            data["Req_Arguments"]["Amount"] = 1

    elif data["Req_Type"] == "Sentence":
        if "Sentence_Type" not in data["Req_Arguments"].keys():
            Void_Log_Debug("Sentence request did not include required Sentence_Type field.")
            return Response(json.dumps({"Message":"Missing Required Argument For Sentence Request: Sentence_Type"}), 400, mimetype='application/json')
        if data["Req_Arguments"]["Sentence_Type"] not in Stories.data.keys():
            Void_Log_Debug("Request's Sentence_Type field was an unsupported value.")
            return Response(json.dumps({"Message":"Argument: Sentence_Type, Is An Unhandled Value"}), 400, mimetype='application/json')
        if "Amount" not in data["Req_Arguments"].keys():
            Void_Log_Debug("Request did not include Amount field, defaulting to: 1")
            data["Req_Arguments"]["Amount"] = 1

    else:
        Void_Log_Debug("Request had an invalied Req_Type field value.")
        return Response(json.dumps({"Message":"Argument: Req_Type, Is An Unhandled Value"}), 400, mimetype='application/json')

    #Rebuild Data Package
    alg_data = {"Req_Type":data["Req_Type"], "Req_Arguments":data["Req_Arguments"], "User_ID":data["User_ID"], "Request_Source":data["Request_Source"]}

    #Hash Key is exclusive to Mobile Requests and is used for retreival purposes
    if "Hash_Key" in data.keys():
        alg_data["Hash_Key"] = data["Hash_Key"]

    #Process Data
    processed_data = Void_Main.ProcessRequest(alg_data)
    
    #Package Data For Response
    Void_Log_Info(f"Sucessfully processed request sending response to {request.remote_addr}.")
    resp = Response(json.dumps({"Data":processed_data}), 200, mimetype='application/json')

    #Send Response
    return resp






