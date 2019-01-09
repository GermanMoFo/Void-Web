#This File Will Handle Managment Of Algorithm Processes
from Void_Algorithm_Processor import RunAlgorithmRequest
from Void_FireStore import UploadDocument, DataBaseReference
from Void_Logger import Void_Log_Info

__StorageCollectionMap__ = {"Name":DataBaseReference.collection("Generated_Names"), "Sentence":DataBaseReference.collection("Generated_Sentences"), "None Specified":DataBaseReference.collection("Bad_Requests")}

def ProcessRequest(Data):

    #Interpret Source (Document Upload or HTTP)
    if Data["Request_Source"] == "Unity" or Data["Request_Source"] == "Web_API":
        Void_Log_Info("Received request from a source outside firebase, fabricating request document.")
        #Create A Request Document
        request_doc = {}
        request_doc["Request_Source"] = Data["Request_Source"]
        request_doc["Req_Type"] = Data["Req_Type"]
        request_doc["Req_Arguments"] = Data["Req_Arguments"]
        request_doc["User_ID"] = Data["User_ID"]
        request_doc["Processed"] = True
        #Enqueue for Upload
        UploadDocument(DataBaseReference.collection("Algorithm_Requests"), request_doc)

    #Run Request To Algorithm
    processed_data = RunAlgorithmRequest(Data)

    #Format Completed_Requests' and Storage's documents
    proc_req_doc = {}
    storage_doc = {}

    proc_req_doc["Request"] = Data
    proc_req_doc["Processed_Request"] = processed_data

    storage_doc["Data"] = processed_data

    #Tag With Hash If Data Exists (For Retreival Purposes On The Mobile Front End)
    if "Hash_Key" in Data.keys():
        proc_req_doc["Hash_Key"] = Data["Hash_Key"]
        storage_doc["Hash_Key"] = Data["Hash_Key"]

    #Build Collection References
    proc_doc_colec_ref = DataBaseReference.collection("Completed_Requests")
    storage_doc_colec_ref = __StorageCollectionMap__[Data["Req_Type"]]

    #Enqueue For Upload
    UploadDocument(proc_doc_colec_ref, proc_req_doc)
    UploadDocument(storage_doc_colec_ref, storage_doc)

    #Return Algorithm Output
    return processed_data