from flask import Flask, render_template, request, Response, jsonify
import json
import requests
from void_scribe import NameGenerator, Stories
import Void_Main

app = Flask(__name__)

@app.route("/crossdomain.xml")
def crossdomain():
    return render_template('crossdomain.xml')

@app.route("/VoidScribeRequest", methods = ['POST'])
def VoidScribeRequest():
    data = request.get_json()
    print(data)

    #Validate Primary Fields
    if "Req_Type" not in data.keys():
        return Response(json.dumps({"Message":"Missing Required Argument: Req_Type"}), 400, mimetype='application/json')
    if "Req_Arguments" not in data.keys():
        return Response(json.dumps({"Message":"Missing Required Argument: Req_Argument"}), 400, mimetype='application/json')
    if "User_ID" not in data.keys():
        return Response(json.dumps({"Message":"Missing Required Argument: User_ID"}), 400, mimetype='application/json')
    if "Request_Source" not in data.keys():
        data["Request_Source"] = "Web_API"

    #Validate Argument Fields
    if data["Req_Type"] == "Name":
        if "Name_Type" not in data["Req_Arguments"].keys():
            return Response(json.dumps({"Message":"Missing Required Argument For Name Request: Name_Type"}), 400, mimetype='application/json')
        if data["Req_Arguments"]["Name_Type"] not in list(NameGenerator.getNameTypes()):
            return Response(json.dumps({"Message":"Argument: Name_Type, Is An Unhandled Value"}), 400, mimetype='application/json')
        if "Amount" not in data["Req_Arguments"].keys():
            data["Req_Arguments"]["Amount"] = 1

    elif data["Req_Type"] == "Sentence":
        if "Sentence_Type" not in data["Req_Arguments"].keys():
            return Response(json.dumps({"Message":"Missing Required Argument For Name Request: Sentence_Type"}), 400, mimetype='application/json')
        if data["Req_Arguments"]["Sentence_Type"] not in Stories.data.keys():
            return Response(json.dumps({"Message":"Argument: Sentence_Type, Is An Unhandled Value"}), 400, mimetype='application/json')
        if "Amount" not in data["Req_Arguments"].keys():
            data["Req_Arguments"]["Amount"] = 1

    else:
        return Response(json.dumps({"Message":"Argument: Req_Type, Is An Unhandled Value"}), 400, mimetype='application/json')

    #Rebuild Data Package
    alg_data = {"Req_Type":data["Req_Type"], "Req_Arguments":data["Req_Arguments"], "User_ID":data["User_ID"], "Request_Source":data["Request_Source"]}

    #Hash Key is exclusive to Mobile Requests and is used for retreival purposes
    if "Hash_Key" in data.keys():
        alg_data["Hash_Key"] = data["Hash_Key"]

    #Process Data
    processed_data = Void_Main.ProcessRequest(alg_data)
    
    #Package Data For Response
    resp = Response(json.dumps({"Data":processed_data}), 200, mimetype='application/json')

    #Send Response
    return resp






