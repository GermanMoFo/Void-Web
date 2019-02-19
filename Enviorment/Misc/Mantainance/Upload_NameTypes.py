import queue
import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate(r'C:\Users\thepe_000\Desktop\PP5\Void-Web\Enviorment\Active\Non-Public\void-scribe-firebase-adminsdk-xtf9j-3b3a1435e9.json')
firebase_admin.initialize_app(cred)

DataBaseReference = firestore.client()
_UploadQueue_ = queue.Queue()
#Objects in Queue must be indexable format -> [0] collection reference [1] document contents [2] (optional) document name

def _UploadDocument_(collection, document_content, document_name=None):
    #collection - A reference to the collection to insert into, utalize DataBaseReference to obtain this
    #document_content - A dictionary object that is the contents of the document to upload
    #document_name - An optional string used to name the uploaded document
    #If no document name is provided push() is used to generate a unique ID
    
    
    doc_ref = collection.document(document_name)
    doc_ref.set(document_data=document_content)

import re
import os
import void_scribe.NamesDictionary
import pickle

source_directory = "C:/Users/thepe_000/Desktop/PP5/VoidScribe/void_scribe/data/Names/"
dest_directory = "C:/Users/thepe_000/Desktop/PP5/VoidScribe/void_scribe/data/MarkovDictionaries/"

nd = void_scribe.NamesDictionary.NamesDictionary()

list_obj = []
for namesDataFile in nd.__index__.keys():
    namesData = pickle.load(open(nd.__index__[namesDataFile], "rb" ))
    dict_obj = {}
    dict_obj["Key"] = namesDataFile

    display = ""
    for i, char in enumerate(namesDataFile):
        if i == 0:
            display += char.upper()
        elif char.istitle():
            display += ' '
            display += char
        else:
            display += char

    dict_obj["Display"] = display
    dict_obj["Tags"] = namesData['Tags']
    dict_obj['Category'] = namesData['Category']

    list_obj.append(dict_obj)

data = {"types":list_obj}
DataBaseReference.collection("Algorithm_Information").document("Name_Types").set(data)

