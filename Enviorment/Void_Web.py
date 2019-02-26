from flask import Flask, render_template, request, Response
import json
import void_scribe
from Void_Logger import Void_Log_Info, Void_Log_Debug

app = Flask(__name__)
dataFilesPath = r'C:\Users\Joshua\Desktop\PP5\Void-Web\Enviorment\data\nametypes'

#Web Site

@app.route("/crossdomain.xml")
def crossdomain():
    return render_template('crossdomain.xml')

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/Usage")
def usage():
    return render_template('usage.html')

@app.route("/NameTypes")
def nametypes():
    return render_template('NameTypes.html')

@app.route("/SentenceTypes")
def sentencetypes():
    return render_template('SentenceTypes.html')

# API endpoints

@app.route("/GenerateNames", methods = ['POST'])
def GenerateNames():
    data = request.get_json(force=True)
    import LocalVoidWebDataSource
    from void_scribe.NameGenerator import NameGenerator
    dataSource = LocalVoidWebDataSource.LocalVoidWebDataSource(dataFilesPath)
    nameGenerator = NameGenerator(dataSource)

    #Validate
    if "Name_Type" not in data.keys():
        Void_Log_Debug("Name request did not include required Name_Type field.")
        return Response(json.dumps({"Message":"Missing Required Argument For Name Request: Name_Type"}), 400, mimetype='application/json')
    if data["Name_Type"] not in dataSource.NameTypes():
        Void_Log_Debug("Request's Name_Type field was an unsupported value.")
        return Response(json.dumps({"Message":"Argument: Name_Type, Is An Unhandled Value"}), 400, mimetype='application/json')
    if "Amount" not in data.keys():
        Void_Log_Debug("Request did not include Amount field, defaulting to: 1")
        data["Amount"] = 1

    #Process Request
    processed_data = nameGenerator.generateNames(nameType = data['Name_Type'], amount = data["Amount"])

    #Package Response
    Void_Log_Info(f"Sucessfully processed request sending response to {request.remote_addr}.")
    resp = Response(json.dumps({"Data":processed_data}), 200, mimetype='application/json')

    #Return Response
    return resp

@app.route("/RetreiveNames", methods = ['POST'])
def RetreiveNames():
    data = request.get_json(force=True)
    import LocalVoidWebDataSource
    from void_scribe.NameGenerator import NameGenerator
    dataSource = LocalVoidWebDataSource.LocalVoidWebDataSource(dataFilesPath)
    nameGenerator = NameGenerator(dataSource)

    #Validate
    if "Name_Type" not in data.keys():
        Void_Log_Debug("Name request did not include required Name_Type field.")
        return Response(json.dumps({"Message":"Missing Required Argument For Name Request: Name_Type"}), 400, mimetype='application/json')
    if data["Name_Type"] not in dataSource.NameTypes():
        Void_Log_Debug("Request's Name_Type field was an unsupported value.")
        return Response(json.dumps({"Message":"Argument: Name_Type, Is An Unhandled Value"}), 400, mimetype='application/json')
    if "Amount" not in data.keys():
        Void_Log_Debug("Request did not include Amount field, defaulting to: 1")
        data["Amount"] = 1

    #Process Request
    processed_data = nameGenerator.retreiveNames(nameType = data['Name_Type'], amount = data["Amount"])

    #Package Response
    Void_Log_Info(f"Sucessfully processed request sending response to {request.remote_addr}.")
    resp = Response(json.dumps({"Data":processed_data}), 200, mimetype='application/json')

    #Return Response
    return resp
    
@app.route("/GeneratePrompts", methods = ['POST'])
def generatePrompts():
    data = request.get_json()

    if "Prompt_Type" not in data.keys():
        Void_Log_Debug("Request's Prompt_Type field was not found.")
        return Response(json.dumps({"Message":"Argument: Prompt_Type, Is Missing."}), 400, mimetype='application/json')
    if "Amount" not in data.keys():
        Void_Log_Debug("Request's Amount field was not found.")
        return Response(json.dumps({"Message":"Argument: Amount, Is Missing"}), 400, mimetype='application/json')

    resp1 = {
        "data":[
            "This is a cool example sentence."
            ]
        }
    resp2 = {
        "data":[
            "Hello there, General Kenobi.",
            "Autobots, ROLL OUT"
            ]
        }
    resp3 = {
        "data":[
            "Sombody once told me the roll was gonna roll me",
            "I ain't the sharpest tool in the shed.",
            "She was looking kinda dumb with her finger and her thumb in the shape of an L on her forehead",
            "Well the years start coming and they don't stop coming",
            "and they don't stop comiming",
            "and they don't stop comiming",
            "and they don't stop comiming",
            "and they don't stop comiming",
            "and they don't stop comiming",
            "and they don't stop comiming",
            "and they don't stop comiming",
            "and they don't stop comiming",
            "and they don't stop comiming",
            "and they don't stop comiming",
            "and they don't stop comiming",
            "and they don't stop comiming",
            "and they don't stop comiming",
            "and they don't stop comiming"
            ]
        }
    responses = [resp1, resp2, resp3]
    from random import randint
    resp = Response(json.dumps(responses[randint(0,2)]), 200, mimetype='application/json')
    return resp

@app.route("/data/names", methods = ['POST'])
def RetreiveData():
    import DataIndex
    from LocalVoidWebDataSource import LocalVoidWebDataSource
    dataSource = LocalVoidWebDataSource(dataFilesPath)

    data = request.get_json(force = True)

    # Verify request structure
    if "nameTypes" not in data.keys():
        Void_Log_Debug("Data request did not include required nameTypes field.")
        return Response(json.dumps({"Message":"Missing Required Argument: nameTypes"}), 400, mimetype='application/json')
    
    # Find which documents are requested
    needMeta, needRaw, needDict = False, False, False
    if "meta" in data.keys():
        needMeta = data['meta']
    if 'raw' in data.keys():
        needRaw = data['raw']
    if 'dictionary' in data.keys():
        needDict = data['dictionary']

    if not (needDict or needMeta or needRaw):
        # No requested document
        Void_Log_Debug("Data request did not include documents for retreival.")
        return Response(json.dumps({"No data specified for retreival in the request. Review JSON structure at www.voidscribe.com/usage"}), 400, mimetype='application/json')

    responseData = {}
    for nameType in data['nameTypes']:
        if nameType not in dataSource.dataIndex.keys():
            Void_Log_Debug("Data request included invalid NameType.")
            return Response(json.dumps({f"Invalid Name Type, the Name Type {nameType} is not valid. Please review www.voidscribe.com/nametypes for a list of valid Name Types."}), 400, mimetype='application/json')

        responseData[nameType] = {}

        if needMeta:
            responseData[nameType]['meta'] = dataSource.MetaData([nameType])[nameType]['meta']
        if needDict:
            responseData[nameType]['dictionary'] = dataSource.MarkovDictionary([nameType])[nameType]['dictionary']
        if needRaw:
            responseData[nameType]['raw'] = dataSource.RawData([nameType])[nameType]['raw']

    Void_Log_Debug("Sucessfully structured data request.")
    return Response(json.dumps(responseData), 200, mimetype='application/json')

@app.route("/data/names/nameTypes", methods = ['GET'])
def NameTypes():
    from LocalVoidWebDataSource import LocalVoidWebDataSource

    dataSource = LocalVoidWebDataSource(dataFilesPath)
    nameTypes = dataSource.NameTypes()

    return Response(json.dumps(nameTypes), 200, mimetype='application/json')


