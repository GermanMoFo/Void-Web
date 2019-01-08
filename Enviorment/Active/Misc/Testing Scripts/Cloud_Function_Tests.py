import requests
data = {"Req_Type":"Name", "Req_Arguments":{"Amount":5, "Name_Type":"americanCities"}, "User_ID":"Josh_Testing_Script", "Processed":True}

import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate(r"C:\Users\Joshua\Desktop\PP5\Void-Web\Enviorment\Active\service_account\void-scribe-firebase-adminsdk-xtf9j-c41e46ae8a.json")
firebase_admin.initialize_app(cred)

DataBaseReference = firestore.client()

collection = DataBaseReference.collection("Algorithm_Requests")

doc = collection.document(None)
doc.set(document_data=data)